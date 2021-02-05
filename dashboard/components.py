import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


def sidebar() -> html.Div:
    """Example sidebar from:
    https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/page-2""" # noqa

    # the style arguments for the sidebar. We use position:fixed and a fixed width
    SIDEBAR_STYLE = {
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "16rem",
        "padding": "2rem 1rem",
        "background-color": "#f8f9fa",
    }

    sidebar = html.Div(
        [
            html.H2("Sidebar", className="display-4"),
            html.Hr(),
            html.P("A simple sidebar layout with navigation links", className="lead"),
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/", active="exact"),
                    dbc.NavLink("Page 1", href="/page-1", active="exact"),
                    dbc.NavLink("Page 2", href="/page-2", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        style=SIDEBAR_STYLE,
    )

    return sidebar


def content() -> html.Div:
    """Content part of the above mentioned sidebar."""

    # the styles for the main content position it to the right of the sidebar and
    # add some padding.
    CONTENT_STYLE = {
        "margin-left": "18rem",
        "margin-right": "2rem",
        "padding": "2rem 1rem",
    }

    return html.Div(id="page-content", style=CONTENT_STYLE)


def kmeans_graph(iris: pd.DataFrame) -> dbc.Container:
    """Example k-means graph from:
    https://dash-bootstrap-components.opensource.faculty.ai/examples/iris/"""

    controls = dbc.Card(
        [
            dbc.FormGroup(
                [
                    dbc.Label("X variable"),
                    dcc.Dropdown(
                        id="x-variable",
                        options=[{"label": col, "value": col} for col in iris.columns],
                        value="sepal length (cm)",
                    ),
                ]
            ),
            dbc.FormGroup(
                [
                    dbc.Label("Y variable"),
                    dcc.Dropdown(
                        id="y-variable",
                        options=[{"label": col, "value": col} for col in iris.columns],
                        value="sepal width (cm)",
                    ),
                ]
            ),
            dbc.FormGroup(
                [
                    dbc.Label("Cluster count"),
                    dbc.Input(id="cluster-count", type="number", value=3),
                ]
            ),
        ],
        body=True,
    )

    graph_container = dbc.Container(
        [
            html.H1("Iris k-means clustering"),
            html.Hr(),
            dbc.Row(
                [
                    dbc.Col(controls, md=4),
                    dbc.Col(dcc.Graph(id="cluster-graph"), md=8),
                ],
                align="center",
            ),
        ],
        fluid=True,
    )

    return graph_container
