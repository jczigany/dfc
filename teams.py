from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QTableView, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, \
    QAction, QSpacerItem, QSizePolicy, QMessageBox
from PySide2.QtCore import *
from modell import TableModel
from database.db import MysqlClient

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

        self.delete_button = QPushButton("&Csapat törlése")
        self.add_button = QPushButton("&Új csapat")
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

        # self.delete_button.clicked.connect(lambda: self.model.delete(self.table_view.selectedIndexes()[0]))
        self.delete_button.clicked.connect(self.csapat_torles)
        self.add_button.clicked.connect(self.model.add)
        # self.modify_button.clicked.connect(self.modify)

    def csapat_torles(self):
        if len(self.table_view.selectedIndexes()) > 0:
            self.model.delete(self.table_view.selectedIndexes()[0])
        else:
            reply = QMessageBox.question(None, 'Hiba!', 'Törlés előtt válasszon csapatot!', QMessageBox.Ok)

    def toolbarpressed(self, a):
        print("Pressed:", a.text())
        if a.text() == "Kilépés":
            self.close()