# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_checkingoutwidget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_WidgetForm(object):
    def setupUi(self, WidgetForm):
        WidgetForm.setObjectName(_fromUtf8("WidgetForm"))
        WidgetForm.resize(422, 341)
        self.verticalLayout_2 = QtGui.QVBoxLayout(WidgetForm)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.mainVerticalLayout = QtGui.QVBoxLayout()
        self.mainVerticalLayout.setObjectName(_fromUtf8("mainVerticalLayout"))
        self.tableWidget = QtGui.QTableWidget(WidgetForm)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.mainVerticalLayout.addWidget(self.tableWidget)
        self.printOutButton = QtGui.QPushButton(WidgetForm)
        self.printOutButton.setObjectName(_fromUtf8("printOutButton"))
        self.mainVerticalLayout.addWidget(self.printOutButton)
        self.deleteColumnButton = QtGui.QPushButton(WidgetForm)
        self.deleteColumnButton.setObjectName(_fromUtf8("deleteColumnButton"))
        self.mainVerticalLayout.addWidget(self.deleteColumnButton)
        self.insertColumnButton = QtGui.QPushButton(WidgetForm)
        self.insertColumnButton.setObjectName(_fromUtf8("insertColumnButton"))
        self.mainVerticalLayout.addWidget(self.insertColumnButton)
        self.verticalLayout_2.addLayout(self.mainVerticalLayout)

        self.retranslateUi(WidgetForm)
        QtCore.QMetaObject.connectSlotsByName(WidgetForm)

    def retranslateUi(self, WidgetForm):
        WidgetForm.setWindowTitle(_translate("WidgetForm", "Checking Table Widget", None))
        self.printOutButton.setText(_translate("WidgetForm", "Print Out", None))
        self.deleteColumnButton.setText(_translate("WidgetForm", "Delete Column", None))
        self.insertColumnButton.setText(_translate("WidgetForm", "Insert Column", None))

