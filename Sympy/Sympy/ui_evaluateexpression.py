# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_evaluateexpression.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(342, 125)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.expressionLabel = QtGui.QLabel(Form)
        self.expressionLabel.setObjectName(_fromUtf8("expressionLabel"))
        self.horizontalLayout.addWidget(self.expressionLabel)
        self.expressionLineEdit = QtGui.QLineEdit(Form)
        self.expressionLineEdit.setObjectName(_fromUtf8("expressionLineEdit"))
        self.horizontalLayout.addWidget(self.expressionLineEdit)
        self.evaluatePushButton = QtGui.QPushButton(Form)
        self.evaluatePushButton.setObjectName(_fromUtf8("evaluatePushButton"))
        self.horizontalLayout.addWidget(self.evaluatePushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.variableValueLabel = QtGui.QLabel(Form)
        self.variableValueLabel.setObjectName(_fromUtf8("variableValueLabel"))
        self.horizontalLayout_2.addWidget(self.variableValueLabel)
        self.variableValueLineEdit = QtGui.QLineEdit(Form)
        self.variableValueLineEdit.setObjectName(_fromUtf8("variableValueLineEdit"))
        self.horizontalLayout_2.addWidget(self.variableValueLineEdit)
        self.setPushButton = QtGui.QPushButton(Form)
        self.setPushButton.setObjectName(_fromUtf8("setPushButton"))
        self.horizontalLayout_2.addWidget(self.setPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.evaluatedExpressionLabel = QtGui.QLabel(Form)
        self.evaluatedExpressionLabel.setObjectName(_fromUtf8("evaluatedExpressionLabel"))
        self.verticalLayout.addWidget(self.evaluatedExpressionLabel)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Evaluate Expression", None))
        self.expressionLabel.setText(_translate("Form", "Expression: ", None))
        self.evaluatePushButton.setText(_translate("Form", "Evaluate", None))
        self.variableValueLabel.setText(_translate("Form", "Variable Value:", None))
        self.setPushButton.setText(_translate("Form", "Set", None))
        self.evaluatedExpressionLabel.setText(_translate("Form", "~~ Evaluated Expression ~~", None))

