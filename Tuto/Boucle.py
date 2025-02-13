nombres = input("saisir une liste de nombres séparés par des virgules")

liste = nombres.split(sep=",")

liste_entiers = []

for i in liste:
    nombre_entiers = int(i)
    liste_entiers.append(nombre_entiers)

somme = 0
moyenne = 0
nombres_sup = []
div = len(liste_entiers)

for i in liste_entiers:
    somme = somme + i
print(somme)

for i in liste_entiers:
    moyenne = moyenne + i
moyenne = moyenne / div
print(moyenne)

for i in liste_entiers:
    if i > moyenne:
        nombres_sup.append(i)
        
        print(len(nombres_sup))