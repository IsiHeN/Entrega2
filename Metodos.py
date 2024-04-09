def maximo (jugadorxs):
    max=-1
    for clave in jugadorxs.keys():
        if(jugadorxs[clave]["goles"]>max):
         max=jugadorxs[clave]["goles"]
         nombre=clave
    print(max)
    print(nombre)