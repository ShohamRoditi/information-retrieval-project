from PyQt5.QtWidgets import QWidget, QFileDialog
from InformationRetrival.PostingFile import create_posting_file
from InformationRetrival.StorageManager import count_posting_files


class Add_Ui(QWidget):

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
        self.openFileNamesDialog()
        self.show()

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "Add Files", "",
                                                "All Files (*);;Text Files (*.txt)", options=options)
        if files:
            for file in files:
                with open(file, 'r') as new_file:
                    file_name = file.split('/')[::-1]
                    with open("src/" + file_name[0], 'w') as src_file:
                        src_file.write(new_file.read())
            create_posting_file(count_posting_files())
