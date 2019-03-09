# -*- coding:utf-8 -*-
import maya.cmds as mc
import pymel.core as pm
from pymel.core import *
import maya.OpenMayaUI as omui
import maya.OpenMayaAnim as oma
import maya.OpenMaya as om
import maya.mel as mel
import inspect

import maya.OpenMayaUI as omui

import newWindow

reload(newWindow)

try:
    import  PySide2.QtCore as QtCore
    import  PySide2.QtGui as QtGui
    import  PySide2.QtWidgets as QtWidgets
    import  shiboken2 as shiboken
except:
    import  PySide.QtCore as QtCore
    import  PySide.QtGui as QtGui
    import  PySide.QtWidgets as QtWidgets
    import  shiboken as shiboken
finally:
    #打印消息
    pass

# try:
#     import  PySide2.QtCore as QtCore
#     import  PySide2.QtGui as QtGui
#     import shiboken2 as shiboken
# except:
#     import  PySide.QtCore as QtCore
#     import  PySide.QtGui as QtGui
#     import shiboken as shiboken
# finally:
#     #打印消息
#     print('成功导入PySide与shiboken'.decode('UTF-8').encode('GBK'))

# Learn Content
# Maya/PyMel  Move \ Namespace \ Sets \ ls \ select \ instance \ rotate
# AnimModule keyFrame


if __name__ == "__main__":
    # print(mc.namespace(exists=':foo'))
    # # mc.polyCube()
    # mc.namespace(set=':')
    # if mc.namespace(exists=':JOE') == False:
    #     mc.namespace(add='JOE')
    # mc.namespace(set=':JOE')
    # mc.polyCube()
    # mc.namespace(set=':')
    # if mc.namespace(exists=':BAR') == False:
    #     mc.namespace(add='BAR')
    #     print("create BAR !!!!!!!!!!!!")
    # else:
    #     print("BAR already existed !!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # mc.namespace(force=True,mv=('JOE','BAR'))
    # mc.namespace(rm='JOE')
    # mc.namespace(set=':BAR')
    # if mc.namespace(exists='TAIL') == False:
    #     mc.namespace(add='TAIL')
    # mc.namespace(set=':BAR:TAIL')
    # mc.polyCube()

    # if mc.namespace(exists=':BAR:HEAD') == False:
    #     mc.namespace(add=':BAR:HEAD',absoluteName=True)
    # mc.namespace(set=':BAR:HEAD')
    # mc.polyCube()
    # mc.select(ado=True)

    # print( mc.ls(sl=True))
    # print(mc.namespace(query=True,isRootNamespace="Foo"))
    # print("Finish--------------------------------!!!!")
    # mc.namespace(rm=":BAR:TAIL")
    # mc.namespace(force=True,rm=":BAR:HEAD",dnc=True)
    # print(mc.namespaceInfo(currentNamespace=True))
    # p1 = mc.polyCube(n='ppp1')
    # p2 = mc.polyCube(n='ppp2')
    # p3 = mc.polyCube(n='ppp3')
    # set1 = mc.sets(p1,p2,p3,name='set1Name')
    # mc.select(set1)
    # print( mc.sets(set1,query=True) )
    # mc.namespace(rm=":BAR")
    # mc.namespace(rm=":BAR:HEAD")
    # mc.sphere(n='sp1')
    # mc.move(3,0,0)
    # mc.sphere(n='sp2')
    # mc.move(-3,0,0)
    # mc.group('sp1','sp2',n='grp1')
    # mc.group('grp1',n='grp2')
    # mc.instance('sp1')
    # mc.instance('grp1',leaf=True)
    # mc.circle(n='circle1')
    # mc.instance()
    # mc.move(3,0,0)
    # mc.instance(smartTransform=True)
    # mc.instance(smartTransform=True)
    # mc.polyCube()
    # mc.move(1,1,1)
    # mc.move(5,x=True,relative=True)
    # oneInche = '1in'
    # print(type(oneInche))
    # mc.move(oneInche,oneInche,oneInche,relative=True,objectSpace=True,worldSpaceDistance=True)
    # mc.move(0,0,0,'pSphere1',absolute=True)
    # mc.circle(n='cirlce1')
    # mc.polyCube(ax=(0,1,0),n='cube1')
    # # mc.group('cube1',n='group1')
    # mc.select('cube1')
    # # mc.rotate(45,0,0,r=True)
    # # mc.rotate('45deg',0,0,r=True)
    # mc.rotate(0,x=True,relative=True)
    # # mc.rotate(15,20,30,a=True,forceOrderXYZ = True)
    # # mc.rotate(60,30,10,'group1',absolute=True)
    # # mc.rotate(45,x=True,relative=True,forceOrderXYZ=False)
    # mc.polyCube(name='cube2')
    # mc.select('cube1')
    # mc.rotate(0,45,0,'cube2',pivot=(1,0,0),t=True)
    # c1 = pm.polyCube()[0]
    # print(c1)
    # c2 = pm.polyCube()
    # print(c2[0])
    # objs = pm.ls(type='camera')
    # print(','.join([str(x) for x in objs]))
    # cam = objs[0]
    # print("camera 1 of %s is named %s"%(len(objs),objs[0]))
    # print(cam.shortName())
    # print(cam.longName())
    # pm.delete( pm.select(ado=True) )
    # orig = pm.polyCube(name="myCube")[0]
    # print ("the orig name now is %s !"%orig.shortName())
    # orig.rename('CrazyCube')
    # print ("the orig name now is %s !"%orig.shortName())
    # dl = pm.directionalLight()
    # print(type(dl))
    # print(isinstance(dl,pm.nodetypes.DirectionalLight))
    # print(isinstance(orig,pm.nodetypes.PolyCube))
    # print(type(cam))
    # cam = general.PyNode('persp')
    # c1 = pm.polyCube(name='MyCube')[0]
    # print(c1.tx.get())
    # print(c1.translate.get().x)
    # fullPath = pm.sceneName()
    # print(fullPath)
    # objs = pm.ls(type='camera')
    # c1.rename('CrazyCube')
    # print(c1.shortName())
    # print(c1.longName())
    # print(c1.getInstances())
    # print(','.join([str(x) for x in objs]))
    # cam = objs[0]
    # print cam
    # new = cam.replace('front','monkey')
    # print new
    # print type(new)
    # print type(cam)
    # print dir()
    # print dir(type(cam))
    # print inspect.getargspec(cam.replace)
    # print inspect.getargspec(c1.getInstances)
    # print cam.replace
    # cam = general.PyNode('persp')
    # print cam.visibility.get()
    # if cam.visibility.isKeyable() and not cam.visibility.isLocked():
    #     cam.visibility.set(True)
    #     cam.visibility.lock()
    # print cam.v.get()
    # print Attribute('persp.visibility')
    # print cam.rotateX.get()
    # print cam.tx.outputs()
    # c = pm.polyCube(name='testCube')[0]
    # print cam.tx>>c.tx
    # print cam.tx.outputs()
    # value = [4,5,6]
    # cam.translate.set(value)
    # print cam.translate.get()

    # win = window(title="my window")
    # layout = verticalLayout()
    # chkBox = checkBox(label = "my checkBox ",value =True, parent=layout)
    # btn = button(label='myBtn',parent = layout)
    # def btnPressed(*args):
    #     if chkBox.getValue():
    #         print "Check box is CHECKED!"
    #         btn.setLabel("Uncheck")
    #     else:
    #         print "Check box is UNCHECKED!"
    #         btn.setLabel("Check")
    # btn.setCommand(btnPressed)
    # def newBtnPressed(name):
    #     print "pressd %s"%name
    # names = ['chad','robert','james']
    # for name in names:
    #     button(label=name,command=Callback(newBtnPressed,name),parent = layout)
    # layout.redistribute(1,3,2,1)
    # win.show()

    # template = uiTemplate("ExampleTemplate", force=True)
    # template.define(button, width=100, height=40, align='mid')
    # template.define(frameLayout, borderVisible=True, labelVisible=False)
    #
    # with window(menuBar=True, menuBarVisible=True) as win:
    #     with template:
    #         with columnLayout(rowSpacing=0):
    #             with frameLayout():
    #                 with columnLayout():
    #                     button(label='One')
    #                     button(label='Two')
    #                     button(label='Three')
    #             with frameLayout():
    #                 with optionMenu():
    #                     menuItem(label='Red')
    #                     menuItem(label='Green')
    #                     menuItem(label='Blue')
    # with win:
    #     with menu():
    #         menuItem(label='One')
    #         menuItem(label='Two')
    #         with subMenuItem(label='Sub'):
    #             menuItem(label='A')
    #             menuItem(label='B')
    #         menuItem(label='Three')

    if __name__ == "__main__":
        # app = QtWidgets.QApplication(sys.argv)
        main = newWindow.SimpleDialogForm()
        main.show()  # 在外面只需要调用simpleDialogForm显示就行，不需要关注内部如何实现了。
        # sys.exit(app.exec_())

print('---------------------------finish-----------------------')
