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


