from PySide6 import QtCore, QtGui, QtWidgets


class PaintableLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.circles = []
        self.setStyleSheet("background-color: transparent;")

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtCore.Qt.red)
        painter.setBrush(QtCore.Qt.red)
        for pos in self.circles:
            painter.drawEllipse(pos, 5, 5)
        painter.end()

    def add_circle(self, pos):
        self.circles.append(pos)
        self.update()

    def clear_circles(self):
        self.circles.clear()
        self.update()
