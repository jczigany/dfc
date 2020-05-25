from PySide2.QtCore import Slot


def create_slots(self):
    @Slot()
    # def exit_app(self, checked):
    def exit_app(self):
        QApplication.quit()


    @Slot()
    def new_player(self):
        print("Új játékos dialog")


    @Slot()
    def new_team(self):
        print("Új Csapat dialog")