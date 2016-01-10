import sys
from project0 import *

class MyForm(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #QtCore.QObject.connect(self.ui.buttonBox.Ok, QtCore.SIGNAL('clicked()'), self.showMessage)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL('accepted()'), self.showMessage)
        QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL('rejected()'), self.printSomethingThenClose)
        QtCore.QObject.connect(self.ui.lineEdit, QtCore.SIGNAL('returnPressed()'), self.showMessage)

    def showMessage(self):
        QtGui.QMessageBox.information(self, "Chdoon" , self.ui.lineEdit.text())
   
    def printSomethingThenClose(self):
        print 'Quitting'
        self.close()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())