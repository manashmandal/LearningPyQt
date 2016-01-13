import sys
from PyQt4 import QtCore, QtGui, uic

ui_file = "ui_testplot.ui"

Ui_Widget, QtBaseClass = uic.loadUiType(ui_file)

class MyApp(QtGui.QWidget, Ui_Widget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        Ui_Widget.__init__(self)
        self.setupUi(self)
        #self.printOutButton.clicked.connect(self.printSomething)
        self.testLineEdit.textEdited.connect(self.printSomething)

    def printSomething(self, txt):
        print "bal", txt

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())