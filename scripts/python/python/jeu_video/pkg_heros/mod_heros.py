#!/usr/bin/python3.6
# -*-coding:Utf-8 -*
"""module mod_heros contenant les fonctions posseseurs_armes et affinite_heros"""
import site
site.addsitedir('/home/hsaid/Bureau/scripts/python/lib')
from inputHelpers import *
"""module mod_heros contenant les fonctions SQL du langage Python"""
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

def attaque_heros(con):
    """Fonction affichant l'attaque d'un héros"""
    print(TVERT + "Attaque du héros", FINC)
    try:
        prenom = input('\nQuel est le prénom du héros? ')
    except:
        print('Une erreur est survenue...')
    #con = dbConnect()
    with con.cursor() as cur:
        cur.execute("SELECT attaque FROM heros WHERE prenom = %s",prenom)
        result=cur.fetchall()
        for row in result:
            print(row['attaque'])

def heros_avec_affinite(con):
    """Fonction affichant la liste des héros avec leur affinité"""
    print(TVERT + "Heros avec leur affinité", FINC)
    try:
        max = input_number_max('\nCombien de héros voulez-vous afficher (max : 4)? ',4)
    except:
        print('Une erreur est survenue...')
    #con = dbConnect()
    with con.cursor() as cur:
        cur.execute("SELECT prenom, affinite FROM heros LIMIT %s",max)
        result=cur.fetchall()
        for row in result:
            if row['affinite'] != '':
                print(row['prenom'],row['affinite']) 