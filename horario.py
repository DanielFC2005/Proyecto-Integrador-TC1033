class Horario:#clase horario. Horarios disponibles para los vuelos
    def __init__(self, hora):
        self.__hora = hora
    
    @property
    def hora(self):#retorna la hora
        return self.__hora
    
