############
#### Import des modules
############
import sys
 # Import du module système et indication de la location du module UI et des ressources
sys.path.insert(2, "fract_ressources")
sys.path.insert(3, "Dessins")
import fractales_draw
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

pytatree_img = PhotoImage(file='fract_ressources/pyta_treepng.png') # Charge l'image
# Crée un bouton avec l'image que l'on a parametré auparavant et on le lie à la fonction du module draw pour dessiner la fractales
b_pytatree = Button(main, image=pytatree_img,command=fractales_draw.draw_pytatree, fg="grey", bg="grey") 
#place le bouton à tel coordonnées
b_pytatree.place(x = 50, y = 60)

# Créer un label (texte) avec le nom de la figure, la police et la mise en forme
pytatree_label = Label(main, text = "Arbre de pythagore", font = ("Verdana", 10, "italic bold "), bg = "grey") 
pytatree_label.place(x = 45, y = 200)
# Place le label

############
#### Bouton Flocon
############

flocon_img = PhotoImage(file='fract_ressources/flocon.png')
b_flocon = Button(main, image=flocon_img,command=fractales_draw.draw_flocon, fg="grey", bg="grey")
b_flocon.place(x = 240, y = 60)

flocon_label = Label(main, text = "Flocon", font = ("Verdana", 10, "italic bold "), bg = "grey") 
flocon_label.place(x = 280, y = 200)


############
#### Bouton Arbre H
############

arbreH_img = PhotoImage(file='fract_ressources/fract1.png')
arbreH = Button(main, image=arbreH_img,command=fractales_draw.draw_arbreenh, fg="grey", bg="grey")
arbreH.place(x = 425 , y = 60)

arbreH_label = Label(main, text = "Arbre en H", font = ("Verdana", 10, "italic bold "), bg = "grey") 
arbreH_label.place(x = 440, y = 200)

############
#### Bouton Sapin
############


    
sapin_img = PhotoImage(file='fract_ressources/sapin.png')
sapin = Button(main, image=sapin_img,command=fractales_draw.draw_sapin, fg="grey", bg="grey")
sapin.place(x = 610 , y = 60)

sapin_label = Label(main, text = "Sapin Bordel", font = ("Verdana", 10, "italic bold "), bg = "grey") 
sapin_label.place(x = 620, y = 200)

############
#### Bouton Surprise
############

surprise_img = PhotoImage(file='fract_ressources/surprise.png')
b_surprise = Button(main, image=surprise_img,command=fractales_draw.draw_surpriseduchef,fg="grey", bg="grey")
b_surprise.place(x = 50, y = 240)

surprise_label = Label(main, text = "Surpise du Chef", font = ("Verdana", 10, "italic bold "), bg = "grey") 
surprise_label.place(x = 50, y = 370)

############
#### Bouton Rect
############

rect_img = PhotoImage(file='fract_ressources/fract_rect.png')
b_rect = Button(main, image=rect_img, command=fractales_draw.draw_rect, fg="grey", bg="grey")
b_rect.place(x = 240, y = 240)

rect_label = Label(main, text = "Giga Rectangle", font = ("Verdana", 10, "italic bold "), bg = "grey") 
rect_label.place(x = 245, y = 370)

############
#### Bouton Dragon
############

dragon_img = PhotoImage(file='fract_ressources/dragon.png')
b_dragon = Button(main, image=dragon_img, command=fractales_draw.draw_dragon, fg="grey", bg="grey")
b_dragon.place(x = 425, y = 240)

dragon_label = Label(main, text = "Dragon", font = ("Verdana", 10, "italic bold "), bg = "grey") 
dragon_label.place(x = 460, y = 370)


############
#### Bouton Mystere
############

mystere_img = PhotoImage(file='fract_ressources/mystere.png')
b_mystere = Button(main, image=mystere_img, command=fractales_draw.draw_mystere, fg="grey", bg="grey")
b_mystere.place(x = 610, y = 240)

mystere_label = Label(main, text = "Mystère", font = ("Verdana", 10, "italic bold "), bg = "grey") 
mystere_label.place(x = 640, y = 370)


############
#### Bouton Couleur pour fractale
############

color_img = PhotoImage(file='fract_ressources/color_picker.png')
b_color = Button(main, image=color_img, command=fractales_draw.choose_color, fg="grey", bg="grey")
b_color.place(x = 750, y = 10)


############
#### Bouton Couleur pour interface
############

color2_img = PhotoImage(file='fract_ressources/color_picker.png')
b_color2 = Button(main, image=color2_img, command=fractales_draw.choose_color_bg, fg="grey", bg="grey")
b_color2.place(x = 20, y = 10)


        
############
#### Définition d'affichage
############

def displayWindow():
    """Affiche l'UI. Ne néscessite et ne renvoi rien"""
    if(main is None):
        raise ValueError("Une erreur a eu lieu lors de la définition 'main' de l'interface graphique")
    main.mainloop()