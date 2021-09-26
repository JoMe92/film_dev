import PySide2

from ui_rate import Ui_MainWindow

if __name__ == "__main__":
	import sys
	app = PySide2.QtWidgets.QApplication(sys.argv)
	MainWindow = PySide2.QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())