import collections
from io import open
import random
import math
from grafo import *
from collections import deque
import sys
sys.setrecursionlimit(10000) # Por default es 999


# Recorrido tipo "Breadth First Search" 
# Pre: Recibe como parametro el grafo dirigido y no ponderado, y el vector origen desde el cual se 
# desea iniciar el recorrido. Opcionalmente puede recibir un vector destino y/o un orden maximo a fin de 
# finalizar el recorrido una vez alcanzada el destino y/o orden maximo.
# Post: Retorna un diccionario con el orden de cada vertice en el grafo y un diccionario con
# el padre correspondiente a cada vertice, de modo de poder reconstruir el recorrido.
def bfs(grafo, origen, destino=None, ordenMax=None):
    visitados = set()
    padre = {}
    orden = {}
    cola = deque()
    visitados.add(origen)
    padre[origen] = None
    orden[origen] = 0
    cola.append(origen)
    while(cola):
        vertice = cola.popleft()

        if(destino != None and vertice == destino):
            return padre,orden
        if(ordenMax and ordenMax == orden[vertice]):
            return padre,orden

        for adyacente in vertice.obtenerAdyacentes():
            if adyacente not in visitados:
                visitados.add(adyacente)
                padre[adyacente] = vertice
                orden[adyacente] = orden[vertice]+1
                cola.append(adyacente)

    return padre,orden

# Recorrido minimo con BFS con destino vertice.
# Pre: Recibe por parametro un grafo dirigido y no ponderado, vertice origen y vertice destino.
# Post: Retorna el orden del vertice destino y una lista con el camino correspondiente
# de origen a destino.
def recorridoMinimoBfs(grafo, origen, destino):
    padres, orden = bfs(grafo, origen, destino)
    if(destino not in padres): return None, None
    camino = []
    vertice = destino
    camino.append(vertice)
    while(padres[vertice]!=None):
        camino.append(padres[vertice])
        vertice = padres[vertice]
    return orden[destino], camino[::-1]

# Recorrido radial con BFS de n distancia maxima.
# Pre: Recibe por parametro un grafo dirigido y no ponderado, vertice origen y una distancia maxima.
# Post: Retorna una lista con los vertices afectados distMax un radio n del origen
def recorridoMinimoBfsMaximo(grafo, origen, distMax):
    padres, orden = bfs(grafo, origen, None, distMax)
    verticesAfectados = []
    for key in padres.keys():
        verticesAfectados.append(key)
    return verticesAfectados


# Comunidades en forma aproximada a traves de label_propagation
# Pre: Recibe por parametro un grafo dirigido y no ponderado, opcionamente un 'n' iteraciones, por default 5,
# esta ultima permite ajustar el numero de iteraciones, a mayor n mas compactas seran las comunidades
# Post: Retorna una lista de comunidades con sus respectivos vertices.
def label_propagation(grafo, n=5):
    label = {}
    i = 1
    for vertice in grafo:
        label[vertice] = i
        i += 1
    for i in range(n):
        for vertice in grafo:
            if len(vertice.obtenerAdyacentes()) > 0:
                label[vertice] = max_freq(label, vertice.obtenerAdyacentes())

    comunidades = {}
    for vertice, comunidad in label.items():
        if comunidad not in comunidades:
            comunidades[comunidad] = []
        comunidades[comunidad].append(vertice)

    return comunidades

# Funcion auxiliar label_propagation
def max_freq(label, adyacentes):
    labelAdyacentes = []
    for adyacente in adyacentes:
        labelAdyacentes.append(label[adyacente])
    return (collections.Counter(labelAdyacentes).most_common()[0][0])


# Centralidad aproximada, a traves de random_walks, de n "cantidad" de vertices
# Pre: Recibe por parametro un grafo dirigido y no ponderado, n 'cantidad' de vertices centrales
# que se buscan
# Post: Retorna una lista de los n "cantidad" de vertices mas centrales de mayor a menor
def centralidad_aprox(grafo, cantidad):
    caminos = random_walks(grafo, 1000, 300)  # Numero arbitrario
    recorridoTotal = []
    for camino in caminos:
        for vertice in camino:
            recorridoTotal.append(vertice)

    verticesCentrales = []
    candidatosCentrales = collections.Counter(recorridoTotal).most_common()
    for i in range(cantidad):
        if i < len(grafo) - 1:
            verticesCentrales.append(candidatosCentrales[i][0])
    return verticesCentrales

# Randon walks - Realiza caminos aleatoreos a lo largo del grafo. 
# Pre: Recibe por parametro un grafo dirigido y no ponderado, una longitudCamino y cantidadCaminos
# Post: Retorna un lista de n 'cantidadCaminos' de longitud 'longitudCaminos' con
# todos los vertices que componen al camino  
def random_walks(grafo, longitudCamino, cantidadCaminos):
    caminos = []
    vertices = grafo.obtenerVertices()
    for i in range(cantidadCaminos):
        camino = []
        verticeActual = random.choice(vertices)
        camino.append(verticeActual)
        for j in range(longitudCamino):
            adyacentes = verticeActual.obtenerAdyacentes()
            if adyacentes:
                verticeActual = random.choice(verticeActual.obtenerAdyacentes())
                camino.append(verticeActual)
        caminos.append(camino)

    return caminos

# Recorrido minimo de tipo BFS, con multiples origenes hacia 'kMasImp' mas centrales
# Pre: Recibe por parametro un grafo dirigido y no ponderado, una lista de vertices origen y
# un int 'kMasImp' vertices de mayor Centalidad. 
# Post: Retorna el camino de menor longitud, desde uno de los vertices origen hacia uno de los
# "kMasImp" mas centrales. Optando a estos, orgien y destino, del modo mas conveniente a la finalidad
# del camino mas corto
def recorrido_min_multi_origen_multi_destino(grafo, idVerticesOrigen, kMasImp):
    kVerticesMasImp = centralidad_aprox(grafo, kMasImp)
    verticesOrigen = []
    for idVerticeOrigen in idVerticesOrigen:
        vertice = grafo.obtenerVertice(idVerticeOrigen)
        if (vertice != None):
            verticesOrigen.append(vertice)
    caminoMin = []
    if len(verticesOrigen) == 0: return caminoMin
    ordenMin = math.inf
    for verticeOrigen in verticesOrigen:
        for kVerticeMasImp in kVerticesMasImp:
            orden, camino = recorridoMinimoBfs(grafo, verticeOrigen, kVerticeMasImp)
            if orden and orden < ordenMin:
                ordenMin = orden
                caminoMin = camino

    return caminoMin


# Componente fuertemente conexo - Algoritmo de Tarjan
# Pre: 
# Post: 
def dfs_cfc(grafo, v, visitados, orden, p, s, cfcs, en_cfs):
    visitados.add(v)
    s.append(v)
    p.append(v)
    for w in v.obtenerAdyacentes():
        if w not in visitados:
            orden[w] = orden[v] + 1
            dfs_cfc(grafo, w, visitados, orden, p, s, cfcs, en_cfs)
        elif w not in en_cfs:
            while p and orden[p[-1]] > orden[w]:
                p.pop()

    if p and p[-1] == v:
        p.pop()
        z = None
        nueva_cfc = []
        while z != v:
            z = s.pop()
            en_cfs.add(z)
            nueva_cfc.append(z)
        cfcs.append(nueva_cfc)

# Componente fuertemente conexo - Algoritmo de Tarjan
# Pre:
# Post:
def cfc(grafo):
    visitados = set()
    orden = {}
    p = []
    s = []
    cfcs = []
    en_cfs = set()
    for v in grafo:
        if v not in visitados:
            orden[v] = 0
            dfs_cfc(grafo, v, visitados, orden, p, s, cfcs, en_cfs)
    return cfcs


# Ciclo de largo n en un grafo - entrategia backtracking
def _ciclo_largo_n(visitados, origen, actual, n):
    if n == 1:
        if origen in actual.obtenerAdyacentes():
            visitados.append(origen)
            return True
        else:
            return False
    else:
        for adyacente in actual.obtenerAdyacentes():
            if adyacente not in visitados:
                visitados.append(adyacente)
                if(_ciclo_largo_n(visitados, origen, adyacente, n-1) == False):
                    visitados.pop()
                else:
                    return True
        return False

# Ciclo de largo n en un grafo
# Pre: Recibe por parametro un grafo dirigido no ponderado, un vertice origen y un 'n'
# como largo del ciclo
# Post: Retorna una lista con el camino del ciclo de largo 'n'
def ciclo_largo_n(grafo, origen, n):
    visitados = [origen]
    _ciclo_largo_n(visitados, origen, origen, n)
    return visitados


# Carga un grafo
# Pre: Recibe por parametro un fichero .tsv en formato:
# id_verticeOrigen   id_verticeDestino
# Post: Retorna un grafo con los vertices y aristas contenidas en el archivo
def cargarGrafo(ficheroRuta):
    grafo = Grafo()
    with open(ficheroRuta,'r') as fichero:
        for linea in fichero:
            origen, destino = linea.strip('\n').split('\t')
            if (origen != destino):
                grafo.agregarArista(str(origen),str(destino))
        fichero.close()
    return grafo