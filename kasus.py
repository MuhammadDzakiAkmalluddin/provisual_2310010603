# This Python file uses the following encoding: utf-8
# kasus.py
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_provisual
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

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
        self.ui.btnPrint.clicked.connect(self.cetakPDF)
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

    def cetakPDF(self):
        filename = "laporan_kasus.pdf"

        tabel = self.ui.tabelKasus
        rows = tabel.rowCount()
        cols = tabel.columnCount()

        # Header tabel
        data = [[tabel.horizontalHeaderItem(c).text() for c in range(cols)]]

        # Isi tabel
        for r in range(rows):
            row_data = []
            for c in range(cols):
                item = tabel.item(r, c)
                row_data.append(item.text() if item else "")
            data.append(row_data)

        # PDF ReportLab
        pdf = SimpleDocTemplate(filename, pagesize=A4)
        table = Table(data)

        style = TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ])
        table.setStyle(style)

        # Simpan PDF
        try:
            pdf.build([table])
            QMessageBox.information(self, "Print PDF", f"Laporan berhasil dicetak:\n{filename}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal mencetak PDF!\n{str(e)}")
