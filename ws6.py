import threading
import random

def generer_liste_aleatoire(bas, haut, taille):
    """Générer une liste de nombres aléatoires."""
    return [random.randint(bas, haut) for _ in range(taille)]

def calculer_somme_carres(nombres, resultat, semaphore):
    """Calculer la somme des carrés pour une partie de la liste."""
    somme_locale = sum(x ** 2 for x in nombres)
    semaphore.acquire()
    try:
        resultat.append(somme_locale)
    finally:
        semaphore.release()
