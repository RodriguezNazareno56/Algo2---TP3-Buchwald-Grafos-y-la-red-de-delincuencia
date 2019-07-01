import sys
import redDeDelincuencia
from controladorMenu import *
import bibliotecaFuncionesGrafos


def menuPrincipal(redDelincuencia):
    controladorMenu = ControladorMenu()
    comando, parametros = controladorMenu.controladorMenuPrincipal()
    while (comando != None):
        if (comando == 'min_seguimientos'):
            origen = parametros[0]
            destino = parametros[1]
            redDelincuencia.minimoSeguimiento(origen, destino)

        elif (comando == 'mas_imp'):
            cant = int(parametros[0])
            redDelincuencia.mas_imp(cant)

        elif (comando == 'persecucion'):
            agentesEncubiertos = parametros[0].split(",")
            kMasImportantes = int(parametros[1])
            redDelincuencia.persecucion(agentesEncubiertos, kMasImportantes)

        elif (comando == 'comunidades'):
            min_integrantes = int(parametros[0])
            redDelincuencia.comunidades(min_integrantes)

        elif (comando == 'divulgar'):
            delincuente = parametros[0]
            distMax = int(parametros[1])
            redDelincuencia.divulgarRumor(delincuente, distMax)

        elif (comando == 'divulgar_ciclo'):
            delincuenteCiclo = parametros[0]
            largoCiclo = int(parametros[1])
            redDelincuencia.divulgar_ciclo(delincuenteCiclo, largoCiclo)

        elif (comando == 'cfc'):
            redDelincuencia.cfc()

        comando, parametros = controladorMenu.controladorMenuPrincipal()


def main(argv):
    if(len(argv) != 1):
        print("Error: Cantidad erronea de parametros")
        return -1
    try:
        grafo = bibliotecaFuncionesGrafos.cargarGrafo(argv[0])
        redDeDelincuentes = redDeDelincuencia.RedDeDelincuentes(grafo)
        menuPrincipal(redDeDelincuentes)
    except FileNotFoundError:
        print("Error: archivo fuente inaccesible")



main(sys.argv[1:])