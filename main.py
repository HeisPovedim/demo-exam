import sys
from PyQt6 import QtWidgets
from interface.authorization import Authorization

if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    window = Authorization()
    window.show()
    sys.exit(app.exec())
    