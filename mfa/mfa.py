# -*- coding: utf-8 -*-
"""
@author: Roberto Manzanaro Pilling

Algoritmo MFA (SECCIÓN 3.2 DEL TFG):
    -CASO 1:
        caso: flujos(1950,2050,20, [1.3,30,20])
        media: 0.008
    -CASO 2:
        caso: flujos(1900,2100,20, [1.5, 30, 45])
        media: 0.031
    - CASO 3:
        caso: flujos(1950,2500,20, [1.3,30,20])
        media: 0.12
"""

from scipy.stats import norm
from scipy.stats import weibull_min
import numpy as np
import matplotlib.pyplot as plt
from time import time

# Número de viviendas entre los años 2013 y 2019.
viviendas_2013_2019 = [18217300, 18303100, 18346200, 18406100, 18472800, 18535900, 18625700]

"""
Esta función calcula los números el número de viviendas aproximado en los años de estudio. La información de las 
viviendas en España de 2013 a 2019 está extraída del INE. Las viviendas se aproximan con una regresión lineal.

ENTRADA: inicio y final son dos naturales que indican el primer año de estudio y el último respectivamente.

SALIDA: array que contiene el número de viviendas en cada uno de los años de nuestro estudio
"""
def viviendas(inicio, final):
    b0, b1 = coeficientes_regresion()
    resultado = viviendas_2013_2019
    # Tomamos los años de 2013 a 2019 contenidos en el intervalo [inicio, final]. El bucle se realiza 7 veces ya que hay
    # 7 años de 2013 a 2020.
    for i in range(0, 7):
        if i + 2013 < inicio or i + 2013 > final:
            # Quitamos el número de viviendas correspondientes al año i + 2013 por no estar en el intervalo de estudio
            resultado.pop(i)
    if inicio < 2013:
        parte_anterior = [b0 + b1 * i for i in range(inicio, 2013)]
        resultado = parte_anterior + resultado
    if 2019 < final:
        parte_posterior = [b0 + b1 * i for i in range(2020, final + 1)]
        resultado = resultado + parte_posterior
    # Redondeamos los números de viviendas al entero más próximo.
    resultado = [int(round(elemento)) for elemento in resultado]
    return resultado


"""
Esta función calcula la recta de regresión con la que se aproxiará el número de viviendas en la función 
viviendas(inicio, final). La recta creada para los datos del INE es -112437500.0 + 64907.142857142855*x

SALIDA: devuelve dos float: b0 y b1. b0 es el punto de corte con el eje de ordenadas de la recta de regresión y b1 es la
pendiente de la misma.
"""
def coeficientes_regresion():
    viviendas = np.array(viviendas_2013_2019)
    anios = np.arange(2013, 2020)
    # Disponemos información de 7 años (2013-2019)
    media_viviendas = sum(viviendas) / 7
    media_anios = sum(anios) / 7
    resta_viviendas = viviendas - media_viviendas
    resta_anios = anios - media_anios
    resta_anios_cuadrado = np.square(resta_anios)
    anios_viviendas = resta_viviendas * resta_anios

    b1 = sum(anios_viviendas) / sum(resta_anios_cuadrado)
    b0 = media_viviendas - b1 * media_anios

    return b0, b1

"""
Esta función calcula la función de renovación cíclica que necesitamos para modelizar las renovaciones de viviendas.

ENTRADA: 
    - numero_de_anios es un natural que indica cuántos años queremos estudiar. 
    - tau indica la media de años de renovación de una vivienda.
    - dist_vida_desplazada es la función de vida desplazada.
    - eje_anios es un array que contiene los años de estudio.

SALIDA: función de probabilidad de renovación de viviendas en los años de nuestro estudio.
"""
def renovaciones_ciclos(numero_de_anios, tau, dist_vida_desplazada, eje_anios):
    fun_renovacion = np.zeros(numero_de_anios)
    # Vemos el número de renovaciones que se pueden hacer en el periodo de tiempo que dura el estudio.
    numero_renovaciones = numero_de_anios // tau
    for i in range(numero_renovaciones):
        fun_renovacion = fun_renovacion + norm.pdf(eje_anios, tau + tau * i, 4) * dist_vida_desplazada
    return fun_renovacion

"""
Función principal que realiza el algoritmo principal de Material Flow Analysis.

ENTRADA: 
    - inicio: primer año de estudio. Tipo int
    - final: últimp año de estudio. Tipo int
    - tau: número de años en los que se renueva una vivienda de media. Tipo int
    - parametros_weibull es un array de tres elementos. El primero es la constante "c" que se utiliza en la función
      de distribución, el segundo es la traslación de la función de distribución (la trasladamos ya que hay un periodo 
      inicial tras construir una casa que es extremadamente improbable que sea demolida) y el tercero es "λ", el 
      parámetro de escala. LOS PARÁMETROS QUE YO HE UTILIZADO SON: [1.3, 30, 20]. Los tres elementos del array son de  
      tipo float.

SALIDA: tres arrays llamados nuevas, demoliciones, renovaciones. La longitud de cada uno de estos es el número de 
años de estudio. Los elementos de estos arrays son de tipo int.
"""
def flujos(inicio, final, tau, param_dem):
    numero_de_anios = final - inicio + 1
    stocks_viviendas = viviendas(inicio, final)
    # Extraemos los elementos de la variable de entrada param_dem
    c = param_dem[0]
    traslacion = param_dem[1]
    escala = param_dem[2]

    # x1 contiene tantos elementos como años de estudio hemos elegido.
    x1 = np.linspace(0, numero_de_anios - 1, numero_de_anios)
    # x2 tiene 20 años extra, para realizar las traslaciones.
    x2 = np.linspace(0, numero_de_anios + tau - 1, numero_de_anios + tau)
    # x3 es para dibujar las gráficas finales.
    x3 = np.linspace(inicio, final, numero_de_anios)

    # Inicializamos las matrices de demolicion y renovación
    matriz_dem = np.zeros((numero_de_anios, numero_de_anios))
    matriz_ren = np.zeros((numero_de_anios, numero_de_anios))
    # Inicializamos los arrays de salida del algoritmo
    nuevas = np.zeros(numero_de_anios)
    demoliciones = np.zeros(numero_de_anios)
    renovaciones = np.zeros(numero_de_anios)

    dist_vida = np.ones(numero_de_anios + tau) - weibull_min.cdf(x2, c, traslacion, escala)
    dist_vida_desplazada = dist_vida[tau:]
    dist_demoliciones = np.array(weibull_min.pdf(x1, c, traslacion, escala))
    dist_renovaciones = renovaciones_ciclos(numero_de_anios, tau, dist_vida_desplazada, x1)

    # c y escala los tomamos igual que en dist_demoliciones pero no trasladamos la función de probabilidad porque esta
    # función de probabilidad se centra en viviendas antiguas
    dist_demoliciones_inic = np.array(weibull_min.pdf(x1, c, 0, escala))
    # Tomamos la función de probabilidad uniforme porque suponemos que cada año se renueva aproximadamente el mismo
    # número de las viviendas iniciales. Damos el valor 1/tau porque suponemos que una vivienda se renueva de media una
    # vez cada tau años, por lo que la probabilidad de renovar en un año concreto es 1/tau
    dist_renovaciones_inic = np.full((1, numero_de_anios), 1/tau)

    # Condiciones iniciales
    matriz_dem[:, 0] = dist_demoliciones_inic * stocks_viviendas[0]
    matriz_ren[:, 0] = dist_demoliciones_inic * stocks_viviendas[0]
    nuevas[0] = matriz_dem[0, 0]
    demoliciones[0] = matriz_dem[0, 0]
    demoliciones[1] = matriz_dem[0, 1]
    renovaciones[0] = matriz_ren[0, 0]

    for i in range(1, numero_de_anios):
        aumento_stock = stocks_viviendas[i] - stocks_viviendas[i - 1]
        nuevas[i] = aumento_stock + demoliciones[i]
        renovaciones[i] = sum(matriz_ren[i, :i])
        if i + 1 < numero_de_anios:
            matriz_dem[i + 1:, i] = dist_demoliciones[:numero_de_anios - 1 - i] * nuevas[i]
            demoliciones[i + 1] = sum(matriz_dem[i + 1, :i + 1])
            matriz_ren[i + 1:, i] = dist_renovaciones[:numero_de_anios - 1 - i] * nuevas[i]

    plt.plot(x3, nuevas, 'r', label="Nº nuevas")
    plt.plot(x3, demoliciones, 'b', label="Nº derruidas")
    plt.plot(x3, renovaciones, 'g', label="Nº renovadas")
    plt.legend(loc="lower right", title="Viviendas", frameon=False)
    plt.show()

    return nuevas, demoliciones, renovaciones
