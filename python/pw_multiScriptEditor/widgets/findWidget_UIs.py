# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dropbox\Dropbox\pw_prefs\RnD\tools\pw_scriptEditor\pw_multiScriptEditor\widgets\findWidget.ui'
#
# Created: Thu Apr 02 15:51:34 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCore, QtWidgets

class Ui_findReplace(object):
    def setupUi(self, findReplace):
        findReplace.setObjectName("findReplace")
        findReplace.resize(246, 101)
        self.verticalLayout = QtWidgets.QVBoxLayout(findReplace)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.replace_le = QtWidgets.QLineEdit(findReplace)
        self.replace_le.setObjectName("replace_le")
        self.gridLayout.addWidget(self.replace_le, 1, 0, 1, 1)
        self.find_le = QtWidgets.QLineEdit(findReplace)
        self.find_le.setObjectName("find_le")
        self.gridLayout.addWidget(self.find_le, 0, 0, 1, 1)
        self.find_btn = QtWidgets.QPushButton(findReplace)
        self.find_btn.setObjectName("find_btn")
        self.gridLayout.addWidget(self.find_btn, 0, 1, 1, 1)
        self.replace_btn = QtWidgets.QPushButton(findReplace)
        self.replace_btn.setObjectName("replace_btn")
        self.gridLayout.addWidget(self.replace_btn, 1, 1, 1, 1)
        self.replaceAll_btn = QtWidgets.QPushButton(findReplace)
        self.replaceAll_btn.setObjectName("replaceAll_btn")
        self.gridLayout.addWidget(self.replaceAll_btn, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(findReplace)
        QtCore.QMetaObject.connectSlotsByName(findReplace)
        findReplace.setTabOrder(self.find_le, self.replace_le)
        findReplace.setTabOrder(self.replace_le, self.find_btn)
        findReplace.setTabOrder(self.find_btn, self.replace_btn)
        findReplace.setTabOrder(self.replace_btn, self.replaceAll_btn)

    def retranslateUi(self, findReplace):
        findReplace.setWindowTitle(QtWidgets.QApplication.translate("findReplace", "Find and Replace", None))
        self.find_btn.setText(QtWidgets.QApplication.translate("findReplace", "Find", None))
        self.replace_btn.setText(QtWidgets.QApplication.translate("findReplace", "Replace", None))
        self.replaceAll_btn.setText(QtWidgets.QApplication.translate("findReplace", "Replace All", None))

