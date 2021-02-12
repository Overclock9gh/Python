#!/usr/bin/python3.6
# -*-coding:Utf-8 -*
import os
import site
import sys
site.addsitedir('/home/hsaid/Bureau/scripts/python/lib')
site.addsitedir('/home/hsaid/Bureau/scripts/python/gestionBd')
from pkg_artefacts.mod_artefacts import *
from pkg_heros.mod_heros import *
from displayMenu import *
from dbHelpers import *
from sauvegardeBd import *
from importexport import *

TVERT =  '\033[32m' # Texte vert
FINC = '\033[m' # Remettre la couleur par défaut

def menu_interrogation_bd(con):
    #serveur = 'local' 
    itemsMenu = ["Afficher l'attaque d'un héros",
        "Afficher les héros avec leur affinité",
        "Afficher l'artefact d'un élément",
        "Afficher les artefacts avec la puissance de leur pouvoir spécial",
        "Quitter\n"]

#con = changer_de_serveur('distant')
    while True:
        #print ('\nOpérations sur le serveur ' + TVERT + serveur, FINC)
        choix = displayMenu(itemsMenu)
        #if choix == 1:
        #    con = changer_de_serveur(serveur)
        #    if serveur == 'local':
        #        serveur = 'distant'
        #    else:
        #        serveur = 'local'
        if choix == 1:
            attaque_heros(con)
        elif choix == 2:
            heros_avec_affinite(con)
        elif choix == 3:
            artefact_selon_element(con)
        elif choix == 4:
            artefacts_avec_pouvoir_special(con)
        elif choix == 5:
            break

def menu_gestion_bd(con, serveur):
    itemsMenu = ["Backup de la BD jeu_video sur " + serveur,
    "Exportations de la table heros sur " + serveur,
    "Importation dans la table heros sur " + serveur,
    "Vérifier l'intégrité d'un fichier csv",
    "Quitter"]

    while True:
        choix = displayMenu(itemsMenu)
        if choix == 1:
            sauvegarde_bd_jeu_video(serveur)
        elif choix == 2:
            sql = "SELECT * FROM `heros`"
            file_path = '/home/hsaid/Bureau/scripts/python/gestionBd/csv/heros.csv'
            mysql_to_csv(sql, file_path, con)
        elif choix == 3:
            sql = "SELECT * FROM `heros`"
            file_path = '/home/hsaid/Bureau/scripts/python/gestionBd/csv/heros_import.csv'
            load_sql = "LOAD DATA LOCAL INFILE '" + file_path + "' INTO TABLE jeu_video.heros FIELDS TERMINATED BY ',' ENCLOSED BY '\"' IGNORE 1 LINES;"
            csv_to_mysql(load_sql, con)
        elif choix == 4:
            InFileName = '/home/hsaid/Bureau/scripts/python/gestionBd/csv/heros_bad.csv'
            OutFileName = '/home/hsaid/Bureau/scripts/python/gestionBd/csv/heros_good.csv'
            csv_integrity(InFileName, OutFileName)
        elif choix == 5:
            break
        print("\n")

def items_menu(serveur):
    itemsMenu = ["Changer de serveur",
        "Interrogations de la BD jeu_video sur le serveur " + serveur,
        "Gestion de la BD jeu_video sur le serveur " + serveur,
        "Quitter"]
    return itemsMenu

serveur = 'localhost'
con = changer_de_serveur('192.168.237.131')
while True:
    choix = displayMenu(items_menu(serveur))
    if choix == 1:
        con = changer_de_serveur(serveur)
        if serveur == 'localhost':
            serveur = '192.168.237.132'
        else:
            serveur = 'localhost'
    elif choix == 2:
        menu_interrogation_bd(con)
    elif choix == 3:
        menu_gestion_bd(con, serveur)
    elif choix == 4:
        break
    print("\n")