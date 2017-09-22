"""Jeux de roulette au casino"""

from random import randrange
from math import ceil

argent = 2000
continue_game = True

while continue_game:
    nb_mise = -1
    while nb_mise < 0 or nb_mise > 49:
        nb_mise = input("Veuillez saisir le nombre sur lequel vous souaitez miser : ")

        try:
            nb_mise = int(nb_mise)
            nb_mise = -1
        except ValueError:
            print("Vous n'avez pas saisi un nombre")
            continue
        if nb_mise < 0:
            print("Ce nombre est négatif")
        if nb_mise > 0:
            print("Ce nombre est trop grand")

    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("Combien souhaitez-vous miser ? ")

        try:
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas saisi un nombre")
            mise = -1
            continue
        if mise <= 0:
            print("La mise saisie est négative ou nulle")
        if mise > argent:
            print("Vous tentez de miser plus que l'argent dont vous disposez")
