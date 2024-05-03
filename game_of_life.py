from random import random
import affichage_Jeu_de_la_vie as aff
import RLE_parser as rle

def main():
    """
        Fonction principale d'une implementation du jeu de la vie.
        Renvoie l’animation de l’automate
    """
    # On crée une matrice aléatoire de 0 et de 1 ou on choisit un patterne à positionner sur la matrice
    n = 100
    tour_max = int(input("Nombre de générations : "))
    path = "/home/rburdino/Bureau/Home_INSA/ISN/ISN2/GameOfLife/RLE_files/"
    pattern = int(input("0: random, 1: pattern \n"))
    if pattern:
        m = matrice_pattern(n, path)
    else:
        m = generation_matrice(n)
    
    # Key : nombre de voisins, value : (next state if cell is dead, next state if cell is alive)
    regles = {0:(0,0), 1:(0,0), 2:(0,1), 3:(1,1), 4:(0,0), 5:(0,0), 6:(0,0), 7:(0,0), 8:(0,0)}
    anim = aff.init_visu()
    aff.add_visu(m, anim)

    i_tour = 0
    permanent = False
    while i_tour < tour_max and not permanent:
            
        # On détermine le nombre de voisins de chaque case
        m_voisin = matrice_voisin(m)
        
        # On copie m et fait evoluer m selon m_voisin et les règles d'evolution
        m_copie = [[_ for _ in subList] for subList in m]
        evolution(m, regles, m_voisin)
        
        permanent = liste_2D_identiques(m_copie, m)
        
        # Ajout de la matrice a l’animation
        aff.add_visu(m, anim)

        i_tour += 1
    
    if permanent:
        print(f"Le régime permanent a été atteint après {i_tour} tours.")
    else:
        print("Le régime permanent n’a pas été atteint.")
    return anim


def matrice_pattern(n, path):
    """
        Function that generates a 2D list with a pattern placed at certain coordinates (chosen by user). coordinates not verified.
        Input : 
            * path -> str, the path leading to the folder of rle files
            * n -> int, the length of the 2D list
        Output : m -> 2D list, composed of 0 except for the pattern
    """
    # Pattern / coordinates choice
    filename = rle.preset_choice(path)
    content = rle.filename_to_dict(path, filename)["content"]
    x, y = map(int, input("Pattern origin 'x y': ").split())
    
    # Pattern placement
    m = [[0 for _ in range(n)] for _ in range(n)]
    list_coo = rle.content_to_coordinates(content)
    for i, j in list_coo:
        m[x+i][y+j] = 1
    
    return m


def generation_matrice(n, proba = 0.10):
    """
        Function that generates a random 2D array composed by 0 and 1
        Input (optional) : 
            * n -> int, the lenght of the n x n 2D array
            * proba -> float, the probability of having a 1 placed in each cell
        Output : m -> 2D list, the 2D array
    """
    m = [[0 for _ in range(n)] for _ in range(n)]
    for line in range(n):
        for column in range(n):
            m[line][column] = random_choice([(0, 1-proba), (1, proba)])
    return m


def random_choice(choices):
    """
        Function that returns a random value with a weighted probability
        Input : choices -> list of 2-uple
            * choices[0] -> int, the number 
            * choices[1] -> float, the probability of having this number
        Output : int, a number in choices
    """
    r = random()
    if r < choices[0][1]:
        number = choices[0][0]
    else:
        number = choices[1][0]
    
    return number


def matrice_voisin(m):
    """
        Function that counts in the 8 neighbouring cells the number of 1. 
        The edge cells are considered.
        Input : m -> 2D list
        Output : m_voisin -> 2D list, the array composed of the number of neighbours.
    """
    lenght = len(m)
    m_voisin = [[0 for _ in range(lenght)] for _ in range(lenght)]
    
    # For each element of m
    for l in range(lenght):
        for c in range(lenght):
            nb_voisin = 0
            for l_v in range(l-1, l+2):
                for c_v in range(c-1, c+2):
                    
                    # True si les indices appartiennent a la liste
                    dans_liste = (l_v >= 0 and l_v < lenght) and (c_v >= 0 and c_v < lenght)
                    # True si on ne se trouve pas sur la case concernée
                    cond_case = not (l_v == l and c_v == c)
                    
                    if dans_liste and cond_case and m[l_v][c_v] == 1:
                        nb_voisin += 1
            
            m_voisin[l][c] = nb_voisin
    
    return m_voisin


def evolution(m, regles, m_voisin):
    for i_line in range(len(m)):
        for i_column in range(len(m)):
            new_state = regles[m_voisin[i_line][i_column]]
            m[i_line][i_column] = new_state[m[i_line][i_column]]


def liste_2D_identiques(m, n):
    """ Compare les 2 listes 2D elt par elt. Renvoie True si identiques, False sinon"""
    i, j = 0, 0
    est_identique = True
    while i < len(m) and est_identique:
        while j < len(m) and est_identique:
            if m[i][j] != n[i][j]:
                est_identique = False
            j += 1
        i += 1
        j = 0
    
    return est_identique


def affichage_matrice(m):
    for line in m:
        for elt in line:
            print(elt, end=" ")
        print()


anim = main()
interval = 150 # ms
aff.show_anim(anim, interval)