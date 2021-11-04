
from h2o_wave import main, app, Q, ui
import lightgbm as lgb
import os
from .ui_utils import *
from .plot import *

# FUNCTIONS FOR MODEL TAB

models_dir = 'models'

async def model(q:Q):
    # GET THE AVAILABLE MODELS
    models = list(q.app.models.keys())
    val = q.args.models or models[0]

    # SHOW MODEL SELECTION/LOAD INPUTS
    q.page['models'] = ui.form_card(box=ui.box('data'), items=[
            ui.combobox(name='models', label='Models', choices=models, value=val),
            ui.buttons(justify='center', items=[
                ui.button(name='load', label='Load', primary=True),
            ])
    ])
    await q.page.save()

    # LOAD SELECTED MODEL
    await load(q, val)

async def load(q:Q, val: str):
    model = q.app.models[val]
    # SHOW MODEL PARAMS WITH STAT CARDS
    q.page['metrics'] = ui.form_card(box='data', items=[
            ui.stats(justify='around', items=[
                *[ui.stat(f'{key}', f'{val}') for (key, val) in model.params.items()]
            ])
        ]
    )

    # UPDATE MAP CARD TO NOTIFY BAR CHART IS BEING MADE
    q.page['map'] = ui.form_card(box='map', items=[
        ui.progress(label='Preparing bar chart...')
    ])
    await q.page.save()

    # LOAD BAR CHART FOR THE FEATURE IMPORTANCE FOR THE SELECTED MODEL
    bar_chart = f"{val.strip('.txt')}_features.html"
    q.page['map'] = ui.form_card(box='map', items=[
        ui.frame(content=(open(bar_chart).read()), height='600px')
    ])
    await q.page.save()

# LOAD APP'S EXISTING MODELS STORED IN THE LOCAL FILE SYSTEM
async def load_models(q:Q):
    q.app.models = models = {}
    models_dir = 'models'

    for model_file in os.listdir(models_dir):
        # SKIP IF THE FILE IS NOT A MODEL, ENDING WITH `.TXT`
        if not model_file.endswith('.txt'):
            continue
        
        # THE DEFAULT MODEL IS A LIGHTGBM MODEL, WHICH IS INITIALIZED
        model_path = f'{models_dir}/{model_file}'
        model = lgb.basic.Booster(model_file=model_path)
        model_params_file = f"{model_path.strip('.txt')}.params"
        model.params = await get_model_params(model_params_file)
        models[model_path] = model

        # SAVE THE MODEL IN APP'S MODELS DICT
        models[model_path] = model


# READ MODEL_PARAMS FOR A LOCAL MODEL FROM FILE
async def get_model_params(model_params_file: str):
    with open(model_params_file) as f:
        contents = f.readlines()

    params = {}
    for line in contents:
        param, param_val = line.strip('\n').split(":")
        params[param] = param_val

    return params