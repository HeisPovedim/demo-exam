from PyQt6 import QtWidgets

class ErrorMessageBox(QtWidgets.QMainWindow):
    def __init__(self, title, message):
        super().__init__()
        
        QtWidgets.QMessageBox.warning(self, title, message)
        
        self.show()