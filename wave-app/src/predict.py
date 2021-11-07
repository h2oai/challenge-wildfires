from h2o_wave import main, app, Q, ui
import plotly.express as px
from sklearn import metrics
from .ui_utils import *
from .plot import *
from .ds import get_data


# Functions for predict tab.

months = {
    'January':1, 'February':2, 'March':3, 'April':4, 'May':5,
    'June':6, 'July':7, 'August':8, 'September':9, 'October':10
}


async def predict(q:Q):
    # Get the available models.
    models = list(q.app.models.keys())
    val = q.args.models or models[0]
 
    # Show model selection/load inputs.
    q.page['models'] = ui.form_card(box=ui.box('data'), items=[
            ui.combobox(name='models', label='Models', choices=models, value=val),
            ui.buttons(justify='center', items=[
                ui.button(name='load', label='Load Model', primary=True),
            ])
    ])
    await q.page.save()

    # Load selected model if load is hit or prediction in progress.
    if q.args.load or q.args.predict:
        await predict_menu(q, val)

async def predict_menu(q:Q, val:str):
    # Display prediction menu, ask user input for month.
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

    # Make prediction using the loaded model.
    if q.args.predict:
        await predict_results(q, val)

async def predict_results(q:Q, val:str):
    # Get year and month from user input.
    year = q.args.year
    month = months[q.args.month]
    
    # Update map card to notify that predictions are being made.
    q.page['map'] = ui.form_card(box='map', items=[
        ui.progress(label=f'Making predictions for {await get_month_str(month)} {year}')
    ])
    await q.page.save()

    # Make the actual prediction.
    await q.run(model_predict, q, val, year, month)


async def model_predict(q:Q, val:str, year:str, month:int):
    model = q.app.models[val]
    
    # Use the data prep step from the submission notebook.
    X, features = await q.run(get_data, q, path =list(q.app.datasets.keys())[0])
    # Filter test data for the selected year and month.
    test = X[X.year == int(year)]
    test = test[test.month == month]

    # Use the model to predict.
    test['fire_prediction'] = model.predict(test[features])
    fig = show_predictions(test)

    # Convert figure to html.
    html = to_html(fig)

    # Show the predictions on map.
    q.page['map'] = ui.form_card(box='map', items=[
        ui.frame(content=html, height='500px')
    ])
    await q.page.save()


# Util function to get month as str from month int.
async def get_month_str(month: int):
    for key, val in months.items():
        if val == month:
            return key
