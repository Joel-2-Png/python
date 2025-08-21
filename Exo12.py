dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5, "f": 6}
fusion = {**dict1, **dict2}

print("Dictionnaire fusionné :", fusion)
dict1.update(dict2)
print("Dictionnaire fusionné (avec update) :", dict1)

