x = 0
y = 0
terrain = [".", ".", ".", ".", "."]
terrain[x] = "R"
commande = ""
rochers = [(2, 3), (4, 1)]

print("Bienvenue sur Mars !")
print("Le rover démarre en position", x, y)

while commande != "x":
    commande = input("Direction (z/q/s/d) ou x pour quitter: ")

    if commande == "z" and y < 4:
        prochaine_position = (x, y + 1)
        if prochaine_position in rochers:
            print("Obstacle détecté !")
        else:
            y = y + 1
    elif commande == "s" and y > 0:
        prochaine_position = (x, y - 1)
        if prochaine_position in rochers:
            print("Obstacle détecté !")
        else:
            y = y - 1
    elif commande == "d" and x < 4:
        prochaine_position = (x + 1, y)
        if prochaine_position in rochers:
            print("Obstacle détecté !")
        else:
            x = x + 1
    elif commande == "q" and x > 0:
        prochaine_position = (x - 1, y)
        if prochaine_position in rochers:
            print("Obstacle détecté !")
        else:
            x = x - 1 

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