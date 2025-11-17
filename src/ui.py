from PyQt5.QtWidgets import QLabel, QPushButton, QGridLayout, QWidget, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from utils import plot_stations, stations
import matplotlib.image as mpimg

class CanvasWidget(QWidget):
    def __init__(self, canvas, img_width, img_height):
        super().__init__()
        self.canvas = canvas
        self.img_ratio = img_width / img_height
        layout = QGridLayout()
        layout.addWidget(self.canvas)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def resizeEvent(self, event):
        w = self.width()
        h = self.height()
        # calculer nouvelle taille pour garder le ratio
        if w / h > self.img_ratio:
            # largeur trop grande → ajuster la largeur
            new_w = int(h * self.img_ratio)
            new_h = h
        else:
            # hauteur trop grande → ajuster la hauteur
            new_w = w
            new_h = int(w / self.img_ratio)
        self.canvas.resize(new_w, new_h)
        super().resizeEvent(event)


class Ui(QWidget):
    def __init__(self):
        super().__init__()

        # Initialisation Labels
        self.chat_lab = QLabel()
        self.hist_lab = QLabel()
        self.txt_chat_lab = QLabel()
        self.button_choice = QLabel()

        # Initialisation Plateau de jeu
        self.ratio_img = 1155/870  
        self.figure = Figure()      # crée une figure Matplotlib
        self.canvas = FigureCanvas(self.figure)  # transforme la figure en widget Qt
        ax = self.figure.add_subplot(111) # ajoute un subplot pour dessiner
        img = mpimg.imread("../data/Plateau.png")  
        img_height, img_width = img.shape[:2] # récupère dimensions image
        ax.imshow(img, origin='upper') # affiche l'image sur le subplot
        plot_stations(stations, ax) # trace les stations sur l'image
            # Supprime les marges et les axes
        self.figure.subplots_adjust(left=0, right=1, top=1, bottom=0)
        ax.set_axis_off()                      
        self.canvas.draw() 
        self.canvas.update()
        self.canvas_widget = CanvasWidget(self.canvas, img_width, img_height)  # gère ratio


        # Position en GridLayout
        layout = QGridLayout()
        layout.addWidget(self.hist_lab, 0, 0, 5, 3)
        layout.addWidget(self.chat_lab, 6, 0, 8, 3)
        layout.addWidget(self.txt_chat_lab, 9, 0, 9, 3)
        layout.addWidget(self.canvas_widget, 0, 4, 5, 10)
        layout.addWidget(self.button_choice, 6, 4, 9, 10)
        self.setLayout(layout)

        # Ouverture du fichier css
        try:
            with open("style.css", "r") as f:
                self.setStyleSheet(f.read())
        except:
            FileNotFoundError 

        # Donne des proprieté au Widgets pour css
        self.chat_lab.setProperty("class", "button")
        self.hist_lab.setProperty("class", "button")
        self.txt_chat_lab.setProperty("class", "button")
        self.button_choice.setProperty("class", "button")

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())