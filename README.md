<h1 align="center">Crea tu dataset</h1>



---

Este es el link del [repositorio](https://github.com/Diegodesantos1/Crea_tu_dataset)
***

## Autores de este proyecto

1. [@jmedina28](https://github.com/jmedina28)
2. [@mat0ta](https://github.com/mat0ta)
3. [@xavitheforce](https://github.com/Xavitheforce)
4. [@Diegodesantos1](https://github.com/Diegodesantos1)

***
Este dataset está compuesto por varios archivos csv, de los cuales hay uno(dataset) que tiene registrados todos los planetas, satélites y lunas conocidos en el sistema solar. En base a este csv hemos conseguido una lista de los planetas cuya gravedad está comprendida entre 8 y 10,5. Estos valores provienen de los experimentos realizados por la valiente tripulación en los que han calculado un valor aproximado de la gravedad en la que se encuentran(9,45 y 9,18). Considerando estos valores y asumiendo un error de medida de una unidad en ambos extremos (8, 10.5) hemos conseguido 4 cuerpos celestes, en este caso todos planetas, que son: Venus, La tierra, Saturno y Urano. Basándonos en nuestros resultados, la gravedad del planeta que más se acerca a la gravedad experimental calculada(media de las dos gravedades = 9,315) es la de Mercurio o Venus(tienen la misma gravedad). 
Con estos resultados, y descartando para este primer análisis la idea de haber sido absorbidos por un agujero negro que distorsione el espacio o incluso el tiempo, podemos concluir que el planeta en el que estamos es Urano, ya que Venus no es opción al no estar en nuestra ruta preestablecida al comienzo del viaje (se queda atrás).

![image](https://user-images.githubusercontent.com/91721855/164943985-75eaf45f-3553-45ac-b012-d5a5c7028d41.png)

![image](https://user-images.githubusercontent.com/91721855/164943993-cbc676f9-06e6-4dcd-843f-d980c27ad4c3.png)

![image](https://user-images.githubusercontent.com/91721855/164944003-28dabed7-c6ee-450c-9b01-01ff54ef4930.png)

![image](https://user-images.githubusercontent.com/91721855/164944008-395bf723-8ff9-419f-b690-656b03fb4b35.png)

(Gráficos con la fuerza de gravedad de todos los cuerpos celestes dentro del sistema solar)

![image](https://user-images.githubusercontent.com/91721855/164944015-5b5cf276-90c0-4dee-a539-fc9643aa55a3.png)

![image](https://user-images.githubusercontent.com/91721855/164944026-34788991-e1e1-4f8c-be66-40b64daf9c0e.png)

(Gráficos con el porcentaje de cuerpos celestes dentro y fuera del sistema solar con una gravedad cercana(+-1,5) a la obtenida durante el experimento realizado por la tripulación(de entre los datos a los que tenemos acceso))
   
   
Volviendo a la teoría del agujero de gusano, no solo es muy poco probable, sino que además no existen en nuestra base de datos(el segundo cvs que poseemos(Nasa)) ningún exoplaneta cuya gravedad se corresponda con los valores experimentales que tenemos a nuestra disposición, por ello, y con el fin de buscar la solución más realista posible al problema, vamos a descartar esta afirmación y centrarnos en el sistema solar.

Para proseguir, la tripulación debe conseguir los datos referentes a las condiciones atmosféricas, físicas y químicas del planeta para poder prepararse para dormir hasta el rescate de forma segura.
Analizando el cvs tenemos:

      eName:Uranus	isPlanet:VERDADERO	semimajorAxis:2870658186	perihelion:2147483647	aphelion:2147483647	eccentricity:457	inclination:772	density:1	gravity:8.87	escape:21380	meanRadius:25362	equaRadius:25559	polarRadius:24973	flattening:2293	dimension:NA	sideralOrbit:30685.4	sideralRotation:-17.24	discoveryDate:13/03/1781	mass_kg:86800000000000000000000000	volume:68300000000000	orbit_type:Primary	orbits:NA	bondAlbido:0.3	geomAlbido:488	RV_abs:296744357103154	p_transit:2510000000000	transit_visibility:4525328742848800	transit_depth:13265444757661600	massj:45684210526315700	semimajorAxis_AU:##########	grav_int:1400000000000000000000
      
Estos datos representan los valores relativos a la física del planeta. Para adentrarnos más en los químicos(los más interesantes a la hora de evaluar nuestra superviviencia) debemos acudir a nuestro tercer csv(planetas).
Analizando el cvs tenemos:

      Nombre:Urano	Presión(kPa):120	TemperaturaMínima(k):59	TemperaturaMedia(k):68	TemperaturaMáxima(k):68	Composición(+Abundante):H	Porcentaje(CAbundante):83	Composición(2+Abundante):He	Porcentaje(2+CAbundante):15	Composición(3+Abundante):CH4	Porcentaje(3+CAbundante):1.99	EstructuraTerrestre:Helado	Agua:Si	TiempodeRotación(años):84
      
Ahora ya tenemos toda la información necesaria para planear con seguridad la espera al rescate.
Lo primero de todo, la temperatura. Es generalmente conocido que el cuerpo humano debe mantenerse a una temperatura de unos 37 grados, mientras que en animación suspendida se mantiene en torno a 10/15 grados. En base a este dato, la nave debe regular su temperatura unos 215,15(= 205,15(valor positivo de la t de Urano) + 10(Temperatura a la que se quiere llegar))) grados a lo sumo aproximadamente, contando con un error de +- 5 grados. Además, debe estar preparada para cambios bruscos en la temperatura exterior de hasta +-10 grados(por aproximar la mínima, y dar un valor distinto a la media en la máxima t de Urano). No obstante, la nave debe mantener la temperatura necesaria lo más baja posible, para reducir el gasto energético(considerando que no tenemos capacidad infinta) por el mayor tiempo posible.

No solo buscamos gastar menos energía en temperatura de lo necesario por ahorro, sino que también por presión. En el planeta Urano conocemos una presión de unos 120kPa, que puede causar problemas en distintas partes de la nave si nos mantenemos demasiado tiempo estáticos(dudamos que la nave se haya diseñado para aguantar semejante presión de forma continua). Por ello, salvaguardar la máxima capacidad posible para mantener la nave operativa es esencial(priorizar la autoreparación y gestión de estado).

Por último en lo referente a posibles daños, no solo hay que mantener en alerta la nave por la presión, sino que también por los residuos espaciales. La gravedad de Urano(8,7) es parecida a la de la Tierra(9,8), pero su atmósfera no. Todo elemento que entre puede impactar con facilidad en la nave, sobretodo estando rodeada de anillos rocosos o teniendo cerca el gran cinturón de Kuiper.

También es importante la composición atmosférica del planeta. Nuestros datos ya nos demuestran que no es una atmósfera óptima para el ser humano, ya que no hay Oxígeno(como mucho podría haber un 2%, lo que sería insuficiente), pero a lo mejor la nave puede aprovechar parte de su composición para reciclar energía (desde luego es inhabitable)**.

Por último, y más importante, el tiempo. El tiempo es la incógnita que decide si la tripulación sobrevive o no. Ya nos hemos preparado para todo lo conocido(temperatura, presión, gravedad, composición atmosférica...), pero será el tiempo que tarden en rescatarnos el factor clave en esta misión. Sabemos que Urano tarda 84 años en dar una vuleta al sol, por lo que relacionándolo con su radio respecto al sol su y posición en el sistema solar podemos concluir que no es un planeta muy rápido. Esto beneficia a nuestros rescatadores, ya que no tendrán que alterar demasiado su rumbo durante el viaje y podrán planificar un rescate seguro. Lo que sí sabemos es que se tarda unos 15 años de media en llegar a Urano(posiblemente mucho menos si tenemos una tecnología más avanzada en lo referente a velocidad, pero supongamos que no), y por lo tanto todas las condiciones que le hemos impuesto a la nave deben perdurar por lo menos 15 años. Otra vez, asumamos un error de año y medio, por lo tanto 16,5 años.

Con toda esta información en mente, podemos concluir que se debe distribuir al menos durante 16 años y medio de manera eficiente toda la energía de la nave(temperatura, autoanálisis, estado en reposo...).

![image](https://user-images.githubusercontent.com/91721855/164944035-28b6a472-0438-43cb-b8c9-41d5e5dc6da7.png)

(Gráficos que comparan las temperaturas y presiones de todos los planetas del sistema solar.)


** Suponemos que la nave debe ser MUY avanzada para poder realizar este viaje con tripulación, así que quizás tenga alguna de las funciones mencionadas(reciclaje a base de hidrógeno, autoreparación y autogestión...).

*** Todos los datos extraídos del dataset, al igual que los gráficos, pueden ser comprobados en las funciones desarrolladas en este repositorio en el archivo gráficos.py
