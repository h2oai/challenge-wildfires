from h2o_wave import main, app, Q, ui, on, data
import lightgbm as lgb
import os

# load app's existing models stored in the local file system
async def load_models(q:Q):
    q.app.models = models = {}
    models_dir = 'models'

    for model_file in os.listdir(models_dir):
        # skip if the file is not a model, ending with `.txt`
        if not model_file.endswith('.txt'):
            continue
        
        # the default model is a lightgbm model, which is initialized 
        model_path = f'{models_dir}/{model_file}'
        model = lgb.basic.Booster(model_file=model_path)
        # FIXME: model.params are not persistent when the model is saved and reloaded
        model.params = {'num_leaves': 10,'max_depth': 8,'objective': 'binary','metric': 'auc','num_iterations': 500,'early_stopping_round': 5}
        
        # save the model in app's models dict
        models[model_path] = model
