# Algoritmia y economía circular
En este repositorio se encuentra todo el código relacionado con el trabajo de fin de grado. Este trabajo trata tres temas: el Environmentally Extended Input-Output Analysis (EEIOA), el Material Flow Analysis (MFA) y el Vehicle Routing Problem (VRP). Todas las funciones del código están comentadas y explicadas en el propio código.

## EEIOA

eeioa.py es el archivo Python con todo el código relativo a este tema.

A tratada.txt es el archivo de salida de la función preparar_tabla_matrices() de eeioa.py

Y tratada.txt es el archivo de salida de la función preparar_tabla_demandas() de eeioa.py

F tratada.txt es el archivo de salida de la función preparar_tabla_emisiones() de eeioa.py

emisiones por pais.txt es el archivo de salida de la función emisiones_por_pais() de eeioa.py

eeioa.txt es el archivo de salida de la función eeioa() de eeioa.py. 

eeioa.xlsx es el archivo de salida de la función pintar_tabla(), con las industrias y los países añadidos posteriormente en Excel y utilizando un gradiente para colorear las celdas según los valores.

## MFA 

mfa.py contiene todo el código del algoritmo MFA.

## VRP

vrp.py contiene el código para ejecutar los algoritos VRP (la versión 1, la versión 2 con ramificación y poda y la versión 2 con CPLEX). Al final del código están ejemplos de grafos de 10, 12, 14 y 15 vértices para utilizar para las pruebas.

grafo50.txt es la matriz de distancias de un grafo de 50 vértices (para realizar pruebas)

grafo200.txtes la matriz de distancias de un grafo de 200 vértices

grafo1000.txt es la matriz de distancias de un grafo de 1000 vértices

## License
[MIT](https://choosealicense.com/licenses/mit/)

