# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_QCWindow(object):
    def setupUi(self, QCWindow):
        if not QCWindow.objectName():
            QCWindow.setObjectName(u"QCWindow")
        QCWindow.resize(902, 654)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QCWindow.sizePolicy().hasHeightForWidth())
        QCWindow.setSizePolicy(sizePolicy)
        QCWindow.setMinimumSize(QSize(902, 654))
        QCWindow.setMaximumSize(QSize(902, 654))
        icon = QIcon(QIcon.fromTheme(u"applications-accessories"))
        QCWindow.setWindowIcon(icon)
        self.layoutWidget = QWidget(QCWindow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 901, 641))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 5, 0, 1, 1)

        self.sendButton = QPushButton(self.layoutWidget)
        self.sendButton.setObjectName(u"sendButton")

        self.gridLayout.addWidget(self.sendButton, 5, 1, 1, 1)

        self.methodBox = QComboBox(self.layoutWidget)
        self.methodBox.addItem("")
        self.methodBox.addItem("")
        self.methodBox.setObjectName(u"methodBox")

        self.gridLayout.addWidget(self.methodBox, 3, 1, 1, 1)

        self.convoBox = QPlainTextEdit(self.layoutWidget)
        self.convoBox.setObjectName(u"convoBox")
        self.convoBox.setReadOnly(True)

        self.gridLayout.addWidget(self.convoBox, 2, 0, 1, 2)


        self.retranslateUi(QCWindow)

        QMetaObject.connectSlotsByName(QCWindow)
    # setupUi

    def retranslateUi(self, QCWindow):
        QCWindow.setWindowTitle(QCoreApplication.translate("QCWindow", u"QuickChatter", None))
        self.label.setText(QCoreApplication.translate("QCWindow", u"Type", None))
        self.sendButton.setText(QCoreApplication.translate("QCWindow", u"Send!", None))
        self.methodBox.setItemText(0, QCoreApplication.translate("QCWindow", u"LLM", None))
        self.methodBox.setItemText(1, QCoreApplication.translate("QCWindow", u"RiveScript", None))

    # retranslateUi

