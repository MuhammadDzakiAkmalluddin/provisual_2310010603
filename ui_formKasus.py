# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formKasus.ui'
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
    QTableWidget, QTableWidgetItem, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(753, 701)
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(30, 570, 71, 31))
        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(120, 570, 71, 31))
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 571, 321))
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

        self.statusLabel = QLabel(self.formLayoutWidget)
        self.statusLabel.setObjectName(u"statusLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.statusLabel)

        self.editJudul = QLineEdit(self.formLayoutWidget)
        self.editJudul.setObjectName(u"editJudul")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editJudul)

        self.telpLabel = QLabel(self.formLayoutWidget)
        self.telpLabel.setObjectName(u"telpLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.telpLabel)

        self.emailLabel = QLabel(self.formLayoutWidget)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.emailLabel)

        self.editTanggal = QLineEdit(self.formLayoutWidget)
        self.editTanggal.setObjectName(u"editTanggal")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editTanggal)

        self.editUraian = QTextEdit(self.formLayoutWidget)
        self.editUraian.setObjectName(u"editUraian")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editUraian)

        self.comboClient = QComboBox(self.formLayoutWidget)
        self.comboClient.setObjectName(u"comboClient")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboClient)

        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(210, 570, 71, 31))
        self.tabelKasus = QTableWidget(Form)
        if (self.tabelKasus.columnCount() < 5):
            self.tabelKasus.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelKasus.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelKasus.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelKasus.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelKasus.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelKasus.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelKasus.setObjectName(u"tabelKasus")
        self.tabelKasus.setGeometry(QRect(10, 380, 721, 151))
        self.editCari = QLineEdit(Form)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(10, 350, 571, 28))
        self.btnPrint = QPushButton(Form)
        self.btnPrint.setObjectName(u"btnPrint")
        self.btnPrint.setGeometry(QRect(310, 570, 71, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.iDAnggotaLabel.setText(QCoreApplication.translate("Form", u"ID Kasus", None))
        self.namaAnggotaLabel.setText(QCoreApplication.translate("Form", u"ID Client", None))
        self.statusLabel.setText(QCoreApplication.translate("Form", u"Judul Kasus", None))
        self.telpLabel.setText(QCoreApplication.translate("Form", u"Deskripsi / Uraian Kasus", None))
        self.emailLabel.setText(QCoreApplication.translate("Form", u"Tanggal Masuk", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        ___qtablewidgetitem = self.tabelKasus.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Kasus", None));
        ___qtablewidgetitem1 = self.tabelKasus.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"ID Client", None));
        ___qtablewidgetitem2 = self.tabelKasus.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Judul Kasus", None));
        ___qtablewidgetitem3 = self.tabelKasus.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Uraian", None));
        ___qtablewidgetitem4 = self.tabelKasus.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u" Tanggal Masuk", None));
        self.btnPrint.setText(QCoreApplication.translate("Form", u"Print", None))
    # retranslateUi

