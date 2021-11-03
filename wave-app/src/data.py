from h2o_wave import main, app, Q, ui, on, data
import pandas as pd
import os

# load app's existing datasets stored in the local file system
async def load_datasets(q: Q):
    q.app. datasets = {}
    data_dir = 'data'

    # for each csv.gz file in the data dir, make a dataframe and save it
    for dataset_file in os.listdir(data_dir):
        # read csv and make dataframe
        path = f'{data_dir}/{dataset_file}'
        df = pd.read_csv(path, parse_dates=['acq_date'])

        # add this dataset to the list of app's datasets
        q.app.datasets[path] = df
