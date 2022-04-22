from email.errors import ObsoleteHeaderDefect
import pandas as pd

planets = []
planetas = 33

def obtenerDatos():
    datos = pd.read_csv("../planets.csv", sep =",")
    for i in range(planetas):
        planets.append({
            'eName': datos['pl_hostname'][i],
            'semimajorAxis': datos['pl_orbsmax'][i],
            'perihelion': datos['st_distlim'][i],
            'aphelion': datos['st_disterr1'][i],
            'eccentricity': datos['pl_orbeccen'][i],
            'inclination': datos['pl_orbincl'][i],
            'density': datos['pl_radjlim'][i],
            'gravity': 'GRAVEDAD',
            'escape': 'VELOCIDA DE ESCAPE',
            'mass_kg': datos['pl_bmassj'][i],
            'density': datos['pl_radjerr1'][i],
            'meanRadius': datos['pl_radjerr1'][i],
            'isPlanet': 'FALSO'
        })
    print(planets)

obtenerDatos()