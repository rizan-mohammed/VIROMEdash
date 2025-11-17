import dash
import dash_bootstrap_components as dbc
from operator import index
from dash import Dash, Input, Output, html, dcc, State, dash_table, callback, clientside_callback
from dash.exceptions import PreventUpdate


layout = html.Div([
    # NAVBAR (sticky)
    dbc.Navbar(
        dbc.Container([
            dbc.Row([
                dbc.Col(dbc.NavbarBrand("VIROMEdash", className="ms-2"), width="auto"),
                dbc.Col(
                    dbc.Nav([
                        dbc.NavLink("HOME", href="/", style={"color": "#fff", "marginLeft": "1rem"}),
                        dbc.NavLink("USER MANUAL", href="https://viromedash.readthedocs.io", style={"color": "#fff", "marginRight": "1rem"}),
                        dbc.NavLink("SEARCH", href="#", style={"color": "#fff"})
                    ], navbar=True),
                    className="ms-auto"
                ),
                dbc.Col(
                    dbc.Checklist(
                        options=[{"label": "Night Mode 🌙", "value": 1}],
                        value=[],
                        id="night-mode-toggle",
                        switch=True,
                        inline=True
                    ),
                    width="auto",
                    className="ms-3"
                )
            ], align="center", className="w-100")
        ], fluid=True),
        color="dark",
        dark=True,
        sticky="top",
        style={"marginBottom": "2rem"}
    ),

    # HEADER
    html.Div([
        html.H1("Global Virome Sequence Metadata Visualizer"),
        html.P([
            "A visualizer for viral sequence metadata from the records in ",
            dbc.Badge("NCBI Virus Database", color="success", href="https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/", style={"fontSize": "1.2rem"})
        ], style={"fontSize": "1.6rem"})
    ], className="text-center my-4"),

    # DASHBOARD CARDS 3x2
    dbc.Container([
        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Species/Genus/Family", className="card-title"),
                    html.P("Find out the number of reports over years, host-organisms, geographic locations and isolation-sources of a viral species/genus/family.", className="card-text"),
                    dcc.Link(dbc.Button("Click Here →", color="success", className="btn"), href="/species")
                ])
            ], className="dashboard-card mb-4"), md=4),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Host species", className="card-title"),
                    html.P("Find out the reported viral species infecting a host-organism.", className="card-text"),
                    dcc.Link(dbc.Button("Click Here →", color="success", className="btn"), href="/host")
                ])
            ], className="dashboard-card mb-4"), md=4),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Collection date", className="card-title"),
                    html.P("Find out the reported viral species in a specific time interval.", className="card-text"),
                    dcc.Link(dbc.Button("Click Here →", color="success", className="btn"), href="/date")
                ])
            ], className="dashboard-card mb-4"), md=4)
        ]),

        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Country/continent", className="card-title"),
                    html.P("Find out the reported viral species in a country/continent.", className="card-text"),
                    dcc.Link(dbc.Button("Click Here →", color="success", className="btn"), href="/geography")
                ])
            ], className="dashboard-card mb-4"), md=4),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Baltimore Classification", className="card-title"),
                    html.P("Sunburst chart to abundance of reported viral sequences based on the Baltimore classification.", className="card-text"),
                    dcc.Link(dbc.Button("Click Here →", color="success", className="btn"), href="/baltimore")
                ])
            ], className="dashboard-card mb-4"), md=4),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Self catalogue", className="card-title"),
                    html.P("This tool helps you to find out/visualize the metadata of uploaded viral sequences.", className="card-text"),
                    dcc.Link(dbc.Button("Click Here →", color="success", className="btn"), href="/self-catalogue")
                ])
            ], className="dashboard-card mb-4"), md=4)
        ])
    ], fluid=True),

    # Last update
    html.Div(html.H5("Last update: January 2023", style={"color": "#16a085", "fontWeight": "600"}), className="text-center my-4")
], id="app-body")


# for night mode :)
@callback(
    Output("app-body", "className"),
    Input("night-mode-toggle", "value")
)
def toggle_night_mode(value):
    if value and 1 in value:
        return "night-mode"
    return ""

