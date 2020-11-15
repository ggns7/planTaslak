import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtUiTools import QUiLoader



class Main:
	def __init__(self):
		super().__init__()
		self.initUi()

	def initUi(self):
		self.ui = QUiLoader().load("ui/main.ui")

		self.ui.pushButton.clicked.connect(self.edit_report)
		self.ui.pushButton_2.clicked.connect(self.new_report)
		self.ui.pushButton_3.clicked.connect(self.statistics_info)

	def edit_report(self):
		self.editReport = EditReport()
		self.editReport.ui.show()

	def new_report(self):
		self.newReport = NewReport()
		self.newReport.ui.show()

	def statistics_info(self):
		self.statistics = Statistics()
		self.statistics.ui.show()

class EditReport:
	def __init__(self):
		super().__init__()
		self.initUi()

	def initUi(self):
		self.ui = QUiLoader().load("ui/editReport.ui")

class NewReport:
	def __init__(self):
		super().__init__()
		self.initUi()

	def initUi(self):
		self.ui = QUiLoader().load("ui/newReport.ui")

class Statistics:
	def __init__(self):
		super().__init__()
		self.initUi()

	def initUi(self):
		self.ui = QUiLoader().load("ui/statistics.ui")









if __name__ == "__main__":
	app = QApplication(sys.argv)
	main = Main()
	main.ui.show()
	sys.exit(app.exec_())