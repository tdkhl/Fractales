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
    mainloop()

print("slt")

