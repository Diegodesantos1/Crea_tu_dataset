import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt
import numpy as np
class Graficos:
    def grafico():
        datos = pd.read_csv("Dataset.csv", sep =",")
        lista_gravedad = list(datos["gravity"])
        lista_nombres = list(datos["eName"])
        gravedad_util, nombres_util = [], []
        print(lista_gravedad)
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
        tierra = datos.iloc[88]
        venus = datos.iloc[263]
        saturno= datos.iloc[228]
        urano = datos.iloc[260]
        print(tierra)
        print(saturno)
        print(urano)
        print(venus)

Graficos.grafico()