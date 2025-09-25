
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import api_client
import plotly.express as px  # Reemplaza a seaborn y matplotlib
import dash
from dash import dcc, html


# def get_fred_series(series_id, start=None, end=None):
#   data = api_client.get_observations(series_id, start, end)
#   df = pd.DataFrame(data["observations"])
#   df["date"] = pd.to_datetime(df["date"])
#   df["value"] = pd.to_numeric(df["value"], errors="coerce")
#   return df, data.get("count", None)

# def plot_series(df, title, ylabel):
#   plt.figure(figsize=(12, 6))
#   sns.lineplot(x="date", y="value", data=df)
#   plt.title(title, fontsize=14)
#   plt.xlabel("Fecha")
#   plt.ylabel(ylabel)
#   plt.show()

# # PIB real USA
# df_gnpca, _ = get_fred_series("GNPCA")
# plot_series(df_gnpca, "PIB Real (GNPCA) - Fuente: FRED", "Billones de dólares")

# # Importaciones de USA
# df_impgs, count_impgs = get_fred_series("IMPGS", start="2000-01-01", end="2025-07-31")
# plot_series(df_impgs, "IMPORTACIONES (IMPGS) - Fuente: FRED", "Billones de dólares")
# print(f"Importaciones count: {count_impgs}")

# # Exportaciones de USA
# df_expgs, _ = get_fred_series("EXPGS", start="2000-01-01", end="2025-07-31")
# plot_series(df_expgs, "EXPORTACIONES (EXPGS) - Fuente: FRED", "Billones de dólares")



# Importa las funciones del cliente
import api_client 

# --- 1) Wrapper para convertir JSON -> DataFrame ---
def get_fred_series(series_id: str, start: str | None = None, end: str | None = None):
    """
    Usa api_client.get_observations para traer datos y devolver (DataFrame, count).
    """
    data = api_client.get_observations(series_id, start, end)
    obs = data.get("observations", [])
    df = pd.DataFrame(obs)
    if df.empty:
        # asegura columnas esperadas para que Plotly no falle
        df = pd.DataFrame(columns=["date", "value"])
        return df, 0
    df["date"] = pd.to_datetime(df["date"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    return df, int(data.get("count", len(df)))

# --- 2) Carga de datos ---
print("Cargando datos desde la API de FRED...")
df_gnpca, hola= get_fred_series("GNPCA", start="2000-01-01", end="2024-07-31")
df_impgs, count_impgs = get_fred_series("IMPGS", start="2000-01-01", end="2025-07-31")
df_expgs, hola= get_fred_series("EXPGS", start="2000-01-01", end="2025-07-31")
print(f"Datos cargados. Se encontraron {count_impgs} observaciones de importaciones.")
print(f"GNPCA {df_gnpca.shape}")
# --- 3) Figuras Plotly ---
fig_gnpca = px.line(
    df_gnpca, x="date", y="value",
    title="PIB Real (GNPCA) - Fuente: FRED",
    labels={"date": "Fecha", "value": "Billones de dólares"}
)
fig_impgs = px.line(
    df_impgs, x="date", y="value",
    title="IMPORTACIONES (IMPGS) - Fuente: FRED",
    labels={"date": "Fecha", "value": "Billones de dólares"}
)
fig_expgs = px.line(
    df_expgs, x="date", y="value",
    title="EXPORTACIONES (EXPGS) - Fuente: FRED",
    labels={"date": "Fecha", "value": "Billones de dólares"}
)

# --- 4) App Dash ---
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1('Indicadores Económicos de EE.UU.', style={'textAlign': 'center'}),
    dcc.Graph(id='pib-graph', figure=fig_gnpca),
    dcc.Graph(id='importaciones-graph', figure=fig_impgs),
    dcc.Graph(id='exportaciones-graph', figure=fig_expgs),
])

# --- 5) Run ---
if __name__ == "__main__":
    app.run(debug=True) 