from PyQt5.QtWidgets import *
import pandas as pd


class Hide_Ui(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Add files to the index'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.hide_files_dialog()
        self.show()

    def hide_files_dialog(self):
        list_to_hide = []
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "Hide Files", "storage/",
                                                "Text Files (*.txt)", options=options)
        for file in files:
            file_to_hide = file.split('/')[-1]
            file_no = file_to_hide.split('.')[0]
            list_to_hide.append(file_no)

        df_stoplist = pd.read_csv('index/index_stoplist.csv')

        for hide in list_to_hide:
            df_stoplist['Doc Location'] = df_stoplist['Doc Location'].str.replace(hide, '')
        df_stoplist.to_csv('index/hide_index_stoplist.csv', index=False)
