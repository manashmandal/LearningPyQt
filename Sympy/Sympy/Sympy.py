"""

from sympy import *
str_expr = "x**2"
expr = sympify(str_expr)

#print expr.subs([('x', 2)])

differentiated = diff(expr)

print differentiated.subs([('x', 5)])

#print diff(expr)
"""

import sys

from ui_evaluateexpression import *
import sympy as sp

class EvaluateForm(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.expression = ''
        self.value = ''
        self.var = ''

        QtCore.QObject.connect(self.ui.expressionLineEdit, QtCore.SIGNAL('textChanged(QString)'), self.setExpression)
       # QtCore.QObject.connect(self.ui.evaluatePushButton, QtCore.SIGNAL('clicked()'), self.printSomething)
        #QtCore.QObject.connect(self.ui.variableValueLineEdit, QtCore.SIGNAL('textChanged(QString)'), self.setValue)
        QtCore.QObject.connect(self.ui.setPushButton, QtCore.SIGNAL('clicked()'), self.setValue)
        QtCore.QObject.connect(self.ui.evaluatePushButton, QtCore.SIGNAL('clicked()'), self.evaluateExpression)

    def setExpression(self, expression):
        self.expression = str(expression)
        #Debugging Purpose
        print self.expression

    def setValue(self):
        value = self.ui.variableValueLineEdit.text()
        var, val = value.split(':')
        var = str(var)
        val = str(val)

        self.var = var
        self.value = val

        print "variable", var
        print "value", val
        #Debugging
        

    def evaluateExpression(self):
        sympified = sp.sympify(self.expression)

        valu = float(self.value)

        print sympified
        ans = sympified.subs([(self.var, valu)])
        self.ui.evaluatedExpressionLabel.setText(QtCore.QString.number(ans))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    EvaluateApp = EvaluateForm()
    EvaluateApp.show()
    sys.exit(app.exec_())