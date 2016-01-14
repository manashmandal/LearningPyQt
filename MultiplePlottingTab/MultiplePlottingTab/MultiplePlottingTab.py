from PyQt4 import QtCore, QtGui, uic, Qt
import sys

ui_plotwindow = "ui_plotwindow.ui"
ui_tabwidget = "ui_tabwidget.ui"

Ui_TabWidget, QtBaseClassTabWidget = uic.loadUiType(ui_tabwidget)
Ui_PlotWindow, QtBaseClassPlotWindow = uic.loadUiType(ui_plotwindow)




class PlottingWindow(QtGui.QWidget, Ui_PlotWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        Ui_PlotWindow.__init__(self)
        self.setupUi(self)
        self.loadPushButton.clicked.connect(self.openDirectoryDialog)


    def openDirectoryDialog(self):
        self.fileName = str( QtGui.QFileDialog.getOpenFileName(self, "Open Image", "C:/",  "Image Files (*.png)"))


        self.dataFilePathLineEdit.setText(self.fileName)
        
        if (self.fileName == None):
            self.dataFilePathLineEdit.clear()

        print self.fileName

class MultiplePlottingWindow(QtGui.QWidget, Ui_TabWidget):
    def __init__(self, numberOfTabs = 5):
        QtGui.QWidget.__init__(self)
        Ui_TabWidget.__init__(self)

        self.tabToBeRemovedIndex = 1

        self.setupUi(self)
        self.tabWidget.removeTab(self.tabToBeRemovedIndex)
        self.tabWidget.removeTab(self.tabToBeRemovedIndex -1 )

        self.plottingWindows = []

        self.allData = []

        for i in range(numberOfTabs):
            self.pw = PlottingWindow()
            self.plottingWindows.append(self.pw)
            self.tabWidget.addTab(self.pw,  "Tab Number %i" %(i+1))

        print self.plottingWindows

        for i in range(len(self.plottingWindows)):
            #self.plottingWindows[i].loadPushButton.setText("Load Data" %(i+1))
            for j in range(self.plottingWindows[i].tableWidget.columnCount()):
                for k in range(self.plottingWindows[i].tableWidget.rowCount()):
                    self.allData.append(self.plottingWindows[i].tableWidget.item(k, j).text())
        
        for i in range(len(self.allData)):
            print self.allData[i]

        print "Length : ", len(self.allData)

        self.x = []
        
        self.bal = self.allData[0:2]
        
        for i in range(len(self.bal)):
            print self.bal[i]

        print self.x
        

        #self.pw = PlottingWindow()
        #self.pw2 = PlottingWindow()
        #self.tab.layout().addWidget(self.pw)
        #self.tab_2.layout().addWidget(self.pw2)
        #self.pw2.loadPushButton.setText("ORE CHODON")
        #del self.tab_2
        



        
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    MPW = MultiplePlottingWindow()
    MPW.show()
    sys.exit(app.exec_())
