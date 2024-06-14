import random
choix = ["tomate", "fraise", "melon", "pomme"]
solution = random.choice(choix)

solution = "pomme"
tentatives = 7
affichage = ""
lettres_trouvees = ""

for l in solution:
  affichage = affichage + "_ "

print(">> Lancement du jeu <<")

while tentatives > 0:
  print("\nMot à deviner : ", affichage)
  proposition = input("proposez une lettre : ")[0:1].lower()

  if proposition in solution:
      lettres_trouvees = lettres_trouvees + proposition
      print("-> Bien vu!")
  else:
    tentatives = tentatives - 1
    print("-> Nope\n")
    if tentatives==0:
        print(" ==========Y= ")
    if tentatives<=1:
        print(" ||/       |  ")
    if tentatives<=2:
        print(" ||        0  ")
    if tentatives<=3:
        print(" ||       /|\ ")
    if tentatives<=4:
        print(" ||       /|  ")
    if tentatives<=5:                    
        print("/||           ")
    if tentatives<=6:
        print("==============\n")

  affichage = ""
  for x in solution:
      if x in lettres_trouvees:
          affichage += x + " "
      else:
          affichage += "_ "

  if "_" not in affichage:
      print(">>> Gagné! <<<")
      break
     
print("\n    * Fin de la partie *    ")
# wordlist = 'wordlist.txt'

# # Lire le contenu du fichier et importer les mots dans une liste
# with open(wordlist, 'r') as fichier:
#     # Lire le fichier entier
#     contenu = fichier.read()

#     # Si les mots sont séparés par des espaces ou des virgules
#     # mots = contenu.split()

#     # Si les mots sont sur des lignes séparées
#     mots = contenu.splitlines()

# # Afficher la liste des mots importés
# print(mots)
