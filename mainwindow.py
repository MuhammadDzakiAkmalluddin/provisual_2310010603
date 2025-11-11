# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from client import Client
from kasus import Kasus
from arsip import Arsip
from keuangan import Keuangan


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # === Muat file UI utama ===
        filenya = QFile('form.ui')
        filenya.open(QFile.ReadOnly)

        muatFile = QUiLoader()
        self.formMenu = muatFile.load(filenya, self)
        filenya.close()

        # === Atur ukuran & menu bar ===
        self.resize(self.formMenu.size())
        self.setMenuBar(self.formMenu.menuBar())

        # === Hubungkan menu ke form masing-masing ===
        self.formMenu.actionData_Client.triggered.connect(self.bukaFormClient)
        self.formMenu.actionData_Kasus.triggered.connect(self.bukaFormKasus)
        self.formMenu.actionData_Arsip.triggered.connect(self.bukaFormArsip)
        self.formMenu.actionData_Keuangan.triggered.connect(self.bukaFormKeuangan)

    # === Fungsi untuk membuka setiap form ===
    def bukaFormClient(self):
        self.tampilClient = Client()
        self.tampilClient.show()

    def bukaFormKasus(self):
        self.tampilKasus = Kasus()
        self.tampilKasus.show()

    def bukaFormArsip(self):
        self.tampilArsip = Arsip()
        self.tampilArsip.show()

    def bukaFormKeuangan(self):
        self.tampilKeuangan = Keuangan()
        self.tampilKeuangan.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
