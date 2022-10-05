############
#### Import de turtle et tout le reste
############

from turtle import *
import math

def draw_pytatree():
    speed(0)

    color('#3f1905')
    sc = Screen()
    sc.title("Arbre de Pythagore")
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
    sc = Screen()
    sc.title("Flocon de Von Koch")
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
    sc = Screen()
    sc.title("Arbre en H")
    __arbreenh__(2, (0, 0), 300)
    done()
    mainloop()

def __sapintree__(x,y,direction,length, golden_ratio):
    up()
    goto(x,y)
    seth(direction)
    pensize(math.log(length,2)/3)
    if length<10: color('forest green')
    else: color('gray')
    down()
    fd(length)
    if length < 3: return
    cx,cy = xcor(), ycor()
    __sapintree__(cx,cy,direction+72,(2-golden_ratio)*length,golden_ratio)
    __sapintree__(cx,cy,direction-72,(2-golden_ratio)*length,golden_ratio)
    __sapintree__(cx,cy,direction,(golden_ratio-1)*length, golden_ratio)



def draw_sapin():
    sc = Screen()
    sc.title('Sapin')
    #sc.setup(1000,1000)
    #sc.setworldcoordinates(-1000,-1000,1000,1000)
    speed(0)
    hideturtle()
    tracer(0,0)
    golden_ratio = (1+5**0.5)/2
    __sapintree__(0,-900,90,700, golden_ratio)
    done()
    mainloop()





