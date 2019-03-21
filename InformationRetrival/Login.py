from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import os
from InformationRetrival.Add_Window import Add_Ui
from InformationRetrival.Hide_Window import Hide_Ui


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.title = "Login S(h)URE Search Engine"
        self.setWindowTitle(self.title)
        self.label_name = QtWidgets.QLabel("Admin Name: ")
        self.label_password = QtWidgets.QLabel("Password: ")
        self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label_name)
        layout.addWidget(self.textName)
        layout.addWidget(self.label_password)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        if self.textName.text() == 'admin' and self.textPass.text() == 'admin':
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Bad user or password')


class Admin_Gui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "S(h)URE Search Engine"
        self.setWindowTitle(self.title)
        self.setFixedSize(600, 110)
        menu = QMenuBar()
        self.setMenuBar(menu)
        layout = QtWidgets.QVBoxLayout(self)
        self.buttonAddFile = QtWidgets.QPushButton('Add Files', self)
        self.buttonHideFile = QtWidgets.QPushButton('Hide Files', self)
        self.buttonUnHideFiles = QtWidgets.QPushButton('UnHide Files', self)
        self.buttonAddFile.resize(200, 100)
        self.buttonHideFile.resize(200, 100)
        self.buttonUnHideFiles.resize(200, 100)

        self.buttonAddFile.move(0, 5)
        self.buttonHideFile.move(200, 5)
        self.buttonUnHideFiles.move(400, 5)
        self.setCentralWidget(menu)

        layout.setMenuBar(self.buttonAddFile)
        layout.setMenuBar(self.buttonHideFile)
        layout.setMenuBar(self.buttonUnHideFiles)

        self.buttonAddFile.clicked.connect(self.add_files)
        self.buttonHideFile.clicked.connect(self.hide_files)
        self.buttonUnHideFiles.clicked.connect(self.un_hide_files)

    def add_files(self):
        Add_Ui()

    def hide_files(self):
        Hide_Ui()

    def un_hide_files(self):
        if os.path.isfile('index/hide_index_stoplist.csv'):
            os.remove('index/hide_index_stoplist.csv')
