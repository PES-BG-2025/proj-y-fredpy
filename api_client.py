import requests
import tomllib as toml

with open("config.toml", "rb") as file:
    config = toml.load(file)
    

BASE_URL = str(config["app"]["fred_url"])
API_KEY = config["app"]["api_key"]
    
def get_observations(id_serie:str, fecha_inicial, fecha_final):
    '''
    Consume el API de la FRED para obtener observaciones de los datos
    '''
    url = BASE_URL + "/series/observations"
    params = {
        "api_key" : API_KEY,
        "file_type" : "json",
        "series_id" : id_serie,
        "observation_start" : fecha_inicial,
        "observation_end" : fecha_final
    }
    result = requests.get(url, params)
    return result.json()


def get_series_info(series_name:str):
    url = BASE_URL + "/series"
    params = {
        "api_key" : API_KEY,
        "file_type" : "json",
        "series_id" : series_name,
    }
    result = requests.get(url, params)
    return result.json()

#Area de pruebas:

# print(get_series_info("GNPCA"))
# print(get_observations("GNPCA", "2024-01-01", "2025-01-12"))

# print(get_series_info("EXPGS"))
# print(get_observations("EXPGS", "2024-01-01", "2025-01-12"))

# print(get_series_info("IMPGS"))
# print(get_observations("IMPGS", "2024-01-01", "2025-01-12"))
