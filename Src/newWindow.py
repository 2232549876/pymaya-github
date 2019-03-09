# -*- coding:utf-8 -*-
import sys
import os

# sys.path.remove("E:\Program Files\Autodesk\Maya2018\Python\PyMayaProjects\pymaya\Src")
# sys.path.append("E:\Python2.7\projects\pybench\pymaya\Src")
# sys.path.remove("E:\Python2.7\projects\pybench\pymaya\Src\Edu")

pcwd = os.getcwd()
if pcwd not in sys.path:
    sys.path.append(pcwd)
else:
    pass
    # print("%s already exists in sys path !\n"%pcwd )
# print("\n".join(sys.path))

import maya.OpenMayaUI as omui

try:
    from  PySide2.QtCore import *
    from  PySide2.QtGui import *
    from  PySide2.QtWidgets import *
    import  shiboken2 as shiboken
except:
    from  PySide.QtCore import *
    from  PySide.QtGui import *
    from  PySide.QtWidgets import *
    import  shiboken as shiboken
finally:
    #打印消息
    pass
    # print('成功导入PySide与shiboken'.decode('UTF-8').encode('GBK'))

import untitled
reload(untitled)
from untitled import *

def getMayaMainWin():
    mainWinWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = shiboken.wrapInstance(long(mainWinWindowPtr),QtWidgets.QWidget)
    return mayaMainWindow

class myWin(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        super(myWin,self).__init__(*args,**kwargs)
        self.setParent(getMayaMainWin())
        self.setWindowFlags(Qt.Window)
        self.setupUi(self)
        self.connectSignals()
    def connectSignals(self):
        print("connects signals")

if __name__ == "__main__":

    # A QApplication instance called mayapy.exe already exists.
    # app=QtWidgets.QApplication(sys.argv)
    ui = myWin()
    ui.resize(500,10)
    ui.show()
    print( ui.objectName() )
    print("finish!!!")
