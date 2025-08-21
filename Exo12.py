# Définir deux dictionnaires
dict1 = {
    "M": 1,
    "b": 2,
    "c": 3
    }
dict2 = {
    "c": 30,
    "d": 4,
    "e": 5
    }

# Fusionner les dictionnaires (les clés identiques sont écrasées par dict2)
fusion = dict1.copy()   # On copie le premier dictionnaire
fusion.update(dict2)    # On ajoute le deuxième dictionnaire

# Afficher le résultat
print("Dictionnaire fusionné :", fusion)
