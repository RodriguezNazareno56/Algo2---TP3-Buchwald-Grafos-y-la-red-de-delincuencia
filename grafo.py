class Vertice:

    def __init__(self, clave):
        self.id = clave
        self.conectadoA = {}

    def __str__(self):
        return str(self.id)

    def agregarVecino(self, vecino, ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def obtenerAdyacentes(self):
        return list(self.conectadoA.keys())

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self, vecino):
        return self.conectadoA[vecino]



class Grafo:

    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def __contains__(self, vertice):
        return vertice in self.listaVertices

    def __iter__(self):
        return iter(self.listaVertices.values())

    def __len__(self):
        return self.numVertices

    def agregarVertice(self, clave):
        self.numVertices += 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self, vertice):
        if vertice in self.listaVertices:
            return self.listaVertices[vertice]
        else:
            return None

    def agregarArista(self, origen, destino, ponderacion=0):
        if origen not in self.listaVertices:
            self.agregarVertice(origen)
        if destino not in self.listaVertices:
            self.agregarVertice(destino)
        self.listaVertices[origen].agregarVecino(self.listaVertices[destino], ponderacion)

    def obtenerVertices(self):
        return list(self.listaVertices.values())