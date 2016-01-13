# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_plotter.ui'
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

class Ui_Plotter(object):
    def setupUi(self, Plotter):
        Plotter.setObjectName(_fromUtf8("Plotter"))
        Plotter.resize(366, 300)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Plotter)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.graphTableWidget = QtGui.QTableWidget(Plotter)
        self.graphTableWidget.setObjectName(_fromUtf8("graphTableWidget"))
        self.graphTableWidget.setColumnCount(0)
        self.graphTableWidget.setRowCount(0)
        self.horizontalLayout.addWidget(self.graphTableWidget)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.loadDataFilePushButton = QtGui.QPushButton(Plotter)
        self.loadDataFilePushButton.setObjectName(_fromUtf8("loadDataFilePushButton"))
        self.verticalLayout_3.addWidget(self.loadDataFilePushButton)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.xlabel = QtGui.QLabel(Plotter)
        self.xlabel.setObjectName(_fromUtf8("xlabel"))
        self.verticalLayout.addWidget(self.xlabel)
        self.xlabelLineEdit = QtGui.QLineEdit(Plotter)
        self.xlabelLineEdit.setObjectName(_fromUtf8("xlabelLineEdit"))
        self.verticalLayout.addWidget(self.xlabelLineEdit)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ylabel = QtGui.QLabel(Plotter)
        self.ylabel.setObjectName(_fromUtf8("ylabel"))
        self.verticalLayout_2.addWidget(self.ylabel)
        self.ylabelLineEdit = QtGui.QLineEdit(Plotter)
        self.ylabelLineEdit.setObjectName(_fromUtf8("ylabelLineEdit"))
        self.verticalLayout_2.addWidget(self.ylabelLineEdit)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.generateGraphPushButton = QtGui.QPushButton(Plotter)
        self.generateGraphPushButton.setObjectName(_fromUtf8("generateGraphPushButton"))
        self.verticalLayout_4.addWidget(self.generateGraphPushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.graphTableWidget.raise_()
        self.xlabel.raise_()
        self.ylabel.raise_()
        self.xlabelLineEdit.raise_()
        self.ylabelLineEdit.raise_()
        self.ylabel.raise_()
        self.xlabel.raise_()
        self.generateGraphPushButton.raise_()

        self.retranslateUi(Plotter)
        QtCore.QMetaObject.connectSlotsByName(Plotter)

    def retranslateUi(self, Plotter):
        Plotter.setWindowTitle(_translate("Plotter", "Plotter", None))
        self.loadDataFilePushButton.setText(_translate("Plotter", "Load Data File", None))
        self.xlabel.setText(_translate("Plotter", "Set xlabel:", None))
        self.ylabel.setText(_translate("Plotter", "Set ylabel:", None))
        self.generateGraphPushButton.setText(_translate("Plotter", "Generate Graph", None))

