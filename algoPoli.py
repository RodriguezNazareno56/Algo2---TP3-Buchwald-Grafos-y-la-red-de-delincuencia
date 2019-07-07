#!/usr/bin/python3
# coding=utf-8
from sys import argv
import bibliotecaFuncionesGrafos
import redDeDelincuencia
import controladorMenu

# Gestiona el menu principal, lleva a cabo los comandos introducidos por consola por el usuario
# Pre: Recibe como parametro una instancia del objeto RedDeDelincuentes
# Post: Mientras el usuario continue instroduciendo comandos, los mismos seran llevados a cabo.
# pone fin a la ejecucion del programa en caso que el usuario introdusca una linea vacia o EOF.
def menuPrincipal(redDelincuencia):
    controlador = controladorMenu.ControladorMenu()
    comando, parametros = controlador.controladorMenuPrincipal()
    while (comando != None):

        if (comando == 'min_seguimientos'):     # Mínimos Seguimientos
            origen = parametros[0]
            destino = parametros[1]
            redDelincuencia.minimoSeguimiento(origen, destino)

        elif (comando == 'mas_imp'):            # Delincuentes más importantes   
            cant = int(parametros[0])
            redDelincuencia.mas_imp(cant)

        elif (comando == 'persecucion'):        # Persecución rápida
            agentesEncubiertos = parametros[0].split(",")
            kMasImportantes = int(parametros[1])
            redDelincuencia.persecucion(agentesEncubiertos, kMasImportantes)

        elif (comando == 'comunidades'):        # Comunidades
            min_integrantes = int(parametros[0])
            redDelincuencia.comunidades(min_integrantes)

        elif (comando == 'divulgar'):          # Divulgación de rumor 
            delincuente = parametros[0]
            distMax = int(parametros[1])
            redDelincuencia.divulgarRumor(delincuente, distMax)

        elif (comando == 'divulgar_ciclo'):    # Ciclo de largo n
            delincuenteCiclo = parametros[0]
            largoCiclo = int(parametros[1])
            redDelincuencia.divulgar_ciclo(delincuenteCiclo, largoCiclo)

        elif (comando == 'cfc'):               # Componentes Fuertemente Conexas
            redDelincuencia.cfc()

        try:
            comando, parametros = controlador.controladorMenuPrincipal()
        except EOFError:
            comando = None

# Recibe como argumento la ruta del archivo .tsv que contiene las comunicaciones
def main(argv):
    if(len(argv) != 1):
        print("Error: Cantidad erronea de parametros")
        return -1
    try:
        # Intancia de Clases
        grafo = bibliotecaFuncionesGrafos.cargarGrafo(argv[0])
        redDeDelincuentes = redDeDelincuencia.RedDeDelincuentes(grafo)
        # Llamado a Menu Principal
        menuPrincipal(redDeDelincuentes)
        return 0
    except FileNotFoundError:
        print("Error: archivo fuente inaccesible")
        return -1




# Bloque Principal
main(argv[1:])