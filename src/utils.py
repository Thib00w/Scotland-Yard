from .classes import Station
import matplotlib.pyplot as plt
 
def init_Station_with_csv(file_path: str):
    """ Methode qui revera une liste d'intance de Station (a besoin de la class Station):
             file : str, chemin d'accee du fichier csv    
             return : liste
    """
    try:
        with open(file_path, 'r') as file:
            headline = file.readline().strip()
            lines = file.readlines()
        list_box = []
        for line in lines:
            elements = line.strip().split(';')
            # Convertion des premiers elements
            numero = int(elements[0])
            x = int(int(elements[1]) * 3.28125) # ratio longueur 3,28125
            y = int(int(elements[2]) * -3.234200743) # ratio largeur 3,234200743 ( multiplier par -1 pour que carte soit dans le bon sens)
            # Traitement des trois suivants : taxi / bus / métro
            access_taxi = [] if elements[3] == "" else [int(e) for e in elements[3].split('-')]
            access_bus = [] if elements[4] == "" else [int(e) for e in elements[4].split('-')]
            access_subway = [] if elements[5] == "" else [int(e) for e in elements[5].split('-')]
            # Ajout d'une nouvelle instance de Station
            list_box.append(Station(numero, x, y, access_taxi, access_bus, access_subway))              
    except:
        print("FileError")
    return list_box        

def plot_stations(stations):
    """Créer un interface MathPlotLib a partir de la lst de stations"""
    x = [s.dist_x for s in stations]
    y = [s.dist_y for s in stations]
    noms = [s.name for s in stations]

    plt.figure(figsize=(10, 10))
    plt.scatter(x, y, color='blue', s=30)

    for i, name in enumerate(noms):
        plt.text(x[i] + 5, y[i] + 5, str(name), fontsize=6)

    # Connexions taxi (orange)
    for s in stations:
        for dest in s.access_to_taxi:
            s2 = next((t for t in stations if t.name == dest), None)
            if s2:
                plt.plot([s.dist_x, s2.dist_x], [s.dist_y, s2.dist_y],
                         color='orange', linestyle='-', linewidth=0.5)

    plt.title("Carte des stations – Scotland Yard")
    plt.xlabel("x (pixels)")
    plt.ylabel("y (pixels)")
    plt.grid(True)
    plt.show()