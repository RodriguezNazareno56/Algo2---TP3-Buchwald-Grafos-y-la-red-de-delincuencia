from redDeDelincuencia import *
from controladorMenu import *
from bibliotecaFuncionesGrafos import*

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
            print(comando)

        elif (comando == 'cfc'):
            print(comando)

        comando, parametros = controladorMenu.controladorMenuPrincipal()



grafo = cargarGrafo('comunidades.tsv')
redDeDelincuentes = RedDeDelincuentes(grafo)
menu = menuPrincipal(redDeDelincuentes)