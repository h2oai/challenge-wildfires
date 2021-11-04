from h2o_wave import main, app, Q, ui
import plotly.express as px
from sklearn import metrics
from .ui_utils import *
from .plot import *
from .ds import get_data


# FUNCTIONS FOR PREDICT TAB

months = {
    'January':1, 'February':2, 'March':3, 'April':4, 'May':5,
    'June':6, 'July':7, 'August':8, 'September':9, 'October':10
}


async def predict(q:Q):
    # GET THE AVAILABLE MODELS
    models = list(q.app.models.keys())
    val = q.args.models or models[0]
 
    # SHOW MODEL SELECTION/LOAD INPUTS
    q.page['models'] = ui.form_card(box=ui.box('data'), items=[
            ui.combobox(name='models', label='Models', choices=models, value=val),
            ui.buttons(justify='center', items=[
                ui.button(name='load', label='Load Model', primary=True),
            ])
    ])
    await q.page.save()

    # LOAD SELECTED MODEL IF LOAD IS HIT OR PREDICTION IN PROGRESS
    if q.args.load or q.args.predict:
        await predict_menu(q, val)

async def predict_menu(q:Q, val:str):
    # DISPLAY PREDICTION MENU, ASK USER INPUT FOR MONTH
    q.page['options'] = ui.form_card(box='predict', items=[
        ui.inline(items=[
           ui.textbox(name='year', label='Year', value='2021', readonly=True),
           ui.combobox(name='month', label='Month', value=(q.args.month or 'October'), choices=list(months.keys())
           ),
        ]),
        ui.separator(),
        ui.buttons(justify='center', items=[
            ui.button(name='predict', label='Predict', primary=True)
        ])
    ])
    await q.page.save()

    # MAKE PREDICTION USING THE LOADED MODEL
    if q.args.predict:
        await predict_results(q, val)

async def predict_results(q:Q, val:str):
    # GET YEAR AND MONTH FROM USER INPUT
    year = q.args.year ; month = months[q.args.month]
    
    # UPDATE MAP CARD TO NOTIFY THAT PREDICTIONS ARE BEING MADE
    q.page['map'] = ui.form_card(box='map', items=[
        ui.progress(label=f'Making predictions for {await get_month_str(month)} {year}')
    ])
    await q.page.save()

    # MAKE THE ACTUAL PREDICTION
    await q.run(model_predict, q, val, year, month)


async def model_predict(q:Q, val:str, year:str, month:int):
    model = q.app.models[val]
    
    # USE THE DATA PREP STEP FROM THE SUBMISSION NOTEBOOK
    X, features = await q.run(get_data, q, path =list(q.app.datasets.keys())[0])
    # FILTER TEST DATA FOR THE SELECTED YEAR AND MONTH
    test = X[X.year == int(year)]
    test = test[test.month == month]

    # USE THE MODEL TO PREDICT
    test_predictions = model.predict(test[features])

    # COMPUTE THE TEST_AUC
    test_auc = metrics.roc_auc_score(test.fire, test_predictions)

    # MAKE THE ROC CURVE
    fpr, tpr, thr = metrics.roc_curve(test.fire, test_predictions)
    fig = await make_line_chart(fpr, tpr, month, year)

    # CONVERT FIGURE TO HTML
    html = to_html(fig)

    # DISPLAY THE TEST_AUC AND RENDER HTML IN THE FORM_CARD
    q.page['map'] = ui.form_card(box='map', items=[
        ui.stats(justify ='around', items=[ui.stat('test_auc', f'{test_auc}')]),
        ui.frame(content=html, height='500px')
    ])
    await q.page.save()


# UTIL MENTHOD TO MAKE LINE CHART FOR TGHE ROC CURVE
async def make_line_chart(fpr, tpr, month, year):
    # USE PLOTLY TO MAKE A FIGUTR
    fig = px.line(pd.DataFrame(dict(FPR=fpr, TPR=tpr)), markers=True, range_x=[-0.2,1], range_y=[0,1.2],
        x='FPR', y='TPR', title=f'Fire/hotspot model performance for {await get_month_str(month)} {year}'
    )
    
    # CUSTOMIZE THE STYLE FOR THE FIGURE
    fig.update_layout(
        {'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'font_color': '#FEC925',
        }
    )
    fig.update_traces(line_color='#FEC925', marker_color='#E25822')

    return fig


# UTIL FUNCTION TO GET MONTH AS STR FROM MONTH INT
async def get_month_str(month: int):
    for key, val in months.items():
        if val == month: return key 
