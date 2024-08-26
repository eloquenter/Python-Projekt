import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Erstellen eines zentralen Widgets und Layouts
        self.central_widget = QWidget()
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        # Initialisieren der ersten Seite
        self.current_page = None
        self.show_startseite()

    def load_ui(self, ui_file):
        # Lädt eine .ui-Datei und gibt das Widget zurück
        widget = QWidget()
        uic.loadUi(ui_file, widget)
        return widget

    def show_startseite(self):
        if self.current_page:
            self.current_page.hide()

        self.current_page = self.load_ui("./gui/ui/startseite.ui")
        self.layout.addWidget(self.current_page)
        self.current_page.show()

    def show_spielseite(self):
        if self.current_page:
            self.current_page.hide()

        self.current_page = self.load_ui("spielseite.ui")
        self.layout.addWidget(self.current_page)
        self.current_page.show()

        # Verbinden von Buttons oder anderen Elementen
        end_button = self.current_page.findChild(QWidget, "endButton")
        end_button.clicked.connect(self.show_endseite)

    def show_endseite(self):
        if self.current_page:
            self.current_page.hide()

        self.current_page = self.load_ui("endseite.ui")
        self.layout.addWidget(self.current_page)
        self.current_page.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
