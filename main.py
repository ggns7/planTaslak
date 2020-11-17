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

		self.tables = [
			self.ui.tableWidget, self.ui.tableWidget_2,
			self.ui.tableWidget_3, self.ui.tableWidget_4,
			self.ui.tableWidget_5, self.ui.tableWidget_6,
			self.ui.tableWidget_7]

		for table in self.tables:
			table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

		self.ui.pushButton.clicked.connect(self.previous_page)
		self.ui.pushButton_2.clicked.connect(self.next_page)
		self.ui.pushButton_3.clicked.connect(self.previous_page)
		self.ui.pushButton_4.clicked.connect(self.next_page)
		self.ui.pushButton_5.clicked.connect(self.previous_page)
		self.ui.pushButton_6.clicked.connect(self.next_page)

		self.ui.comboBox.setPlaceholderText("Vardiyayı Seçin")
		self.ui.comboBox_2.setPlaceholderText("Sistemi Seçin")
		self.ui.dateEdit.setCalendarPopup(True)
		self.ui.dateEdit.setDateTime(QDateTime().currentDateTime())

		self.shifts = {
			1: {"07:00-15:00": ["07:30", "08:30",
								"09:30", "10:30",
								"11:30", "12:30",
								"13:30", "14:30"]},
			2: {"15:00-23:00": ["15:30", "16:30",
								"17:30", "18:30",
								"19:30", "20:30",
								"21:30", "22:30"]},
			3: {"23:00-07:00": ["23:30", "00:30",
								"01:30", "02:30",
								"03:30", "04:30",
								"05:30", "06:30"]},
		}

		self.systems = {
			1: "SPX",
			2: "EGLI",
			3: "SPX & EGLI"
		}

		try:
			for x in range(1,4):
				self.ui.comboBox.addItem(str(*self.shifts[x].keys()))
				self.ui.comboBox_2.addItem(self.systems[x])
		except KeyError:
			pass

		for r in range(5):
			self.ui.tableWidget.setCellWidget(r, 4, QTimeEdit())
			self.ui.tableWidget.setCellWidget(r, 5, QTimeEdit())

		c = 0
		t = 0

		while t < len(self.tables):
			for x in range(self.tables[t].columnCount()):
				r = -1
				rowCount = self.tables[t].rowCount()
				while r < rowCount:
					r += 1
					try:
						item = self.tables[t].setItem(r,c, QTableWidgetItem())
					except AttributeError:
						pass
				if r >= rowCount:
					c += 1
			t += 1
			c = 0

	def shift_selected(self):
		for i in range(3,6):
			self.tables[i].setEditTriggers(QTableWidget.AllEditTriggers)
		if self.ui.comboBox.currentIndex() == 0:
			self.tables[3].setHorizontalHeaderLabels(self.shifts[1]["07:00-15:00"])
			self.tables[4].setHorizontalHeaderLabels(self.shifts[1]["07:00-15:00"])
		if self.ui.comboBox.currentIndex() == 1:
			self.tables[3].setHorizontalHeaderLabels(self.shifts[2]["15:00-23:00"])
			self.tables[4].setHorizontalHeaderLabels(self.shifts[2]["15:00-23:00"])
		if self.ui.comboBox.currentIndex() == 2:
			self.tables[3].setHorizontalHeaderLabels(self.shifts[3]["23:00-07:00"])
			self.tables[4].setHorizontalHeaderLabels(self.shifts[3]["23:00-07:00"])

	def previous_page(self):
		self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.currentIndex()-1)

	def next_page(self):
		self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.currentIndex()+1)

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