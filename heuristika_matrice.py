from heuristika import heuristika

def heuristika_matrice(matrica):
    for i, x in enumerate(matrica):
        for j, y in enumerate(x):
            kolona = j
            if y != "Q":
                matrica_pom = []
                for k, t in enumerate(matrica):
                    matrica_pom.append(matrica[k].copy())
                matrica_pom[i][matrica_pom[i].index("Q")] = 0
                matrica_pom[i][j] = "Q"
                matrica[i][j] = heuristika(matrica_pom)
    return matrica