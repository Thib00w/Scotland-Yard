from src.utils import init_Station_with_csv, plot_stations

# Créons une version mock de la classe Station pour les tests
class Station:
    def __init__(self, name, dist_x, dist_y, access_to_taxi, access_to_bus, access_to_subway):
        self.name = name
        self.dist_x = dist_x
        self.dist_y = dist_y
        self.access_to_taxi = access_to_taxi
        self.access_to_bus = access_to_bus
        self.access_to_subway = access_to_subway

# On va remplacer temporairement import utils.Station pour le test
from src.utils import Station as utils
utils.Station = Station

def test_init_station_with_csv(tmp_path):
    # Créons un fichier CSV temporaire
    csv_content = """numero;x;y;taxi;bus;metro
1;10;20;2-3;4-5;6
2;30;40;;7-8;"""
    csv_file = tmp_path / "stations.csv"
    csv_file.write_text(csv_content)

    stations = init_Station_with_csv(str(csv_file))
    
    assert len(stations) == 2
    assert stations[0].name == 1
    assert stations[0].dist_x == int(10 * 3.28125)
    assert stations[0].dist_y == int(20 * -3.234200743)
    assert stations[0].access_to_taxi == [2, 3]
    assert stations[1].access_to_taxi == []

def test_plot_stations(monkeypatch):
    # Créons des stations fictives
    stations = [
        Station(1, 0, 0, [2], [], []),
        Station(2, 10, 10, [], [], [])
    ]

    # On patch plt.show pour éviter l'affichage lors des tests
    import matplotlib.pyplot as plt
    monkeypatch.setattr(plt, "show", lambda: None)

    # Appel de la fonction (doit fonctionner sans erreur)
    plot_stations(stations)
