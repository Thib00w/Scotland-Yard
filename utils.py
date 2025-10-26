from classes import Station

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
            x = int(elements[1])
            y = int(elements[2])
            # Traitement des trois suivants : taxi / bus / métro
            def parse_access(field: str):
                # Si vide → liste vide
                if field == "":
                    return []
                # sinon → découpe les numéros séparés par des tirets
                return [int(e) for e in field.split('–')]
            access_taxi = parse_access(elements[3])
            access_bus = parse_access(elements[4])
            access_subway = parse_access(elements[5])
            # Ajout d'une nouvelle instance de Station
            list_box.append(Station(numero, x, y, access_taxi, access_bus, access_subway))              
    except:
        print("FileError")
    
    return list_box        

if "__main__" == __name__:
    stations = init_Station_with_csv("station.csv")
    for list in stations:
        print('---------------------------')
        print(list)
        print('---------------------------')