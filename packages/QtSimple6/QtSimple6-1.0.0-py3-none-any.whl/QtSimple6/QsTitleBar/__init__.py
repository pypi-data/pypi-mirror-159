from QtSimple6.QsBase import QsBaseFrame, QWidget
from QtSimple6.QsDrag import QsDrag
from sys import exit


class QsTitleBar(QsBaseFrame):
    def __init__(self, parent: QWidget, window: QWidget):
        super(QsTitleBar, self).__init__(parent=parent)
        self._window = window

    def showMininizedWindow(self):
        self._window.showMinimized()

    def showMaximizedWindow(self):
        self._window.showMaximized()

    def showRestoreWindow(self):
        if self._window.isMaximized():
            self._window.showNormal()
        else:
            self._window.showMaximized()

    def closeWindow(self):
        self._window.close()

    def mouseDoubleClickEvent(self, event):
        self.showRestoreWindow()
        return QWidget().mouseDoubleClickEvent(event)

    def mousePressEvent(self, event):
        self.isPressed = True
        self.startPos = event.globalPosition().toPoint()
        return QWidget().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.isPressed = False
        return QWidget().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if self.isPressed:
            if self._window.isMaximized:
                self._window.showNormal()

            movePos = event.globalPosition().toPoint() - self.startPos
            self.startPos = event.globalPosition().toPoint()
            self._window.move(self._window.pos() + movePos)

        return QWidget().mouseMoveEvent(event)
