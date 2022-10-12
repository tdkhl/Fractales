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
global arbre_cb
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
    if(flocon_cb.get() == "Flocon Classique"): #si le choix de l'utilisateur est égale à "Flocon classique"
        #alors le script draw_flocon execute la fonction draw_flocon
        fractales_draw.draw_flocon()
    else: # sinon le script execute draw_flocon_diff
        fractales_draw.draw_flocon_diff()

    

def showFloconMenu():
    """ Affiche le menu déroulant pour choisir le type de flocon"""
    index.ouverturefenetreChoix()
    __nettoyerFenetreChoix__(index.fenetreChoix)
    global flocon_cb
    flocon_cb = ttk.Combobox(index.fenetreChoix)

    flocon_cb['values'] = ["Flocon Classique", "Flocon Difforme"] # attribut des noms

    flocon_cb['state'] = 'readonly' # empêche l'utilisateur d'écrire

    flocon_cb.pack(fill=BOTH, padx=10, pady=5) # place la barre de selection à tel "x" et "y"



    flocon_cb.bind('<<ComboboxSelected>>', flocon_changed)

############
#### Gestion des choix de l'utilisateur en terme de Arbre
############  

def arbre_changed(event):
    """ On s'abonne a l'événement si l'utilisateur change de type de arbre"""
    if(arbre_cb.get() == "Arbre Classique"): #si le choix de l'utilisateur est égale à "Arbre classique"
        #alors le script draw_flocon execute la fonction draw_pytatree
        fractales_draw.angle_arbre = 30
        fractales_draw.draw_pytatree()
    else: # sinon le script execute draw_pytatree avec un angle différent
        fractales_draw.angle_arbre = 110
        fractales_draw.draw_pytatree()



def showArbreMenu():
    """ Affiche le menu déroulant pour choisir le type de arbre"""
    index.ouverturefenetreChoix()
    __nettoyerFenetreChoix__(index.fenetreChoix)
    global arbre_cb
    arbre_cb = ttk.Combobox(index.fenetreChoix)

    arbre_cb['values'] = ["Arbre Classique", "Arbre Shuriken"]


    arbre_cb['state'] = 'readonly'

    arbre_cb.pack(fill=BOTH, padx=10, pady=5)



    arbre_cb.bind('<<ComboboxSelected>>', arbre_changed)




