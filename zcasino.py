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

    win_number = randrange(50)
    print("Rien ne va plus...")
    print("La roulette tourne, ...")
    print("Et le numéro gagnant est le ...", win_number)

    if win_number == nb_mise:
        print("Vous avez misé sur le bon numéro, vous gagnez 3 fois votre mise, votre solde est de ", 3 * mise)
        argent += 3 * mise
    elif win_number % 2 == 0 and nb_mise % 2 == 0 or win_number % 2 == 1 and nb_mise % 2 == 1:
        print("Vous avez la bonne couleur, je vous rend donc la moitié de votre mise, votre solde est de ", mise / 2)
        argent += mise / 2
    else:
        argent -= mise
        print("Vous avez perdu, votre solde est de : ", argent)
