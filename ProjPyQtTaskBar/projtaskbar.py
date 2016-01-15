from PyQt4 import QtGui, QtCore, uic
import sys

ui_taskwidget = "ui_taskwidget.ui"
ui_tasklist = "ui_tasklist.ui"

Ui_TaskWidget, TaskBaseClass = uic.loadUiType(ui_taskwidget)
Ui_TaskList, TaskListBaseClass = uic.loadUiType(ui_tasklist)

class ListWidget(QtGui.QWidget, Ui_TaskList):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		Ui_TaskList.__init__(self)
		self.setupUi(self)
		self.addTaskPushButton.clicked.connect(self.addNewTask)


	def addNewTask(self):
		self.qListWidgetItem = QtGui.QListWidgetItem(self.listWidget)
		self.listWidget.addItem(self.qListWidgetItem)
		self.taskWidgetForm = TaskWidget()
		self.qListWidgetItem.setSizeHint(self.taskWidgetForm.minimumSizeHint())
		self.listWidget.setItemWidget(self.qListWidgetItem, self.taskWidgetForm)





class TaskWidget(QtGui.QWidget, Ui_TaskWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		Ui_TaskWidget.__init__(self)
		self.setupUi(self)
		self.doneCheckBox.stateChanged.connect(self.isChecked)

	def isChecked(self, value):
		if (value):
			print "the box is checked"
		else:
			print "The box is not checked"



if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	# taskWidget = TaskWidget()
	# taskWidget.show()
	lw = ListWidget()
	lw.show()

	sys.exit(app.exec_())