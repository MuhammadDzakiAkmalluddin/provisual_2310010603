# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formClient.ui'
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
        Form.resize(744, 503)
        self.tabelClient = QTableWidget(Form)
        if (self.tabelClient.columnCount() < 5):
            self.tabelClient.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelClient.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelClient.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelClient.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelClient.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelClient.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelClient.setObjectName(u"tabelClient")
        self.tabelClient.setGeometry(QRect(10, 230, 701, 151))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(200, 410, 71, 31))
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 401, 170))
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

        self.editNama = QLineEdit(self.formLayoutWidget)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.statusLabel = QLabel(self.formLayoutWidget)
        self.statusLabel.setObjectName(u"statusLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.statusLabel)

        self.editAlamat = QLineEdit(self.formLayoutWidget)
        self.editAlamat.setObjectName(u"editAlamat")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editAlamat)

        self.telpLabel = QLabel(self.formLayoutWidget)
        self.telpLabel.setObjectName(u"telpLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.telpLabel)

        self.editTelp = QLineEdit(self.formLayoutWidget)
        self.editTelp.setObjectName(u"editTelp")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editTelp)

        self.emailLabel = QLabel(self.formLayoutWidget)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.emailLabel)

        self.editEmail = QLineEdit(self.formLayoutWidget)
        self.editEmail.setObjectName(u"editEmail")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editEmail)

        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(20, 410, 71, 31))
        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(110, 410, 71, 31))
        self.editCari = QLineEdit(Form)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(10, 190, 591, 28))
        self.btnPrint = QPushButton(Form)
        self.btnPrint.setObjectName(u"btnPrint")
        self.btnPrint.setGeometry(QRect(300, 410, 71, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.tabelClient.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Client", None));
        ___qtablewidgetitem1 = self.tabelClient.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama Client", None));
        ___qtablewidgetitem2 = self.tabelClient.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Alamat Client", None));
        ___qtablewidgetitem3 = self.tabelClient.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Password", None));
        ___qtablewidgetitem4 = self.tabelClient.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Email", None));
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.iDAnggotaLabel.setText(QCoreApplication.translate("Form", u"ID Client", None))
        self.namaAnggotaLabel.setText(QCoreApplication.translate("Form", u"Nama Client", None))
        self.statusLabel.setText(QCoreApplication.translate("Form", u"Alamat Client", None))
        self.telpLabel.setText(QCoreApplication.translate("Form", u"Telp", None))
        self.emailLabel.setText(QCoreApplication.translate("Form", u"Email", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnPrint.setText(QCoreApplication.translate("Form", u"Print", None))
    # retranslateUi

