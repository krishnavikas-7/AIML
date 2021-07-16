import sys
from factors import *
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3
con = sqlite3.connect('crime1')


class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues) 

   

  def insertvalues(self):
         
     with con:
    
        cur = con.cursor()
        fact1 = str(self.ui.lineEdit_14.text())
        fact2 = str(self.ui.lineEdit_4.text())
        fact3 = str(self.ui.lineEdit_5.text())
        fact4 = str(self.ui.lineEdit_6.text())
        fact5 = str(self.ui.lineEdit_7.text())	
        cur.execute('INSERT INTO factors VALUES(?,?,?,?,?)',(fact1,fact2,fact3,fact4,fact5))
        con.commit()
        
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


