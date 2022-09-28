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
b_pytatree.place(x = 5, y = 50)

pytatree_label = Label(main, text = "Arbre de pythagore", font = ("Verdana", 10, "italic bold "), bg = "grey") 
pytatree_label.place(x = 10, y = 225)



def __displayWindow__():
    main.mainloop()


        
