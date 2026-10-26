x = 0
y = 0
commande = ""
rochers = [(2, 3), (4, 1)]
batterie = 100

print("Bienvenue sur Mars !")
print("Le rover démarre en position", x, y)

while commande != "x":
    commande = input("Direction (z/q/s/d) ou x pour quitter: ")

    nx = x
    ny = y

    if commande == "z" and y < 4:
        ny = y + 1
    elif commande == "s" and y > 0:
        ny = y - 1
    elif commande == "d" and x < 4:
        nx = x + 1
    elif commande == "q" and x > 0:
        prochaine_position = (x - 1, y)
        nx = x - 1 
    elif commande != "x":
        print("Mouvement impossible ou commande inconnue")

    if (nx, ny) in rochers:
        print("Obstacle détecté !")
    else:
        if(nx, ny) != (x, y):
            batterie = batterie - 1
        x = nx
        y = ny

    for ligne in range(5):
        for colonne in range(5):
            if colonne == x and ligne == y:
                print("R", end=" ")
            elif (colonne, ligne) in rochers:
                print("X", end=" ")
            else:
                print(".", end=" ")
                
        print()
    print(f"Position du rover x : {x}, y : {y}")
    blocs_pleins = batterie // 10
    print("Batterie : [" + "█" * blocs_pleins + "░" * (10 - blocs_pleins) + "] " + str(batterie) + "%")


    if batterie == 0:
        print("Batterie vide, le rover est perdu sur Mars !")
        commande = "x"