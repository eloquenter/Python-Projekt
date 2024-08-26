import sys
from PyQt5.QtWidgets import QApplication

from gui.handler.mainHandler import MainHandler

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainHandler()
    window.resize(900, 700)
    window.show()
    sys.exit(app.exec_())


# TODO Dices have to be a button to be locked
# TODO Progress bar func to go with round number
