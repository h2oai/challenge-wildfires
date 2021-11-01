from h2o_wave import main, app, Q, ui

from .ui_utils import init_ui
from .datasets import get_datasets
from .model import get_models

# a client is a private broswer tab, which stores it's own run-time information
async def init_client(q: Q):
    # render the header and footer
    await init_ui(q)

    # render user persona
    q.page['persona'] = ui.form_card(box='persona', items=[
            ui.persona(title='User', subtitle='Team', initials_color='#bbc605', size='s')
    ])

    # set the app theme to neon / dark-mode
    q.page['meta'].theme = 'neon'

    # begin application flow with the Data tab
    q.client.tab = 'data'

    # flag client as initialized
    q.client.initialized = True

# app-level initialization, run-time information shared across all users
async def init_app(q:Q):
    # get the list of available datasets
    await get_datasets(q)

    # get the list of default model(s)
    await get_models(q)

    # flag app as initialized
    q.app.initialized = True