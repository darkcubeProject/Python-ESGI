# Rédigez un programme ws3.py recherchant un entier selon la méthode dichotomique.
# Commencez par trier le tableau en entrée par ordre croissant.
# La recherche dichotomique consiste à vérifier l’item au milieu du tableau, et selon la valeur, 
# d’aller chercher une valeur vers le quart suivant du tableau, jusqu’à trouver (ou non) la 
# valeur souhaitée.

from tabulate import tabulate

tableau = ['3','2','1','4','6','8','7','5','0','9']
tableau.sort()
print(tabulate(tableau, headers='firstrow', tablefmt='fancy_grid'))