fruits = {
    "pomme": 1000,
    "banane": 300,
    "cerise": 1200,
}

fruit_demande = input("Quel fruit voulez-vous connaître le prix : ")
if fruit_demande in fruits:
    print(f"Le prix de {fruit_demande} est {fruits[fruit_demande]} fcfa.")
else:
    print("Ce fruit n'est pas dans la liste.")  