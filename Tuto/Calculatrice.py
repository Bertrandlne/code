nombre1 = input("Veuillez entrer le premier nombre : ")
nombre2 = input("Veuillez entrer le second nombre : ")

if not nombre1.isnumeric() or not nombre2.isnumeric():
     raise SystemExit("Fin du programme")
else: 
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)

operation = input("Veuillez entrer l'opération souhaitée (+, -, *, /) : ")

if operation not in ['+', '-', '*', '/']:
    raise SystemExit("Opération non valide. Fin du programme.")

if operation == '+':
    resultat = nombre1 + nombre2
elif operation == '-':
    resultat = nombre1 - nombre2
elif operation == '*':
    resultat = nombre1 * nombre2
elif operation == '/':
    if nombre2 == 0:
        raise SystemExit("Division par zéro impossible. Fin du programme.")
    resultat = round(nombre1 / nombre2, 2)  # Arrondir à 2 décimales

# Afficher le résultat
print(f"Le résultat de l'opération est : {resultat}")