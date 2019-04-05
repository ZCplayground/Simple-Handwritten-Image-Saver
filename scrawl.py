import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)

qtCreatorFile = "E:/code/2d_draw/2D_draw.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyDraw(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.pix = QPixmap(400, 400)          # 画布大小
        self.pix.fill(QColor(255, 255, 255))  # 白色背景
        self.endPoint = QPoint()
        self.lastPoint = QPoint()
        self.painter = QPainter()

        self.btn1 = QPushButton('Save', self)    # 保存按钮
        self.btn1.resize(self.btn1.sizeHint())   # 给按钮一个推荐的大小
        self.btn1.move(500, 50) 
        self.btn1.clicked.connect(self.btn_save)
        
        self.btn2 = QPushButton('Clear', self)   # 清空按钮
        self.btn2.resize(self.btn2.sizeHint())  
        self.btn2.move(500, 100) 
        self.btn2.clicked.connect(self.btn_clear)

    def btn_save(self, event):
        directory = QtWidgets.QFileDialog.getSaveFileName(self, 
              "getSaveFileName","./",
              "All Files (*);;JPG (*.jpg)") 
        self.pix.save(directory[0])

    def btn_clear(self, event):
        self.pix = QPixmap(400, 400)          
        self.pix.fill(QColor(255, 255, 255)) 
        self.update();

    def paintEvent(self, event):
        self.painter.begin(self)
        self.painter.drawPixmap(0, 0, self.pix)
        self.painter.end()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint

    def mouseMoveEvent(self, event):
            if event.buttons() == Qt.LeftButton:      
                self.endPoint = event.pos()            
                self.painter.begin(self.pix)        
                pen = QPen(Qt.black, 5, Qt.SolidLine) # 画笔，参数分别是颜色、粗、线条类型
                self.painter.setPen(pen)
                self.painter.drawLine(self.lastPoint, self.endPoint)
                self.painter.end()
                self.update()
                self.lastPoint = self.endPoint

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyDraw()
    window.show()
    sys.exit(app.exec_())