import threading
import random

def generer_liste_aleatoire(bas, haut, taille):
    """Générer une liste de nombres aléatoires."""
    return [random.randint(bas, haut) for _ in range(taille)]
