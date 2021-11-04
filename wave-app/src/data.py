from h2o_wave import main, app, Q, ui
import os
from .ui_utils import make_markdown_table
from .plot import *
from .model import *

# FUNCTIONS FOR DATA TAB

async def data(q:Q):
    # GET EXISTING DATASETS FOR THE APP
    app_datasets = list(q.app.datasets.keys())
    # SELECT DATASET FROM USER INPUT OR THE FIRST DATASET
    val = app_datasets[0]
    if q.args.describe:
        val = q.args.datasets

    # DISPLAY THE HEAD OF THE DATAFRAME AS A UI MARKDOWN TABLE
    df = q.app.datasets[val]
    df_head = df.head(10)
    df_table = await make_markdown_table(
        fields=df_head.columns.tolist(),
        rows=df_head.values.tolist()
    )
    q.page['df'] = ui.form_card(box=ui.box('data'), items=[
        ui.combobox(name='datasets', label='Datasets', choices=app_datasets, value=val),
        ui.buttons(justify='center', items=[
            ui.button(name='describe', label='Describe', primary=True),
        ]),
        ui.separator(),
        ui.text(df_table),
    ])

    # UPDATE MAP CARD TO NOTIFY SCATTER PLOT IS BEING MADE
    q.page['map'] = ui.form_card(box='map', items=[
        ui.progress(label='Making a Scatter Plot...')
    ])
    await q.page.save()

    # MAKE SCATTER PLOT FOR THE FIRST 10000 DATAPOINTS
    fig = await q.run(make_scatter_plot, q, df[:10000])
    # CONVERT PLOTLY FIGURE TO HTML
    html = await q.run(to_html, fig)
    # RENDER FIGURE'S HTML ON ON THE FORM CARD
    q.page['map'] = ui.form_card(box=ui.box('map', order=2), items=[
        ui.frame(content=html, height='600px')
    ])
    await q.page.save()


# INIT EXISTING DATASETS FOR THE DAPP
async def load_datasets(q: Q):
    q.app. datasets = {}
    data_dir = 'data'

    # FOR EACH CSV.GZ FILE IN THE DATA DIR, MAKE A DATAFRAME AND SAVE IT
    for dataset_file in os.listdir(data_dir):
        # READ CSV AND MAKE DATAFRAME
        path = f'{data_dir}/{dataset_file}'
        df = pd.read_csv(path, parse_dates=['acq_date'])
        # ADD THIS DATASET TO THE LIST OF APP'S DATASETS
        q.app.datasets[path] = df
