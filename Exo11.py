notes = {
        "joel": 15,
         "joelle": 12, 
         "sam": 18,
         "samuel": 14
    }
meilleur_etudiant = max(notes, key=notes.get)
print("L'étudiant avec la meilleure note est :", meilleur_etudiant)