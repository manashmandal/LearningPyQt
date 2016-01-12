# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_plottercreator.ui'
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

class Ui_PlotterCreator(object):
    def setupUi(self, PlotterCreator):
        PlotterCreator.setObjectName(_fromUtf8("PlotterCreator"))
        PlotterCreator.resize(183, 99)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(PlotterCreator)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.graphLabel = QtGui.QLabel(PlotterCreator)
        self.graphLabel.setObjectName(_fromUtf8("graphLabel"))
        self.horizontalLayout.addWidget(self.graphLabel)
        self.graphSpinBox = QtGui.QSpinBox(PlotterCreator)
        self.graphSpinBox.setMinimum(1)
        self.graphSpinBox.setMaximum(10)
        self.graphSpinBox.setObjectName(_fromUtf8("graphSpinBox"))
        self.horizontalLayout.addWidget(self.graphSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(PlotterCreator)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.noOfDataLineEdit = QtGui.QLineEdit(PlotterCreator)
        self.noOfDataLineEdit.setObjectName(_fromUtf8("noOfDataLineEdit"))
        self.horizontalLayout_2.addWidget(self.noOfDataLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton = QtGui.QPushButton(PlotterCreator)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(PlotterCreator)
        QtCore.QMetaObject.connectSlotsByName(PlotterCreator)

    def retranslateUi(self, PlotterCreator):
        PlotterCreator.setWindowTitle(_translate("PlotterCreator", "Plotter Creator", None))
        self.graphLabel.setText(_translate("PlotterCreator", "No. of Graphs:", None))
        self.label.setText(_translate("PlotterCreator", "No. of Data:", None))
        self.pushButton.setText(_translate("PlotterCreator", "Generate Window", None))

