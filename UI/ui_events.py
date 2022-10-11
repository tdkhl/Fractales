############
#### Import des modules
############
import sys
 # Import du module système et indication de la location du module UI et des ressources
sys.path.insert(2, "fract_ressources")
sys.path.insert(3, "Dessins")
sys.path.insert(4, "UI")
import fractales_draw
import index
from tkinter import *
from tkinter import ttk

############
#### Création des variables globales pour la suite du programme
############
global flocon_cb

############
#### Fonction afin d'éviter l'apparition de plusieurs combobox dans la frame de choix
############

def __nettoyerFenetreChoix__(fenetre):
    """ Evite l'apparition de plusieurs combobox dans la frame"""
    for widget in fenetre.winfo_children():
       widget.destroy()


############
#### Gestion des choix de l'utilisateur en terme de flocon
############       

def flocon_changed(event):
    """ On s'abonne a l'événement si l'utilisateur change de type de flocon"""
    if(flocon_cb.get() == "Flocon Classique"):
        fractales_draw.draw_flocon()
    else:
        fractales_draw.draw_flocon_diff()

    

def showFloconMenu():
    """ Affiche le menu déroulant pour choisir le type de flocon"""
    index.ouverturefenetreChoix()
    __nettoyerFenetreChoix__(index.fenetreChoix)
    global flocon_cb
    flocon_cb = ttk.Combobox(index.fenetreChoix)

    flocon_cb['values'] = ["Flocon Classique", "Flocon Difforme"]


    flocon_cb['state'] = 'readonly'

    flocon_cb.pack(fill=BOTH, padx=10, pady=5)



    flocon_cb.bind('<<ComboboxSelected>>', flocon_changed)




