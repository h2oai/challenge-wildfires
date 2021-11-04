from h2o_wave import main, app, Q, ui, on, data
import pandas as pd
import os

# LOAD APP'S EXISTING DATASETS STORED IN THE LOCAL FILE SYSTEM
async def load_datasets(q: Q):
    q.app. datasets = {}
    data_dir = 'data'

    # FOR EACH CSV.GZ FILE IN THE DATA DIR, MAKE A DATAFRAME AND SAVE IT
    for dataset_file in os.listdir(data_dir):
        # READ CSV AND MAKE DATAFRAME
        path = f'{data_dir}/{dataset_file}'
        df = pd.read_csv(path, parse_dates=['acq_date'])

        # ADD THIS DATASET TO THE LIST OF APP'S DATASETS
        q.app.datasets[path] = df
