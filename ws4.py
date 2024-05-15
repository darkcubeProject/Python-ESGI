# Votre programme doit analyser un texte de votre choix, et représenter dans la console la
# fréquence d’apparition de chaque lettre par un caractère ■ en ne dépassant pas une
# largeur de 40 caractères de large. La largeur de la barre doit être proportionnelle à la
# fréquence.

from collections import Counter

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec dictum non mauris in tempor. Phasellus fringilla varius elit vel mattis. Proin cursus malesuada urna a viverra. Cras fermentum porta efficitur. Sed tincidunt accumsan lacinia. Sed auctor congue finibus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec scelerisque est vitae congue ornare."

def analyse_text(text):

    lettres= 'ceida'
    text = text.lower()
    compteur = Counter(c for c in text if c in lettres)

    max_freq = max(compteur.values(), default=1)
    largeur_max = 40


    for lettre in lettres:
        freq = compteur.get(lettre, 0)
        largeur_barre = int((freq / max_freq) * largeur_max)
        print(f"{lettre}: {'■' * largeur_barre} ({freq})")

analyse_text(text)