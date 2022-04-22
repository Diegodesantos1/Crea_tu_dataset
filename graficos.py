import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt
class Graficos:
    def grafico():
        datos = pd.read_csv("Dataset.csv", sep =",")
        datos_exo = pd.read_csv("PS_2022.04.22_04.00.41.csv", sep =",")
        lista_gravedad = list(datos["gravity"])
        lista_nombres = list(datos["eName"])
        lista_gravedad_exo = list(datos_exo["st_logg"])
        lista_nombres_exo = list(datos_exo["pl_name"])
        gravedad_util, nombres_util = [], []
        for i in range (len(lista_gravedad)):
            if 8.0 < lista_gravedad[i] <10.5:
                gravedad_util.append(lista_gravedad[i])
                nombres_util.append(lista_nombres[i])
        print(gravedad_util)
        print("son las gravedades correspondientes a los siguientes nombres:")
        print(nombres_util)
        utiles_porcentaje = 0.01509433962
        no_utiles_porcentaje = 1 -utiles_porcentaje
        nombre = ["Gravedad válida", "Gravedad no válida"] ; parametros = [utiles_porcentaje, no_utiles_porcentaje] ; colores = ["#AAF683", "#EE6055"]
        plt.subplot(1,2,1)
        plt.bar (nombres_util, gravedad_util, color = ["r", "g", "b", "y"])
        plt.subplot (1,2,2)
        plt.pie (parametros, labels=nombre, colors = colores)
        plt.show()
        tierra = datos.iloc[86]
        venus = datos.iloc[261]
        saturno= datos.iloc[226]
        urano = datos.iloc[258]
        print(f"\n Los datos de la tierra son {tierra}")
        print(f"\n Los datos de venus son {venus}")
        print(f"\n Los datos de saturno son {saturno}")
        print(f"\n Los datos de urano son {urano}")

Graficos.grafico()