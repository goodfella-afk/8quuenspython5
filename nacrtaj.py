import matplotlib.pyplot as plt

def nacrtaj(matrica):

    fig, ax = plt.subplots()
    # hide axes
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    colors = []
    for row in matrica:
        items = []
        for value in row:
            if value == 'Q':
                items.append('r')
            elif value =='X':
                items.append('blue')
            else:
                items.append('white')
        colors.append(items)

    x = ax.table(cellText=matrica, cellColours = colors, loc='center')
    x.set_fontsize(18)
    x.scale(1, 3)
    fig.tight_layout()
    fig.canvas.manager.set_window_title('Osam Kraljica v3 klapa 10')
    plt.show(block = False)
    plt.pause(1.5)
    plt.close()