from PySide6.QtCore import Qt, QMimeData, QPoint
from PySide6.QtGui import QDrag
from QtSimple6.QsBase import QsBaseWidget


class QsDrag(object):
    def __init__(self, widget: QsBaseWidget):
        self.widget = widget
        self.widget.bind("mousePressEvent", self.press)
        self.widget.bind("mouseMoveEvent", self.move)
        self.iniDragCor = [0, 0]

    def press(self, event):
        self.iniDragCor[0] = event.x()
        self.iniDragCor[1] = event.y()

    def move(self, event):
        x = event.x() - self.iniDragCor[0]
        y = event.y() - self.iniDragCor[1]

        cor = QPoint(x, y)
        self.widget.move(self.widget.mapToParent(QPoint(x, y)))  # 需要maptoparent一下才可以的,否则只是相对位置。
