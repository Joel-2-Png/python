notes = {
        "Alice": 15,
         "Bob": 12, 
         "Charlie": 18,
         "David": 14
    }
meilleur_etudiant = max(notes, key=notes.get)
print("L'étudiant avec la meilleure note est :", meilleur_etudiant)