import sys
from InformationRetrival.Login import *
from InformationRetrival.QueryParser import process_query
from InformationRetrival.ScrollMessageBox import ScrollMessageBox


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "S(h)URE Search Engine"
        self.is_admin()

    def is_admin(self):
        msgbox = QMessageBox(QMessageBox.Question, "S(h)URE Search Engine", "WELCOME TO S(h)URE SEARCH ENGINE\nAre you admin ?")
        msgbox.addButton(QMessageBox.Yes)
        msgbox.addButton(QMessageBox.No)
        msgbox.addButton(QMessageBox.Cancel)
        reply = msgbox.exec_()

        if reply == QMessageBox.No:
            self.initUI()
            app = QApplication(sys.argv)
            sys.exit(app.exec_())

        elif reply == QMessageBox.Cancel:
            sys.exit(reply)

        if reply == QMessageBox.Yes:
            app = QtWidgets.QApplication(sys.argv)
            login = Login()

            if login.exec_() == QtWidgets.QDialog.Accepted:
                admin = Admin_Gui()
                admin.show()
                sys.exit(app.exec_())

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(800, 600)
        grid = QGridLayout(self)

        top_box = QHBoxLayout(self)
        search_group = QGroupBox("S(h)URE Search Engine", self)
        search_group.setAlignment(5)
        search_box = QVBoxLayout(search_group)
        self.search_field = QLineEdit(self)
        self.search_field.returnPressed.connect(self.load_table_content)
        search_button = QPushButton('Search', self)
        search_box.addWidget(self.search_field)
        search_box.addWidget(search_button)
        top_box.addWidget(search_group)

        bot_box = QHBoxLayout(self)
        bot_box.setContentsMargins(5, 5, 5, 5)
        result_group = QGroupBox("Your results", self)
        table_layout = QVBoxLayout(result_group)
        self.table = QTableWidget()
        """connect the button to the function """
        search_button.clicked.connect(self.load_table_content)
        self.table.setColumnCount(3)

        self.table.setHorizontalHeaderLabels(["No.", "File", "Description"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.table.setColumnWidth(0, 40)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 410)

        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.doubleClicked.connect(self.open_selected_file)
        table_layout.addWidget(self.table)

        bot_box.addWidget(result_group)

        help_button = QPushButton('help', self)
        help_button.clicked.connect(self.open_manual)
        grid.addWidget(help_button, 0, 1)
        grid.addLayout(top_box, 0, 0)
        grid.addLayout(bot_box, 1, 0)
        self.show()

    def load_table_content(self):
        # bolded_items_list = []
        storage_dir = os.listdir("storage/")
        posting_files_list = []
        posting_files_number = []
        for files in storage_dir:
            posting_files_list.append(files)
        for file in posting_files_list:
            posting_files_number.append(file.split('.')[0])
        files_to_present = ''
        if self.search_field.text():
            files_to_present = process_query(self.search_field.text())
            # files_to_present, bolded_items_list = process_query(self.search_field.text(), bolded_items_list)
        if files_to_present == 'Not Found' or not files_to_present or files_to_present[0] == 'nan':
            # if files_to_present == 'Not Found' or not files_to_present:
            """ open a message box """
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Not Fount")
            msg.setInformativeText('Please Try To Search Another Word')
            msg.setWindowTitle("Shoham and Uri's Search Engine")
            msg.exec_()
            return
        not_found_files = files_to_present[::-1]
        for file in files_to_present:
            if file == 'nan':
                not_found_files.remove('nan')
            elif file == '':
                not_found_files.remove('')
        files_to_present = not_found_files[::-1]
        rows_amount = len(files_to_present)
        self.table.setRowCount(rows_amount)
        i = 0
        for file in files_to_present:
            for files in posting_files_list:
                if file == files.split('.')[0]:
                    self.table.setRowHeight(i, 100)
                    item = QTableWidgetItem(files.split('.')[0])
                    item.setTextAlignment(132)
                    self.table.setItem(i, 0, item)
                    item = QTableWidgetItem(files.split('.')[1])
                    item.setTextAlignment(132)
                    self.table.setItem(i, 1, item)
                    with open("storage/" + files, 'r') as f:
                        description = f.read(280)
                    description = description.replace('\n', ' ')
                    # for bolded_term in bolded_items_list:
                    #     if description.find(bolded_term) == -1:
                    #         description = description.replace(bolded_term, '<b>' + bolded_term + '</b>')
                    item = QTableWidgetItem(description + ' ...')
                    item.setTextAlignment(132)
                    self.table.setItem(i, 2, item)
                    i += 1

    def open_selected_file(self):
        file_name = ''
        for currentItem in self.table.selectedItems():
            selected_file_number = self.table.item(currentItem.row(), 0)
            selected_file_name = self.table.item(currentItem.row(), 1)
            file_name = 'storage/' + selected_file_number.text() + '.' + selected_file_name.text() + '.txt'
        txt = ScrollMessageBox(file_name)
        txt.exec_()

    def open_manual(self):
        help_file = ScrollMessageBox('help.help')
        help_file.exec_()
