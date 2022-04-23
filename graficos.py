import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt
class Dataset1:
    def sistema_solar():
        datos = pd.read_csv("Dataset1.csv", sep =";")
        lista_gravedad = list(datos["gravity"]) ; lista_nombres = list(datos["eName"])
        lista_gravedad_util, lista_nombres_util,gravedad_util, nombres_util, gravedad_grafico1, nombres_grafico1, gravedad_grafico2, nombres_grafico2, gravedad_grafico3, nombres_grafico3, gravedad_grafico4, nombres_grafico4 = [], [], [], [], [], [], [], [], [], [], [], []
        diccionario = {}
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
        for i in range (15):
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
        print(f"\n\nExisten 265 planetas y cuerpos del sistema solar con gravedad, pero solo estos cumplen las condiciones \n{diccionario}")
        utiles_porcentaje = 0.01509433962 ; no_utiles_porcentaje = 1 -utiles_porcentaje
        parametros = [utiles_porcentaje, no_utiles_porcentaje] ; colores1 = ["#AAF683", "#EE6055"] ; colores2 = ["r", "r", "r", "g", "r", "g", "r", "r", "r", "r", "r", "r", "r", "g", "g"]
        plt.bar (nombres_grafico1, gravedad_grafico1, color = "red") ; plt.ylabel("Gravedad") ; plt.xlabel("Cuerpos Celestes"); plt.title("Sistema Solar") ; plt.show()
        plt.bar (nombres_grafico2, gravedad_grafico2, color = "red") ; plt.ylabel("Gravedad") ; plt.xlabel("Cuerpos Celestes"); plt.title("Sistema Solar") ; plt.show()
        plt.bar (nombres_grafico3, gravedad_grafico3, color = "red") ; plt.ylabel("Gravedad") ; plt.xlabel("Cuerpos Celestes"); plt.title("Sistema Solar") ; plt.show()
        plt.bar (nombres_grafico4, gravedad_grafico4, color = colores2) ; plt.ylabel("Gravedad") ; plt.xlabel("Cuerpos Celestes"); plt.title("Sistema Solar") ; plt.show()
        plt.pie (parametros, colors = colores1, autopct="%0.1f %%") ; plt.title("Planetas que cumplen las condidiones") ; plt.legend(["Las cumple", "No las cumple"], loc='upper right')
        plt.show()
        tierra = datos.iloc[86] ; venus = datos.iloc[261]
        saturno= datos.iloc[226] ; urano = datos.iloc[258]
        print(f"\n Los datos de la tierra son: \n {tierra}") ; print(f"\n Los datos de venus son: \n  {venus}")
        print(f"\n Los datos de saturno son: \n {saturno}") ; print(f"\n Los datos de urano son: \n {urano}")
    def exoplanetas():
        datos_exo = pd.read_csv("PS_2022.04.22_04.00.41.csv", sep =",")
        lista_gravedad_exo = list(datos_exo["st_logg"]) ; lista_nombres_exo = list(datos_exo["pl_name"])
        lista_gravedad_util, lista_nombres_util = [], []
        for i in range (len(lista_gravedad_exo)):
            if lista_gravedad_exo[i] != 0:
                lista_gravedad_util.append(lista_gravedad_exo[i])
                lista_nombres_util.append(lista_nombres_exo[i])
        print(f"\n\nExisten {len(lista_gravedad_util)} exoplanetas con gravedad, pero ninguno cumple las condiciones")
        utiles_porcentaje = 0 ; no_utiles_porcentaje = 1
        parametros = [utiles_porcentaje, no_utiles_porcentaje] ; colores = ["#AAF683", "#EE6055"]
        plt.pie (parametros, colors = colores, autopct="%0.1f %%")
        plt.title("Exoplanetas que cumplen las condidiones") ; plt.legend(["Las cumple", "No las cumple"], loc='upper right')
        plt.show()

class Dataset2:
    def datosTemperaturas():
        datos = pd.read_csv("planetas.csv", sep =",").to_dict()
        planetas = 7
        datos_dict = []
        print(f"\n\n {datos}\n \n")
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


def ejecutar():
    Dataset1.sistema_solar()
    Dataset1.exoplanetas()
    Dataset2.datosTemperaturas()