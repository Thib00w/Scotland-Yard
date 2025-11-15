from PyQt5.QtWidgets import QLabel, QPushButton, QGridLayout, QWidget, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

class Ui(QWidget):
    def __init__(self):
        super().__init__()

        # Initialisation Labels
        self.chat_lab = QLabel()
        self.hist_lab = QLabel()
        self.img_lab =QLabel()
        self.txt_chat_lab = QLabel()
        self.button_choice = QLabel()
        pix = QPixmap("Documentation/Capture_decran_du_2025-11-12_16-21-55.png")
        print(pix.width(), pix.height()) 

        # Position en GridLayout
        layout = QGridLayout()
        layout.addWidget(self.hist_lab, 0, 0, 5, 3)
        layout.addWidget(self.chat_lab, 6, 0, 8, 3)
        layout.addWidget(self.txt_chat_lab, 9, 0, 9, 3)
        layout.addWidget(self.img_lab, 0, 4, 5, 10)
        layout.addWidget(self.button_choice, 6, 4, 9, 10)

        # Donne des proprieté au Widgets pour css
        self.chat_lab.setProperty("class", "button")
        self.hist_lab.setProperty("class", "button")
        self.img_lab.setProperty("class", "button")
        self.txt_chat_lab.setProperty("class", "button")
        self.button_choice.setProperty("class", "button")

        # Ouverture du fichier css
        try:
            with open("style.css", "r") as f:
                self.setStyleSheet(f.read())
        except:
            FileNotFoundError 

if "__main__" == __name__:
    app = QApplication(sys.argv)
    ui = Ui()
    ui.show()
    sys.exit(app.exec_())
