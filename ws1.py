# Créer un jeu juste prix générant un nombre aléatoire et indiquant à l'utilisateur plus ou moins celon ses réponses
import random
test = random.randint(1, 100)
print (test)


while True:
    user_choice = int(input("entrer un nombre entier > O : "))
    if user_choice > test :
        print ("c'est moins")
    if user_choice < test :
        print ("c'est plus")
    if user_choice == test:
        break    
print ("gagné")
# Rédigez un programme ws1.py tirant un nombre aléatoire, et demandant à l’utilisateur de  le deviner en indiquant simplement « plus » ou « moins ».

import random

nombre = random.randint(0, 10)

result = False


while not result:
 reponse = input("Devine le nombre:")


 chiffre = int(reponse)

 if chiffre > nombre: 
  print("C'est moins")
 elif chiffre < nombre:
  print("C'est plus")
 else:
  print("Vous avez trouvé !")
  break


