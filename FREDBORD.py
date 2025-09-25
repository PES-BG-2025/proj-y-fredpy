import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import api_client


def get_fred_series(series_id, start=None, end=None):
  data = api_client.get_observations(series_id, start, end)
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
