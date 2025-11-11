# This Python file uses the following encoding: utf-8
# client.py
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_provisual

class Client(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        f = QFile('formClient.ui')
        f.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(f, self)
        f.close()

        self.db = crud_provisual()
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.editCari.textChanged.connect(self.filterDataClient)

        self.tampilData()

    def filterDataClient(self):
        nama = self.ui.editCari.text()
        tabel = self.ui.tabelClient
        tabel.setRowCount(0)
        data = self.db.filterClient(nama)
        for r, baris in enumerate(data):
            tabel.insertRow(r)
            for c, val in enumerate(baris):
                tabel.setItem(r, c, QTableWidgetItem(str(val)))

    # ==== TAMPIL DATA ====
    def tampilData(self):
        data = self.db.tampilClient()
        tabel = self.ui.tabelClient
        tabel.setRowCount(0)
        for r, row in enumerate(data):
            tabel.insertRow(r)
            for c, val in enumerate(row):
                tabel.setItem(r, c, QTableWidgetItem(str(val)))

    def simpan(self):
        idc = self.ui.editID.text().strip()
        nama = self.ui.editNama.text().strip()
        alamat = self.ui.editAlamat.text().strip()
        telp = self.ui.editTelp.text().strip()
        email = self.ui.editEmail.text().strip()

        if not idc:
            QMessageBox.warning(self, "Validasi Gagal", "ID Client tidak boleh kosong!")
        elif not nama:
            QMessageBox.warning(self, "Validasi Gagal", "Nama tidak boleh kosong!")
        elif not telp:
            QMessageBox.warning(self, "Validasi Gagal", "Nomor telepon tidak boleh kosong!")
        elif not telp.isdigit():
            QMessageBox.warning(self, "Validasi Gagal", "Nomor telepon hanya boleh angka!")
        elif "@" not in email or "." not in email:
            QMessageBox.warning(self, "Validasi Gagal", "Format email tidak valid!")
        else:
            try:
                self.db.simpanClient(idc, nama, alamat, telp, email)
                QMessageBox.information(self, "Sukses", "Data client berhasil disimpan.")
                self.tampilData()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal menyimpan data!\n{str(e)}")

    def ubah(self):
        idc = self.ui.editID.text().strip()
        nama = self.ui.editNama.text().strip()

        if not idc:
            QMessageBox.warning(self, "Peringatan", "Masukkan ID Client yang akan diubah!")
        elif not nama:
            QMessageBox.warning(self, "Peringatan", "Nama tidak boleh kosong!")
        else:
            try:
                self.db.ubahClient(idc, nama, self.ui.editAlamat.text(),
                                   self.ui.editTelp.text(), self.ui.editEmail.text())
                QMessageBox.information(self, "Sukses", "Data client berhasil diubah.")
                self.tampilData()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal mengubah data!\n{str(e)}")

    def hapus(self):
        idc = self.ui.editID.text().strip()

        if not idc:
            QMessageBox.warning(self, "Peringatan", "Masukkan ID Client yang akan dihapus!")
        else:
            try:
                self.db.hapusClient(idc)
                QMessageBox.information(self, "Sukses", "Data client berhasil dihapus.")
                self.tampilData()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal menghapus data!\n{str(e)}")
