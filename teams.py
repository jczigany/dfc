from datetime import datetime

from PySide2.QtGui import QIcon

from database.db import MysqlClient
# from PySide2.QtGui import QColor, QIcon
from PySide2.QtWidgets import QMainWindow, QTableView, QWidget, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, \
    QFormLayout, QDialog, QLineEdit, QDialogButtonBox, QAction, QSpacerItem, QSizePolicy
from PySide2.QtCore import QAbstractTableModel, Qt, QRect
from PySide2.QtCore import *
from menus import create_menus
from modell import TableModel





class manageTeams(QMainWindow):
    def __init__(self, parent):
        super(manageTeams, self).__init__(parent)
        self.setWindowTitle("Csapatok kezelése")
        widget = QWidget()
        main_layout = QHBoxLayout()
        widget.setLayout(main_layout)

        self.setCentralWidget(widget)
        self.client = MysqlClient()
        self.table_view = QTableView()
        # a megjelenített tábla neve
        self.table_name = "team"

        main_layout.addWidget(self.table_view)
        fejlec = ['id', "Csapat neve", "Rövid név "]
        self.model = TableModel(self.table_name, fejlec)
        # self.model = TableModel(self.table_name)
        # print(self.model.fejlec)

        self.table_view.setModel(self.model)
        self.table_view.setSortingEnabled(True)
        # Az első oszlop (id) elrejtése
        self.table_view.hideColumn(0)
        self.table_view.resizeColumnsToContents()

        gomb_layout = QVBoxLayout()
        main_layout.addLayout(gomb_layout)

        self.delete_button = QPushButton("&Delete Record")
        self.add_button = QPushButton("&Add New Record")
        self.modify_button = QPushButton("&Modify Record")

        gomb_layout.addWidget(self.delete_button)
        gomb_layout.addWidget(self.add_button)
        gomb_layout.addWidget(self.modify_button)
        self.space = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        gomb_layout.addItem(self.space)

        # self.resize(320, 200)
        self.setFixedSize(320, 200)
        self.setWindowFlags(Qt.Window|Qt.WindowTitleHint)
        tb = self.addToolBar("File")

        exit = QAction(QIcon("images/door--arrow.png"), "Kilépés", self)
        tb.actionTriggered[QAction].connect(self.toolbarpressed)
        tb.addAction(exit)

        self.delete_button.clicked.connect(lambda: self.model.delete(self.table_view.selectedIndexes()[0]))
        self.add_button.clicked.connect(self.model.add)
        # self.modify_button.clicked.connect(self.modify)

    def toolbarpressed(self, a):
        print("Pressed:", a.text())
        if a.text() == "Kilépés":
            self.close()