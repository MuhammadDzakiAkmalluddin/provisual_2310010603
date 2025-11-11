# This Python file uses the following encoding: utf-8
# kasus.py
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_provisual

class Kasus(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        f = QFile('formKasus.ui'); f.open(QFile.ReadOnly)
        loader = QUiLoader(); self.ui = loader.load(f, self); f.close()

        self.db = crud_provisual()
        self.isiComboClient()
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.editCari.textChanged.connect(self.filterDataKasus)
        self.tampilData()

    def isiComboClient(self):
        try:
            data_client = self.db.tampilClient()
            self.ui.comboClient.clear()
            for row in data_client:
                id_client = str(row[0])
                nama_client = str(row[1])
                self.ui.comboClient.addItem(f"{id_client} - {nama_client}", id_client)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal memuat daftar client!\n{str(e)}")

    def filterDataKasus(self):
        keyword = self.ui.editCari.text()
        tabel = self.ui.tabelKasus
        tabel.setRowCount(0)
        data = self.db.filterKasus(keyword)
        for r, baris in enumerate(data):
            tabel.insertRow(r)
            for c, val in enumerate(baris):
                tabel.setItem(r, c, QTableWidgetItem(str(val)))

    def tampilData(self):
        data = self.db.tampilKasus()
        tabel = self.ui.tabelKasus
        tabel.setRowCount(0)
        for r, row in enumerate(data):
            tabel.insertRow(r)
            for c, val in enumerate(row):
                tabel.setItem(r, c, QTableWidgetItem(str(val)))

    def simpan(self):
        idk = self.ui.editID.text().strip()
        id_client = self.ui.comboClient.currentData()
        judul = self.ui.editJudul.text().strip()
        uraian = self.ui.editUraian.toPlainText().strip()
        tgl = self.ui.editTanggal.text().strip()

        if not idk:
            QMessageBox.warning(self, "Validasi", "ID Kasus tidak boleh kosong!")
        elif not id_client:
            QMessageBox.warning(self, "Validasi", "Pilih ID Client terlebih dahulu!")
        elif not judul:
            QMessageBox.warning(self, "Validasi", "Judul kasus tidak boleh kosong!")
        elif not tgl:
            QMessageBox.warning(self, "Validasi", "Tanggal masuk tidak boleh kosong!")
        else:
            try:
                self.db.simpanKasus(idk, id_client, judul, uraian, tgl)
                QMessageBox.information(self, "Sukses", "Data kasus berhasil disimpan.")
                self.tampilData()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal menyimpan data!\n{str(e)}")

    def ubah(self):
        idk = self.ui.editID.text().strip()
        id_client = self.ui.comboClient.currentData()
        judul = self.ui.editJudul.text().strip()
        uraian = self.ui.editUraian.toPlainText().strip()
        tgl = self.ui.editTanggal.text().strip()

        if not idk:
            QMessageBox.warning(self, "Validasi", "Masukkan ID Kasus yang akan diubah!")
        elif not id_client:
            QMessageBox.warning(self, "Validasi", "Pilih ID Client terlebih dahulu!")
        elif not judul:
            QMessageBox.warning(self, "Validasi", "Judul kasus tidak boleh kosong!")
        else:
            try:
                self.db.ubahKasus(idk, id_client, judul, uraian, tgl)
                QMessageBox.information(self, "Sukses", "Data kasus berhasil diubah.")
                self.tampilData()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal mengubah data!\n{str(e)}")

    def hapus(self):
        idk = self.ui.editID.text().strip()
        if not idk:
            QMessageBox.warning(self, "Peringatan", "Masukkan ID Kasus yang akan dihapus!")
        else:
            try:
                self.db.hapusKasus(idk)
                QMessageBox.information(self, "Sukses", "Data kasus berhasil dihapus.")
                self.tampilData()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal menghapus data!\n{str(e)}")
