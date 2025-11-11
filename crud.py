# This Python file uses the following encoding: utf-8
import mysql.connector

class crud_provisual:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dbvisual3_2310010603'
        )

    def simpanClient(self, idc, nama, alamat, telepon, email):
        cur = self.koneksi.cursor()
        cur.execute("INSERT INTO client (IDClient, Nama, Alamat, Telepon, Email) VALUES (%s,%s,%s,%s,%s)",
                    (idc, nama, alamat, telepon, email))
        self.koneksi.commit()
        cur.close()

    def ubahClient(self, idc, nama, alamat, telepon, email):
        cur = self.koneksi.cursor()
        cur.execute("UPDATE client SET Nama=%s, Alamat=%s, Telepon=%s, Email=%s WHERE IDClient=%s",
                    (nama, alamat, telepon, email, idc))
        self.koneksi.commit()
        cur.close()

    def hapusClient(self, idc):
        cur = self.koneksi.cursor()
        cur.execute("DELETE FROM client WHERE IDClient=%s", (idc,))
        self.koneksi.commit()
        cur.close()

    def tampilClient(self):
        cur = self.koneksi.cursor()
        cur.execute("SELECT IDClient, Nama, Alamat, Telepon, Email FROM client")
        rows = cur.fetchall()
        cur.close()
        return rows

    def filterClient(self, cari):
        cur = self.koneksi.cursor()
        cur.execute("SELECT * FROM client WHERE Nama LIKE %s", (f"%{cari}%",))
        return cur.fetchall()


    def simpanKasus(self, idk, idclient, judul, uraian, tgl):
        cur = self.koneksi.cursor()
        cur.execute("INSERT INTO kasus (IDKasus, IDClient, JudulKasus, Uraian, TanggalMasuk) VALUES (%s,%s,%s,%s,%s)",
                    (idk, idclient, judul, uraian, tgl))
        self.koneksi.commit()
        cur.close()

    def ubahKasus(self, idk, idclient, judul, uraian, tgl):
        cur = self.koneksi.cursor()
        cur.execute("UPDATE kasus SET IDClient=%s, JudulKasus=%s, Uraian=%s, TanggalMasuk=%s WHERE IDKasus=%s",
                    (idclient, judul, uraian, tgl, idk))
        self.koneksi.commit()
        cur.close()

    def hapusKasus(self, idk):
        cur = self.koneksi.cursor()
        cur.execute("DELETE FROM kasus WHERE IDKasus=%s", (idk,))
        self.koneksi.commit()
        cur.close()

    def tampilKasus(self):
        cur = self.koneksi.cursor()
        cur.execute("SELECT IDKasus, IDClient, JudulKasus, Uraian, TanggalMasuk FROM kasus")
        rows = cur.fetchall()
        cur.close()
        return rows

    def filterKasus(self, cari):
        cur = self.koneksi.cursor()
        cur.execute("SELECT * FROM kasus WHERE JudulKasus LIKE %s OR Uraian LIKE %s",
                    (f"%{cari}%", f"%{cari}%"))
        rows = cur.fetchall()
        cur.close()
        return rows

    def simpanArsip(self, ida, nosurat, judul, tgl, lokasi):
        cur = self.koneksi.cursor()
        cur.execute("INSERT INTO arsip (IDArsip, NomorSurat, Judul, Tanggal, LokasiPenyimpanan) VALUES (%s,%s,%s,%s,%s)",
                    (ida, nosurat, judul, tgl, lokasi))
        self.koneksi.commit()
        cur.close()

    def ubahArsip(self, ida, nosurat, judul, tgl, lokasi):
        cur = self.koneksi.cursor()
        cur.execute("UPDATE arsip SET NomorSurat=%s, Judul=%s, Tanggal=%s, LokasiPenyimpanan=%s WHERE IDArsip=%s",
                    (nosurat, judul, tgl, lokasi, ida))
        self.koneksi.commit()
        cur.close()

    def hapusArsip(self, ida):
        cur = self.koneksi.cursor()
        cur.execute("DELETE FROM arsip WHERE IDArsip=%s", (ida,))
        self.koneksi.commit()
        cur.close()

    def tampilArsip(self):
        cur = self.koneksi.cursor()
        cur.execute("SELECT IDArsip, NomorSurat, Judul, Tanggal, LokasiPenyimpanan FROM arsip")
        rows = cur.fetchall()
        cur.close()
        return rows

    def filterArsip(self, cari):
        cur = self.koneksi.cursor()
        cur.execute("SELECT * FROM arsip WHERE NomorSurat LIKE %s OR Judul LIKE %s OR LokasiPenyimpanan LIKE %s",
                    (f"%{cari}%", f"%{cari}%", f"%{cari}%"))
        rows = cur.fetchall()
        cur.close()
        return rows


    def simpanKeu(self, idk, tgl, ket, jenis, jumlah):
        cur = self.koneksi.cursor()
        cur.execute("INSERT INTO keuangan (IDKeu, Tanggal, Keterangan, Jenis, Jumlah) VALUES (%s,%s,%s,%s,%s)",
                    (idk, tgl, ket, jenis, jumlah))
        self.koneksi.commit()
        cur.close()

    def ubahKeu(self, idk, tgl, ket, jenis, jumlah):
        cur = self.koneksi.cursor()
        cur.execute("UPDATE keuangan SET Tanggal=%s, Keterangan=%s, Jenis=%s, Jumlah=%s WHERE IDKeu=%s",
                    (tgl, ket, jenis, jumlah, idk))
        self.koneksi.commit()
        cur.close()

    def hapusKeu(self, idk):
        cur = self.koneksi.cursor()
        cur.execute("DELETE FROM keuangan WHERE IDKeu=%s", (idk,))
        self.koneksi.commit()
        cur.close()

    def tampilKeu(self):
        cur = self.koneksi.cursor()
        cur.execute("SELECT IDKeu, Tanggal, Keterangan, Jenis, Jumlah FROM keuangan")
        rows = cur.fetchall()
        cur.close()
        return rows

    def filterKeu(self, cari):
        cur = self.koneksi.cursor()
        cur.execute("SELECT * FROM keuangan WHERE Keterangan LIKE %s OR Jenis LIKE %s",
                    (f"%{cari}%", f"%{cari}%"))
        rows = cur.fetchall()
        cur.close()
        return rows

