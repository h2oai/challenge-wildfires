from h2o_wave import main, app, Q, ui

from .ui_utils import init_ui
from .data import load_datasets
from .model import load_models

# A client is a private broswer tab, which stores it's own run-time information.
async def init_client(q: Q):
    # Render the header and footer.
    await init_ui(q)

    # Begin application flow with the data tab.
    q.client.tabs = 'data'

    # Flag client as initialized.
    q.client.initialized = True

    await q.page.save()

# App-level initialization, run-time information shared across all users.
async def init_app(q:Q):
    # Get the list of available datasets.
    await load_datasets(q)

    # Get the list of default model(s).
    await load_models(q)

    # Flag app as initialized.
    q.app.initialized = True
