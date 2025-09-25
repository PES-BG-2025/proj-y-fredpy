import api_client
import pandas as pd


def transformar_csv(data_dict:dict, filename:str):
    """
    Usa los datos de observaciones para computar la columna QoQ
    """
    df_observaciones = pd.DataFrame(data_dict["observations"])
    num_observaciones = data_dict["count"]

    df_observaciones["QoQ"] = None
    for i in range(1, num_observaciones): 
        print(df_observaciones.at[i-1,"value"])
        df_observaciones.loc[i, "QoQ"] = cambio_porcentual(
                                            float(df_observaciones.at[i-1,"value"]), 
                                            float(df_observaciones.at[i, "value"])
                                        )
    
    df_observaciones.to_csv(filename, index=False)

def cambio_porcentual(valor_t0:float, valor_t1:float):
    variacion = (valor_t1 - valor_t0) / valor_t0
    variacion_porcentual = variacion * 100
    return round(variacion_porcentual,2)

def actualizar_archivos_csv() :
    transformar_csv(api_client.get_observations("EXPGS", "2000-01-01", "2025-01-12"), "EXPGS_out.csv")
    transformar_csv(api_client.get_observations("IMPGS", "2000-01-01", "2025-01-12"), "IMPGS_out.csv")
    transformar_csv(api_client.get_observations("GNPCA", "2000-01-01", "2025-01-12"), "GNPCA_out.csv")

