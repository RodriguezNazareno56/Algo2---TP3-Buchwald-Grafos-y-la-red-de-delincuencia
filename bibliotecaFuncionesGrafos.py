from collections import Counter
from io import open
import random
import math
from grafo import *

def bfs(grafo, origen, destino=None, ordenMax=None):
    visitados = []
    padre = {}
    orden = {}
    cola = [] # Esto deberia ser una cola y deberia tener mejor nombre
    visitados.append(origen)
    padre[origen] = None
    orden[origen] = 0
    cola.append(origen)
    while(len(cola) != 0):
        vertice = cola.pop(0)
        if(destino and vertice == destino):
            return padre,orden
        if(ordenMax and ordenMax == orden[vertice]):
            return padre,orden
        for adyacente in vertice.obtenerAdyacentes():
            if adyacente not in visitados:
                visitados.append(adyacente)
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
    return (Counter(labelAdyacentes).most_common()[0][0])

# Centralidad aproximada
def centralidad_aprox(grafo, cantidad):
    caminos = random_walks(grafo, 30, 30)  # Numero arbitrario
    recorridoTotal = []
    for camino in caminos:
        for vertice in camino:
            recorridoTotal.append(vertice)

    verticesCentrales = []
    candidatosCentrales = Counter(recorridoTotal).most_common()
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

def cargarGrafo(ficheroRuta):
    grafo = Grafo()
    with open(ficheroRuta,'r') as fichero:
        for linea in fichero:
            origen, destino = linea.strip('\n').split('\t')
            grafo.agregarArista(str(origen),str(destino))
        fichero.close()
    return grafo