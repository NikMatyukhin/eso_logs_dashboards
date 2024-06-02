from dash import Dash


def create_layout() -> list:
    return []


def create_app() -> Dash:
    external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
    app = Dash(__name__, external_stylesheets=external_stylesheets)

    app.layout = create_layout()

    return app
