import sys
sys.path.insert(1, "UI") # Import du module système et indication de la location du module UI et des ressources
sys.path.insert(2, "fract_ressources")

import index
print("Lancement de l'application..") # Importation du fichier index contenant l'interface graphique
if(index is None):
    # gestion d'erreur si on a pas reussi a importer l' UI
    raise ImportError("Une erreur a eue lieu lors de l'importation de l'UI")
# utilise la fonction du module index afin d'afficher la fenêtre principale
index.displayWindow()

input('Press ENTER to exit') 