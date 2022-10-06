# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TImer(object):
    def setupUi(self, TImer):
        if not TImer.objectName():
            TImer.setObjectName(u"TImer")
        TImer.resize(483, 135)
        self.centralwidget = QWidget(TImer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ln = QHBoxLayout()
        self.ln.setObjectName(u"ln")
        self.day_ln = QLCDNumber(self.centralwidget)
        self.day_ln.setObjectName(u"day_ln")

        self.ln.addWidget(self.day_ln)

        self.day_lb = QLabel(self.centralwidget)
        self.day_lb.setObjectName(u"day_lb")

        self.ln.addWidget(self.day_lb)

        self.hour_ln = QLCDNumber(self.centralwidget)
        self.hour_ln.setObjectName(u"hour_ln")

        self.ln.addWidget(self.hour_ln)

        self.h_lb = QLabel(self.centralwidget)
        self.h_lb.setObjectName(u"h_lb")

        self.ln.addWidget(self.h_lb)

        self.min_ln = QLCDNumber(self.centralwidget)
        self.min_ln.setObjectName(u"min_ln")

        self.ln.addWidget(self.min_ln)

        self.min_lb = QLabel(self.centralwidget)
        self.min_lb.setObjectName(u"min_lb")

        self.ln.addWidget(self.min_lb)

        self.s_ln = QLCDNumber(self.centralwidget)
        self.s_ln.setObjectName(u"s_ln")

        self.ln.addWidget(self.s_ln)

        self.s_lb = QLabel(self.centralwidget)
        self.s_lb.setObjectName(u"s_lb")

        self.ln.addWidget(self.s_lb)

        self.ms_ln = QLCDNumber(self.centralwidget)
        self.ms_ln.setObjectName(u"ms_ln")

        self.ln.addWidget(self.ms_ln)

        self.ms_lb = QLabel(self.centralwidget)
        self.ms_lb.setObjectName(u"ms_lb")

        self.ln.addWidget(self.ms_lb)


        self.verticalLayout.addLayout(self.ln)

        self.pbtn = QHBoxLayout()
        self.pbtn.setObjectName(u"pbtn")
        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")

        self.pbtn.addWidget(self.start)

        self.pause = QPushButton(self.centralwidget)
        self.pause.setObjectName(u"pause")

        self.pbtn.addWidget(self.pause)

        self.cleanr = QPushButton(self.centralwidget)
        self.cleanr.setObjectName(u"cleanr")

        self.pbtn.addWidget(self.cleanr)


        self.verticalLayout.addLayout(self.pbtn)

        TImer.setCentralWidget(self.centralwidget)

        self.retranslateUi(TImer)

        QMetaObject.connectSlotsByName(TImer)
    # setupUi

    def retranslateUi(self, TImer):
        TImer.setWindowTitle(QCoreApplication.translate("TImer", u"\u8ba1\u65f6\u5668", None))
        self.day_lb.setText(QCoreApplication.translate("TImer", u"\u5929", None))
        self.h_lb.setText(QCoreApplication.translate("TImer", u"\u65f6", None))
        self.min_lb.setText(QCoreApplication.translate("TImer", u"\u5206", None))
        self.s_lb.setText(QCoreApplication.translate("TImer", u"\u79d2", None))
        self.ms_lb.setText(QCoreApplication.translate("TImer", u"ms", None))
        self.start.setText(QCoreApplication.translate("TImer", u"\u5f00\u59cb", None))
        self.pause.setText(QCoreApplication.translate("TImer", u"\u6682\u505c", None))
        self.cleanr.setText(QCoreApplication.translate("TImer", u"\u6e05\u7a7a", None))
    # retranslateUi

