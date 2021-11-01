from h2o_wave import main, app, Q, ui

from .ui_utils import *
from .datasets import *
from .initializers import *
from . import get_started, data, model

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
    q.page['meta'] = ui.meta_card(box='', title = 'Challenge Wildfires | H2O Olympics', layouts=[
        # apply layout to all viewport widths
        ui.layout(breakpoint='xs', zones=[
            # predefine app's wrapper height to 100% viewpoer height
            ui.zone(name='main', size='100vh', zones=[
                # zone for the header
                ui.zone(name='header', size='80px'),
                # zone for tabs and persona
                ui.zone('top', direction='row', zones=[
                    ui.zone('menu', size='80%'), ui.zone('persona', size='20%'),
                ]),
                # zone for the actual content and data
                ui.zone(name='body', size='1', zones=[
                    ui.zone(name='data'),
                    # set direction `row` for horizontal cards layout
                    ui.zone(name='model', direction='row', zones=[
                        ui.zone(name='stats'), ui.zone(name='text', size='70%')
                    ]),
                    ui.zone(name='map')
                ]),
                # app footer of fixed sized, aligned in the center
                ui.zone(name='footer', size='60px', align='center')
            ])
        ])
    ])

# handler for Tab content
async def handler(q: Q):
    # clear UI, delete pages/cards of other tabs
    await reset_pages(q)

    # set the current tab to the user-selected tab, otherwise stay on the same tab
    q.client.tab = q.args.tabs or q.client.tab

    # display the menu bar with different tabs
    await render_menu(q)

    # handler for each tab / menu option
    if q.client.tab == 'home':
        await get_started.get_started(q)

    elif q.client.tab == "data":
        await data.data(q)

    elif q.client.tab == "model":
        await model.model(q)
