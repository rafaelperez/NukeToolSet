# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dropbox\Dropbox\pw_prefs\RnD\tools\pw_scriptEditor\pw_multiScriptEditor\widgets\about.ui'
#
# Created: Thu Apr 02 22:56:45 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCore, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(465, 393)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 20, -1, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.icon_lb = QtWidgets.QLabel(Dialog)
        font = QtWidgets.QFont()
        font.setPointSize(20)
        self.icon_lb.setFont(font)
        self.icon_lb.setText("")
        self.icon_lb.setObjectName("icon_lb")
        self.horizontalLayout.addWidget(self.icon_lb)
        self.title_lb = QtWidgets.QLabel(Dialog)
        font = QtWidgets.QFont()
        font.setPointSize(20)
        self.title_lb.setFont(font)
        self.title_lb.setObjectName("title_lb")
        self.horizontalLayout.addWidget(self.title_lb)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.text_link_lb = QtWidgets.QLabel(Dialog)
        self.text_link_lb.setObjectName("text_link_lb")
        self.verticalLayout.addWidget(self.text_link_lb)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.donate_btn = QtWidgets.QPushButton(Dialog)
        self.donate_btn.setObjectName("donate_btn")
        self.horizontalLayout_2.addWidget(self.donate_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "About Multi Script Editor", None))
        self.title_lb.setText(QtWidgets.QApplication.translate("Dialog", "Multi Script Editor v", None))
        self.text_link_lb.setText(QtWidgets.QApplication.translate("Dialog", "Paul Winex 2015", None))
        self.textBrowser.setHtml(QtWidgets.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">File not Found :(</span></p></body></html>", None))
        self.donate_btn.setText(QtWidgets.QApplication.translate("Dialog", "Donate", None))

