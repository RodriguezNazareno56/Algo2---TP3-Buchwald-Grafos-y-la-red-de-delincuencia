import grafo
from bibliotecaFuncionesGrafos import *

class RedDeDelincuentes:

    # Constructor 
    # Recibe por parametro un grafo que representa las comunicaciones de delincuentes
    def __init__(self, grafo):
        self.grafoDelincuentes = grafo

    # Imprime una lista con los delincuentes (su código identificador) con los cuáles vamos del 
    # delincuente origen al delincuente destino de la forma más rápida. En caso de no poder hacer
    # el seguimiento (i.e. no existe camino), imprimir Seguimiento imposible.
    def minimoSeguimiento(self, origen, destino):
        vOrigen = self.grafoDelincuentes.obtenerVertice(origen)
        vDestino = self.grafoDelincuentes.obtenerVertice(destino)
        orden, camino = recorridoMinimoBfs(self.grafoDelincuentes, vOrigen, vDestino)
        if ((orden and camino) is None):
            return print("Seguimiento imposible")
        self.__visualizar_resultado(camino, ' -> ')

    # Imprime una lista con todos los delincuentes a los cuales les termina llegando un rumor que 
    # comienza en el delincuente pasado por parámetro, y a lo sumo realiza n saltos (luego, se 
    # empieza a tergiversar el mensaje), teniendo en cuenta que todos los delincuentes transmitirán 
    # el rumor a sus allegados.
    def divulgarRumor(self, origen, distMax):
        vOrigen = self.grafoDelincuentes.obtenerVertice(origen)
        if (vOrigen == None): return print("El delincuente no existe")
        afectados = recorridoMinimoBfsMaximo(grafo, vOrigen, distMax)
        self.__visualizar_resultado(afectados[1:], ', ')

    # Imprime un listado de comunidades de al menos n integrantes.
    def comunidades(self, n):
        comunidades = label_propagation(self.grafoDelincuentes)
        num_comunidad = 1
        for comunidad, integrantes in comunidades.items():
            if len(integrantes) >= n:
                print("Comunidad " + str(num_comunidad) + ":", end=" ")
                self.__visualizar_resultado(integrantes, ', ')
                num_comunidad += 1

    # Imprime, de mayor a menor importancia, los cant delincuentes más importantes.
    def mas_imp(self, cant):
        mas_importantes = centralidad_aprox(self.grafoDelincuentes, cant)
        for i in range(cant - 1):
            if i < len(self.grafoDelincuentes) - 1:
                print(mas_importantes[i], end=", ")
        print(mas_importantes[-1])

    # Dado cada uno de los delincuentes pasados (agentes encubiertos), obtener cuál es el camino más 
    # corto para llegar desde alguno de los delincuentes pasados por parámetro, a alguno de los K 
    # delincuentes más importantes. En caso de tener caminos de igual largo, priorizar los que vayan 
    # a un delincuente más importante.
    def persecucion(self, agentesEncubiertos, kMasImp):
        caminoMin = recorrido_min_multi_origen_multi_destino(self.grafoDelincuentes, agentesEncubiertos, kMasImp)
        if (len(caminoMin) == 0):
            return print("La persecución no es posible")
        self.__visualizar_resultado(caminoMin, ' -> ')

    # Imprime cada conjunto de vértices entre los cuales todos están conectados con todos.
    def cfc(self):
        componente_fuertemente_conexas = cfc(self.grafoDelincuentes)
        comp_contador = 1
        for componente in componente_fuertemente_conexas:
            #if len(componente) > 1:
            print("CFC " + str(comp_contador) + ": ", end="")
            self.__visualizar_resultado(componente, ' ,')
            comp_contador += 1

    # Imprime un camino simple que empiece y termine en el delincuente pasado por parámetro,
    # de largo n. En caso de no encontrarse un ciclo de ese largo y dicho comienzo, imprimir No se 
    # encontro recorrido.
    def divulgar_ciclo(self, delincuente, n):
        vDelincuente = self.grafoDelincuentes.obtenerVertice(delincuente)
        if (vDelincuente == None): return print("El delincuente no existe")
        ciclo = ciclo_largo_n(grafo, vDelincuente, n)
        if (len(ciclo) < n + 1): return print("No se encontro recorrido")
        self.__visualizar_resultado(ciclo, ' -> ')

    # Visuliza por consola los elementos de una lista separados por el parametro 'separador'
    def __visualizar_resultado(self, lista, separador):
        for i in range(0, len(lista) - 1):
            print(lista[i], end=separador)
        print(lista[-1])