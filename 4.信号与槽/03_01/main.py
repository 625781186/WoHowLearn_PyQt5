# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5 import  QtGui, QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.a=1
        
        self.pushButton.clicked.connect(self.add1)
        self.pushButton_4.clicked.connect(self.add1)
        self.pushButton_5.clicked.connect(self.add1)
        self.pushButton_2.clicked.connect(self.reduce)
#        self.pushButton_2.clicked.connect(self.on_pushButton_pressed)
    
#    def add2(self):
#        self.a+=2
#        print("add2--", self.a)
        
    def add1(self):
        if self.sender().objectName()=="pushButton":
            self.a+=1
            print("add1--", self.a)            
        elif self.sender().objectName()=="pushButton_4":
            self.a+=2
            print("add2--", self.a)
        elif self.sender().objectName()=="pushButton_5":
            self.a+=3           
            print("add3--", self.a)
#        
#        print("add1--", self.a)
#        print(self.sender().text())
        
        
#    def add3(self):
#        self.a+=3
#        print("add3--", self.a)
        
        
    def reduce(self):
        self.a-=1
        print("red1--", self.a)
        
#    @pyqtSlot()
#    def on_pushButton_pressed(self):
#        print("按下")
#    
#    @pyqtSlot()
#    def on_pushButton_released(self):
#        
#        print("松开")
if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        
        ui = MainWindow()
    
        ui.show()
        sys.exit(app.exec_())        
    

