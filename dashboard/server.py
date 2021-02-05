import dash_bootstrap_components as dbc
from dash import Dash
from flask import Flask

server = Flask("dashboard-app")
app = Dash(
    server=server,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)
