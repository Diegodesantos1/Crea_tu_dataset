import pandas as pd
import matplotlib.pyplot as plt
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

Graficos.grafico()
