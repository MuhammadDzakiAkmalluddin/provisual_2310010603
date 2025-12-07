# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formKeuangan.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(810, 604)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 571, 184))
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

        self.editTanggal = QLineEdit(self.formLayoutWidget)
        self.editTanggal.setObjectName(u"editTanggal")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editTanggal)

        self.editKeterangan = QLineEdit(self.formLayoutWidget)
        self.editKeterangan.setObjectName(u"editKeterangan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editKeterangan)

        self.statusLabel = QLabel(self.formLayoutWidget)
        self.statusLabel.setObjectName(u"statusLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.statusLabel)

        self.telpLabel = QLabel(self.formLayoutWidget)
        self.telpLabel.setObjectName(u"telpLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.telpLabel)

        self.emailLabel = QLabel(self.formLayoutWidget)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.emailLabel)

        self.editJumlah = QLineEdit(self.formLayoutWidget)
        self.editJumlah.setObjectName(u"editJumlah")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editJumlah)

        self.comboJenis = QComboBox(self.formLayoutWidget)
        self.comboJenis.addItem("")
        self.comboJenis.addItem("")
        self.comboJenis.setObjectName(u"comboJenis")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.comboJenis)

        self.tabelKeuangan = QTableWidget(Form)
        if (self.tabelKeuangan.columnCount() < 5):
            self.tabelKeuangan.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelKeuangan.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelKeuangan.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelKeuangan.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelKeuangan.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelKeuangan.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelKeuangan.setObjectName(u"tabelKeuangan")
        self.tabelKeuangan.setGeometry(QRect(10, 240, 711, 151))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(20, 420, 71, 31))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(200, 420, 71, 31))
        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(110, 420, 71, 31))
        self.editCari = QLineEdit(Form)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(10, 210, 571, 28))
        self.btnPrint = QPushButton(Form)
        self.btnPrint.setObjectName(u"btnPrint")
        self.btnPrint.setGeometry(QRect(300, 420, 71, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDAnggotaLabel.setText(QCoreApplication.translate("Form", u"ID Keuangan", None))
        self.namaAnggotaLabel.setText(QCoreApplication.translate("Form", u"Tanggal", None))
        self.statusLabel.setText(QCoreApplication.translate("Form", u"Keterangan Transaksi", None))
        self.telpLabel.setText(QCoreApplication.translate("Form", u"Jenis Transaksi", None))
        self.emailLabel.setText(QCoreApplication.translate("Form", u"Nominal (angka)", None))
        self.comboJenis.setItemText(0, QCoreApplication.translate("Form", u"Pemasukan", None))
        self.comboJenis.setItemText(1, QCoreApplication.translate("Form", u"Pengeluaran", None))

        ___qtablewidgetitem = self.tabelKeuangan.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Keuangan", None));
        ___qtablewidgetitem1 = self.tabelKeuangan.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Tanggal", None));
        ___qtablewidgetitem2 = self.tabelKeuangan.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Keterangan Transaksi", None));
        ___qtablewidgetitem3 = self.tabelKeuangan.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Jenis Transaksi", None));
        ___qtablewidgetitem4 = self.tabelKeuangan.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Nominal (angka)", None));
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnPrint.setText(QCoreApplication.translate("Form", u"Print", None))
    # retranslateUi

