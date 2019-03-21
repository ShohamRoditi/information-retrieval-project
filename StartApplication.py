import sys
from PyQt5.QtWidgets import QApplication
from InformationRetrival.gui_test import App
from InformationRetrival.PostingFile import create_posting_file
from InformationRetrival.StorageManager import count_posting_files, check_index_existence


def main():
    check_index_existence()
    amount_of_files = count_posting_files()
    create_posting_file(amount_of_files)
    app = QApplication(sys.argv)
    App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
