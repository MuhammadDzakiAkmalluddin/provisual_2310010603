# This Python file uses the following encoding: utf-8
# keuangan.py
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_provisual

class Keuangan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        f = QFile('formKeuangan.ui'); f.open(QFile.ReadOnly)
        loader = QUiLoader(); self.ui = loader.load(f, self); f.close()
        self.db = crud_provisual()
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.editCari.textChanged.connect(self.filterDataKeu)
        self.tampilData()

    def filterDataKeu(self):
        keyword = self.ui.editCari.text()
        tabel = self.ui.tabelKeuangan
        tabel.setRowCount(0)
        data = self.db.filterKeu(keyword)
        for r, baris in enumerate(data):
            tabel.insertRow(r)
            for c, val in enumerate(baris):
                tabel.setItem(r, c, QTableWidgetItem(str(val)))

    def tampilData(self):
        data = self.db.tampilKeu()
        tabel = self.ui.tabelKeuangan
        tabel.setRowCount(0)
        for r, row in enumerate(data):
            tabel.insertRow(r)
            for c, val in enumerate(row):
                tabel.setItem(r, c, QTableWidgetItem(str(val)))

    def simpan(self):
        idk = self.ui.editID.text().strip()
        tgl = self.ui.editTanggal.text().strip()
        ket = self.ui.editKeterangan.text().strip()
        jenis = self.ui.comboJenis.currentText().strip()
        jumlah = self.ui.editJumlah.text().strip()

        if not idk:
            QMessageBox.warning(self, "Validasi", "ID Keuangan tidak boleh kosong!")
        elif not tgl:
            QMessageBox.warning(self, "Validasi", "Tanggal transaksi belum diisi!")
        elif not ket:
            QMessageBox.warning(self, "Validasi", "Keterangan tidak boleh kosong!")
        elif not jumlah:
            QMessageBox.warning(self, "Validasi", "Jumlah transaksi belum diisi!")
        else:
            try:
                jumlah = jumlah.replace(".", "").replace(",", ".")
                self.db.simpanKeu(idk, tgl, ket, jenis, jumlah)
                QMessageBox.information(self, "Sukses", "Data keuangan berhasil disimpan.")
                self.tampilData()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal menyimpan data!\n{str(e)}")

    def ubah(self):
        idk = self.ui.editID.text().strip()
        tgl = self.ui.editTanggal.text().strip()
        ket = self.ui.editKeterangan.text().strip()
        jenis = self.ui.comboJenis.currentText().strip()
        jumlah = self.ui.editJumlah.text().strip()

        if not idk:
            QMessageBox.warning(self, "Validasi", "Masukkan ID Keuangan yang ingin diubah!")
        elif not ket:
            QMessageBox.warning(self, "Validasi", "Keterangan tidak boleh kosong!")
        elif not jumlah:
            QMessageBox.warning(self, "Validasi", "Jumlah transaksi belum diisi!")
        else:
            try:
                jumlah = jumlah.replace(".", "").replace(",", ".")
                self.db.ubahKeu(idk, tgl, ket, jenis, jumlah)
                QMessageBox.information(self, "Sukses", "Data keuangan berhasil diubah.")
                self.tampilData()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal mengubah data!\n{str(e)}")

    def hapus(self):
        idk = self.ui.editID.text().strip()
        if not idk:
            QMessageBox.warning(self, "Peringatan", "Masukkan ID Keuangan yang akan dihapus!")
        else:
            try:
                self.db.hapusKeu(idk)
                QMessageBox.information(self, "Sukses", "Data keuangan berhasil dihapus.")
                self.tampilData()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal menghapus data!\n{str(e)}")
