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

def somme_carres_parallele(liste_nombres, nombre_threads):
    """Diviser le travail entre les threads et calculer la somme totale des carrés."""
    threads = []
    resultat = []
    semaphore = threading.Semaphore()

    # Diviser la liste en parties approximativement égales
    taille_chunk = len(liste_nombres) // nombre_threads
    for i in range(nombre_threads):
        debut_index = i * taille_chunk
        fin_index = (i + 1) * taille_chunk if i != nombre_threads - 1 else len(liste_nombres)
        thread = threading.Thread(target=calculer_somme_carres, args=(liste_nombres[debut_index:fin_index], resultat, semaphore))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sum(resultat)

if __name__ == "__main__":
    liste_nombres = generer_liste_aleatoire(1, 50, 1000)
    nombre_threads = 4
    somme_totale = somme_carres_parallele(liste_nombres, nombre_threads)
    print(f"Somme des carrés: {somme_totale}")
