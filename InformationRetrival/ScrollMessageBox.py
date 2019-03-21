""" When pressed on an item in the result table (gui), open a window which contains the whole file text """

from PyQt5.QtWidgets import *


class ScrollMessageBox(QMessageBox):
    def __init__(self, file_path):
        QMessageBox.__init__(self)
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        self.content = QWidget()
        scroll.setWidget(self.content)
        lay = QVBoxLayout(self.content)
        with open(file_path, 'r') as f:
            file_content = f.read()
            self.label = QLabel(file_content, self)
        lay.addWidget(self.label)
        self.layout().addWidget(scroll, 0, 0, 1, self.layout().columnCount())
        self.setWindowTitle(file_path.split('.')[1])
        self.setStyleSheet("QScrollArea{min-width:400 px; min-height: 400px}")
