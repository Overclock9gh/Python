#!/usr/bin/python3.6
# -*-coding:Utf-8 -*
"""module mod_heros contenant les fonctions pouvoir_special_artefact et """
import site
site.addsitedir('/home/hsaid/Bureau/scripts/python/lib')
from inputHelpers import *
#import pymysql
#import pymysql.cursors

TVERT =  '\033[32m' # Texte vert
FINC = '\033[m' # Remettre la couleur par défaut

#def dbConnect():
#    con = pymysql.connect(host='localhost',
#    user='root',
#    password='79w24A9',
#    db='jeu_video',
#    charset='utf8mb4',
#    cursorclass=pymysql.cursors.DictCursor)
#    return(con)

def artefact_selon_element(con):
    """Fonction affichant l'artefact correspondant à l'élément choisi"""
    print(TVERT + "Artefact disposant de l'élément choisi", FINC)
    try:
        element = input('\nQuel est l\'élément de l\'artefact ? ')
    except:
        print('Une erreur est survenue...')
    #con = dbConnect()
    with con.cursor() as cur:
        cur.execute("SELECT nom FROM artefacts WHERE element = %s",element)
        result=cur.fetchall()
        for row in result:
            print(row['nom'])

def artefacts_avec_pouvoir_special(con):
    """Fonction affichant les artefacts avec leur force de pouvoir spécial"""
    print(TVERT + "Artefacts avec la puissance de leur pouvoir spécial", FINC)
    try:
        max = input_number_max('\nCombien d\'artefacts voulez-vous afficher (max : 3)? ',3)
    except:
        print('Une erreur est survenue...')
    #con = dbConnect()
    with con.cursor() as cur:
        cur.execute("SELECT nom, pouvoir_special FROM artefacts LIMIT %s",max)
        result=cur.fetchall()
        for row in result:
            if row['pouvoir_special'] != '':
                print(row['nom'], row['pouvoir_special']) 