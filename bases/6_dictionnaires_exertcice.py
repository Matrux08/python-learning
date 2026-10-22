#Créez un dictionnaire appelruits  avec les clés  pomme  ,  banane  et  orange  , et les valeurs  rouge  ,  jaune  et  orange  .
#Ajoutez la clé  kiwi  avec la valeur  vert  au dictionnaire  fruits  .
#Accédez à la valeur correspondant à la clé  banane  et stockez-la dans une variable appelée  couleur_banane  .
#Modifiez la valeur associée à la clé  pomme  pour  vert  .
#Supprimez la clé  banane  du dictionnaire  fruits  .
#Affichez les clés restantes dans le dictionnaire.


fruits = {"pomme":"rouge","banane": "jaune","orange":"orange"}
fruits["kiwi"] = "vert"
couleur_banane = fruits["banane"] 
fruits["pomme"] = "vert"
del fruits["banane"]

print(fruits.keys())
print("banne" in fruits)