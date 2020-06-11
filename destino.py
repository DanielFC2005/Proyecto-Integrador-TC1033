from horario import Horario
class Destino:#Clase destino
    def __init__(self, nombre, precio):#Inicilizamos con un nombre, un precio, y horarios vacios
        self.__nombre = nombre
        self.__precio_base = precio
        self.__horarios = []
    
    
    def cambiar_precio(self, precio):#cambia el precio base
        self.__precio_base = precio
    
    def añadir_horario(self,horario):#añade un horario al destino
        self.__horarios.append(horario)
    
    def eliminar_horario(self, horario):#elimina el horario del destino
        self.__horarios.remove(horario)
        
    def horario_especifico(self, ):##retorna el horario seleccionado
#        x = None
#        for i in range(len(self.__horarios)):
#            if self.__horarios[i] == Horario:
#               x = self.__destinos.index(Horario)
        return Horario.hora
    
    @property
    def precio(self):
        return self.__precio_base
    
    @property
    def nombre(self):#regresa el nombre del destino
        return self.__nombre
    
    @property
    def horarios(self):#da formato a todos los horarios para este destino y los regresa de forma ordenada
        x=""
        for i in range (len(self.__horarios)):
            x += f'\n{i+1:5}.- {self.__horarios[i].hora}'
        return x

