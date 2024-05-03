from os import listdir
from os.path import isfile, join

#path = "/home/rburdino/Bureau/Home_INSA/ISN/ISN2/GameOfLife/RLE_files/"

def preset_choice(path):
    """
        Input : files -> list, the list of the name of every file in the RLE_files folder
        Output : the name of the file that is chosen
    """
    files = [f for f in listdir(path) if isfile(join(path, f))]
    
    for i_file in range(len(files)):
        print(f"{i_file} : {files[i_file]}")
    print()
    i_user = int(input())
    
    return files[i_user]


def filename_to_dict(path, filename):
    """
        Function that parses an RLE file, converts its data to a dict with name, size and content keys.
        Input :
            * path -> str, the path of the RLE files folder
            * filename -> str, the name of the RLE file
        Output :
            * dict
    """
    file = open(path+filename, "r") # r : read only
    unformated = file.read()
    file_list = unformated.split("\n")
    preset_info = {"name": filename}
    
    # Removing line break
    formated = []
    for line in file_list:
        if line[0] != "#":
            formated.append(line)
    
    # Fetching the size
    size_list = formated[0].split(",")
    size_list.pop()
    x = int(size_list[0].split(" ")[2])
    y = int(size_list[1].split(" ")[3]) # there’s a space before y
    preset_info["size"] = (x, y)
    
    # Fetching the pattern
    cpt = len(formated) - 1
    content = ""
    while formated[cpt][0] != "x": # Tant qu’on tombe pas sur un x (size) en partant de la fin
        content = formated[cpt] + content
        cpt -= 1
    
    preset_info["content"] = content
    
    return preset_info
            

def content_to_coordinates(content):
    """
        Function that converts a string to a list of coordinates (of alive cells)
        Input :
            * content -> string, b -> dead cell, o -> alive cell, $ -> end of line, ! -> end of content
        Output :
            * list of 2-uple, the coordinates of the alive cells (line, column)
        Example :
            "11b2o$2bo9bo!" -> [(0,11), (0,12), (1,2), ...]
            
    """
    cells = []
    l, c = 0, 0
    j = 0
    
    while j < len(content):
        # On détermine le nombre qui précède le caractère
        nombre = ""
        while content[j].isdigit(): # Tant que c’est un chiffre (et donc pas un caractère)
            nombre = nombre + content[j]
            j += 1
        if nombre == "":
            nombre = 1
        else:
            nombre = int(nombre)
        
        # On traite chaque caractère comme un cas différent
        if content[j] == "b":
            c += nombre

        elif content[j] == "o":
            for _ in range(nombre):
                cells.append((l, c))
                c += 1
                
        elif content[j] == "$":
            c = 0
            l = l+nombre
        
        # On avance dans la chaine de caractère
        j = j + 1
    
    return cells