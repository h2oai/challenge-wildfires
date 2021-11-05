from h2o_wave import main, app, Q, ui
import os
from .ui_utils import make_markdown_table
from .plot import *
from .model import *

# Functions for data tab.

async def data(q:Q):
    # Get existing datasets for the app.
    app_datasets = list(q.app.datasets.keys())
    # Select dataset from user input or the first dataset.
    val = app_datasets[0]
    if q.args.describe:
        val = q.args.datasets

    # Display the head of the dataframe as a ui markdown table.
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

    # Update map card to notify scatter plot is being made.
    q.page['map'] = ui.form_card(box='map', items=[
        ui.progress(label='Making a Scatter Plot...')
    ])
    await q.page.save()

    # Make scatter plot for the 2019-2020 bushfire season.
    fig = await q.run(show_bush_fires, q, df)
    # Convert plotly figure to html.
    html = await q.run(to_html, fig)
    # Render figure's html on on the form card.
    q.page['map'] = ui.form_card(box=ui.box('map', order=2), items=[
        ui.frame(content=html, height='600px')
    ])
    await q.page.save()


# Init existing datasets for the app.
async def load_datasets(q: Q):
    q.app. datasets = {}
    data_dir = 'data'

    # For each csv.gz file in the data dir, make a dataframe and save it.
    for dataset_file in os.listdir(data_dir):
        # Read csv and make dataframe.
        path = f'{data_dir}/{dataset_file}'
        df = pd.read_csv(path, parse_dates=['acq_date'])
        # Add this dataset to the list of app's datasets.
        q.app.datasets[path] = df
