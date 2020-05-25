from datetime import datetime

from PySide2.QtGui import QIcon

from database.db import MysqlClient
# from PySide2.QtGui import QColor, QIcon
from PySide2.QtWidgets import QMainWindow, QTableView, QWidget, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, \
    QFormLayout, QDialog, QLineEdit, QDialogButtonBox, QAction
from PySide2.QtCore import QAbstractTableModel, Qt, QRect
from PySide2.QtCore import *
from menus import create_menus
from modell import TableModel

class manageTeams(QMainWindow):
    def __init__(self, parent):
        super(manageTeams, self).__init__(parent)

        widget = QWidget()
        main_layout = QVBoxLayout()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        self.client = MysqlClient()
        self.table_view = QTableView()
        # a megjelenített tábla neve
        self.table_name = "players"

        main_layout.addWidget(self.table_view)

        self.model = TableModel(self.table_name)

        self.table_view.setModel(self.model)
        self.table_view.setSortingEnabled(True)
        # Az első oszlop (id) elrejtése
        self.table_view.hideColumn(0)

        self.resize(400, 250)
        tb = self.addToolBar("File")

        exit = QAction(QIcon("images/filenew.png"), "Kilépés", self)
        tb.actionTriggered[QAction].connect(self.toolbarpressed)
        tb.addAction(exit)

    def toolbarpressed(self, a):
        print("Pressed:", a.text())
        if a.text() == "Kilépés":
            self.close()