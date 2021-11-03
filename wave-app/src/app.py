from h2o_wave import main, app, Q, ui

from .ui_utils import *
from .initializers import *
from . import data, model, predict

@app('/')
async def serve(q: Q):
    # initialize app and client if not already initialized
    if not q.app.initialized:
        await init_app(q)

    if not q.client.initialized:
        await init_client(q)

    # attach a Flex layout for the cards
    await layouts(q)

    # check which Tab is active and invoke the corresponding handler
    await handler(q)

# a Flex layout for an adaptive UI
async def layouts(q:Q):
    q.page['meta'] = ui.meta_card(box='', theme='h2o-dark', title = 'Challenge Wildfires | H2O Olympics', layouts=[
        # apply layout to all viewport widths
        ui.layout(breakpoint='xs', zones=[
            # predefine app's wrapper height to 100% viewpoer height
            ui.zone(name='main', size='100vh', zones=[
                # zone for the header
                ui.zone(name='header', size='80px'),
                # zone for navigation menu
                ui.zone('tabs'),
                # zone for the actual content and data
                ui.zone(name='body', size='1', zones=[
                    ui.zone(name='data'),
                    ui.zone('predict', align='center'),
                    ui.zone(name='map'),
                ]),
                # app footer of fixed sized, aligned in the center
                ui.zone(name='footer', size='120px', align='center')
            ])
        ])
    ])

# handler for Tab content
async def handler(q: Q):
    # clear UI, delete pages/cards of other tabs
    await reset_pages(q)

    # set the current tab to the user-selected tab, otherwise stay on the same tab
    q.client.tabs = q.args.tabs or q.client.tabs

    # display the menu bar with different tabs
    await render_menu(q)

    # handler for each tab / menu option
    if q.client.tabs == "data":
        await data.data(q)

    elif q.client.tabs == "model":
        await model.model(q)

    elif q.client.tabs == "predict":
        await predict.predict(q)
