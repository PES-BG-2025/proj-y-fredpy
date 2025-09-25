import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

API_KEY = "6f87a4be50cef4ad00bd25a16db9f1b0"
BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

def get_fred_series(series_id, start=None, end=None):
  params = {
    "api_key": API_KEY,
    "file_type": "json",
    "series_id": series_id
  }
  if start:
    params["observation_start"] = start
  if end:
    params["observation_end"] = end
  response = requests.get(BASE_URL, params=params)
  response.raise_for_status()
  data = response.json()
  df = pd.DataFrame(data["observations"])
  df["date"] = pd.to_datetime(df["date"])
  df["value"] = pd.to_numeric(df["value"], errors="coerce")
  return df, data.get("count", None)

def plot_series(df, title, ylabel):
  plt.figure(figsize=(12, 6))
  sns.lineplot(x="date", y="value", data=df)
  plt.title(title, fontsize=14)
  plt.xlabel("Fecha")
  plt.ylabel(ylabel)
  plt.show()

# PIB real USA
df_gnpca, _ = get_fred_series("GNPCA")
plot_series(df_gnpca, "PIB Real (GNPCA) - Fuente: FRED", "Billones de dólares")

# Importaciones de USA
df_impgs, count_impgs = get_fred_series("IMPGS", start="2000-01-01", end="2025-07-31")
plot_series(df_impgs, "IMPORTACIONES (IMPGS) - Fuente: FRED", "Billones de dólares")
print(f"Importaciones count: {count_impgs}")

# Exportaciones de USA
df_expgs, _ = get_fred_series("EXPGS", start="2000-01-01", end="2025-07-31")
plot_series(df_expgs, "EXPORTACIONES (EXPGS) - Fuente: FRED", "Billones de dólares")
