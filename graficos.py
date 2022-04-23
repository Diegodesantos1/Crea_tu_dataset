import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt
import numpy as np
class Graficos:
    def grafico():
        datos = pd.read_csv("Dataset.csv", sep =",")
        datos_exo = pd.read_csv("PS_2022.04.22_04.00.41.csv", sep =",")
        lista_gravedad = list(datos["gravity"]) ; lista_nombres = list(datos["eName"])
        lista_gravedad_exo = list(datos_exo["st_logg"]) ; lista_nombres_exo = list(datos_exo["pl_name"])
        gravedad_util, nombres_util = [], []
        # print(lista_gravedad) ; print(lista_gravedad_exo)
        for i in range (len(lista_gravedad)):
            if 8.0 < lista_gravedad[i] <10.5:
                gravedad_util.append(lista_gravedad[i])
                nombres_util.append(lista_nombres[i])
        for i in range(len(lista_gravedad_exo)):
            if 8.0 < lista_gravedad_exo[i] < 10.5:
                gravedad_util.append(lista_nombres_exo[i])
                nombres_util.append(lista_nombres_exo[i])

        print(gravedad_util)
        print("son las gravedades correspondientes a los siguientes nombres:")
        print(nombres_util)
        utiles_porcentaje = 0.01509433962
        no_utiles_porcentaje = 1 -utiles_porcentaje
        parametros = [utiles_porcentaje, no_utiles_porcentaje] ; colores = ["#AAF683", "#EE6055"]
        plt.bar (lista_nombres, lista_gravedad) ; plt.show()
        plt.pie (parametros, colors = colores, autopct="%0.1f %%")
        plt.legend(["Gravedad válida", "Gravedad no válida"], loc='upper right')
        plt.show()
        tierra = datos.iloc[86] ; venus = datos.iloc[261]
        saturno= datos.iloc[226] ; urano = datos.iloc[258]
        print(f"\n Los datos de la tierra son: \n {tierra}") ; print(f"\n Los datos de venus son: \n  {venus}")
        print(f"\n Los datos de saturno son: \n {saturno}") ; print(f"\n Los datos de urano son: \n {urano}")

Graficos.grafico()

def datosTemperaturas():
    datos = pd.read_csv("planetas.csv", sep =",").to_dict()
    planetas = 7
    datos_dict = []
    print(datos)
    for i in range(planetas):
        datos_dict.append({
            datos['Nombre'][i]:{
                'Presión(kPa)': datos['Presión(kPa)'][i],
                'TemperaturaMínima(k)': datos['TemperaturaMínima(k)'][i],
                'TemperaturaMáxima(k)': datos['TemperaturaMáxima(k)'][i],
                'TemperaturaMedia(k)': datos['TemperaturaMedia(k)'][i],
                'Composición(+Abundante)': datos['Composición(+Abundante)'][i],
                'Composición(2+Abundante)': datos['Composición(2+Abundante)'][i],
                'Composición(3+Abundante)': datos['Composición(3+Abundante)'][i],
                'Porcentaje(CAbundante)': datos['Porcentaje(CAbundante)'][i],
                'Porcentaje(2+CAbundante)': datos['Porcentaje(2+CAbundante)'][i],
                'Porcentaje(3+CAbundante)': datos['Porcentaje(3+CAbundante)'][i],
                'EstructuraTerrestre': datos['EstructuraTerrestre'][i],
                'Agua': datos['Agua'][i],
                'TiempodeRotación(años)': datos['TiempodeRotación(años)'][i]
            }
        })
    print(datos_dict)

datosTemperaturas()