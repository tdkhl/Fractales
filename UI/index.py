############
#### Import des modules
############
import sys
 # Import du module système et indication de la location du module UI et des ressources
sys.path.insert(2, "fract_ressources")
from tkinter import *

############
#### Fenetre Principale
############

        
       
global main # Création de la variable globale réutilisable dans un autre fichier
main = Tk() 
main.geometry('800x400') # Dimension de la fenêtre
main.title("Les fractales") # Titre de la fenêtre
main['bg'] = 'grey' # Couleur de l'arrière plan
main.resizable(height = False, width = False) # Est-ce que la taille de la fenêtre est ajustable ?
#main.overrideredirect(1) #Remove border

label = Label(main, text = "Voici les différentes fractales récursives disponibles", font = ("Verdana", 15, "italic bold underline"), bg = "grey") # Création d'un label
label.pack(pady=10) # Position du label

############
#### Bouton Arbre Pythagore
############

pytatree_img = PhotoImage(file='fract_ressources/pyta_treepng.png')
b_pytatree = Button(main, image=pytatree_img, fg="grey", bg="grey")
b_pytatree.place(x = 50, y = 60)

pytatree_label = Label(main, text = "Arbre de pythagore", font = ("Verdana", 10, "italic bold "), bg = "grey") 
pytatree_label.place(x = 45, y = 200)

############
#### Bouton Flocon
############

flocon_img = PhotoImage(file='fract_ressources/flocon.png')
b_flocon = Button(main, image=flocon_img, fg="grey", bg="grey")
b_flocon.place(x = 240, y = 60)

flocon_label = Label(main, text = "Flocon", font = ("Verdana", 10, "italic bold "), bg = "grey") 
flocon_label.place(x = 280, y = 200)


############
#### Bouton Arbre H
############

arbreH_img = PhotoImage(file='fract_ressources/fract1.png')
arbreH = Button(main, image=arbreH_img, fg="grey", bg="grey")
arbreH.place(x = 425 , y = 60)

arbreH_label = Label(main, text = "Arbre en H", font = ("Verdana", 10, "italic bold "), bg = "grey") 
arbreH_label.place(x = 440, y = 200)

############
#### Bouton Sapin
############

sapin_img = PhotoImage(file='fract_ressources/sapin.png')
sapin = Button(main, image=sapin_img, fg="grey", bg="grey")
sapin.place(x = 610 , y = 60)

sapin_label = Label(main, text = "Sapin Bordel", font = ("Verdana", 10, "italic bold "), bg = "grey") 
sapin_label.place(x = 620, y = 200)

############
#### Bouton Surprise
############

surprise_img = PhotoImage(file='fract_ressources/surprise.png')
b_surprise = Button(main, image=surprise_img, fg="grey", bg="grey")
b_surprise.place(x = 50, y = 240)

surprise_label = Label(main, text = "Surpise du Chef", font = ("Verdana", 10, "italic bold "), bg = "grey") 
surprise_label.place(x = 45, y = 370)
        
############
#### Définition d'affichage
############

def displayWindow():
    """Affiche l'UI. Ne néscessite et ne renvoi rien"""
    if(main is None):
        raise ValueError("Une erreur a eu lieu lors de la définition 'main' de l'interface graphique")
    main.mainloop()