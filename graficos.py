import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt
import numpy as np
class Graficos:
    def sistema_solar():
        datos = pd.read_csv("Dataset1.csv", sep =";")
        lista_gravedad = list(datos["gravity"]) ; lista_nombres = list(datos["eName"])
        lista_gravedad_util, lista_nombres_util,gravedad_util, nombres_util, gravedad_grafico1, nombres_grafico1, gravedad_grafico2, nombres_grafico2, gravedad_grafico3, nombres_grafico3, gravedad_grafico4, nombres_grafico4 = [], [], [], [], [], [], [], [], [], [], [], []
        diccionario = {}
        # print(lista_gravedad) ; print(lista_gravedad_exo)
        for i in range (len(lista_gravedad)):
            if 8.0 < lista_gravedad[i] <10.5:
                gravedad_util.append(lista_gravedad[i])
                nombres_util.append(lista_nombres[i])
        for i in range (len(lista_gravedad)):
            if lista_gravedad[i] != 0:
                lista_gravedad_util.append(lista_gravedad[i])
                lista_nombres_util.append(lista_nombres[i])
        for i in range (14):
            gravedad_grafico1.append(lista_gravedad_util.pop(0))
            nombres_grafico1.append(lista_nombres_util.pop(0))
        for i in range (14):
            gravedad_grafico2.append(lista_gravedad_util.pop(0))
            nombres_grafico2.append(lista_nombres_util.pop(0))
        for i in range (14):
            gravedad_grafico3.append(lista_gravedad_util.pop(0))
            nombres_grafico3.append(lista_nombres_util.pop(0))
        for i in range (15):
            gravedad_grafico4.append(lista_gravedad_util.pop(0))
            nombres_grafico4.append(lista_nombres_util.pop(0))
        for i in range (4):
            a=nombres_util.pop(0)
            b = gravedad_util.pop(0)
            diccionario[a] = b
        print(f"Los planetas junto a sus gravedades en los que nos podríamos encontrar son: {diccionario}\n \n")
        utiles_porcentaje = 0.01509433962 ; no_utiles_porcentaje = 1 -utiles_porcentaje
        parametros = [utiles_porcentaje, no_utiles_porcentaje] ; colores = ["#AAF683", "#EE6055"]
        plt.bar (nombres_grafico1, gravedad_grafico1) ; plt.ylabel("Gravedad") ; plt.xlabel("Cuerpos Celestes"); plt.title("Sistema Solar") ; plt.show()
        plt.bar (nombres_grafico2, gravedad_grafico2) ; plt.ylabel("Gravedad") ; plt.xlabel("Cuerpos Celestes"); plt.title("Sistema Solar") ; plt.show()
        plt.bar (nombres_grafico3, gravedad_grafico3) ; plt.ylabel("Gravedad") ; plt.xlabel("Cuerpos Celestes"); plt.title("Sistema Solar") ; plt.show()
        plt.bar (nombres_grafico4, gravedad_grafico4) ; plt.ylabel("Gravedad") ; plt.xlabel("Cuerpos Celestes"); plt.title("Sistema Solar") ; plt.show()
        plt.pie (parametros, colors = colores, autopct="%0.1f %%")
        plt.legend(["Gravedad válida", "Gravedad no válida"], loc='upper right')
        plt.show()
        tierra = datos.iloc[86] ; venus = datos.iloc[261]
        saturno= datos.iloc[226] ; urano = datos.iloc[258]
        print(f"\n Los datos de la tierra son: \n {tierra}") ; print(f"\n Los datos de venus son: \n  {venus}")
        print(f"\n Los datos de saturno son: \n {saturno}") ; print(f"\n Los datos de urano son: \n {urano}")
    def exoplanetas():
        gravedad_util, nombres_util = [], []
        datos_exo = pd.read_csv("PS_2022.04.22_04.00.41.csv", sep =",")
        lista_gravedad_exo = list(datos_exo["st_logg"]) ; lista_nombres_exo = list(datos_exo["pl_name"])
        for i in range(len(lista_gravedad_exo)):
            if 8.0 < lista_gravedad_exo[i] < 10.5:
                gravedad_util.append(lista_nombres_exo[i])
                nombres_util.append(lista_nombres_exo[i])
        print(f"No existen exoplanetas junto a sus gravedades en los que nos podríamos encontrar\n")
Graficos.sistema_solar()
Graficos.exoplanetas()

def datosTemperaturas():
    datos = pd.read_csv("planetas.csv", sep =",").to_dict()
    planetas = 7
    datos_dict = []
    print(f"\n\n {datos}")
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