import time
from rndmtr import random_matrica
from nacrtaj import nacrtaj
from heuristika import heuristika
from heuristika_matrice import heuristika_matrice
from planinar import planinarenje



# MAIN 

planinarenje(1)

brojaci_svi = 0



for i in range(0, 200):
    brojaci_svi += planinarenje()
print ('Kraj')
print ('Brojaci: ', brojaci_svi)
print('Prosjecna uspjesnost pronalaska resenja: ', 200/brojaci_svi)
print('Prosjecan broj potrebnih restartovanja',brojaci_svi/200)
