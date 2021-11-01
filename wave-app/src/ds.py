from h2o_wave import main, app, Q, ui, on, data
import pandas as pd

PRECISION = 1
MIN_FIRE_RECORDS = 2

# Data prep step from the submission notebook (challenge_wildfires/notebook/).
async def get_data(q:Q, path:str):

    aus_fires = pd.read_csv(path, parse_dates=['acq_date'])
    aus_fires['year'] = aus_fires.acq_date.dt.year
    aus_fires['month'] = aus_fires.acq_date.dt.month
    aus_fires.latitude = aus_fires.latitude.round(PRECISION)
    aus_fires.longitude = aus_fires.longitude.round(PRECISION)
    fires = aus_fires.groupby(['latitude', 'longitude', 'year', 'month']).size().reset_index()
    fires.columns = ['latitude', 'longitude', 'year', 'month', 'cnt']

    coords = fires[['latitude', 'longitude']].drop_duplicates()
    times = fires[['year', 'month']].drop_duplicates()
    coords['one'] = 1; times['one'] = 1
    base = pd.merge(coords, times, how='outer', on='one')
    history = base.merge(fires, how='left', on=['latitude', 'longitude', 'year', 'month'])

    history = history.fillna(0)
    history.cnt.value_counts().head()

    history['fire'] = 1 * (history['cnt'] >= MIN_FIRE_RECORDS)

    yearly = history.groupby(['latitude', 'longitude', 'year'])[['cnt', 'fire']].mean().reset_index()
    monthly = history.groupby(['latitude', 'longitude', 'year', 'month'])[['cnt', 'fire']].mean().reset_index()


    last_year = yearly.copy()
    last_year.year += 1
    last_year.columns = ['latitude', 'longitude','year', 'cnt_last_year', 'fire_last_year']
    
    last_year_month = monthly.copy()
    last_year_month.year += 1
    last_year_month.columns = ['latitude', 'longitude', 'year','month', 'cnt_last_year_month', 'fire_last_year_month']
    
    past = yearly.copy()
    past['one'] = 1
    past = history[['latitude', 'longitude', 'year', 'one']].drop_duplicates().merge(
        past, on=['latitude', 'longitude', 'one'])
    past = past[past.year_x < past.year_y]
    past = past.groupby(['latitude', 'longitude', 'year_y'])[['cnt', 'fire']].mean().reset_index()
    past.columns = ['latitude', 'longitude', 'year', 'cnt_past', 'fire_past']
  
    X = history.merge(past, how='left', on=['latitude', 'longitude', 'year'])
    X = X.merge(last_year, how='left', on=['latitude', 'longitude', 'year'])
    X = X.merge(last_year_month, how='left', on=[
                'latitude', 'longitude', 'year', 'month'])
    X = X.drop(columns='one')

    features = ['latitude', 'longitude', 'month', 'cnt_past', 'fire_past', 'cnt_last_year', 'fire_last_year',
        'cnt_last_year_month', 'fire_last_year_month']
    
    return (X, features)
