from h2o_wave import main, app, Q, ui

from .ui_utils import init_ui
from .data import load_datasets
from .model import load_models

# A CLIENT IS A PRIVATE BROSWER TAB, WHICH STORES IT'S OWN RUN-TIME INFORMATION
async def init_client(q: Q):
    # RENDER THE HEADER AND FOOTER
    await init_ui(q)

    # BEGIN APPLICATION FLOW WITH THE DATA TAB
    q.client.tabs = 'data'

    # FLAG CLIENT AS INITIALIZED
    q.client.initialized = True

    await q.page.save()

# APP-LEVEL INITIALIZATION, RUN-TIME INFORMATION SHARED ACROSS ALL USERS
async def init_app(q:Q):
    # GET THE LIST OF AVAILABLE DATASETS
    await load_datasets(q)

    # GET THE LIST OF DEFAULT MODEL(S)
    await load_models(q)

    # FLAG APP AS INITIALIZED
    q.app.initialized = True
