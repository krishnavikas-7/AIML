import sys
import os
from apri import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.psympts)
     self.ui.pushButton_2.clicked.connect(self.crcsv)
     self.ui.pushButton_3.clicked.connect(self.pdtls)
     self.ui.pushButton_4.clicked.connect(self.assoc)
     self.ui.pushButton_5.clicked.connect(self.confi)
     self.ui.pushButton_6.clicked.connect(self.lft)

  def psympts(self):
    os.system("python factors1.py")       

  def crcsv(self):
    os.system("python createcsv1.py")

  def pdtls(self):
    os.system("python criminal1.py")

  def assoc(self):
    os.system("python apr1.py")

  def confi(self):
    os.system("python apr2.py")

  def lft(self):
    os.system("python apr3.py")
     
          
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
