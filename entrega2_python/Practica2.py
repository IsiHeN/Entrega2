import Metodos
names = """ Agustin, Yanina, Andrés, Ariadna, Bautista, CAROLINA,
CESAR, David, Diego, Dolores, DYLAN, ELIANA, Emanuel, Fabián, Noelia,
Francsica', FEDERICO, Fernanda, GONZALO, Nancy """
goals = [0, 10, 4, 0, 5, 14, 0, 0, 7, 2, 1, 1, 1, 5, 6, 1, 1, 2, 0,
11]
goals_avoided = [0, 2, 0, 0, 5, 2, 0, 0, 1, 2, 0, 5, 5, 0, 1, 0, 2,
3, 0, 0]
assists = [0, 5, 1, 0, 5, 2, 0, 0, 1, 2, 1, 5, 5, 0, 1, 0, 2, 3, 1,
0]

names = [name.strip() for name in names.split(',')] #hacemos una lista con los nombres, split miranod las ,

jugadorxs = {}

for i in range(len(names)):  # creamos un diccionario con las estadisticas 
    jugadorxs[names[i]] = {
        "goles": goals[i],
        "goles_atajados": goals_avoided[i],
        "asistencias": assists[i]
    }

Metodos.maximo(jugadorxs)
Metodos.MasInfluyente(jugadorxs)
Metodos.PromedioGoles(jugadorxs)
Metodos.PromedioGolGoleadorxs(jugadorxs)





















