# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5 import  QtGui, QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_main import Ui_MainWindow


class MainWindow__(Ui_MainWindow, QMainWindow):
    b=20
    def __init__(self, parent=None):
        print("b", self.b)
        super(MainWindow__, self).__init__(parent)
        #从继承的界面类 调用实例化对象的函数
        self.setupUi(self)
        
        self.resize(200, 200)
#        print("MainWindow__", self)

        self.a=10
        c=30        
        self.myprint()
        self.myprint1()
        self.myprint1(c)
        
        self.mybutton = MyPushButton(self)
        self.mybutton1 = MyPushButton(self)
        self.mybutton1.setGeometry(QtCore.QRect(70, 100, 80, 20))
        self.mybutton1.setText("改变按钮")
        
    def myprint(self):
        print("a", self.a)
    def myprint1(self, *x):
        print("c", x)

class MyPushButton(QPushButton):
    def __init__(self, parent=None):
        super(MyPushButton, self).__init__(parent)
        self.setText("我的按钮")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    ui = MainWindow__()

    ui.show()
    sys.exit(app.exec_())
