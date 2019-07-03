import collections
from io import open
import random
import math
from grafo import *
import sys
sys.setrecursionlimit(10000)
from collections import deque

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

# Recorrido minimo con BFS con destino vertice
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

# Recorrido minimo con BFS con maximo de n saltos
def recorridoMinimoBfsMaximo(grafo, origen, distMax):
    padres, orden = bfs(grafo, origen, None, distMax)
    verticesAfectados = []
    for key in padres.keys():
        verticesAfectados.append(key)
    return verticesAfectados

# Comunidades - label_propagation
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

def max_freq(label, adyacentes):
    labelAdyacentes = []
    for adyacente in adyacentes:
        labelAdyacentes.append(label[adyacente])
    return (collections.Counter(labelAdyacentes).most_common()[0][0])

# Centralidad aproximada
def centralidad_aprox(grafo, cantidad):
    caminos = random_walks(grafo, 30, 30)  # Numero arbitrario
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


def random_walks(grafo, longitudCamino, cantidadCaminos):
    caminos = []
    vertices = grafo.obtenerVertices()
    for i in range(cantidadCaminos):
        camino = []
        verticeActual = random.choice(vertices)
        camino.append(verticeActual)
        for j in range(longitudCamino):
            verticeActual = random.choice(verticeActual.obtenerAdyacentes())
            camino.append(verticeActual)
        caminos.append(camino)

    return caminos


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
            if orden < ordenMin:
                ordenMin = orden
                caminoMin = camino

    return caminoMin


def dfs_cfc(grafo, v, visitados, orden, p, s, cfcs, en_cfs):
    visitados.add(v)
    s.append(v)
    p.append(v)
    for w in v.obtenerAdyacentes():
        if w not in visitados:
            orden[w] = orden[v] + 1
            dfs_cfc(grafo, w, visitados, orden, p, s, cfcs, en_cfs)
        elif w not in en_cfs:
            while len(p) != 0 and orden[p[-1]] > orden[w]:
                p.pop()

    if (len(p) != 0) and p[-1] == v:
        p.pop()
        z = None
        nueva_cfc = []
        while z != v:
            z = s.pop()
            en_cfs.add(z)
            nueva_cfc.append(z)
        cfcs.append(nueva_cfc)


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


def ciclo_largo_n(grafo, origen, n):
    visitados = [origen]
    _ciclo_largo_n(visitados, origen, origen, n)
    return visitados


def cargarGrafo(ficheroRuta):
    grafo = Grafo()
    with open(ficheroRuta,'r') as fichero:
        for linea in fichero:
            origen, destino = linea.strip('\n').split('\t')
            if (origen != destino):
                grafo.agregarArista(str(origen),str(destino))
        fichero.close()
    return grafo