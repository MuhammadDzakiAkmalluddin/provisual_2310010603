# This Python file uses the following encoding: utf-8
# arsip.py
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_provisual

class Arsip(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        f = QFile('formArsip.ui'); f.open(QFile.ReadOnly)
        loader = QUiLoader(); self.ui = loader.load(f, self); f.close()
        self.db = crud_provisual()
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.editCari.textChanged.connect(self.filterDataArsip)
        self.tampilData()

    def filterDataArsip(self):
        keyword = self.ui.editCari.text()
        tabel = self.ui.tabelArsip
        tabel.setRowCount(0)
        data = self.db.filterArsip(keyword)
        for r, baris in enumerate(data):
            tabel.insertRow(r)
            for c, val in enumerate(baris):
                tabel.setItem(r, c, QTableWidgetItem(str(val)))

    def tampilData(self):
        data = self.db.tampilArsip()
        tabel = self.ui.tabelArsip
        tabel.setRowCount(0)
        for r, row in enumerate(data):
            tabel.insertRow(r)
            for c, val in enumerate(row):
                tabel.setItem(r, c, QTableWidgetItem(str(val)))

    def simpan(self):
        ida = self.ui.editID.text().strip()
        nosurat = self.ui.editNomor.text().strip()
        judul = self.ui.editJudul.text().strip()
        tgl = self.ui.editTanggal.text().strip()
        lokasi = self.ui.editLokasi.text().strip()

        if not ida:
            QMessageBox.warning(self, "Validasi", "ID Arsip tidak boleh kosong!")
        elif not nosurat:
            QMessageBox.warning(self, "Validasi", "Nomor surat tidak boleh kosong!")
        elif not judul:
            QMessageBox.warning(self, "Validasi", "Judul arsip harus diisi!")
        elif not tgl:
            QMessageBox.warning(self, "Validasi", "Tanggal arsip belum diisi!")
        elif not lokasi:
            QMessageBox.warning(self, "Validasi", "Lokasi penyimpanan tidak boleh kosong!")
        else:
            try:
                self.db.simpanArsip(ida, nosurat, judul, tgl, lokasi)
                QMessageBox.information(self, "Sukses", "Data arsip berhasil disimpan.")
                self.tampilData()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal menyimpan data!\n{str(e)}")

    def ubah(self):
        ida = self.ui.editID.text().strip()
        nosurat = self.ui.editNomor.text().strip()
        judul = self.ui.editJudul.text().strip()
        tgl = self.ui.editTanggal.text().strip()
        lokasi = self.ui.editLokasi.text().strip()

        if not ida:
            QMessageBox.warning(self, "Validasi", "Masukkan ID Arsip yang ingin diubah!")
        elif not nosurat:
            QMessageBox.warning(self, "Validasi", "Nomor surat tidak boleh kosong!")
        elif not judul:
            QMessageBox.warning(self, "Validasi", "Judul arsip belum diisi!")
        else:
            try:
                self.db.ubahArsip(ida, nosurat, judul, tgl, lokasi)
                QMessageBox.information(self, "Sukses", "Data arsip berhasil diubah.")
                self.tampilData()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal mengubah data!\n{str(e)}")

    def hapus(self):
        ida = self.ui.editID.text().strip()
        if not ida:
            QMessageBox.warning(self, "Peringatan", "Masukkan ID Arsip yang akan dihapus!")
        else:
            try:
                self.db.hapusArsip(ida)
                QMessageBox.information(self, "Sukses", "Data arsip berhasil dihapus.")
                self.tampilData()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal menghapus data!\n{str(e)}")
