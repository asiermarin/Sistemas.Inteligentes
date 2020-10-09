class Agente(object):
    
    def retorna_accion(self, mundo, estado):
        if (mundo == 'A' and estado == "sucio"):
            self.__limpiar_A()
        elif (mundo == 'B' and estado == "sucio"):
            self.__limpiar_B()
        else:
            None


    def __limpiar_A(self):
       return None;

    def __limpiar_B(self):
       return None;





