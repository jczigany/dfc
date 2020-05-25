from PySide2.QtWidgets import QAction

def create_menus(self):
    # Menu
    self.menu = self.menuBar()
    # File menü
    self.file_menu = self.menu.addMenu("File")

    # Exit action
    exit_action = QAction("Kilépés", self)
    exit_action.setShortcut("Ctrl+Q")
    exit_action.triggered.connect(self.exit_app)
    self.file_menu.addAction(exit_action)

    # Szerkesztés menü
    self.edit_menu = self.menu.addMenu("Szerkesztés")

    # Gyakorlás menü
    self.practice_menu = self.menu.addMenu("Gyakorlás")

    # Eszközök menü
    self.tools_menu = self.menu.addMenu("Eszközök")

    # Új Játékos action
    new_player_action = QAction("Új Játékos", self)
    new_player_action.setShortcut("Ctrl+P")
    new_player_action.triggered.connect(self.new_player)
    self.tools_menu.addAction(new_player_action)

    # Új Csapat action
    new_team_action = QAction("Új Csapat", self)
    new_team_action.setShortcut("Ctrl+T")
    new_team_action.triggered.connect(self.new_team)
    self.tools_menu.addAction(new_team_action)

    # Nézet menü
    self.view_menu = self.menu.addMenu("Nézet")

    # Beállítások menü
    self.settings_menu = self.menu.addMenu("Beállítások")

    # Adatbázis menü
    self.database_menu = self.menu.addMenu("Adatbázis")

    # Segítség menü
    self.help_menu = self.menu.addMenu("Segítség")

