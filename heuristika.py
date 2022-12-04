
def heuristika(matrica):
    heuristika = 0
    for i, red in enumerate(matrica):
        for j, elem in enumerate(red):
            kolona = j
            if elem == "Q":
                #kolone
                for r, elem_pom in enumerate(matrica):
                    if r > i:
                        if elem_pom[kolona] == "Q":
                            heuristika += 1
                # dijagonala dolje lijevo
                kolona = j - 1
                for r, elem_pom in enumerate(matrica):
                    if r > i:
                        if kolona >= 0 and elem_pom[kolona] == "Q":
                            heuristika += 1
                        kolona -= 1
                kolona = j + 1
                # dijagonala dolje desno
                for r, elem_pom in enumerate(matrica):
                    if r > i:
                        if kolona < 8 and elem_pom[kolona] == "Q":
                            heuristika += 1
                        kolona += 1
    return heuristika