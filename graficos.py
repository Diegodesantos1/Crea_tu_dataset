import pandas as pd
import matplotlib.pyplot as plt
class Graficos:
    def grafico():
        datos = pd.read_csv("Dataset.csv", sep =",")
        lista_gravedad = list(datos["gravity"])
        gravedad_util = []
        print(lista_gravedad)
        for i in range (len(lista_gravedad)):
            dato = lista_gravedad.pop(0)
            if 8 < dato < 10.5:
                gravedad_util.append(dato)
            else:
                pass
        print(gravedad_util)

Graficos.grafico()
