# Consignes
# Créez une liste nommée  fruits  contenant les éléments  pomme  ,  banane  et  orange  .
# Ajoutez  kiwi  à la liste  fruits  .
# Supprimez  orange  de la liste  fruits  .
# Modifiez le deuxième élément de la liste  fruits  en  ananas  .
# Affichez la longueur de la liste  fruits  .
# Triez la liste  fruits  par ordre alphabétique et affichez-la.


fruits = ["pomme","banane","orange"]


fruits.append("kiwi")
print(fruits)
fruits.remove("orange")
print(fruits)
fruits[1] = "ananas"
print(fruits[2])
print(len(fruits))
fruits.sort()
print(fruits)




