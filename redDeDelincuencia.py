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
        self.__visualizar_resultado(camino, ' -> ')

    def divulgarRumor(self, origen, distMax):
        vOrigen = self.grafoDelincuentes.obtenerVertice(origen)
        if (vOrigen == None): return print("El delincuente no existe")
        afectados = recorridoMinimoBfsMaximo(grafo, vOrigen, distMax)
        self.__visualizar_resultado(afectados, ', ')

    def comunidades(self, n):
        comunidades = label_propagation(self.grafoDelincuentes, 5)  # El 5 este medio arbitrario
        num_comunidad = 1
        for comunidad, integrantes in comunidades.items():
            if len(integrantes) >= n:
                print("Comunidad " + str(num_comunidad) + ":", end=" ")
                self.__visualizar_resultado(integrantes, ', ')
                num_comunidad += 1

    def mas_imp(self, cant):
        mas_importantes = centralidad_aprox(self.grafoDelincuentes, cant)
        for i in range(cant - 1):
            if i < len(grafo) - 1:
                print(mas_importantes[i], end=", ")
        print(mas_importantes[-1])

    def persecucion(self, agentesEncubiertos, kMasImp):
        caminoMin = recorrido_min_multi_origen_multi_destino(self.grafoDelincuentes, agentesEncubiertos, kMasImp)
        if (len(caminoMin) == 0):
            return print("La persecución no es posible")
        self.__visualizar_resultado(caminoMin, ' -> ')

    def cfc(self):
        componente_fuertemente_conexas = cfc(self.grafoDelincuentes)
        comp_contador = 1
        for componente in componente_fuertemente_conexas:
            if len(componente) > 1:
                print("CFC " + str(comp_contador) + ": ", end="")
                self.__visualizar_resultado(componente, ' ,')
                comp_contador += 1

    def divulgar_ciclo(self, delincuente, n):
        vDelincuente = self.grafoDelincuentes.obtenerVertice(delincuente)
        if (vDelincuente == None): return print("El delincuente no existe")
        ciclo = ciclo_largo_n(grafo, vDelincuente, n)
        if (len(ciclo) < n + 1): return print("El ciclo de largo {0} no es posible".format(str(n)))
        self.__visualizar_resultado(ciclo, ' -> ')

    def __visualizar_resultado(self, lista, separador):
        for i in range(0, len(lista) - 1):
            print(lista[i], end=separador)
        print(lista[-1])