class Terminal: #Clase Terminal. Indica las terminales existentes que pueden usar las aerolineas
    __numero_terminal = 0 #contador que lleva el numero de terminales creados
    
    def __init__(self):
        self.__numero_terminal = Terminal.__numero_terminal #se genera el numero de la terminal
        Terminal.__numero_terminal += 1 #aumenta en 1 el contador
    
    @property
    def numero_terminal(self):#regresa el numero de la terminal
        return self.__numero_terminal
