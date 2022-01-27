import os.path

from msilib.schema import Directory
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import ImageGrab

class Ui_MainWindow(object):

	

	def setupUi(self, MainWindow):

		self.class_output_location = ""

		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(366, 197)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit.setGeometry(QtCore.QRect(20, 70, 211, 25))
		self.lineEdit.setObjectName("lineEdit")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.clicked.connect(self.browse)

		self.pushButton.setGeometry(QtCore.QRect(250, 70, 75, 25))
		self.pushButton.setObjectName("pushButton")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(20, 50, 111, 16))
		self.label.setObjectName("label")

		# Save button sends location to save method.
		self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_2.setGeometry(QtCore.QRect(140, 110, 91, 41))
		self.pushButton_2.clicked.connect(self.save)

		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.pushButton_2.setFont(font)
		self.pushButton_2.setObjectName("pushButton_2")
		

		self.comboBox = QtWidgets.QComboBox(self.centralwidget)
		self.comboBox.setGeometry(QtCore.QRect(250, 30, 69, 22))
		self.comboBox.setObjectName("comboBox")

		self.comboBox.addItems([".png",".jpg"])

		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(200, 30, 51, 16))
		self.label_2.setObjectName("label_2")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 366, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushButton.setText(_translate("MainWindow", "Browse"))
		self.label.setText(_translate("MainWindow", "Where to save?"))
		self.pushButton_2.setText(_translate("MainWindow", "Save!"))
		self.label_2.setText(_translate("MainWindow", "File Type: "))

	def browse(self):
		output_location = QtWidgets.QFileDialog.getExistingDirectory(
			None,
			caption="Select a Folder",
		)
		self.lineEdit.setText(output_location)
		self.class_output_location = output_location
		print(self.class_output_location)

	def save(self):
		
			format = self.comboBox.currentText()
			save_location = f"{self.class_output_location}/capture{format}"

			try:
				current_capture = 0

				image = ImageGrab.grabclipboard()
				while os.path.isfile(save_location):
					current_capture += 1
					save_location = f"{self.class_output_location}/capture_{current_capture}{format}"

				# Saves once it checks that no other file with the same name exists	
				image.save(save_location, 'PNG')

			except:
				print("No image in clipboard.")

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
