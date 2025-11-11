# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formArsip.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(761, 607)
        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(100, 420, 71, 31))
        self.tabelArsip = QTableWidget(Form)
        if (self.tabelArsip.columnCount() < 5):
            self.tabelArsip.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelArsip.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelArsip.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelArsip.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelArsip.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelArsip.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelArsip.setObjectName(u"tabelArsip")
        self.tabelArsip.setGeometry(QRect(10, 250, 721, 151))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(10, 420, 71, 31))
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 571, 184))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDAnggotaLabel = QLabel(self.formLayoutWidget)
        self.iDAnggotaLabel.setObjectName(u"iDAnggotaLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDAnggotaLabel)

        self.editID = QLineEdit(self.formLayoutWidget)
        self.editID.setObjectName(u"editID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editID)

        self.namaAnggotaLabel = QLabel(self.formLayoutWidget)
        self.namaAnggotaLabel.setObjectName(u"namaAnggotaLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaAnggotaLabel)

        self.editNomor = QLineEdit(self.formLayoutWidget)
        self.editNomor.setObjectName(u"editNomor")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNomor)

        self.editTanggal = QLineEdit(self.formLayoutWidget)
        self.editTanggal.setObjectName(u"editTanggal")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editTanggal)

        self.editJudul = QLineEdit(self.formLayoutWidget)
        self.editJudul.setObjectName(u"editJudul")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editJudul)

        self.statusLabel = QLabel(self.formLayoutWidget)
        self.statusLabel.setObjectName(u"statusLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.statusLabel)

        self.telpLabel = QLabel(self.formLayoutWidget)
        self.telpLabel.setObjectName(u"telpLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.telpLabel)

        self.emailLabel = QLabel(self.formLayoutWidget)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.emailLabel)

        self.editLokasi = QLineEdit(self.formLayoutWidget)
        self.editLokasi.setObjectName(u"editLokasi")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editLokasi)

        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(190, 420, 71, 31))
        self.editCari = QLineEdit(Form)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(10, 210, 571, 28))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        ___qtablewidgetitem = self.tabelArsip.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Arsip", None));
        ___qtablewidgetitem1 = self.tabelArsip.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nomor Surat", None));
        ___qtablewidgetitem2 = self.tabelArsip.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Judul Dokumen", None));
        ___qtablewidgetitem3 = self.tabelArsip.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Tanggal", None));
        ___qtablewidgetitem4 = self.tabelArsip.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Lokasi Penyipanan", None));
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.iDAnggotaLabel.setText(QCoreApplication.translate("Form", u"ID Arsip", None))
        self.namaAnggotaLabel.setText(QCoreApplication.translate("Form", u"Nomor Surat", None))
        self.statusLabel.setText(QCoreApplication.translate("Form", u"Judul Dokumen", None))
        self.telpLabel.setText(QCoreApplication.translate("Form", u"Tanggal", None))
        self.emailLabel.setText(QCoreApplication.translate("Form", u"Lokasi Penyimpanan", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
    # retranslateUi

