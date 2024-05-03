import matplotlib.pyplot as plt
import matplotlib.animation as animation
#from random import randint

########### INITIALISATION DE L’ANIMATION
def init_visu() :
    '''
    Création initiale de l'animation
    '''
    fig, ax = plt.subplots()
    ims = []
    plt.axis("off")
    return [fig, ax, ims]

########### AJOUT D’UN ETAT A L’ANIMATION
def add_visu(grid, visu) :
    '''
    Ajout d'un état de l'automate grid à l'animation visu
    '''
    fig, ax, ims = visu[0], visu[1], visu[2]
    im = ax.imshow(grid, animated=True)
    ims.append([im])
    return [fig, ax, ims]

########### AFFICHAGE DE L’ANIMATION
def show_anim(visu, inter=100) :
    '''
    lance l'affichage de l'animation dans une nouvelle fenêtre
    '''
    fig, ims = visu[0], visu[2]
    ani = animation.ArtistAnimation(fig, ims, interval=inter, blit=True, repeat_delay=1000)
    plt.show()
    visu.append(ani)


"""
def update(m):
    for i in range(len(m)):
        for j in range(len(m)):
            m[i][j] = randint(0,1)
    return m


########## PARTIE PRINCIPALE
anim = init_visu()

monde = [[0, 0 , 0 , 0 , 0, 0],
        [0, 0 , 1 , 0 , 0, 0],
        [0, 1 , 1 , 0 , 0, 0],
        [0, 1 , 1 , 0 , 0, 0],
        [0, 0 , 0 , 1 , 0, 0],
        [0, 0 , 0 , 0 , 0, 0]]

anim = add_visu(monde, anim)

for i in range(10) :
    monde = update(monde)
    anim = add_visu(monde, anim)

show_anim(anim)
"""