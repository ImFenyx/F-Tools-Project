# This file contins functions of this application.
from os import name, system

# Clear Screen / Limpa tela
def clear():
    if name == "nt":
        system('cls')
    else:
        system('clear') 
