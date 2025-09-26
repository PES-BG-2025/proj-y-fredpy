# Import packages
from dash import Dash, html, dash_table, dcc
import plotly.express as px
import pandas as pd

# Incorporate data
df_imp = pd.read_csv("IMPGS_out.csv")
df_exp = pd.read_csv("EXPGS_out.csv")
df_pnb = pd.read_csv("GNPCA_out.csv")

# Initialize the app
app = Dash()

fig_imp = px.line(
        df_imp, 
        x="date", 
        y="value",
        title="Imports of Good and Services"
    )

fig_exp = px.line(
        df_exp, 
        x="date", 
        y="value",
        title="Exports of Good and Services"
    )

fig_pnb = px.line(
        df_pnb, 
        x="date", 
        y="value",
        title="Real Gross National Product"
    )
# App layout
app.layout = html.Div(children=[

    html.H1(children="Dashboard Federal Reserve Bank"),
    html.H2(children="Dashboard"),
    html.Div([
        dcc.Graph(
            id="imports-graph",
            figure=fig_imp
        ),
        dcc.Graph(
            id="imports-graph",
            figure=fig_exp
        ),
        dcc.Graph(
            id="imports-graph",
            figure=fig_pnb
        ),
    ], style={
        "display": "grid",
        "gridGap": "20px",
        "gridTemplateColumns": "1fr 1fr 1fr"
    })
], style={"textAlign":"center"})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)