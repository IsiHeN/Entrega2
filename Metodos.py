def maximo (jugadorxs):
    max=-1
    for clave in jugadorxs.keys():
        if(jugadorxs[clave]["goles"]>max):
         max=jugadorxs[clave]["goles"]
         nombre=clave
    print("nombre del goleadorx:",nombre)
    print("goles del goleadorx:",max)
    return max

def MasInfluyente(jugadorx):
    max=-1
    for clave in jugadorx.keys():
       goles=0
       atajados=0
       asistencias=0
       goles=jugadorx[clave]["goles"]*1.5
       atajados=jugadorx[clave]["goles_atajados"]*1.25
       asistencias=jugadorx[clave]["asistencias"]*1
       suma = goles+atajados+asistencias
       if(suma>max):
         max=suma
         nombre=clave
       suma=0
    print("Jugadorxs mas influyente:",nombre)

def PromedioGoles(jugadorx):
   suma=0
   for clave in jugadorx.keys():
      suma=suma+jugadorx[clave]["goles"]
   print("promedio de goles por partido:",suma/25)

def PromedioGolGoleadorxs(jugadorxs):
   print("Promedio de goles del goleadorx:",maximo(jugadorxs)/25) 
   