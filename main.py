# importing required librarie
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtCore import QDate,QDateTime


class Window(QWidget):

	def __init__(self):
		super().__init__()
		self.setStyleSheet("color:cyan;background-color: black;")
		self.setWindowTitle("Clock")
		# self.setStyleSheet()

		# setting geometry of main window
		self.setGeometry(100, 100, 800, 400)

		# creating a vertical layout
		layout = QVBoxLayout()

		# creating font object
		font = QFont('Arial', 80, QFont.Bold)
		font1 = QFont('Arial', 40)


		# creating a label object
		self.label = QLabel()
		self.labeldate = QLabel()


		# setting centre alignment to the label
		self.label.setAlignment(Qt.AlignCenter)
		self.labeldate.setAlignment(Qt.AlignCenter)

		# setting font to the label
		self.label.setFont(font)
		self.labeldate.setFont(font1)


		# adding label to the layout
		layout.addWidget(self.label)
		layout.addWidget(self.labeldate)


		# setting the layout to main window
		self.setLayout(layout)

		# creating a timer object
		timer = QTimer(self)

		# adding action to timer
		timer.timeout.connect(self.showTime)
		timer.timeout.connect(self.showDate)


		# update the timer every second
		timer.start(1000)

	# method called by timer
	def showTime(self):

		# getting current time
		current_time = QTime.currentTime()


		# converting QTime object to string
		label_time = current_time.toString('hh:mm:ss')

		# showing it to the label
		self.label.setText(label_time)

	def showDate(self):
		now = QDate.currentDate()

		datetime = QDateTime.currentDateTime()
		x = datetime.toString()
		y = x.split()
		day = y[0]

		label_time = now.toString(Qt.DefaultLocaleLongDate)
		tt =  day+' '+ label_time
		# showing it to the label
		self.labeldate.setText(tt)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# showing all the widgets
window.show()

# start the app
App.exit(App.exec_())
