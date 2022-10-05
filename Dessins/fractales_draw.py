############
#### Import de turtle et tout le reste
############

from turtle import *

def draw_pytatree():
    speed(0)

    color('#3f1905')

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
    angle = 30
    if n==0:
        color('green')
        forward(longueur) # avance
        backward(longueur) # recule
        color('#3f1905')
    else:
        width(n)
        forward(longueur/3) #avance
        left(angle) # tourne vers la gauche de angle degrés
        __arbre__(n-1,longueur*2/3)
        right(2*angle) # tourne vers la droite de angle degrés
        __arbre__(n-1,longueur*2/3)
        left(angle) # tourne vers la gauche de angle degrés
        backward(longueur/3) # recule




def __courbeVonKoch__(  n=3, cote=200  ):
	if n == 0 :
		forward(cote)
	else :
		__courbeVonKoch__(n-1, cote/3)
		left(60)
		__courbeVonKoch__(n-1, cote/3)
		left(-120)
		__courbeVonKoch__(n-1, cote/3)
		left(60)
		__courbeVonKoch__(n-1, cote/3)


def draw_flocon(n=3, cote=200):
    
    setheading(0) # orientation intiale de la tête : vers la droite de l'écran
    hideturtle() # on cache la tortue
    speed(0)	 # on accélère la tortue
    color('blue')
    for y in range(3):
	    __courbeVonKoch__(  n, cote  )
	    left(-120)
    done()
    mainloop()
    
def __dessinh__(center, size):
    penup()
    goto(center)
    pendown()

    forward(size / 2)  # right side of H
    left(90)
    forward(size / 2)
    right(180)
    forward(size)

    penup()
    goto(center)
    pendown()

    right(90)  # left side of H
    forward(size / 2)
    right(90)
    forward(size / 2)
    right(180)
    forward(size)

    right(90)  # return turtle to original orientation

def __get_h_coord__(center, size):
    ep1 = center[0] + size / 2
    ep2 = center[1] + size / 2
    ep3 = center[0] - size / 2
    ep4 = center[1] - size / 2

    return ep1, ep2, ep3, ep4

def __arbreenh__(order,center,size):
    __dessinh__(center, size)

    if order > 0:
        ep1, ep2, ep3, ep4 = __get_h_coord__(center, size)

        __arbreenh__(order - 1, (ep1, ep2), size / 2)
        __arbreenh__(order - 1, (ep1, ep4), size / 2)
        __arbreenh__(order - 1, (ep3, ep2), size / 2)
        __arbreenh__(order - 1, (ep3, ep4), size / 2)

def draw_arbreenh():
    color('green')
    __arbreenh__(2, (0, 0), 300)





