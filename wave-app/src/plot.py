import numpy as np
import pandas as pd
import plotly
import plotly.graph_objects as go
from plotly.missing_ipywidgets import FigureWidget

AUS_LAT_RANGE = (-40, -9)
AUS_LON_RANGE = (112, 155)

GEO = dict(
    showland=True,
    landcolor="rgb(128, 128, 128)",
    subunitcolor="rgb(255, 255, 255)",
    countrycolor="rgb(255, 255, 255)",
    showlakes=True,
    lakecolor="rgb(0, 0, 0)",
    showrivers=True,
    rivercolor="rgb(0, 0, 0)",
    showocean=True,
    oceancolor="rgb(0, 0, 0)",
    showsubunits=True,
    showcountries=True,
    resolution=50,
    lonaxis=dict(
        showgrid=True,
        gridwidth=0.5,
        range=AUS_LON_RANGE,
        dtick=5
    ),
    lataxis=dict(
        showgrid=True,
        gridwidth=0.5,
        range=AUS_LAT_RANGE,
        dtick=5
    )
)


# Use plotly to make scatter plot for dataset description.
def show_bush_fires(df: pd.DataFrame):
    aus_fires = df.copy()
    aus_fires.latitude = aus_fires.latitude.round(1)
    aus_fires.longitude = aus_fires.longitude.round(1)
    sample = aus_fires[(aus_fires.acq_date >= '2019-09-01') & (aus_fires.acq_date <= '2020-03-31')]
    sample = sample.groupby(['latitude', 'longitude']).size().reset_index()
    sample.columns = ['latitude', 'longitude', 'fire_cnt']
    sample = sample[sample.fire_cnt > 3]
    fig = go.Figure(data=go.Scattergeo(
        lat=sample['latitude'],
        lon=sample['longitude'],
        marker=dict(
            color=sample['fire_cnt'],
            reversescale=True,
            opacity=0.8,
            line=dict(width=0),
            size=np.log(sample.fire_cnt) + 1,
        ),
    ))
    fig.update_layout(
        geo=GEO,
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=10, r=10, t=50, b=10),
    )
    return fig


# Convert plotly figure to html.
def to_html(fig: FigureWidget):
    config = {'scrollZoom': False, 'showLink': False, 'displayModeBar': False}
    return plotly.io.to_html(fig, validate=False, include_plotlyjs='cdn', config=config)


# Use plotly to make scatter plot for prediction visualization.
def show_predictions(df: pd.DataFrame):
    worst = df[df.fire_prediction > 0.1]
    fig = go.Figure(data=go.Scattergeo(
        lat=worst['latitude'],
        lon=worst['longitude'],
        marker=dict(
            color=worst['fire_prediction'],
            reversescale=True,
            opacity=0.8,
            line=dict(width=0),
            size=3,
        ),
    ))
    fig.update_layout(
        geo=GEO,
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=10, r=10, t=10, b=10),
    )
    return fig
