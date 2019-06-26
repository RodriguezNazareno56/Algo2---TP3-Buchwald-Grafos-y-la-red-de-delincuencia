import grafo
from bibliotecaFuncionesGrafos import *

class RedDeDelincuentes:

    def __init__(self, grafo):
        self.grafoDelincuentes = grafo

    def minimoSeguimiento(self, origen, destino):
        vOrigen = self.grafoDelincuentes.obtenerVertice(origen)
        vDestino = self.grafoDelincuentes.obtenerVertice(destino)
        orden, camino = recorridoMinimoBfs(self.grafoDelincuentes, vOrigen, vDestino)
        if ((orden and camino) is None):
            return print("Seguimiento imposible")
        for i in range(0, len(camino) - 1):
            print(camino[i], end=" -> ")
        print(camino[-1])

    def divulgarRumor(self, origen, distMax):
        vOrigen = self.grafoDelincuentes.obtenerVertice(origen)
        if (vOrigen == None): return print("El delincuente no existe")
        afectados = recorridoMinimoBfsMaximo(grafo, vOrigen, distMax)
        for i in range(0, len(afectados) - 1):
            print(afectados[i], end=", ")
        print(afectados[-1])

    def comunidades(self, n):
        comunidades = label_propagation(self.grafoDelincuentes, 5)  # El 5 este medio arbitrario
        num_comunidad = 1
        for comunidad, integrantes in comunidades.items():
            if len(integrantes) >= n:
                print("Comunidad" + str(num_comunidad) + ":", end=" ")
                for i in range(0, len(integrantes)):
                    print(integrantes[i], end=", ")
                print(integrantes[-1])
                num_comunidad += 1

    def mas_imp(self, cant):
        mas_importantes = centralidad_aprox(self.grafoDelincuentes, cant)
        for i in range(cant - 1):
            if i < len(self.grafoDelincuentes) - 1:
                print(mas_importantes[i], end=", ")
        print(mas_importantes[-1])

    def persecucion(self, agentesEncubiertos, kMasImp):
        caminoMin = persecucion_rapida(self.grafoDelincuentes, agentesEncubiertos, kMasImp)
        if (len(caminoMin) == 0):
            return print("La persecución no es posible")
        for i in range(0, len(caminoMin) - 1):
            print(caminoMin[i], end=" -> ")
        print(caminoMin[-1])