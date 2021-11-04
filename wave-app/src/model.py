from h2o_wave import main, app, Q, ui, on, data
import lightgbm as lgb
import os

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