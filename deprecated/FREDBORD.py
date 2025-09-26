
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, dash 
from dash.dependencies import Input, Output

# Carga de datos
df_gnpca = pd.read_csv("GNPCA_out.csv")
df_impgs = pd.read_csv("IMPGS_out.csv")
df_expgs = pd.read_csv("EXPGS_out.csv")

# Asegura tipo fecha (por si vienen como string)
for df in (df_gnpca, df_impgs, df_expgs):
    df["date"] = pd.to_datetime(df["date"])
years_all = pd.concat([df_gnpca["date"], df_impgs["date"], df_expgs["date"]]).dt.year
ymin, ymax = int(years_all.min()), int(years_all.max())

# Graficas iniciales
fig_gnpca    = px.line(df_gnpca, x="date", y="value",
                       title="PIB Real (GNPCA) - Fuente: FRED",
                       labels={"date": "Años", "value": "Billones de dólares"})
fig_gnpcQoQ  = px.line(df_gnpca, x="date", y="QoQ",
                       title="GNPCA Variaciones Trimestrales - Fuente: FRED",
                       labels={"date": "Años", "QoQ": "QoQ"})
fig_impgs    = px.line(df_impgs, x="date", y="value",
                       title="IMPORTACIONES (IMPGS) - Fuente: FRED",
                       labels={"date": "Años", "value": "Billones de dólares"})
fig_impgsQoQ = px.line(df_impgs, x="date", y="QoQ",
                       title="IMPGS Variaciones Trimestrales - Fuente: FRED",
                       labels={"date": "Años", "QoQ": "QoQ"})
fig_expgs    = px.line(df_expgs, x="date", y="value",
                       title="EXPORTACIONES (EXPGS) - Fuente: FRED",
                       labels={"date": "Años", "value": "Billones de dólares"})
fig_expgsQoQ = px.line(df_expgs, x="date", y="QoQ",
                       title="EXPGS Variaciones Trimestrales - Fuente: FRED",
                       labels={"date": "Años", "QoQ": "QoQ"})

# App Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Estadísticas Macroeconómicas de USA"),
    html.H2("Federal Reserve Bank"),

    # Filtro de años
    html.Div([
        html.Label("Rango de años"),
        dcc.RangeSlider(
            id="year-range",
            min=ymin, max=ymax, step=1,
            value=[ymin, ymax],
            marks={y: str(y) for y in range(ymin, ymax+1, max(1, (ymax-ymin)//8))}
        )
    ], style={"margin": "10px 30px"}),
    html.Div([
        dcc.Graph(id="gnpca-graph",        figure=fig_gnpca),
        dcc.Graph(id="gnpca-qoq-graph",    figure=fig_gnpcQoQ),
        dcc.Graph(id="expgs-graph",        figure=fig_expgs),
        dcc.Graph(id="expgs-qoq-graph",    figure=fig_expgsQoQ),
        dcc.Graph(id="impgs-graph",        figure=fig_impgs),
        dcc.Graph(id="impgs-qoq-graph",    figure=fig_impgsQoQ),
    ], style={"display": "grid", "gridGap": "20px", "gridTemplateColumns": "1fr 1fr"})
], style={"textAlign": "center"})

# Callback: actualiza las 6 figuras según el rango de años
@app.callback(
    Output('gnpca-graph', 'figure'),
    Output('gnpca-qoq-graph', 'figure'),
    Output('expgs-graph', 'figure'),
    Output('expgs-qoq-graph', 'figure'),
    Output('impgs-graph', 'figure'),
    Output('impgs-qoq-graph', 'figure'),
    Input('year-range', 'value')
)
def update_figures(year_range):
    start_year, end_year = year_range

    m_g = (df_gnpca["date"].dt.year >= start_year) & (df_gnpca["date"].dt.year <= end_year)
    m_i = (df_impgs["date"].dt.year >= start_year) & (df_impgs["date"].dt.year <= end_year)
    m_e = (df_expgs["date"].dt.year >= start_year) & (df_expgs["date"].dt.year <= end_year)

    fig_gnpca = px.line(df_gnpca.loc[m_g], x="date", y="value",
                        title="PIB Real (GNPCA) - Fuente: FRED",
                        labels={"date": "Fecha", "value": "Billones de dólares"})
    fig_gnpcQoQ = px.line(df_gnpca.loc[m_g], x="date", y="QoQ",
                          title="GNPCA Variaciones Trimestrales - Fuente: FRED",
                          labels={"date": "Fecha", "QoQ": "QoQ"})
    fig_expgs = px.line(df_expgs.loc[m_e], x="date", y="value",
                        title="EXPORTACIONES (EXPGS) - Fuente: FRED",
                        labels={"date": "Fecha", "value": "Billones de dólares"})
    fig_expgsQoQ = px.line(df_expgs.loc[m_e], x="date", y="QoQ",
                           title="EXPGS Variaciones Trimestrales - Fuente: FRED",
                           labels={"date": "Fecha", "QoQ": "QoQ"})
    fig_impgs = px.line(df_impgs.loc[m_i], x="date", y="value",
                        title="IMPORTACIONES (IMPGS) - Fuente: FRED",
                        labels={"date": "Fecha", "value": "Billones de dólares"})
    fig_impgsQoQ = px.line(df_impgs.loc[m_i], x="date", y="QoQ",
                           title="IMPGS Variaciones Trimestrales - Fuente: FRED",
                           labels={"date": "Fecha", "QoQ": "QoQ"})

    return fig_gnpca, fig_gnpcQoQ, fig_expgs, fig_expgsQoQ, fig_impgs, fig_impgsQoQ

# Run app
if __name__ == "__main__":
    app.run(debug=True)