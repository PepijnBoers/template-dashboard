import dash_core_components as dcc
import dash_html_components as html

from . import sidebar
from .server import app, server

# Define web app layout
app.layout = html.Div([dcc.Location(id="url"), sidebar.sidebar(), sidebar.content()])
