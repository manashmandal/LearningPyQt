import sys
from PyQt4 import QtGui, QtCore, uic
from sympy import init_printing
import sympy as sp
import matplotlib as mpl
from matplotlib.backends.backend_agg import FigureCanvasAgg

sp.init_printing()

expressionUiFile = "ui_expressionform.ui"

Ui_ExpressionForm, QtBaseClass = uic.loadUiType(expressionUiFile)

class ExpressionForm(QtGui.QWidget, Ui_ExpressionForm):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        Ui_ExpressionForm.__init__(self)
        self.setupUi(self)

        self.expression = ''
        self.expressionFontSize = 10
        self.latexExpression = ''
        self.fontsizeSpinBox.setValue(10)

        self.fontsizeSpinBox.valueChanged.connect(self.changeFontSize)
        self.expressionLineEdit.textEdited.connect(self.parseToMathTex)

    def renderExpression(self, text):
        self.expression = str(text)
        self.expression = '$' + self.expression
        self.expression = self.expression + '$'

        print self.expression

        self.label_2.setPixmap(self.mathTexToQPixMap(self.expression, self.expressionFontSize))
        print self.expression

    def mathTexToQPixMap( self ,mathTex, fs):
        fig = mpl.figure.Figure()
        fig.patch.set_facecolor('none')
        fig.set_canvas(FigureCanvasAgg(fig))
        renderer = fig.canvas.get_renderer()

        #---- plot the mathTex expression ----

        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('off')
        ax.patch.set_facecolor('none')
        t = ax.text(0, 0, mathTex, ha='left', va='bottom', fontsize=fs)

        #---- fit figure size to text artist ----

        fwidth, fheight = fig.get_size_inches()
        fig_bbox = fig.get_window_extent(renderer)

        text_bbox = t.get_window_extent(renderer)

        tight_fwidth = text_bbox.width * fwidth / fig_bbox.width
        tight_fheight = text_bbox.height * fheight / fig_bbox.height

        fig.set_size_inches(tight_fwidth, tight_fheight)

        #---- convert mpl figure to QPixmap ----

        buf, size = fig.canvas.print_to_buffer()
        qimage = QtGui.QImage.rgbSwapped(QtGui.QImage(buf, size[0], size[1],
                                                      QtGui.QImage.Format_ARGB32))
        self.qpixmap = QtGui.QPixmap(qimage)

        return self.qpixmap

    def changeFontSize(self, fontsize):
        self.expressionFontSize = int(fontsize)
        self.parseToMathTex(str(self.expressionLineEdit.text()))
        print self.expressionFontSize

    def parseToMathTex(self, expression):
        self.expression = str(expression)
        self.latexExpression = sp.latex(sp.sympify(self.expression))
        print (sp.latex(sp.sympify(self.expression)))
        self.renderExpression(self.latexExpression)
        
        



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    expressionForm = ExpressionForm()
    expressionForm.show()
    sys.exit(app.exec_())
