import pandas as pd
import matplotlib.pyplot as plt
class Graficos:
    def grafico():
        indices = []
        datos = pd.read_csv("Dataset.csv", sep =",")
        lista_gravedad = list(datos["gravity"])
        gravedad_util = []
        print(lista_gravedad)
        for i in range (len(lista_gravedad)):
            if 8.0 < lista_gravedad[i] <10.5:
                gravedad_util.append(lista_gravedad[i])
Graficos.grafico()
