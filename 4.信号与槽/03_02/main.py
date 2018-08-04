# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5 import  QtGui, QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Ui_main import Ui_MainWindow
import functools


class MainWindow(QMainWindow, Ui_MainWindow):
    mySignal = pyqtSignal(str)
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
#        self.pushButton.clicked.connect(lambda:print("你好"))
        self.pushButton.clicked.connect(lambda:self.mypr("大家好"))
        self.pushButton.clicked.connect(lambda:self.mySignal.emit("我好"))
        self.listWidget.currentRowChanged.connect(self.mypr)
        self.myfun = functools.partial(self.mypr, "123", "456", )
        self.myfun()
        
        self.mySignal.connect(self.mypr2)
    def mypr(self , *a ):
        print(a)
#        self.mySignal.emit("我好")
    def mypr2(self , *b ):
        print(b)
        
if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        
        ui = MainWindow()
    
        ui.show()
        sys.exit(app.exec_())        
    

