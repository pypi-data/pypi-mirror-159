from PySide6.QtWidgets import QWidget, QFrame, QPushButton, QToolButton
from PySide6.QtGui import QMouseEvent, QKeyEvent, Qt


def emptyFunc(event=None):
    pass


class QsBaseWidget(QWidget):
    def __init__(self, parent: QWidget = None):
        super(QsBaseWidget, self).__init__(parent=parent)
        self._mousePressEvent = emptyFunc
        self._mouseReleaseEvent = emptyFunc
        self._mouseDoubleClickEvent = emptyFunc
        self._mouseMoveEvent = emptyFunc
        self._keyPressEvent = emptyFunc

    def bind(self, eventName, eventFunc):
        """
        mousePressEvent
        mouseReleaseEvent
        mouseDoubleClickEvent
        mouseMoveEvent
        keyPressEvent
        :param eventName: 事件名称
        :param eventFunc: 事件函数
        :return: 无
        """
        if eventName == 'mousePressEvent':
            self._mousePressEvent = eventFunc
        elif eventName == 'mouseReleaseEvent':
            self._mouseReleaseEvent = eventFunc
        elif eventName == 'mouseDoubleClickEvent':
            self._mouseDoubleClickEvent = eventFunc
        elif eventName == 'mouseMoveEvent':
            self._mouseMoveEvent = eventFunc
        elif eventName == 'keyPressEvent':
            self._keyPressEvent = eventFunc

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self._mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self._mouseReleaseEvent(event)

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        self._mouseDoubleClickEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self._mouseMoveEvent(event)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        self._keyPressEvent(event)


class QsBaseFrame(QFrame):
    def __init__(self, parent: QWidget = None):
        super(QsBaseFrame, self).__init__(parent=parent)
        self._mousePressEvent = emptyFunc
        self._mouseReleaseEvent = emptyFunc
        self._mouseDoubleClickEvent = emptyFunc
        self._mouseMoveEvent = emptyFunc
        self._keyPressEvent = emptyFunc

    def bind(self, eventName, eventFunc):
        """
        mousePressEvent
        mouseReleaseEvent
        mouseDoubleClickEvent
        mouseMoveEvent
        keyPressEvent
        :param eventName: 事件名称
        :param eventFunc: 事件函数
        :return: 无
        """
        if eventName == 'mousePressEvent':
            self._mousePressEvent = eventFunc
        elif eventName == 'mouseReleaseEvent':
            self._mouseReleaseEvent = eventFunc
        elif eventName == 'mouseDoubleClickEvent':
            self._mouseDoubleClickEvent = eventFunc
        elif eventName == 'mouseMoveEvent':
            self._mouseMoveEvent = eventFunc
        elif eventName == 'keyPressEvent':
            self._keyPressEvent = eventFunc

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self._mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self._mouseReleaseEvent(event)

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        self._mouseDoubleClickEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self._mouseMoveEvent(event)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        self._keyPressEvent(event)


class QsBasePushButton(QPushButton):
    def __init__(self, parent: QWidget = None, text: str = ""):
        super(QsBasePushButton, self).__init__(parent=parent, text=text)
        self._mousePressEvent = emptyFunc
        self._mouseReleaseEvent = emptyFunc
        self._mouseDoubleClickEvent = emptyFunc
        self._mouseMoveEvent = emptyFunc
        self._keyPressEvent = emptyFunc

    def bind(self, eventName, eventFunc):
        """
        mousePressEvent
        mouseReleaseEvent
        mouseDoubleClickEvent
        mouseMoveEvent
        keyPressEvent
        :param eventName: 事件名称
        :param eventFunc: 事件函数
        :return: 无
        """
        if eventName == 'mousePressEvent':
            self._mousePressEvent = eventFunc
        elif eventName == 'mouseReleaseEvent':
            self._mouseReleaseEvent = eventFunc
        elif eventName == 'mouseDoubleClickEvent':
            self._mouseDoubleClickEvent = eventFunc
        elif eventName == 'mouseMoveEvent':
            self._mouseMoveEvent = eventFunc
        elif eventName == 'keyPressEvent':
            self._keyPressEvent = eventFunc

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self._mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self._mouseReleaseEvent(event)

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        self._mouseDoubleClickEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self._mouseMoveEvent(event)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        self._keyPressEvent(event)


class QsBaseToolButton(QToolButton):
    def __init__(self, parent: QWidget = None):
        super(QsBaseToolButton, self).__init__(parent=parent)
        self._mousePressEvent = emptyFunc
        self._mouseReleaseEvent = emptyFunc
        self._mouseDoubleClickEvent = emptyFunc
        self._mouseMoveEvent = emptyFunc
        self._keyPressEvent = emptyFunc

    def bind(self, eventName, eventFunc):
        """
        mousePressEvent
        mouseReleaseEvent
        mouseDoubleClickEvent
        mouseMoveEvent
        keyPressEvent
        :param eventName: 事件名称
        :param eventFunc: 事件函数
        :return: 无
        """
        if eventName == 'mousePressEvent':
            self._mousePressEvent = eventFunc
        elif eventName == 'mouseReleaseEvent':
            self._mouseReleaseEvent = eventFunc
        elif eventName == 'mouseDoubleClickEvent':
            self._mouseDoubleClickEvent = eventFunc
        elif eventName == 'mouseMoveEvent':
            self._mouseMoveEvent = eventFunc
        elif eventName == 'keyPressEvent':
            self._keyPressEvent = eventFunc

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self._mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self._mouseReleaseEvent(event)

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        self._mouseDoubleClickEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self._mouseMoveEvent(event)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        self._keyPressEvent(event)
