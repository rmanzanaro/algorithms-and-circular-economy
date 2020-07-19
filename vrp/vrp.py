# -*- coding: utf-8 -*-
"""
@author: Roberto Manzanaro Pilling

CASOS DE PRUEBA DE LOS ALGORITMOS DEL CAPÍTULO 4 DEL TRABAJO:

VERSIÓN 1 :
    -CASO 1:
        · caso: sitio_optimo(grafo50, [5, 3, 7, 6, 2, 6, 6, 5, 5, 2, 2, 0, 1, 3, 6, 0, 5, 5, 4, 4, 3, 1, 2, 6, 3, 7, 6, 5, 4, 0, 6, 0, 5, 4, 1, 5, 3, 3, 2, 2, 1, 2, 0, 7, 1, 7, 7, 4, 1, 5])
        · tiempo: 0.33 s
        · resultado: vértice ideal --> 30, distancia recorrida --> 1001 uds
    -CASO 2:
        · caso: sitio_optimo(grafo200, [4,3,7,7,3,3,3,5,5,1,5,3,7,3,6,7,1,3,7,2,4,1,5,6,2,7,6,0,3,1,0,7,6,1,6,6,4,1,2,1,1,2,6,1,7,0,3,6,1,6,3,4,4,2,4,5,1,5,7,0,0,4,1,7,5,2,3,3,0,1,1,6,1,0,0,6,6,3,2,2,3,0,6,2,5,1,6,5,0,0,3,6,1,1,3,3,1,4,2,7,3,6,1,7,6,5,4,0,2,6,2,1,0,0,3,2,3,0,7,7,7,0,6,3,0,1,6,6,0,2,1,4,4,6,0,6,1,5,5,5,5,3,4,2,7,2,1,0,5,2,5,6,2,4,3,7,5,3,5,7,7,4,4,0,6,2,5,5,1,0,2,4,6,6,1,3,0,4,6,2,1,2,3,4,3,3,0,7,4,7,1,2,4,0,5,3,4,3,6,6])
        · tiempo: 1.91 s
        · resultado: vértice ideal --> 75, distancia recorrida --> 3664 uds
    - CASO 3:
        · caso: sitio_optimo(grafo1000, [7, 0, 3, 6, 6, 1, 2, 2, 3, 3, 0, 1, 7, 4, 4, 7, 1, 6, 1, 0, 4, 0, 2, 1, 0, 2, 6, 2, 7, 6, 6, 3, 4, 1, 2, 4, 5, 1, 5, 2, 5, 2, 4, 0, 1, 3, 4, 1, 7, 7, 2, 5, 0, 4, 3, 3, 1, 6, 6, 5, 1, 4, 7, 6, 6, 3, 1, 1, 1, 0, 4, 4, 7, 4, 7, 5, 3, 1, 6, 2, 2, 7, 1, 5, 4, 2, 2, 0, 1, 5, 3, 4, 3, 5, 0, 7, 5, 3, 6, 0, 5, 0, 3, 1, 1, 7, 5, 5, 5, 4, 3, 5, 5, 6, 0, 2, 3, 1, 4, 2, 2, 6, 7, 5, 0, 6, 1, 7, 5, 5, 5, 0, 1, 2, 6, 7, 2, 2, 3, 6, 5, 3, 7, 6, 0, 3, 1, 4, 0, 3, 6, 1, 3, 2, 0, 3, 4, 1, 7, 6, 0, 3, 6, 6, 4, 5, 5, 0, 2, 3, 7, 1, 3, 2, 4, 7, 5, 2, 1, 4, 6, 1, 4, 7, 1, 7, 5, 4, 0, 3, 1, 0, 5, 0, 3, 0, 1, 1, 0, 3, 5, 1, 7, 1, 6, 2, 5, 4, 2, 3, 4, 4, 7, 4, 6, 7, 3, 3, 1, 0, 1, 6, 5, 4, 7, 2, 5, 7, 5, 7, 5, 2, 7, 4, 7, 7, 1, 4, 4, 3, 4, 3, 0, 4, 1, 3, 7, 6, 6, 5, 3, 6, 2, 0, 2, 5, 5, 2, 0, 0, 7, 6, 7, 3, 2, 5, 4, 3, 7, 5, 2, 2, 2, 6, 1, 7, 4, 3, 1, 4, 1, 3, 1, 2, 5, 0, 5, 0, 7, 0, 1, 1, 5, 0, 2, 5, 4, 1, 5, 6, 7, 3, 4, 7, 7, 0, 5, 4, 2, 5, 0, 0, 6, 2, 3, 0, 3, 3, 1, 1, 3, 7, 4, 6, 7, 4, 7, 0, 4, 3, 4, 2, 1, 4, 4, 0, 7, 3, 6, 1, 0, 3, 7, 0, 2, 5, 6, 3, 6, 2, 1, 6, 5, 0, 1, 0, 3, 1, 1, 0, 6, 6, 0, 4, 1, 5, 0, 5, 7, 4, 1, 0, 1, 0, 7, 0, 3, 5, 2, 6, 1, 0, 6, 7, 5, 2, 5, 6, 4, 7, 5, 5, 0, 3, 2, 3, 1, 6, 2, 7, 2, 4, 1, 0, 1, 4, 5, 1, 4, 7, 0, 7, 7, 0, 0, 7, 2, 2, 4, 1, 6, 7, 2, 7, 1, 7, 6, 5, 5, 4, 0, 4, 1, 3, 0, 5, 2, 7, 0, 1, 4, 5, 4, 5, 0, 2, 3, 3, 4, 0, 0, 6, 7, 4, 4, 7, 2, 3, 4, 3, 2, 3, 1, 2, 6, 2, 1, 4, 2, 0, 6, 2, 6, 7, 3, 4, 2, 1, 0, 0, 1, 3, 2, 5, 5, 5, 7, 0, 4, 6, 6, 2, 3, 7, 4, 0, 1, 3, 4, 7, 6, 0, 1, 7, 2, 0, 5, 6, 1, 5, 3, 0, 7, 0, 3, 4, 2, 1, 7, 3, 5, 3, 3, 7, 4, 3, 6, 5, 0, 4, 3, 2, 6, 6, 4, 4, 7, 2, 2, 6, 4, 0, 2, 7, 7, 5, 5, 3, 5, 3, 2, 4, 5, 7, 7, 1, 7, 4, 4, 2, 6, 2, 1, 6, 3, 6, 3, 3, 7, 7, 6, 5, 2, 4, 7, 1, 6, 2, 0, 3, 0, 7, 2, 5, 7, 0, 0, 1, 6, 1, 0, 1, 2, 6, 2, 7, 5, 0, 0, 0, 4, 5, 7, 5, 5, 5, 5, 5, 5, 7, 2, 7, 2, 5, 0, 2, 0, 5, 5, 7, 5, 6, 3, 0, 4, 2, 7, 3, 3, 3, 1, 1, 6, 1, 7, 0, 7, 0, 3, 1, 2, 1, 1, 1, 0, 1, 4, 6, 4, 5, 1, 1, 6, 0, 2, 6, 6, 7, 3, 0, 2, 1, 4, 2, 3, 2, 0, 7, 6, 1, 6, 6, 7, 3, 3, 2, 4, 3, 2, 7, 5, 3, 6, 6, 1, 4, 7, 1, 1, 7, 6, 3, 2, 0, 7, 7, 6, 7, 4, 5, 6, 5, 3, 5, 5, 5, 3, 0, 4, 0, 4, 2, 4, 2, 5, 0, 4, 3, 2, 2, 6, 1, 1, 3, 6, 1, 1, 3, 5, 6, 0, 6, 2, 4, 3, 5, 7, 2, 7, 3, 2, 7, 0, 7, 1, 7, 5, 7, 4, 0, 7, 5, 4, 2, 5, 3, 0, 3, 6, 4, 4, 3, 7, 5, 0, 5, 2, 3, 6, 7, 2, 6, 7, 2, 2, 0, 7, 1, 2, 0, 6, 5, 5, 6, 1, 0, 5, 3, 4, 4, 7, 4, 0, 3, 3, 7, 0, 6, 2, 0, 0, 3, 4, 5, 5, 1, 3, 7, 5, 5, 2, 4, 2, 3, 6, 0, 2, 4, 6, 2, 4, 3, 1, 0, 7, 6, 3, 2, 3, 1, 1, 4, 7, 4, 1, 2, 6, 6, 2, 6, 5, 7, 1, 7, 0, 7, 4, 6, 3, 5, 6, 7, 2, 7, 2, 0, 1, 3, 2, 6, 7, 4, 2, 4, 4, 3, 5, 1, 7, 7, 2, 5, 2, 6, 2, 3, 0, 3, 3, 5, 1, 3, 2, 5, 4, 5, 4, 2, 0, 2, 3, 6, 1, 4, 6, 7, 2, 5, 2, 7, 7, 6, 5, 2, 7, 6, 5, 7, 2, 3, 4, 5, 4, 5, 6, 4, 6, 7, 4, 0, 3, 2, 5, 7, 2, 7, 7, 0, 0, 6, 3, 5, 6, 7, 7, 6, 7, 2, 4, 1, 0, 0, 1, 4, 2, 6, 1, 3, 2, 5, 2, 6, 6, 5, 5, 6, 5, 6, 3, 4, 5, 6, 2, 2, 5, 7, 6, 5, 0, 6, 7, 1, 0, 5, 6, 2, 6, 5, 3, 7, 2, 4, 7, 6, 5, 2, 3, 7, 3, 1, 3, 4, 1, 4, 4, 0, 7, 2, 4, 0])
        · tiempo: 311.97 s
        · resultado: vértice ideal --> 886, distancia recorrida --> 19300 uds
VERSIÓN 2:
    · RAMIFICACIÓN Y PODA:
        - CASO 1:
            · caso: capacitated_vehicle_routing([7,5,4],10,np.array([[0,2,3,4,math.inf],[2,0,5,math.inf,5],[3,5,0,math.inf,3],[4,math.inf,math.inf,0,2],[math.inf,5,3,2,0]]))
            · tiempo: 0.003 s
            · resultado: 10
        - CASO 2:
            · caso: capacitated_vehicle_routing([6,3,5,4,7,5,11],16,grafo10)
            · tiempo: 6.37 s
            · resultado: 51
        - CASO 3:
            · caso: capacitated_vehicle_routing([6,3,5,4,7,5,11,6,2],18,grafo12)
            · tiempo: 45.98 s
            · resultado: 63
        - CASO 4:
            · caso: capacitated_vehicle_routing([6,3,5,4,7,5,11,6,2,7],20,grafo14)
            · tiempo: 351.94 s
            · resultado: 67
        - CASO 5:
            · caso: capacitated_vehicle_routing([6,3,5,4,7,5,11,6,2,7],20,grafo14)
            · tiempo: 9663.92 s
            · resultado: 77

    · PROGRAMACIÓN LINEAL:
        - CASO 1:
            · problema: heuristico_cvrp[7,5,4],10,np.array([[0,2,3,4,math.inf],[2,0,5,math.inf,5],[3,5,0,math.inf,3],[4,math.inf,math.inf,0,2],[math.inf,5,3,2,0]]))
            · tiempo: 0.38 s
            · resultado: 10
        - CASO 2:
            · problema: heuristico_cvrp([6,3,5,4,7,5,11],16,grafo10)
            · tiempo: 0.86 s
            · resultado: 51
        - CASO 3:
            · problema: heuristico_cvrp([6,3,5,4,7,5,11,6,2],18,grafo12)
            · tiempo: 4.68 s
            · resultado: 59
        - CASO 4:
            · caso: heuristico_cvrp([6,3,5,4,7,5,11,6,2,7],20,grafo14)
            · tiempo: 38.64 s
            · resultado: 67
        .- CASO 5:
            · caso: heuristico_cvrp([8,4,6,7,2,6,9,5,4,1,4,6],20,grafo15)
            · tiempo: 633.47
            · resultado: 77
"""
import numpy as np
import copy
import random
from docplex.mp.model import Model
import math
from heapq import heappush, heappop, heapify

"""
Esta función devuelve la matriz de distancias de un grafo como un array de arrays.

ENTRADA: 
    - limite-inferior y limite-superior indican los límites del intervalo de distancias entre vértices que nos 
      interesa. 
    - numero_vertices indica el número de vértices que tendrá el grafo de salida.

SALIDA: devuelve la matriz de distancias de un grafo de tamaño numero_vertices.
"""
def crear_grafo(limite_inferior, limite_superior, numero_vertices):
    grafo = np.zeros((numero_vertices, numero_vertices))
    randoms = []
    for i in range(0, numero_vertices):
        restantes = numero_vertices - i - 1
        for j in range(0, restantes):
            randoms.append(random.randint(limite_inferior, limite_superior))
        for k in range(numero_vertices - len(randoms), numero_vertices):
            numero_random = random.randint(1, 4)
            if numero_random == 1:
                grafo[i][k] = math.inf
                grafo[k][i] = math.inf
            else:
                grafo[i][k] = int(randoms[k - (numero_vertices - len(randoms))])
                grafo[k][i] = int(randoms[k - (numero_vertices - len(randoms))])
        randoms = []
    return grafo

"""
Esta función aplica el algoritmo de Floyd para encontrar las distancias mínimas entre todos los vértices de un grafo.

ENTRADA: aristas es una matriz nxn en el que la posición ij representa la distancia desde el vértice i hasta el j.

SALIDA: distancias es una matriz nxn en el que la posición ij representa la menor distancia desde el vértice i hasta
el j.
"""
def floyd(aristas):
    num_vertices = len(aristas[0])
    distances = aristas
    for k in range(0, num_vertices):
        for i in range(0, num_vertices):
            for j in range(0, num_vertices):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    return distances


"""
Esta función transforma un grafo en formato string a una lista de listas.

ENTRADA: archivo_grafo es la ruta al grafo en formato string.

SALIDA: 
    - aristas es la matriz de distancias del grafo.
    - frecuencias es la lista con el número de veces que hay que visitar cada punto de recogida de basuras.
"""
def string_a_grafo(archivo_grafo):
    with open(archivo_grafo) as myfile:
        data = myfile.read()
    grafo = data.split('\n')
    # Primera parte del archivo contiene las aristas del grafo
    aristas = grafo[0]
    # Con split('|') obtenemos una lista que contiene las filas de la matriz de aristas de nuestro grafo
    aristas = aristas.split('|')
    for i in range(0, len(aristas)):
        aristas[i] = aristas[i].split(',')
        for j in range(0, len(aristas[i])):
            if aristas[i][j] == "math.inf":
                aristas[i][j] = math.inf
            else:
                aristas[i][j] = int(aristas[i][j])

    # La segunda parte del archivo contiene la lista de frecuencias
    frecuencias = grafo[1]
    frecuencias = frecuencias.split(',')
    for i in range(0, len(frecuencias)):
        frecuencias[i] = int(frecuencias[i])

    return aristas, frecuencias


"""
Esta función devuelve el vértice óptimo del grafo para colocar la planta de reciclaje de forma que se minimice la 
distancia a todos los puntos de recogida de basuras. Es el algoritmo correspondiente a la sección 4.1 del TFG.

ENTRADA: 
    - aristas es una matriz nxn en el que la posición ij representa la distancia desde el vértice i hasta el j. El 
      valor math.inf en aristas indica que los dos vértices no están conectados.
    - frecuencias es una lista de tamaño n que indica la frecuencia de llenado de los puntos de recogida.

SALIDA: 
    - suma_optima es la distancia recorrida en la solución óptima.
    - posicion es el vértice del grafo que minimiza la distancia. 
"""
def sitio_optimo(aristas, frecuencias):
    num_vertices = len(frecuencias)
    distancias = floyd(aristas)
    suma_optima = math.inf
    posicion = -1
    for i in range(0, num_vertices):
        suma = 0
        for j in range(0, num_vertices):
            suma = suma + distancias[i][j] * frecuencias[j]
        if suma < suma_optima:
            suma_optima = suma
            posicion = i
    return suma_optima, posicion


"""
Este objeto representa las soluciones parciales del algoritmo de ramificación y poda.

PARÁMETROS: 
    - solucion_parcial es un array que contiene los vértices visitados hasta el momento en la solución parcial. 
    - puntos_restantes es un número que indica cuántos vértices quedan por visitar. 
    - capacidad_restante es un número que indica la capacidad del camión en ese momento. 
    - distancia_por_ahora indica la distancia recorrida por la situación parcial.
    - booleanos_visitados es una lista de booleanos tal que la posición correspondiente a los vértices visitados es True
      y los no visitados es False. 
    - evaluación_optimista es un número que indica la evaluación optimista de esa situación parcial. Se inicia a 0 y se 
      modifica posteriormente.
"""
class Situacion:
    evaluacion_optimista = 0

    def __init__(self, solucion_parcial, puntos_restantes, capacidad_restante, distancia_por_ahora, booleanos_visitados):
        self.solucion_parcial = solucion_parcial
        self.puntos_restantes = puntos_restantes
        self.capacidad_restante = capacidad_restante
        self.distancia_por_ahora = distancia_por_ahora
        self.booleanos_visitados = booleanos_visitados

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.evaluacion_optimista == other.evaluacion_optimista

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.evaluacion_optimista < other.evaluacion_optimista

    def __str__(self):
        return "eval-opt: " + str(self.evaluacion_optimista) + ", sol-par: " + str(self.solucion_parcial) + ", ptos-rest: " \
        + str(self.puntos_restantes) + ", bool: " + str(self.booleanos_visitados)


"""
Esta función devuelve el vértice óptimo del grafo para colocar la planta de reciclaje de forma que se minimice la 
distancia a todos los puntos de recogida de basuras en el algoritmo CVRP. Es el algoritmo correspondiente a la sección 
4.2 del TFG.

ENTRADA: 
    - pesos_puntos es una lista que indica la cantidad de basura que hay que recoger en cada vértice con punto de 
      recogida. 
    - capacidad_camion es un número que indica la capacidad del camión de recogida. 
    - aristas es la matriz de distancias del grafo.

SALIDA 
    - mejor_solucion es un array que indica la ruta que ha hecho el camión para recoger todas las basuras.
    - mejor_distancia es la distancia recorrida por la solución óptima.
"""
def capacitated_vehicle_routing(pesos_puntos, capacidad_camion, aristas):
    # numero_vertices_con_punto corresponde a m en el pseudocódigo
    numero_vertices_con_punto = len(pesos_puntos)
    mejor_distancia = math.inf
    mejor_solucion = []
    mejor_distancia_actual = 0
    # calculamos las distancias con floyd
    distancias = floyd(aristas)

    # numero_puntos_totales corresponde a N en el pseudocódigo
    numero_puntos_totales = len(distancias)
    # colapr en la que vamos metiendo las soluciones parciales
    cola_prioridad = []
    distancias_minimas = np.zeros(len(distancias))
    for i in range(0, numero_puntos_totales):
        distancias_minimas[i] = min(np.concatenate([distancias[i][:i], distancias[i][i + 1:]]))
    # Esta es la evaluación optimista
    for j in range(0, numero_puntos_totales):
        situacion_inicial = Situacion([j], numero_vertices_con_punto, capacidad_camion, 0, [False]*numero_vertices_con_punto)
        if j < numero_vertices_con_punto:
            situacion_inicial.puntos_restantes -= 1
            situacion_inicial.booleanos_visitados[j] = True
        situacion_inicial.evaluacion_optimista = eval_optimista(situacion_inicial.solucion_parcial,
                                                                situacion_inicial.distancia_por_ahora,
                                                                distancias_minimas, numero_vertices_con_punto)
        cola_prioridad.append(situacion_inicial)
    # Transformamos la lista en un montículo
    heapify(cola_prioridad)
    # Sacamos el primero
    situacion_actual = heappop(cola_prioridad)
    # Ya hemos sacado uno
    while len(cola_prioridad) > 0 and mejor_distancia_actual < mejor_distancia:
        # situacion_actual = cola_prioridad.pop(0)
        # Sacamos la info importante del elemento de la pila
        ultimo_visitado = situacion_actual.solucion_parcial[-1]
        primero_visitado = situacion_actual.solucion_parcial[0]

        # tenemos una solucion factible, vemos si actualizar o no
        if situacion_actual.puntos_restantes == 0:
            # sumamos la distancia de vuelta
            situacion_actual.distancia_por_ahora += distancias[primero_visitado][ultimo_visitado]
            if situacion_actual.distancia_por_ahora < mejor_distancia:
                mejor_distancia = situacion_actual.distancia_por_ahora
                mejor_solucion = situacion_actual.solucion_parcial
        # solucion parcial de momento
        else:
            for i in range(0, numero_vertices_con_punto):
                if not situacion_actual.booleanos_visitados[i]:
                    if len(situacion_actual.solucion_parcial) > 1:
                        situacion_origen = copy.deepcopy(situacion_actual)
                        # Volvemos al origen
                        distancia_extra = distancias[ultimo_visitado][primero_visitado].item() + distancias[primero_visitado][i].item()
                        eval_optimista_origen = situacion_actual.evaluacion_optimista - distancias_minimas[i] + distancia_extra
                        if eval_optimista_origen < mejor_distancia:
                            # tenemos posibilidades de mejorar la actual mejor solucion
                            situacion_origen.solucion_parcial += [primero_visitado, i]
                            situacion_origen.puntos_restantes -= 1
                            situacion_origen.capacidad_restante = capacidad_camion - pesos_puntos[i]
                            situacion_origen.distancia_por_ahora += distancia_extra
                            situacion_origen.evaluacion_optimista = eval_optimista_origen
                            situacion_origen.booleanos_visitados[i] = True
                            heappush(cola_prioridad, situacion_origen)
                            # anadir_colapr(cola_prioridad, situacion_actual)
                            # desmarcamos
                    if pesos_puntos[i] <= situacion_actual.capacidad_restante:
                        # Podemos ir directamente
                        situacion_directa = copy.deepcopy(situacion_actual)
                        distancia_extra = distancias[ultimo_visitado][i].item()
                        eval_optimista_directa = situacion_actual.evaluacion_optimista - distancias_minimas[i] + distancia_extra
                        if eval_optimista_directa < mejor_distancia:
                            situacion_directa.solucion_parcial.append(i)
                            situacion_directa.puntos_restantes -= 1
                            situacion_directa.capacidad_restante -= pesos_puntos[i]
                            situacion_directa.distancia_por_ahora += distancias[ultimo_visitado][i]
                            situacion_directa.evaluacion_optimista = eval_optimista_directa
                            situacion_directa.booleanos_visitados[i] = True
                            heappush(cola_prioridad, situacion_directa)
                            # anadir_colapr(cola_prioridad, situacion_actual)
                            # Desmarcamos
                            # situacion_actual = desmarcar(situacion_actual, False, distancia_actual, capacidad_actual, eval_optimista_actual, lista_booleanos)
                if len(cola_prioridad) > 0:
                    mejor_distancia_actual = cola_prioridad[0].evaluacion_optimista
                    # mejor_distancia_actual = cola_prioridad[0].evaluacion_optimista
        situacion_actual = heappop(cola_prioridad)
    return mejor_solucion, mejor_distancia


"""
Esta función devuelve la evaluación optimista de una solución parcial (una situación)

ENTRADA: toma los argumentos de una situación
    - solucion_parcial es la solución parcial hasta el momento de la situación.
    - distancia_por_ahora es la distancia recorrida hasta el momento por la situación.
    - distancias_minimas es un vector tal que la posición i contiene la distancia menor desde el vértice i hasta algún
      otro.
    - numero_vertices_con_punto es el número de vértices en los que hay punto de recogida.

SALIDA: evaluacion es la evaluación optimista de la situación de entrada
"""
def eval_optimista(solucion_parcial, distancia_por_ahora, distancias_minimas, numero_vertices_con_punto):
    evaluacion = distancia_por_ahora
    vertice_inicial = solucion_parcial[0]

    for i in range(0, numero_vertices_con_punto):
        if not i in solucion_parcial:
            evaluacion += distancias_minimas[i]
    # Sumamos la vuelta al vértice inicial
    evaluacion += distancias_minimas[vertice_inicial]
    return evaluacion


"""
Esta función resuelve el algoritmo CVRP con CPLEX de IBM. Se modeliza el problema con programación lineal como se indica
en la sección 3.2 del TFG.

ENTRADA: 
    - pesos_puntos es una lista que indica la cantidad de basura que hay que recoger en cada vértice con punto de 
      recogida. 
    - capacidad_camion es un número que indica la capacidad del camión de recogida. 
    - aristas es la matriz de distancias del grafo.

SALIDA: 
    - minimo es la distancia total recorrida por la solución óptima.
    - indice es el vétice inicial del que sale la solución óptima.
"""
def heuristico_cvrp(pesos_puntos, capacidad_camion, aristas):
    numero_vertices_totales = len(aristas)
    numero_vertices_punto = len(pesos_puntos)
    distancias = floyd(aristas)
    resultados = []

    for vertice_inicial in range(0, numero_vertices_totales):
        V = [j for j in range(0, numero_vertices_punto)]
        N = [j for j in range(0, numero_vertices_punto)]

        if vertice_inicial >= numero_vertices_punto:
            V.append(vertice_inicial)
        else:
            N.remove(vertice_inicial)
        A = [(i, j) for i in V for j in V if i != j]
        c = {(i, j): distancias[i, j] for i, j in A}
        mdl = Model('CVRP')
        x = mdl.binary_var_dict(A, name='x')
        # By default continuous decision variables have a lower bound of 0
        u = mdl.continuous_var_dict(N, ub=capacidad_camion, name='u')

        mdl.minimize(mdl.sum(c[i, j] * x[i, j] for i, j in A))
        mdl.add_constraints(mdl.sum(x[i, j] for j in V if j != i) == 1 for i in N)
        mdl.add_constraints(mdl.sum(x[i, j] for i in V if i != j) == 1 for j in N)
        mdl.add_indicator_constraints(mdl.indicator_constraint(x[i, j], u[i] + pesos_puntos[j] == u[j]) for i, j in A if
                                      i != vertice_inicial and j != vertice_inicial)

        mdl.add_constraints(u[i] >= pesos_puntos[i] for i in N)
        solution = mdl.solve()
        resultados.append(solution)
    minimo = resultados[0].get_objective_value()
    indice = 0
    for i in range(1, len(resultados)):
        if resultados[i].get_objective_value() < minimo:
            minimo = resultados[i].get_objective_value()
            indice = i
    return minimo, indice



#Grafos para pruebas

grafo10 = np.array([[0, math.inf, 8, math.inf, 5, 5, 8, math.inf, 11, 4],
                    [math.inf, 0, 5, 3, 11, math.inf, 9, math.inf, 5, 9],
                    [8, 5, 0, 5, math.inf, 7, math.inf, 9, 5, 4],
                    [math.inf, 3, 5, 0, 11, 11, math.inf, 6, 4, 3],
                    [5, 11, math.inf, 11, 0, 6, 3, 10, 10, math.inf],
                    [5, math.inf, 7, 11, 6, 0, 12, math.inf, math.inf, 10],
                    [8, 9, math.inf, math.inf, 3, 12, 0, 10, 11, 4],
                    [math.inf, math.inf, 9, 6, 10, math.inf, 10, 0, 11, math.inf],
                    [11, 5, 5, 4, 10, math.inf, 11, 11, 0, 4],
                    [4, 9, 4, 3, math.inf, 10, 4, math.inf, 4, 0]])

grafo12 = np.array([[0, math.inf, 8, math.inf, math.inf, 6, 6, 10, math.inf, math.inf, 4, 8],
                    [math.inf, 0, 4, 8, 7, 8, 8, 7, 11, 4, 7, math.inf],
                    [8, 4, 0, 11, 3, math.inf, math.inf, math.inf, 5, math.inf, 11, 7],
                    [math.inf, 8, 11, 0, math.inf, 11, 4, 4, 11, 9, 12, 11],
                    [math.inf, 7, 3, math.inf, 0, 7, math.inf, math.inf, 10, math.inf, 7, 3],
                    [6, 8, math.inf, 11, 7, 0, math.inf, 8, math.inf, math.inf, 9, 9],
                    [6, 8, math.inf, 4, math.inf, math.inf, 0, 8, 4, math.inf, math.inf, 12],
                    [10, 7, math.inf, 4, math.inf, 8, 8, 0, 10, 4, math.inf, 10],
                    [math.inf, 11, 5, 11, 10, math.inf, 4, 10, 0, math.inf, 8, 9],
                    [math.inf, 4, math.inf, 9, math.inf, math.inf, math.inf, 4, math.inf, 0, 4, 6],
                    [4, 7, 11, 12, 7, 9, math.inf, math.inf, 8, 4, 0, 4],
                    [8, math.inf, 7, 11, 3, 9, 12, 10, 9, 6, 4, 0]])

grafo14 = np.array([[ 0,  8,  7,  7,  5, 10,  7,  6,  7, math.inf, math.inf,  7,  9,  5],
                     [8,  0,  4,  5,  5,  5,  4, 10, math.inf, 10,  9, math.inf,  4,  7],
                     [ 7,  4,  0,  7, 10, 10,  6,  6, 10,  5, math.inf,  6,  5,  5],
                     [ 7,  5,  7,  0, math.inf,  9,  8, 10, math.inf, math.inf,  4,  4, math.inf,  9],
                     [ 5,  5, 10, math.inf,  0,  6,  9,  9, math.inf, math.inf,  7,  9,  4,  5],
                     [10,  5, 10,  9,  6,  0,  7, math.inf,  6, math.inf,  4,  4,  9, 10],
                     [ 7,  4,  6,  8,  9,  7,  0, 10,  9, 10,  5,  5,  4, math.inf],
                     [ 6, 10,  6, 10,  9, math.inf, 10,  0, math.inf,  5,  9,  9,  6, math.inf],
                     [ 7, math.inf, 10, math.inf, math.inf,  6,  9, math.inf,  0,  8, 10,  5,  4,  7],
                     [math.inf, 10,  5, math.inf, math.inf, math.inf, 10,  5,  8,  0,  6,  8,  8, math.inf],
                     [math.inf,  9, math.inf,  4,  7,  4,  5,  9, 10,  6,  0,  6,  4,  4],
                     [ 7, math.inf,  6,  4,  9,  4,  5,  9,  5,  8,  6,  0,  7, 10],
                     [ 9,  4,  5, math.inf,  4,  9,  4,  6,  4,  8,  4,  7,  0,  6],
                     [ 5,  7,  5,  9,  5, 10, math.inf, math.inf,  7, math.inf,  4, 10,  6,  0]])

grafo15 = np.array([[ 0,  5, 10,  4,  6,  6,  8,  7, math.inf, 10,  4, math.inf, math.inf,  5, 10],
                     [ 5,  0,  7, math.inf, math.inf,  6,  8,  9,  6,  6,  5,  7,  9, 11,  9],
                     [10,  7,  0, math.inf,  9, 10, math.inf,  9, 10,  7, 11,  5,  5,  5, 11],
                     [ 4, math.inf, math.inf,  0, 11, 10, math.inf,  9, 10,  4,  8, math.inf, 11,  7,  9],
                     [ 6, math.inf,  9, 11,  0,  5,  8,  9, math.inf,  8,  6,  9, math.inf, 11, 10],
                     [ 6,  6, 10, 10,  5,  0, math.inf,  8,  9,  7,  9, math.inf,  6,  9,  5],
                     [ 8,  8, math.inf, math.inf,  8, math.inf,  0,  9, 10, 10, 11,  9, 10,  8,  5],
                     [ 7,  9,  9,  9,  9,  8,  9,  0,  6,  4,  8,  8,  5, math.inf,  7],
                     [math.inf,  6, 10, 10, math.inf,  9, 10,  6,  0, math.inf, math.inf,  6,  8,  6, math.inf],
                     [10,  6,  7,  4,  8,  7, 10,  4, math.inf,  0,  5,  8,  8, math.inf, math.inf],
                     [ 4,  5, 11,  8,  6,  9, 11,  8, math.inf,  5,  0,  4,  6,  8, 10],
                     [math.inf,  7,  5, math.inf,  9, math.inf,  9,  8,  6,  8,  4,  0, 11,  6, 10],
                     [math.inf,  9,  5, 11, math.inf,  6, 10,  5,  8,  8,  6, 11,  0,  9,  7],
                     [ 5, 11,  5,  7, 11,  9,  8, math.inf,  6, math.inf,  8,  6,  9,  0, math.inf],
                     [10,  9, 11,  9, 10,  5,  5,  7, math.inf, math.inf, 10, 10,  7, math.inf,  0]])

