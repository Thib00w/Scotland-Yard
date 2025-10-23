# Creation class box [name, x, y, access_to_taxi, access_to_bus, access_to_subway]

class box:
    """Définir la classe qui permettra d’implémenter les stations, ses attributs sont :
            numero_station : int ;
            x_en_pixels : int ;
            y_en_pixels : int ;
            accessibles_taxi : list;
            accessibles_bus : list ;
            accessibles_metro : list ;
    """
    def __init__(self, name: str, x: int, y: int, access_to_taxi: list, access_to_bus: list, access_to_subway: list):
        self.name = name
        self.dist_x = x
        self.dist_y = y
        self.access_to_taxi = access_to_taxi
        self.access_to_bus = access_to_bus
        self.access_to_subway = access_to_subway

    #TODO: Modifier __repr__ pour + lisibilité
    def init_with_csv(self, file):
        pass 

if "__main__" == __name__:
    pass