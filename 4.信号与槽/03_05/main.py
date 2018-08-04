# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""

from PyQt5 import  QtGui, QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Ui_main import Ui_Form
import time

class MyThread(QThread):
    endSignal=pyqtSignal(str)
    def __init(self):
        super(MyThread, self).__init__()
        
    def run(self):
        print("开始")  
        time.sleep(5)
        print("结束")
        self.endSignal.emit( "我睡饱了")
#        self.label.setText("结束")

    def _start(self, label):
        self.label = label
        self.start()
        
class Form(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):

        super(Form, self).__init__(parent)
        self.setupUi(self)
        self.MyThread = MyThread(self.label)
        self.MyThread.endSignal.connect(self.label.setText)
        
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.MyThread._start(self.label)
        self.label.setText("开始")
if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        
        ui = Form()
    
        ui.show()
        sys.exit(app.exec_())        
    

