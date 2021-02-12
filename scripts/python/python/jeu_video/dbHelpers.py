#!/usr/bin/python3.6
# -*-coding:Utf-8 -*
"""module dhHelpers contenant la fonction de connexion à la BD"""
import pymysql
import pymysql.cursors

TVERT =  '\033[32m' # Texte vert
FINC = '\033[m' # Remettre la couleur par défaut

def dbConnect(host, user):
    con = pymysql.connect(host, user,
        password='79w24A9',
        db='jeu_video',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor, autocommit=True, local_infile=1)
    if (con):
        # Carry out normal procedure
        print("\nConnection to " + TVERT + host, FINC + "successful")

        cursor = con.cursor()

        cursor.execute("SELECT VERSION()")

        data = cursor.fetchone()
        print("Database version : %s " % data['VERSION()'])
    else:
        # Terminate
        print("\nConnection to " + TVERT + host, FINC + "unsuccessful")
    return(con)

def changer_de_serveur(serveur):
    if serveur is 'localhost':
        host='192.168.237.132'
        user='bdadmin'
    else:
        host='localhost'
        user='root'
    return dbConnect(host, user)