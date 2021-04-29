from math import sqrt
print("Bonjour ces un programe permet de calculer selon le théorème de Pythagore (trouver l'hypoténuse).")
print("On notera les cotés du triangle rectangle AB,BC,CA et AB est l'hypoténuse.")
unité=input("Entrer l'abréviation de votre unité (en minuscule) pour les côtés du triangle mais ne pas les ré-écrire quand vous rentrez les valeurs des côtés : ")
print("information: la virgule s'ecrit avec un point")
BC=float(input("Entrer la Valeur BC:"))
CA=float(input("Entrer la Valeur CA:"))
print("AB²= BC²+ CA²")
print("AB²=",BC,"²","+",CA,"²")
BC=BC*BC
CA=CA*CA
#Les valeurs BC et CA ont été mis au carrée
print("AB²=",BC,"+",CA)
AB=BC+CA
print(AB,"²","=",BC,"+",CA)
print("√AB²=",sqrt(AB),unité)