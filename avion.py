class Avion:#Tipos de aviones existentes
    
    __numero_avion = 0#generador de id automatico del avion
    
    def __init__(self, nombre, capacidad, precio, clase):
        self.__ID = Avion.__numero_avion
        self.__nombre = nombre#Nombre del modelo
        self.__capacidad = int(capacidad)
        self.__precio = float(precio)
        self.__clase = clase
        Avion.__numero_avion += 1
    
    @property
    def precio(self):#retorna el precio base del avion
        return self.__precio
    
    @precio.setter#modifica el precio base del avion
    def precio(self, precio):
        self.__precio = precio
    @property
    def capacidad(self):#retorna la capacidad del avion
        return self.__capacidad
    
    @capacidad.setter
    def capacidad(self, numero):#disminuye/aumenta la capacidad del avion
        self.__capacidad +=numero

    @property
    def clase(self):
        return self.__clase