from h2o_wave import main, app, Q, ui

from .ui_utils import init_ui
from .data import load_datasets
from .model import load_models

# a client is a private broswer tab, which stores it's own run-time information
async def init_client(q: Q):
    # render the header and footer
    await init_ui(q)

    # begin application flow with the Data tab
    q.client.tabs = 'data'

    # flag client as initialized
    q.client.initialized = True

    await q.page.save()

# app-level initialization, run-time information shared across all users
async def init_app(q:Q):
    # get the list of available datasets
    await load_datasets(q)

    # get the list of default model(s)
    await load_models(q)

    # flag app as initialized
    q.app.initialized = True
