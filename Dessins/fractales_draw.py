############
#### Import de turtle, du colorchooser de tkinter et tout le reste
############

from turtle import *
import math
import time
import random
from tkinter import colorchooser
from tkinter import messagebox
from math import cos, pi

############
#### Création de la liste globale comportant toutes les fonctions pour dessiner, on l'utilisera plus tard dans le code
#### Création de la variable contenant la couleur custom choisie par l'utilisateur, on l'utilisera plus tard dans le code
############
global list_des_dessins
custom_color = '#000000'
custom_color_bg = '#000000'
angle_arbre = 30
############
#### Fonctions publique et sous fonctions encapsulées pour le dessin de l'arbre de pythagore
############


def draw_pytatree():
    """fonction publique du module qui sera utilisé dans le module de l'UI"""
    speed(0)

    color('#3f1905')
    sc = Screen()
    sc.title("Arbre de Pythagore")
    if(custom_color_bg != '#000000'):
        sc.bgcolor(custom_color_bg) 
    else:
        sc.bgcolor("white") 
    hideturtle() # cache la tortue
    up() # lève le stylo
    right(90) # tourne de 90 degrés vers la droite 
    forward(300) # avance de 300 pixels
    left(180) # fait un demi-tour
    down() # pose le stylo
    __arbre__(11,700) # exécute la macro
    done()
    mainloop()
    

def __arbre__(n,longueur):
    """fonction encapsulé necessaire a la creation de l'arbre de pythagore"""
    global angle_arbre

    
    if n==0:
        global custom_color
        if(custom_color != '#000000'):
            color(custom_color)
        else:
            color('green')
        forward(longueur) # avance
        backward(longueur) # recule
        color('#3f1905')
    else:
        width(n)
        forward(longueur/3) #avance
        left(angle_arbre) # tourne vers la gauche de angle degrés
        __arbre__(n-1,longueur*2/3)
        right(2*angle_arbre) # tourne vers la droite de angle degrés
        __arbre__(n-1,longueur*2/3)
        left(angle_arbre) # tourne vers la gauche de angle degrés
        backward(longueur/3) # recule


############
#### Fonctions publique et sous fonctions encapsulées pour le dessin du flocon de vonkoch
############

# Flocon classique

def __courbeVonKoch__(  n=3, cote=200):
    """fonction encapsulé necessaire a la creation du flocon"""
    global custom_color
    if(custom_color != '#000000'):
        color(custom_color)
    else:
        color("blue")
    if n == 0:
        forward(cote)
    else:
        __courbeVonKoch__(n-1, cote/3)
        left(60)
        __courbeVonKoch__(n-1, cote/3)
        left(-120)
        __courbeVonKoch__(n-1, cote/3)
        left(60)
        __courbeVonKoch__(n-1, cote/3)


def draw_flocon(n=5, cote=500):
    """fonction publique du module qui sera utilisé dans le module de l'UI"""
    
    setheading(0) # orientation intiale de la tête : vers la droite de l'écran
    hideturtle() # on cache la tortue
    speed(0)	 # on accélère la tortue
    sc = Screen()
    sc.title("Flocon de Von Koch")
    if(custom_color_bg != '#000000'):
        sc.bgcolor(custom_color_bg) 
    else:
        sc.bgcolor("white") 
    for y in range(3):
        __courbeVonKoch__(  n, cote  )
        left(-120)
    done()
    mainloop()


# Flocon difforme

def __courbeVonKochDiff__(  n, cote  ) :
    global custom_color
    if(custom_color != '#000000'):
        color(custom_color)
    else:
        color("blue")
    if n == 0:
        forward(cote)
    else:
        __courbeVonKochDiff__(n-1, cote/3)
        left(90)
        __courbeVonKochDiff__(n-1, cote/3)
        right(90)
        __courbeVonKochDiff__(n-1, cote/3)
        right(90)
        __courbeVonKochDiff__(n-1, cote/3)
        left(90)
        __courbeVonKochDiff__(n-1, cote/3)


def draw_flocon_diff(n=3, cote=200) :
    setheading(0) # orientation intiale de la tête : vers la droite de l'écran
    hideturtle() # on cache la tortue
    speed(0)	 # on accélère la tortue
    sc = Screen()
    sc.title("Flocon de Von Koch Difforme")
    if(custom_color_bg != '#000000'):
        sc.bgcolor(custom_color_bg) 
    else:
        sc.bgcolor("white") 
    for _ in range(3) :
        __courbeVonKochDiff__(  n, cote  )
        left(-120)
    done()
    mainloop()


############
#### Fonctions publique et sous fonctions encapsulées pour le dessin de l'arbre en H
############
    
def __dessinh__(center, size):
    """fonction encapsulé necessaire a la creation du arbre en h"""
    penup()
    goto(center)
    pendown()

    forward(size / 2)
    left(90)
    forward(size / 2)
    right(180)
    forward(size)

    penup()
    goto(center)
    pendown()

    right(90)
    forward(size / 2)
    right(90)
    forward(size / 2)
    right(180)
    forward(size)

    right(90)

def __get_h_coord__(center, size):
    """fonction encapsulé necessaire a la creation du arbre en h"""
    ep1 = center[0] + size / 2
    ep2 = center[1] + size / 2
    ep3 = center[0] - size / 2
    ep4 = center[1] - size / 2

    return ep1, ep2, ep3, ep4

def __arbreenh__(order,center,size):
    """fonction encapsulé necessaire a la creation du arbre en h """
    __dessinh__(center, size)

    if order > 0:
        ep1, ep2, ep3, ep4 = __get_h_coord__(center, size)

        __arbreenh__(order - 1, (ep1, ep2), size / 2)
        __arbreenh__(order - 1, (ep1, ep4), size / 2)
        __arbreenh__(order - 1, (ep3, ep2), size / 2)
        __arbreenh__(order - 1, (ep3, ep4), size / 2)

def draw_arbreenh():
    """fonction publique du module qui sera utilisé dans le module de l'UI"""
    global custom_color
    if(custom_color != '#000000'):
        color(custom_color)
    else:
        color('green')
    sc = Screen()
    sc.title("Arbre en H")
    if(custom_color_bg != '#000000'):
        sc.bgcolor(custom_color_bg) 
    else:
        sc.bgcolor("white") 
    __arbreenh__(2, (0, 0), 300)
    done()
    mainloop()


############
#### Fonctions publique et sous fonctions encapsulées pour le dessin du sapin
############

def __sapintree__(x,y,direction,length, golden_ratio):
    """fonction encapsulé necessaire a la creation du sapin"""
    up()
    goto(x,y)
    seth(direction)
    pensize(math.log(length,2)/3)
    if length<10:
        global custom_color
        if(custom_color != '#000000'):
            color(custom_color)
        else:
            color('forest green')
    else: 
        color('gray')
    down()
    fd(length)
    if length < 3: return
    cx,cy = xcor(), ycor()
    __sapintree__(cx,cy,direction+72,(2-golden_ratio)*length,golden_ratio)
    __sapintree__(cx,cy,direction-72,(2-golden_ratio)*length,golden_ratio)
    __sapintree__(cx,cy,direction,(golden_ratio-1)*length, golden_ratio)



def draw_sapin():
    """fonction publique du module qui sera utilisé dans le module de l'UI"""
    sc = Screen()
    sc.title('Sapin')
    if(custom_color_bg != '#000000'):
        sc.bgcolor(custom_color_bg) 
    else:
        sc.bgcolor("white") 
    speed(0)
    hideturtle()
    tracer(0,0)
    golden_ratio = (1+5**0.5)/2
    __sapintree__(0,-900,90,700, golden_ratio)
    done()
    mainloop()


############
#### Fonctions publique et sous fonctions encapsulées pour le dessin de la surprise du chef
############

def __drawcarre__(n):
    """fonction encapsulé necessaire a la creation de la surprise du chef"""
    if(n == 0):
        return None
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    left(n)
    return __drawcarre__(n-1)

def draw_surpriseduchef():
    """fonction publique du module qui sera utilisé dans le module de l'UI"""
    sc = Screen()
    sc.title('La Surprise du Chef')
    if(custom_color_bg != '#000000'):
        sc.bgcolor(custom_color_bg) 
    else:
        sc.bgcolor("white") 
    speed(0)
    global custom_color
    if(custom_color != '#000000'):
        color(custom_color)
    else:
        color('green')
    __drawcarre__(360)
    done()
    mainloop()


############
#### Fonctions publique et sous fonctions encapsulées pour le dessin du rectangle
############

def __tropPetit__(width, height):
    """fonction encapsulé necessaire a la creation du giga rectangle"""
    MIN_SIZE = 6 
    DRAW_SOLID = True
    
    return width < MIN_SIZE or height < MIN_SIZE

def __drawlesPtitsRectangles__(x, y, width, height):
    """fonction encapsulé necessaire a la creation du giga rectangle"""
    if __tropPetit__(width, height):
        # cas de base
        return
    else:
        

        oneThirdWidth = width / 3
        oneThirdHeight = height / 3
        twoThirdsWidth = 2 * (width / 3)
        twoThirdsHeight = 2 * (height / 3)

        
        penup()
        goto(x + oneThirdWidth, y + oneThirdHeight)
        DRAW_SOLID = True

        
        if DRAW_SOLID:
            fillcolor('white')
            begin_fill()
        pendown()
        goto(x + oneThirdWidth, y + twoThirdsHeight)
        goto(x + twoThirdsWidth, y + twoThirdsHeight)
        goto(x + twoThirdsWidth, y + oneThirdHeight)
        goto(x + oneThirdWidth, y + oneThirdHeight)
        penup()
        if DRAW_SOLID:
            end_fill()

       
        __drawlesPtitsRectangles__(x, y + twoThirdsHeight, oneThirdWidth, oneThirdHeight)
        __drawlesPtitsRectangles__(x + oneThirdWidth, y + twoThirdsHeight, oneThirdWidth, oneThirdHeight)
        __drawlesPtitsRectangles__(x + twoThirdsWidth, y + twoThirdsHeight, oneThirdWidth, oneThirdHeight)

       
        __drawlesPtitsRectangles__(x, y + oneThirdHeight, oneThirdWidth,
        oneThirdHeight)
        __drawlesPtitsRectangles__(x + twoThirdsWidth, y + oneThirdHeight, oneThirdWidth,
        oneThirdHeight)

        
        __drawlesPtitsRectangles__(x, y, oneThirdWidth, oneThirdHeight)
        __drawlesPtitsRectangles__(x + oneThirdWidth, y, oneThirdWidth, oneThirdHeight)
        __drawlesPtitsRectangles__(x + twoThirdsWidth, y, oneThirdWidth,
        oneThirdHeight)

def __drawfond__(x, y, width, height):
    """fonction encapsulé necessaire a la creation du giga rectangle"""
    DRAW_SOLID = True
    
    penup()
    goto(x, y)

    
    pendown()
    if DRAW_SOLID:
        global custom_color
        if(custom_color != '#000000'):
            color(custom_color)
        else:
            fillcolor('black')
        begin_fill()
    goto(x, y + height)
    goto(x + width, y + height)
    goto(x + width, y)
    goto(x, y)
    if DRAW_SOLID:
        end_fill()
    penup()

    
    __drawlesPtitsRectangles__(x, y, width, height)

def draw_rect():
    """fonction publique du module qui sera utilisé dans le module de l'UI"""
    sc = Screen()
    sc.title('Giga Rectangle')
    if(custom_color_bg != '#000000'):
        sc.bgcolor(custom_color_bg) 
    else:
        sc.bgcolor("white") 
        
    speed(0)
    tracer(10, 0)
    setworldcoordinates(0, 0, 700, 700)
    hideturtle()
    __drawfond__(50, 50, 600, 600)


############
#### Fonctions publique et sous fonctions encapsulées pour le dessin du dragon
############


def __dragon_build__(turtle_string, n):
    """fonction encapsulé necessaire a la creation du dragon"""
    rules = {'x':'x+yf', 'y':'fx-y','f':'f', '-':'-', '+':'+'}
    turtle_string = ''.join([rules[x] for x in turtle_string])
    if n > 1: return __dragon_build__(turtle_string, n-1)
    else: return turtle_string

def __dragon__(size=20):
    """fonction encapsulé necessaire a la creation du dragon"""
    turtle_string = __dragon_build__('fx', size)
    for x in turtle_string:
        if x == 'f': forward(5)
        elif x == '+': right(90)
        elif x == '-': left(90)



def draw_dragon():
    """fonction publique du module qui sera utilisé dans le module de l'UI"""
    speed(0) 
    hideturtle() 
    wn=Screen() 
    wn.title('Dragon')
    if(custom_color_bg != '#000000'):
        wn.bgcolor(custom_color_bg) 
    else:
        wn.bgcolor("white") 

    if(custom_color != '#000000'):
        color(custom_color)
    else:   
        pencolor("blue") 
    __dragon__()
    done()
    mainloop()

############
#### Assignation de toutes les fonctions de dessin à la liste globale
#### Fonctions publique et sous fonctions encapsulées pour le dessin aléatoire
############

list_des_dessins = [draw_pytatree, draw_flocon, draw_arbreenh, draw_sapin, draw_surpriseduchef, draw_rect, draw_dragon]
def draw_mystere():
    list_des_dessins[random.randint(0,6)]()
    done()
    mainloop()


def choose_color():
    """fonction publique du module qui sera utilisé dans le module de l'UI pour choisir la couleur de toutes les fractales"""
    messagebox.showwarning("Choix des couleurs", "Vous vous apprêtez à changer la couleur des fractales")
    global custom_color
    custom_color = str(colorchooser.askcolor()[1])

def choose_color_bg():
    """fonction publique du module qui sera utilisé dans le module de l'UI pour choisir la couleur de l'arrière plan de toutes les fractales"""
    messagebox.showwarning("Choix des couleurs", "Vous vous apprêtez à changer la couleur de l'arrière plan des fractales")
    global custom_color_bg
    custom_color_bg = str(colorchooser.askcolor()[1])
    
    






    





