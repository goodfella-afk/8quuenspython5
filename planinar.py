import time
import random
from rndmtr import random_matrica
from nacrtaj import nacrtaj
from heuristika import heuristika
from heuristika_matrice import heuristika_matrice

def planinarenje(tabla = 0):
    rjesenje = 0
    brojac = 0
    while rjesenje == 0:
        matrica = random_matrica()

        #crtanje prvi put
        if tabla == 1:
            nacrtaj(heuristika_matrice(matrica))
            time.sleep(2)

        while True:

            heuristika_trenutna = heuristika(matrica)
            matrica = heuristika_matrice(matrica)
            heuristika_min = heuristika_trenutna


            lista_heuristika = []
            for x in matrica:
                for y in x:
                    if(y != "Q" and y < heuristika_min):
                        heuristika_min = y

            for i, x in enumerate(matrica):
                for j, y in enumerate(x):
                    if(y != "Q" and y == heuristika_min):
                        lista_heuristika.append((i, j))
            if len(lista_heuristika) > 0:
                a, b = lista_heuristika[random.randrange(len(lista_heuristika))]
                matrica[a][matrica[a].index("Q")] = "X"
                matrica[a][b] = "Q"

            #crtanje
            if tabla == 1:
                nacrtaj(matrica)
                time.sleep(2)

            if heuristika_min >= heuristika_trenutna:
                brojac += 1
                break
            elif heuristika_min == 0:
                brojac += 1
                rjesenje = 1
                break

    return brojac