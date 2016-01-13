import sys
from PyQt4 import QtCore, QtGui, uic
import matplotlib.pyplot as plt

ui_plotter = "ui_plotter.ui"

Ui_Plotter, QtBaseClass = uic.loadUiType(ui_plotter)

class PlotterWindow(QtGui.QWidget, Ui_Plotter):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        Ui_Plotter.__init__(self)
        self.setupUi(self)
        for i in range(2):
            self.graphTableWidget.insertColumn(i)
        for i in range(2):
            self.graphTableWidget.insertRow(i)

        self.xlabel = ''
        self.ylabel = ''
        

        self.xlabelLineEdit.textEdited.connect(self.setXLabel)
        self.ylabelLineEdit.textEdited.connect(self.setYLabel)
        self.setLabelPushButton.clicked.connect(self.setLabels)
        self.generatePushButton.clicked.connect(self.plotGraph)

    def setXLabel(self, label):
        self.xlabel = str(label)
        print self.xlabel

    def setYLabel(self, label):
        self.ylabel = str(label)
        print self.ylabel

    def setLabels(self):
        self.labelArray = []
        self.labelArray.append(self.xlabel)
        self.labelArray.append(self.ylabel)
        self.graphTableWidget.setHorizontalHeaderLabels(self.labelArray)

    def plotGraph(self):
        self.x = []
        self.y = []
        for i in range(self.graphTableWidget.rowCount()):
            self.x.append(float(self.graphTableWidget.item(i, 0).text()))
            self.y.append(float(self.graphTableWidget.item(i, 1).text()))
        print self.x
        print self.y

        self.anotherWidg = PlotterWindow()

        self.verticalLayout.addWidget(self.anotherWidg)

        #plt.plot(self.x, self.y)
        #plt.xlabel(self.xlabel)
        #plt.ylabel(self.ylabel)
        #plt.legend()
        #plt.show()
        
        

        


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = PlotterWindow()
    win.show()
    sys.exit(app.exec_())