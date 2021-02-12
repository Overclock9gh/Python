#!/usr/local/bin/python3.7
# -*-coding:Utf-8 -*
"""module inputHelpers contenant les fonctions input_number et input_number_max"""

def input_number(message):
  while True:
    try:
       userInput = int(input(message))
    except ValueError:
       print("Pas un entier! Essayez à nouveau.")
       continue
    else:
       return userInput 
       break 
     
def input_number_max(message, max=100):
  while True:
    try:
       userInput = input_number(message)
       if userInput > max:
           raise ValueError("Nombre trop élevé")       
    except ValueError:
       print("Erreur : Nombre trop élevé")
       continue
    else:
       return userInput 
       break 

