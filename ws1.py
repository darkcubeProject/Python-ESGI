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
