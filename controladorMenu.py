class ControladorMenu:

    def __init__(self):
        pass

    # Imprime Menu pasando titulo y opciones como parametro
    # --> parametro string titulo - Titulo a Mostrar
    # --> parametro lista opciones - Opciones para Mostrar
    # --> retorna comando y parametros ingresados
    def __mostrarMenu(self, titulo, opciones):
        # print('\n{0}'.format(titulo))
        # for opcion in opciones:
        #     print('-',opcion)

        respuesta = input() #("Ingrese la operación que desea realizar: ")
        if(respuesta == ''): return None, None
        operacion = respuesta.split(' ')
        comando = operacion[0]
        parametros = operacion[1:]

        while (comando not in opciones or
               not self.__validarParametros(comando, parametros)):
            respuesta = input() #("Ingrese la operación que desea realizar: ")
            if (respuesta == ''): return None, None
            operacion = respuesta.split(' ')
            comando = operacion[0]
            parametros = operacion[1:]

        return comando, parametros

    # Valida los parametros de entrada
    def __validarParametros(self, comando, parametros):
        if (comando == 'min_seguimientos'):
            if len(parametros) == 2: return True
        elif (comando == 'mas_imp'):
            if len(parametros) == 1 and parametros[0].isdigit(): return True
        elif (comando == 'persecucion'):
            if len(parametros) == 2 and parametros[-1].isdigit(): return True
        elif (comando == 'comunidades'):
            if len(parametros) == 1 and parametros[0].isdigit(): return True
        elif (comando == 'divulgar'):
            if len(parametros) == 2 and parametros[-1].isdigit(): return True
        elif (comando == 'divulgar_ciclo'):
            if len(parametros) == 2 and parametros[-1].isdigit(): return True
        elif (comando == 'cfc'):
            if len(parametros) == 0: return True
        return False

    # Visualiza el menuPrincipal, retorna la respuesta elegida
    def controladorMenuPrincipal(self):
        return self.__mostrarMenu("¿Que operación desea realizar?",
                                  ['min_seguimientos', 'mas_imp', 'persecucion', 'comunidades', 'divulgar',
                                   'divulgar_ciclo', 'cfc'])
    