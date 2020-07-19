# -*- coding: utf-8 -*-
"""
@author: Roberto Manzanaro Pilling

La información está sacada de la base de datos EXIOBASE3 (https://www.exiobase.eu/index.php).Es una base de datos
específica para realizar análisis input output. En concreto, la versión que he utilizado es exiobase_3.4_iot_2011_ixi.
Para este análisis se necesitan los archivos A.txt, Y.txt y F.txt de EXIOBASE.
El objetivo final es ver las emisiones de las industrias españolas.

F.txt = emisiones
Y.txt = demandas de consumidores finales
A.txt = matrices de coeficientes
"""
from ast import literal_eval
import numpy as np
import random
import pandas as pd

NUMERO_INDUSTRIAS = 163
NUMERO_PAISES = 49

# 49 países
paises = ["AUT", "BEL", "BGR", "CYP", "CZE", "DEU", "DNK", "EST", "ESP", "FIN", "FRA", "GRC", "HRV", "HUN", "IRL",
          "ITA", "LTU", "LUX", "LVA", "MLT", "NLD", "POL", "PRT", "ROM", "SWE", "SVN", "SVK", "GBR", "USA", "JPN",
          "CHN", "CAN", "KOR", "BRA", "IND", "MEX", "RUS", "AUS", "CHE", "TUR", "TWN", "NOR", "IDN", "ZAF", "WWA",
          "WWL", "WWE", "WWF", "WWM"]
# 163 industrias
industrias = ["Cultivation of paddy rice", "Cultivation of wheat", "Cultivation of cereal grains nec", "Cultivation of vegetables, fruit, nuts",
              "Cultivation of oil seeds", "Cultivation of sugar cane, sugar beet", "Cultivation of plant-based fibers", "Cultivation of crops nec",
              "Cattle farming", "Pigs farming", "Poultry farming", "Meat animals nec", "Animal products nec", "Raw milk", "Wool, silk-worm cocoons",
              "Manure treatment (conventional), storage and land application", "Manure treatment (biogas), storage and land application",
              "Forestry, logging and related service activities (02)", "Fishing, operating of fish hatcheries and fish farms; service activities incidental to fishing (05)",
              "Mining of coal and lignite; extraction of peat (10)", "Extraction of crude petroleum and services related to crude oil extraction, excluding surveying",
              "Extraction of natural gas and services related to natural gas extraction, excluding surveying", "Extraction, liquefaction, and regasification of other petroleum and gaseous materials",
              "Mining of uranium and thorium ores (12)", "Mining of iron ores", "Mining of copper ores and concentrates", "Mining of nickel ores and concentrates",
              "Mining of aluminium ores and concentrates", "Mining of precious metal ores and concentrates", "Mining of lead, zinc and tin ores and concentrates",
              "Mining of other non-ferrous metal ores and concentrates", "Quarrying of stone", "Quarrying of sand and clay",
              "Mining of chemical and fertilizer minerals, production of salt, other mining and quarrying n.e.c.", "Processing of meat cattle",
              "Processing of meat pigs", "Processing of meat poultry", "Production of meat products nec", "Processing vegetable oils and fats",
              "Processing of dairy products", "Processed rice", "Sugar refining", "Processing of Food products nec", "Manufacture of beverages",
              "Manufacture of fish products", "Manufacture of tobacco products (16)", "Manufacture of textiles (17)", "Manufacture of wearing apparel; dressing and dyeing of fur (18)",
              "Tanning and dressing of leather; manufacture of luggage, handbags, saddlery, harness and footwear (19)",
              "Manufacture of wood and of products of wood and cork, except furniture; manufacture of articles of straw and plaiting materials (20)",
              "Re-processing of secondary wood material into new wood material", "Pulp", "Re-processing of secondary paper into new pulp", "Paper",
              "Publishing, printing and reproduction of recorded media (22)", "Manufacture of coke oven products", "Petroleum Refinery",
              "Processing of nuclear fuel", "Plastics, basic", "Re-processing of secondary plastic into new plastic", "N-fertiliser",
              "P- and other fertiliser", "Chemicals nec", "Manufacture of rubber and plastic products (25)", "Manufacture of glass and glass products",
              "Re-processing of secondary glass into new glass", "Manufacture of ceramic goods", "Manufacture of bricks, tiles and construction products, in baked clay",
              "Manufacture of cement, lime and plaster", "Re-processing of ash into clinker", "Manufacture of other non-metallic mineral products n.e.c.",
              "Manufacture of basic iron and steel and of ferro-alloys and first products thereof", "Re-processing of secondary steel into new steel",
              "Precious metals production", "Re-processing of secondary preciuos metals into new preciuos metals", "Aluminium production",
              "Re-processing of secondary aluminium into new aluminium", "Lead, zinc and tin production", "Re-processing of secondary lead into new lead, zinc and tin",
              "Copper production", "Re-processing of secondary copper into new copper", "Other non-ferrous metal production",
              "Re-processing of secondary other non-ferrous metals into new other non-ferrous metals", "Casting of metals",
              "Manufacture of fabricated metal products, except machinery and equipment (28)", "Manufacture of machinery and equipment n.e.c. (29)",
              "Manufacture of office machinery and computers (30)", "Manufacture of electrical machinery and apparatus n.e.c. (31)",
              "Manufacture of radio, television and communication equipment and apparatus (32)", "Manufacture of medical, precision and optical instruments, watches and clocks (33)",
              "Manufacture of motor vehicles, trailers and semi-trailers (34)", "Manufacture of other transport equipment (35)",
              "Manufacture of furniture; manufacturing n.e.c. (36)", "Recycling of waste and scrap", "Recycling of bottles by direct reuse",
              "Production of electricity by coal", "Production of electricity by gas", "Production of electricity by nuclear",
              "Production of electricity by hydro", "Production of electricity by wind", "Production of electricity by petroleum and other oil derivatives",
              "Production of electricity by biomass and waste", "Production of electricity by solar photovoltaic", "Production of electricity by solar thermal",
              "Production of electricity by tide, wave, ocean", "Production of electricity by Geothermal", "Production of electricity nec",
              "Transmission of electricity", "Distribution and trade of electricity", "Manufacture of gas; distribution of gaseous fuels through mains",
              "Steam and hot water supply", "Collection, purification and distribution of water (41)", "Construction (45)",
              "Re-processing of secondary construction material into aggregates", "Sale, maintenance, repair of motor vehicles, motor vehicles parts, motorcycles, motor cycles parts and accessoiries",
              "Retail sale of automotive fuel", "Wholesale trade and commission trade, except of motor vehicles and motorcycles (51)",
              "Retail trade, except of motor vehicles and motorcycles; repair of personal and household goods (52)", "Hotels and restaurants (55)",
              "Transport via railways", "Other land transport", "Transport via pipelines", "Sea and coastal water transport", "Inland water transport", "Air transport (62)", "Supporting and auxiliary transport activities; activities of travel agencies (63)", "Post and telecommunications (64)", "Financial intermediation, except insurance and pension funding (65)", "Insurance and pension funding, except compulsory social security (66)", "Activities auxiliary to financial intermediation (67)", "Real estate activities (70)", "Renting of machinery and equipment without operator and of personal and household goods (71)", "Computer and related activities (72)", "Research and development (73)", "Other business activities (74)", "Public administration and defence; compulsory social security (75)", "Education (80)", "Health and social work (85)", "Incineration of waste: Food", "Incineration of waste: Paper", "Incineration of waste: Plastic", "Incineration of waste: Metals and Inert materials", "Incineration of waste: Textiles", "Incineration of waste: Wood", "Incineration of waste: Oil/Hazardous waste", "Biogasification of food waste, incl. land application", "Biogasification of paper, incl. land application", "Biogasification of sewage slugde, incl. land application", "Composting of food waste, incl. land application", "Composting of paper and wood, incl. land application", "Waste water treatment, food", "Waste water treatment, other", "Landfill of waste: Food", "Landfill of waste: Paper", "Landfill of waste: Plastic", "Landfill of waste: Inert/metal/hazardous", "Landfill of waste: Textiles", "Landfill of waste: Wood", "Activities of membership organisation n.e.c. (91)", "Recreational, cultural and sporting activities (92)", "Other service activities (93)", "Private households with employed persons (95)", "Extra-territorial organizations and bodies"]

"""
Esta función toma el archivo F.txt y extrae las emisiones de España de CO2 en 2011.

ENTRADA: ruta_a_F es la ruta del archivo "F.txt" y ruta_salida_F_tratada es la ruta donde se ubicará el archivo de salida.

SALIDA: escribe en la ruta deseada (ruta_salida_F_tratada) un array con 163 elementos en la que el elemento i indica el
CO2 que ha emitido la industria i a la atmósfera.
"""
def preparar_tabla_emisiones(ruta_a_F, ruta_salida_F_tratada):
    with open(ruta_a_F, 'r') as myfile:
        data = myfile.read()

    # Esta constante nos permiten localizar los datos de emisiones de España. Antes de la información que nos interesa
    # hay 8 países.
    primera_posicion_esp = 1 + NUMERO_INDUSTRIAS * 8

    data_list = data.split('\n')
    # Cogemos la línea 26 de F.txt que contiene la información del CO2. Lo pasamos a lista con split('\t') y finalmente
    # cogemos los datos relevantes a España de las 163 industrias.
    CO2 = data_list[25].split('\t')[primera_posicion_esp:primera_posicion_esp + NUMERO_INDUSTRIAS]
    # Pasamos a float todos los elementos de la lista.
    CO2 = [float(i) for i in CO2]

    f = open(ruta_salida_F_tratada, "w")
    f.write(str(CO2))
    f.close()
    return None


"""
Esta función toma el archivo Y.txt y extrae las demandas finales de los 49 países de productos españoles en 2011.
EXIOBASE3 segrega la demanda final en 7 categorías: Final consumption expenditure by households, Final consumption 
expenditure by non-profit organisations serving households (NPISH), Final consumption expenditure by government, Gross 
fixed capital formation, Changes in inventories, Changes in valuables y Exports: Total (fob).

Para el algoritmo de EE-IOA nos interesa obtener una única demanda final por lo que se suman las 7 demandas. 

ENTRADA: ruta_a_Y es la ruta del archivo "Y.txt" y ruta_salida_Y_tratada es la ruta donde se ubicará el archivo de salida.

SALIDA: escribe en la ruta deseada (ruta_salida_Y_tratada) una matriz 163x49. El elemento j de la fila i de la matriz 
corresponde a la demanda final de la industria i en el país j.
"""
def preparar_tabla_demandas(ruta_a_Y, ruta_salida_Y_tratada):
    with open(ruta_a_Y, 'r') as myfile:
        data = myfile.read()

    NUMERO_DEMANDAS = 7
    primera_posicion_esp = 3 + NUMERO_INDUSTRIAS * 8
    data_list = data.split('\n')
    # Cogemos las líneas que dan la información de España.
    espania = data_list[primera_posicion_esp:primera_posicion_esp + NUMERO_INDUSTRIAS]
    lista_demandas_disgregadas = []
    for i in range(0, NUMERO_INDUSTRIAS):
        # Transformamos con split('\t') las líneas en arrays y desechamos los dos primeros elementos del array por ser
        # encabezados.
        lista_str = espania[i].split('\t')[2:]
        # Pasamos de str a float los elementos del array.
        lista_float = [float(i) for i in lista_str]
        lista_demandas_disgregadas.append(lista_float)
    lista_demandas_agregadas = []
    for i in range(0, NUMERO_INDUSTRIAS):
        lista_demandas_agregadas.append([])
        fila = lista_demandas_disgregadas[i]
        for j in range(0, NUMERO_PAISES):
            lista_demandas_agregadas[i].append(sum(fila[NUMERO_DEMANDAS * j:NUMERO_DEMANDAS * (j + 1)]))
    f = open(ruta_salida_Y_tratada, "w")
    f.write(str(lista_demandas_agregadas))
    f.close()
    return None


"""
Esta función toma el archivo A.txt y extrae las matrices input-output de exportaciones de España hacia cada uno de los 
49 países contenidos en EXIOBASE3. 

ENTRADA: ruta_a_A es la ruta del archivo "A.txt" y ruta_salida_A_tratada es la ruta donde se ubicará el archivo de 
salida.

SALIDA: escribe en la ruta deseada (ruta_salida_A_tratada) 49 matrices (una por cada país) de dimensión 
163x163 (cada matriz es como la matriz de ejemplo de la sección 3.1, solo que en vez de 2 industrias hay 163). 
"""
def preparar_tabla_matrices(ruta_a_A, ruta_salida_A_tratada):
    with open(ruta_a_A, 'r') as myfile:
        data = myfile.read()

    primera_posicion_esp = 3 + NUMERO_INDUSTRIAS * 8
    matrices = [[] for _ in range(0, NUMERO_PAISES)]
    # Desechamos las tres primeras líneas por ser encabezados
    data_list = data.split('\n')[primera_posicion_esp:primera_posicion_esp + NUMERO_INDUSTRIAS]
    # lista_previa = []

    for i in range(0, NUMERO_INDUSTRIAS):
        # Cogemos la fila data_list[i], la pasamos a array con split('\t') y cogemos las columnas de España.
        # lista_previa.append(data_list[i].split('\t')[primera_posicion_esp:primera_posicion_esp + NUMERO_INDUSTRIAS])
        data_list[i] = data_list[i].split('\t')

    for i in range(0, NUMERO_PAISES):
        for j in range(0, NUMERO_INDUSTRIAS):
            lista_previa = data_list[j][2 + i * NUMERO_INDUSTRIAS: 2 + (i+1) * NUMERO_INDUSTRIAS]
            matrices[i].append([float(k) for k in lista_previa])

    f = open(ruta_salida_A_tratada, "w")
    f.write(str(matrices))
    f.close()
    return None


"""
Esta función toma los archivos A tratada.txt, Y tratada.txt y F tratada.txt. En F tratada.txt tenemos el consumo de CO2 
de cada una de las 163  industrias. Sin embargo, cuando apliquemos Leontief en eeioa() a cada país por separado tenemos
que ver cuales son las emisiones de CO2 solo de los productos españoles que compra ese país. En esta función de 
disgregan estas emisiones para los distintos paises. Esto lo hacemos viendo las ventas totales de una industria española
a todos los demás países y con este total vemos qué porcentaje compra cada país. Así, multiplicando el porcentaje de un
país por las emisiones totales obtenemos las emisiones de CO2 necesarias para fabricar lo que compra ese país.

ENTRADA: toma cuatro rutas de archivos. ruta_a_A_tratada es la ruta al archivo obtenido con la función
preparar_tabla_matrices(), ruta_a_Y_tratada es la ruta al archivo obtenido con la función preparar_tabla_demandas(),
ruta_a_F_tratada es la ruta al archivo obtenido con la función  preparar_tabla_emisiones() y ruta_salida_emisiones es 
la ruta en la que se escribe la salida de esta función.

SALIDA: escribe en la ruta deseada (ruta_salida_emisiones) una matriz de tamaño 163x49. El elemento j de la fila i de 
esta matriz corresponde a las emisiones emitidas por la industria i en el país j.
"""
def emisiones_por_pais(ruta_a_A_tratada, ruta_a_Y_tratada, ruta_a_F_tratada, ruta_salida_emisiones):
    # Centramos en el CO2
    # Emisiones de cada industria en todos los paises
    with open(ruta_a_A_tratada, 'r') as myfile:
        matrices = myfile.read()
    with open(ruta_a_Y_tratada, 'r') as myfile:
        demandas = myfile.read()
    with open(ruta_a_F_tratada, 'r') as myfile:
        emisiones = myfile.read()

    # literal_eval transforma un string en array
    matrices = literal_eval(matrices)
    emisiones = literal_eval(emisiones)
    demandas = literal_eval(demandas)

    resultado = []

    # Veamos cómo se disgregan las emisiones de una industria en función de los países que importan los productos.
    for i in range(0, NUMERO_INDUSTRIAS):
        emisiones_industria = emisiones[i]
        gasto_de_paises = []
        # Veamos cuanto corresponde a cada pais
        for j in range(0, NUMERO_PAISES):
            pais = matrices[j]
            # Sumo la columna i de la industria i del pais j y la demanda final del pais j de industria i
            suma = sum([lista[i] for lista in pais]) + demandas[i][j]
            gasto_de_paises.append(suma)
        # El dinero total que todos los paises gastan en la industria i
        suma_paises = sum(gasto_de_paises)
        # Cantidad de las emisiones que va a cada pais en esta industra
        emisiones_proporcionales = []
        for k in range(0, NUMERO_PAISES):
            # Diferenciamos dos casos para evitar dividir por 0. Si suma_paises == 0 no se habrá fabricado nada y por lo
            # tanto las emisiones serán 0.
            if suma_paises == 0:
                emisiones_proporcionales.append(0)
            else:
                emisiones_proporcionales.append((gasto_de_paises[k] * emisiones_industria) / suma_paises)
        resultado.append(emisiones_proporcionales)

    f = open(ruta_salida_emisiones, "w")
    f.write(str(resultado))
    f.close()
    return None

"""
Esta función toma los archivos A tratada.txt, Y tratada.txt y emisiones por pais.txt y aplica la matriz de Leontief para
ver las emisiones reales de las distintas idustrias españolas. 

ENTRADA: toma cuatro rutas de archivos. ruta_a_A_tratada es la ruta al archivo obtenido con la función
preparar_tabla_matrices(), ruta_a_Y_tratada es la ruta al archivo obtenido con la función preparar_tabla_demandas(), 
ruta_a_emisiones es la ruta al archivo obtenido con la función emisiones_por_pais() y ruta_salida_eeioa es la ruta 
en la que se escribe la salida de esta función.

SALIDA: escribe en la ruta deseada (ruta_salida_eeioa) los resultados del análisis EE-IOA descrito en la sección 3.1 del
trabajo. La salida son 49 arrays (uno por país) de 163 elementos cada uno (el número de industrias de cada uno). La 
posición j del vector iindica las emisiones de CO2 que España ha emitido a la atmósfera para fabricar productos de la 
industria j que son exportados al país i.
"""
def eeioa(ruta_a_A_tratada, ruta_a_Y_tratada, ruta_a_emisiones, ruta_salida_eeioa):
    with open(ruta_a_A_tratada, 'r') as myfile:
        matrices = myfile.read()
    with open(ruta_a_Y_tratada, 'r') as myfile:
        demandas = myfile.read()
    with open(ruta_a_emisiones, 'r') as myfile:
        emisiones_proporcionales = myfile.read()

    matrices = np.array(literal_eval(matrices))
    demandas = np.array(literal_eval(demandas))
    emisiones_proporcionales = np.array(literal_eval(emisiones_proporcionales))
    # vector_de_cambio es un vector de longitud 163 compuesto por 162 ceros y un 1 al final. Este vector se utiliza
    # para sustituir una fila o columna de ceros en una matriz, ya que para haber inversa no puede ocurrir esto. Sin
    # embargo debemos tener cuidado ya que si hay 2 filas o columnas sustituidas por vector_de_cambio el determinante de
    # la matriz será cero y no tendrá inversa. Es por esto que cada vez que se introduce vector_de_cambio en una matriz
    # el 1 varía en una cantidad muy pequeña.
    vector_de_cambio = np.zeros(NUMERO_INDUSTRIAS - 1)
    vector_de_cambio = np.append(vector_de_cambio, 1)
    columna_dividida = []
    identidad = np.identity(NUMERO_INDUSTRIAS)

    emisiones_finales = []
    # En cada i saco una matriz y hago Leonfief
    for i in range(0, NUMERO_PAISES):
        matriz = matrices[i]
        # Cojo la columna i de emisiones_proporcionales
        vector_emisiones = emisiones_proporcionales[:, i]
        demanda = demandas[:, i]
        vector_outputs_totales = []
        matriz_coef_tecnicos = []
        # Sacamos los vectores de output total
        for j in range(0, NUMERO_INDUSTRIAS):
            vector_outputs_totales.append(demanda[j] + sum(matriz[j, :]))
        # Hallemos la matriz
        for j in range(0, NUMERO_INDUSTRIAS):
            # Diferenciamos casos para no dividir por cero
            if vector_outputs_totales[j] != 0:
                columna_dividida = np.divide(matriz[:, j], vector_outputs_totales[j]).tolist()
            else:
                # Si es igual a cero significa que hay una fila o columna de ceros y debemos introducir vector_de_cambio
                # haciendo una pequeña variación.
                columna_dividida = vector_de_cambio
                columna_dividida[NUMERO_INDUSTRIAS - 1] += random.uniform(-0.01, 0.01)
            # Las uno como columnas
            matriz_coef_tecnicos.append(columna_dividida)
        # Ya tenemos la matriz de coeficientes haciendo la traspuesta
        matriz_coef_tecnicos = np.transpose(np.array(matriz_coef_tecnicos))
        # Aquí hallamos f, el vector de intensidad directa
        vector_intensidad_directa = np.zeros(163)
        for j in range(0, NUMERO_INDUSTRIAS):
            # Si es 0 dejamos a 0 vector_intensidad_directa[i]
            if vector_outputs_totales[j] != 0:
                vector_intensidad_directa[j] = vector_emisiones[j]/vector_outputs_totales[j]
        # Aplicamos la matriz de Leontief
        inversa = np.linalg.inv(identidad - matriz_coef_tecnicos)
        resultado = np.dot(vector_intensidad_directa, inversa)
        emisiones_finales.append(resultado.tolist())

    f = open(ruta_salida_eeioa, "w")
    f.write(str(emisiones_finales))
    f.close()
    return None



"""
Esta función coge el resultado del análisis eeioa (en formato array de arrays) y lo pasa a formato excel para poder
visualizarlo.

ENTRADA: ruta_entrada_eeioa es la ruta del archivo eeioa y ruta_salida_excel es la ruta donde se ubicará el archivo
excel de salida.
 
SALIDA: escribe en la ruta deseada (ruta_salida_excel) los resultados del análisis EE-IOA en formato excel. 
"""
def pintar_tabla(ruta_entrada_eeioa, ruta_salida_excel):
    with open(ruta_entrada_eeioa, 'r') as myfile:
        emisiones = myfile.read()
    emisiones = np.array(literal_eval(emisiones))
    df = pd.DataFrame(emisiones)
    filepath = ruta_salida_excel
    df.to_excel(filepath, index=False)
    return None

pintar_tabla()
#preparar_tabla_matrices(r'C:\Users\Roberto\Documents\Asignaturas-Uni\TFG\exiobase nueva\A.txt',r'C:\Users\Roberto\Documents\Asignaturas-Uni\TFG\exiobase nueva\A tratada.txt')
#emisiones_por_pais(r'C:\Users\Roberto\Documents\Asignaturas-Uni\TFG\exiobase nueva\A tratada.txt', r'C:\Users\Roberto\Documents\Asignaturas-Uni\TFG\exiobase nueva\Y tratada.txt', r'C:\Users\Roberto\Documents\Asignaturas-Uni\TFG\exiobase nueva\F tratada.txt', r'C:\Users\Roberto\Documents\Asignaturas-Uni\TFG\exiobase nueva\emisiones por pais.txt')
#eeioa(r'C:\Users\Roberto\Documents\Asignaturas-Uni\TFG\exiobase nueva\A tratada.txt', r'C:\Users\Roberto\Documents\Asignaturas-Uni\TFG\exiobase nueva\Y tratada.txt', r'C:\Users\Roberto\Documents\Asignaturas-Uni\TFG\exiobase nueva\emisiones por pais.txt', r'C:\Users\Roberto\Documents\Asignaturas-Uni\TFG\exiobase nueva\eeioa.txt')