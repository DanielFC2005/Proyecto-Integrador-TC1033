from destino import Destino
from terminal import Terminal
from avion import Avion
from horario import Horario
class Aerolinea:#Clase que define cada aerolinea operando en el aeropuerto
    def __init__(self, nombre, terminal):#inicializa el objeto
        self.__nombre = nombre
        self.__terminal = terminal
        self.__tipos_de_avion = {}
        self.__destinos = []
    
    def añadir_destino(self, Destino):
        '''Añade un destino a la lista de destinos'''
        self.__destinos.append(Destino)
    
    def eliminar_destino(self, Destino):#Elimina un destino de la lista
        self.__destinos.remove(Destino)
    
    def horario(self, Destino, numero):#Retorna el horario seleccionado de x destino
        x = 0
        y = None
        for i in range(len(self.__destinos)):
            if self.__destinos[i] == Destino:
               x = self.__destinos.index(Destino)
               y = self.__destinos[x]
               return (self.__destinos[i].horario_especifico(numero))
            else:
                return "Horario no existe para este destino"
    
    def añadir_tipo_avion(self, Avion):#Marca un avion como disponible o lo añade en caso de la adquisicion de uno
        self.__tipos_de_avion[Avion] = Avion.capacidad

    
    def precio_avion(self, Avion):#retorna el precio del avion
        x = list(self.__tipos_de_avion)
        if Avion in self.__tipos_de_avion: 
            disponibilidad = self.__tipos_de_avion[Avion]
            if disponibilidad > 0:
                for i in range (len(x)):
                    if x[i] == Avion:
                        Avion.capacidad -= 1
                        return Avion.precio
            else:
                return 'VUELO LLENO'
        else:
            return "VUELO INEXISTENTE"
    
    @property
    def nombre(self):#retorna el nombre de la aerolinea
        return self.__nombre
    
    def seleccionar_destino(self,destino):#retorna el nombre del destino seleccionado
        return destino.nombre
    
    @property
    def destinos(self):#retorna una lista con todos los destinos y horarios de la aerolinea
        x = ""
        for i in range (len(self.__destinos)):
            
            x += f'{i+1}.- {self.__destinos[i].nombre} Hora: {self.__destinos[i].horarios}\n'
        return (f'Aerolinea: {self.__nombre}\n{x}')
    
    def elegir_avion(self, Avion):
        return Avion.clase
                    
