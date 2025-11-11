# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionData_Client = QAction(MainWindow)
        self.actionData_Client.setObjectName(u"actionData_Client")
        self.actionData_Kasus = QAction(MainWindow)
        self.actionData_Kasus.setObjectName(u"actionData_Kasus")
        self.actionData_Arsip = QAction(MainWindow)
        self.actionData_Arsip.setObjectName(u"actionData_Arsip")
        self.actionData_Keuangan = QAction(MainWindow)
        self.actionData_Keuangan.setObjectName(u"actionData_Keuangan")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuHalaman_Utama = QMenu(self.menubar)
        self.menuHalaman_Utama.setObjectName(u"menuHalaman_Utama")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHalaman_Utama.menuAction())
        self.menuHalaman_Utama.addAction(self.actionData_Client)
        self.menuHalaman_Utama.addAction(self.actionData_Kasus)
        self.menuHalaman_Utama.addAction(self.actionData_Arsip)
        self.menuHalaman_Utama.addAction(self.actionData_Keuangan)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionData_Client.setText(QCoreApplication.translate("MainWindow", u"Data Client", None))
        self.actionData_Kasus.setText(QCoreApplication.translate("MainWindow", u"Data Kasus", None))
        self.actionData_Arsip.setText(QCoreApplication.translate("MainWindow", u"Data Arsip", None))
        self.actionData_Keuangan.setText(QCoreApplication.translate("MainWindow", u"Data Keuangan", None))
        self.menuHalaman_Utama.setTitle(QCoreApplication.translate("MainWindow", u"Halaman Utama", None))
    # retranslateUi

