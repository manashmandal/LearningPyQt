from ui_checkingoutwidget import *

import sys

class CheckingOutWidget(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_WidgetForm()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.insertColumnButton, QtCore.SIGNAL('clicked()'), self.insertColumn)
        QtCore.QObject.connect(self.ui.deleteColumnButton, QtCore.SIGNAL('clicked()'), self.deleteColumn)
        QtCore.QObject.connect(self.ui.printOutButton, QtCore.SIGNAL('clicked()'), self.printOut)
    
    def insertColumn(self):
        self.ui.tableWidget.insertColumn(self.ui.tableWidget.columnCount())
        self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())

    def deleteColumn(self):
        self.ui.tableWidget.removeColumn(self.ui.tableWidget.currentColumn())

    def printOut(self):
        print "BEGIN"
        for i in range(self.ui.tableWidget.columnCount()):
            for j in range(self.ui.tableWidget.rowCount()):
                print self.ui.tableWidget.item(i, j).text()
        print "END"


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    checkingOutWidget = CheckingOutWidget()
    checkingOutWidget.show()
    sys.exit(app.exec_())