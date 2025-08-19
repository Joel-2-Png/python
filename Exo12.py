dict1 = {
    "nom": "mable",
    "prenom": "joel",
    "age": 18 }
dict2 = {
    "nom": "mable",
    "prenom": "Eyram",
    "age": 20}
 
fusion = {**dict1, **dict2}
print("Dictionnaire fusionné :", fusion)

# dict1.update(dict2)
# print("Dictionnaire fusionné (avec update) :", dict1)
