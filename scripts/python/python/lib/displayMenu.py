#!/usr/bin/python3.6
# -*-coding:Utf-8 -*
import os
from inputHelpers import *

def displayMenu(options):
    # display menu options
    print('')
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
    choice = 0
    while not(1 <= choice <= len(options)+1):
        choice = input_number_max("Choisissez un item s.v.p. : ", len(options)+1)
    return(choice)

#test de la fonction displayMenu
if __name__ == "__main__":
    itemsMenu = ["Quel nom", "Bonjour", "Quitter"]
    while True:
        choix = displayMenu(itemsMenu)
        if choix == 1:
            nom = input("Entrez votre nom : ")
        elif choix == 2:
            print("Bonjour", nom)
        elif choix == 3:
            break
