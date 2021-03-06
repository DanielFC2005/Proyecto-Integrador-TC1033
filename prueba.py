from aerolinea import Aerolinea
from destino import Destino
from terminal import Terminal
from avion import Avion
from horario import Horario
from boleto import Boleto
'''Casos prueba:
##PRUEBAS##
>>>
h1 = Horario("12:30 PM")#crea un horario
d1 = Destino("Hawaii", 1500)#crea un destino con costo base
t1 = Terminal()#crea una terminal
a1 = Avion("BOEING", 1, 1500, "Primera clase")#registra un nuevo avion
aerolinea = Aerolinea("Aeromexico", t1)#genera una neuva aerolinea
aerolinea.añadir_destino(d1)#añade un destino a la aerolinea
aerolinea.añadir_tipo_avion(a1)#añade un tipo de avion a la aerolinea
print(aerolinea.destinos)#imprimie los destinos de la aerolinea
print(boleto.ticket())#imprime el boleto
print(boleto2.ticket())#imprime el boleto
>>>
Aerolinea: Aeromexico
1.- Hawaii Hora: 
    1.- 12:30 PM
*** Aeromexico ***
Boleto #0
Destino: Hawaii
Clase: Primera clase
Hora de salida: 12:30 PM
Precio del boleto: $3000.0
 '''
class Prueba:
    def start(self):
        #Crea tus objetos aqui
        h1 = Horario("12:30 PM")#crea un horario
        h2 = Horario("13:00 PM")#crea un horario
        h3= Horario("06:00 AM")#crea un horario
        h4= Horario("10:00 AM")#crea un horario
        d1 = Destino("Hawaii", 1500)#crea un destino con costo base
        d2 = Destino("Canada", 100)#crea un destino con costo base
        d3 = Destino("China", 10000)#crea un destino con costo base
        d4 = Destino("Oaxaca", 99999)#crea un destino con costo base
        d1.añadir_horario(h1)#añade un horario al desitno
        d1.añadir_horario(h3)#añade un horario al desitno
        d1.añadir_horario(h2)#añade un horario al destino
        d2.añadir_horario(h1)#añade un horario al destino
        d2.añadir_horario(h2)#añade un horario al destino
        d2.añadir_horario(h3)#añade un horario al destino
        d2.añadir_horario(h4)#añade un horario al destino
        d3.añadir_horario(h4)#añade un horario al destino
        d4.añadir_horario(h1)#añade un horario al destino
        t1 = Terminal()#crea una terminal
        t2 = Terminal()#crea una terminal
        a1 = Avion("BOEING", 1, 1500, "Primera clase")#registra un nuevo avion
        a2 = Avion("AJ1800", 200, 100, "Clase turista")#registra un nuevo avion
        a3 = Avion("AKKAD0", 200, 100, "Primera Clase")#registra un nuevo avion
        a4 = Avion("MDP123", 150, 100, "Clase turista")#registra un nuevo avion
        a5 = Avion("009OLO", 100, 100, "Clase turista")#registra un nuevo avion
        aerolinea = Aerolinea("Aeromexico", t1)#genera una neuva aerolinea
        aerolinea2 = Aerolinea("VivaAerobus", t2)#genera una nueva aerolinea
        aerolinea3 = Aerolinea("MexicoVuela", t2)#genera una nueva aerolinea
        aerolinea4 = Aerolinea("AeroNautica", t2)#genera una nueva aerolinea
        aerolinea.añadir_destino(d1)#añade un destino a la aerolinea
        aerolinea.añadir_destino(d2)#añade un destino a la aerolinea
        aerolinea2.añadir_destino(d2)#añade un destino a la aerolinea
        aerolinea3.añadir_destino(d1)#añade un destino a la aerolinea
        aerolinea3.añadir_destino(d4)#añade un destino a la aerolinea
        aerolinea3.añadir_destino(d3)#añade un destino a la aerolinea
        aerolinea3.añadir_destino(d2)#añade un destino a la aerolinea
        aerolinea4.añadir_destino(d2)#añade un destino a la aerolinea
        aerolinea.añadir_tipo_avion(a1)#añade un tipo de avion a la aerolinea
        aerolinea3.añadir_tipo_avion(a1)#añade un tipo de avion a la aerolinea
        aerolinea3.añadir_tipo_avion(a2)#añade un tipo de avion a la aerolinea
        aerolinea3.añadir_tipo_avion(a3)#añade un tipo de avion a la aerolinea
        aerolinea3.añadir_tipo_avion(a4)#añade un tipo de avion a la aerolinea
        aerolinea2.añadir_tipo_avion(a2)#añade un tipo de avion a la aerolinea
        aerolinea.añadir_tipo_avion(a2)#añade un tipo de avion a la aerolinea
        print(aerolinea.destinos)#imprimie los destinos de la aerolinea
        print(aerolinea2.destinos)#imprime los destinos de la aerolinea
        print(aerolinea3.destinos)#imprime los destinos de la aerolinea
        boleto = Boleto(aerolinea, d1, h1, a1)#genera un boleto
        print(boleto.ticket())#imprime el boleto
        boleto2 = Boleto(aerolinea2, d2, h1, a1)#genera un boleto
        boleto3 = Boleto(aerolinea2, d2, h2, a1)#genera un boleto
        boleto4 = Boleto(aerolinea, d1, h1, a2)#genera un boleto
        boleto5 = Boleto(aerolinea3, d4, h3, a4)#genera un boleto
        print(boleto2.ticket())#imprime el boleto
        print(boleto3.ticket())#imprime el boleto
        print(boleto4.ticket())#imprime el boleto
        print(boleto5.ticket())#imprime el boleto



if __name__ == "__main__":
    Vuelos= Prueba()
    Vuelos.start()