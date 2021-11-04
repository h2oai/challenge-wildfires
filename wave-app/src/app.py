from h2o_wave import main, app, Q, ui

from .ui_utils import *
from .initializers import *
from . import data, model, predict

@app('/')
async def serve(q: Q):
    # INITIALIZE APP AND CLIENT IF NOT ALREADY INITIALIZED
    if not q.app.initialized:
        await init_app(q)

    if not q.client.initialized:
        await init_client(q)

    # ATTACH A FLEX LAYOUT FOR THE CARDS
    await layouts(q)

    # CHECK WHICH TAB IS ACTIVE AND INVOKE THE CORRESPONDING HANDLER
    await handler(q)

# A FLEX LAYOUT FOR AN ADAPTIVE UI
async def layouts(q:Q):
    q.page['meta'] = ui.meta_card(box='', theme='h2o-dark', title = 'Challenge Wildfires | H2O Olympics', layouts=[
        # APPLY LAYOUT TO ALL VIEWPORT WIDTHS
        ui.layout(breakpoint='xs', zones=[
            # PREDEFINE APP'S WRAPPER HEIGHT TO 100% VIEWPOER HEIGHT
            ui.zone(name='main', size='100vh', zones=[
                # zone for the header
                ui.zone(name='header', size='80px'),
                # ZONE FOR NAVIGATION MENU
                ui.zone('tabs'),
                # ZONE FOR THE ACTUAL CONTENT AND DATA
                ui.zone(name='body', size='1', zones=[
                    ui.zone(name='data'),
                    ui.zone('predict', align='center'),
                    ui.zone(name='map'),
                ]),
                # APP FOOTER OF FIXED SIZED, ALIGNED IN THE CENTEr
                ui.zone(name='footer', size='120px', align='center')
            ])
        ])
    ])

# HANDLER FOR TAB CONTENT
async def handler(q: Q):
    # CLEAR UI, DELETE PAGES/CARDS OF OTHER TABS
    await reset_pages(q)

    # SET THE CURRENT TAB TO THE USER-SELECTED TAB, OTHERWISE STAY ON THE SAME TAB
    q.client.tabs = q.args.tabs or q.client.tabs

    # DISPLAY THE MENU BAR WITH DIFFERENT TABS
    await render_menu(q)

    # HANDLER FOR EACH TAB / MENU OPTION
    if q.client.tabs == "data":
        await data.data(q)

    elif q.client.tabs == "model":
        await model.model(q)

    elif q.client.tabs == "predict":
        await predict.predict(q)
