# Algorithms and circular economy
This repository contains all the code I created for my bachelor's thesis. It covers three topics, Environmentally Extended Input-Output Analysis (EEIOA), Material Flow Analysis (MFA) and the Vehicle Routing Problem (VRP). All the code is commented to explain how it works. 

## EEIOA

eeioa.py is the python file with the code relevant for the EEIOA part.

A tratada.txt is the text file that contains the output of the function preparar_tabla_matrices()

Y tratada.txt is the text file that contains the output of the function preparar_tabla_demandas()

F tratada.txt is the text file that contains the output of the function preparar_tabla_emisiones() 

emisiones por pais.txt is the text file that contains the output of the function emisiones_por_pais()

eeioa.txt is the text file that contains the output of the function eeioa() 

eeioa.xlsx is the text file that contains the output of the function pintar_tabla(), with the industries and countries added posteriorly in Excel and using a gradient to colour the cells according to the values.

## MFA 

mfa.py contains the code of the MFA algorithm.

## VRP

vrp.py contains the code to exectute the VRP algorithms (version 1, version 2 with branch and cut and version 2 with CPLEX). At the end of the code, there are examples of graphs with 10, 12, 14 and 15 vertices to use in the test cases.

grafo50.txt es is the matrix of distances of a graph with 50 vertices (to test the functions)

grafo200.txt is the matrix of distances of a graph with 200 vértices

grafo1000.txt is the matrix of distances of a graph with 1000 vértices

## License
[MIT](https://choosealicense.com/licenses/mit/)

