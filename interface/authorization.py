from PyQt6 import QtCore, QtWidgets

from interface.registration import Registration
from database.request import authorization


class Authorization(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Авторизация")
        self.setFixedSize(292, 98)
        
        self.setupUi() # инициализация интерфейса
    
    
    def setupUi(self):
        """Инициализация интерфейса"""

        # Выравнивание по центу
        central_widget = QtWidgets.QWidget(parent=self)
        gridLayout_central = QtWidgets.QGridLayout(central_widget)

        # Сетка
        gridLayout = QtWidgets.QGridLayout()

        # Логин
        label_login = QtWidgets.QLabel(parent=central_widget)
        label_login.setText("Логин:")
        gridLayout.addWidget(label_login, 0, 0, 1, 1)
        
        lineEdit_login = QtWidgets.QLineEdit(parent=central_widget)
        gridLayout.addWidget(lineEdit_login, 0, 1, 1, 1)
        
        # Пароль
        label_password = QtWidgets.QLabel(parent=central_widget)
        label_password.setText("Пароль:")
        gridLayout.addWidget(label_password, 1, 0, 1, 1)
  
        lineEdit_password = QtWidgets.QLineEdit(parent=central_widget)
        gridLayout.addWidget(lineEdit_password, 1, 1, 1, 1)
        
        # кнопки
        buttons_container = QtWidgets.QHBoxLayout()
        
        btn_login = QtWidgets.QPushButton(parent=central_widget)
        btn_login.setText("Войти")
        btn_login.clicked.connect(lambda: self.req_authorization(lineEdit_login.text(), lineEdit_password.text()))
        buttons_container.addWidget(btn_login, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        
        btn_reg = QtWidgets.QPushButton(parent=central_widget)
        btn_reg.setText("Зарегистрироваться")
        btn_reg.clicked.connect(lambda: self.open_registration())
        buttons_container.addWidget(btn_reg, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        
        gridLayout.addLayout(buttons_container, 2, 0, 1, 2)
        
        # Размещение элементов в интерфейс
        gridLayout_central.addLayout(gridLayout, 0, 0, 1, 1)
        self.setCentralWidget(central_widget)
        
    def req_authorization(self, login, password):
        """Авторизация"""
        
        result = authorization(login, password)
        print(result)
        
    def open_registration(self):
        """Открытие окна регистрации"""
        
        self.wdindow_reg = Registration(self)
        self.close()