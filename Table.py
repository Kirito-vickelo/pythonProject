
print("Bonjour je vous présente un programme permettant de calculer n'importe quelle table de multiplication et jusqu'à le nombres que vous souhaitez")
table=numero=int(input("taper la table souhaiter:"))
compteur=0
multiplie=1
repetition=int(input("Entrer le nombres de fois que vous voulez avant que la table s'arrête:"))
print(numero,"X 0 = 0")

while compteur < repetition :
     print(int(numero),"X",int(multiplie),"=", int(table))
     table += numero
     multiplie += 1
     compteur += 1