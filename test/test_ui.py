import pytest
from PyQt5.QtWidgets import QApplication
from src.ui import Ui

@pytest.fixture(scope="session")
def app():
    """Fixture pour créer l'application PyQt une seule fois."""
    app = QApplication([])
    return app

def test_ui_creation(app):
    """Test que l'UI se crée correctement."""
    ui = Ui()
    assert ui is not None
    assert ui.isVisible() == False  # La fenêtre n'est pas encore affichée
