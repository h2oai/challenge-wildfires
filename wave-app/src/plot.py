from h2o_wave import main, app, Q, ui
import pandas as pd
import plotly
import plotly.graph_objects as go
from plotly.missing_ipywidgets import FigureWidget

# Use plotly to make scatter plot for dataset description.
def make_scatter_plot(q:Q, df: pd.DataFrame):
    fig = go.Figure(
        data=go.Scattergeo(lat=df['latitude'], lon=df['longitude']),
        layout=go.Layout(
            title='Australia Fire Daily', title_font_color = '#FEC925',
            paper_bgcolor='rgba(0, 0, 0, 0)',
            margin_r=10, margin_l=10, margin_t = 50, margin_b=10
    )).update_geos(
        fitbounds='locations'
    )
    fig.update_traces(marker_color='#E25822')

    return fig

# Convert plotly figure to html.
def to_html(fig:FigureWidget):
    html = plotly.io.to_html(fig)
    return html
