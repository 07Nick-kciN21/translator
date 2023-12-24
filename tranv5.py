from PyQt5 import QtCore, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 200)

pushButton = QtWidgets.QPushButton(MainWindow)
pushButton.setGeometry(QtCore.QRect(100, 70, 113, 32))
pushButton.setObjectName("pushButton")
pushButton.setText("PushButton")

MainWindow.show()
sys.exit(app.exec_())