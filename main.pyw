import sys
sys.path.insert(1, "UI") # Import du module système et indication de la location du module UI et des ressources
sys.path.insert(2, "fract_ressources")

import index
if(index is None):
    raise ImportError("Une erreur a eue lieu lors de l'importation de l'UI")

index.displayWindow()

input('Press ENTER to exit') 
