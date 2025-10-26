# Creation class box [name, x, y, access_to_taxi, access_to_bus, access_to_subway]

class Station:
    """Définir la classe qui permettra d’implémenter les stations, ses attributs sont :
            numero_station : int ;
            x_en_pixels : int ;
            y_en_pixels : int ;
            accessibles_taxi : list;
            accessibles_bus : list ;
            accessibles_metro : list ;
    """
    def __init__(self, name: int = None, x: int = None, y: int = None, access_to_taxi: list = None, 
                 access_to_bus: list = None, access_to_subway: list = None):
        self.name = name
        self.dist_x = x
        self.dist_y = y
        self.access_to_taxi = access_to_taxi
        self.access_to_bus = access_to_bus
        self.access_to_subway = access_to_subway

    def __repr__(self):
        affichage = f"The Station {self.name}: \n-x position: {self.dist_x}\n-y position: {self.dist_y}\n-Accessible taxi station: {self.access_to_taxi}\n-Accessible bus station: {self.access_to_bus}\n-Accessible subway station: {self.access_to_subway}\n"
        return affichage