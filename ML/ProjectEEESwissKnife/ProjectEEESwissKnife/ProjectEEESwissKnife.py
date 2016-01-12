from ui_plottercreator import *
import sys

class PlotterCreator(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_PlotterCreator()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.noOfDataLineEdit, QtCore.SIGNAL('textEdited(QString)'), self.parseData)
        

    """
    Convert 1 2 3 into 1:2:3

    """
    def parseData(self, input_string = ""):
        self.parsedString = str(input_string)
        self.parsedString = self.parsedString.replace(' ', ':')
        self.ui.noOfDataLineEdit.setText(self.parsedString)

    
        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    PlotterCreatorApp = PlotterCreator()
    PlotterCreatorApp.show()
    sys.exit(app.exec_())