from PySide6 import QtCore, QtGui, QtWidgets

# https://stackoverflow.com/questions/59914185/pyqt5-mouse-tracking-over-qlabel-object


class MouseTracker(QtCore.QObject):
    positionChanged = QtCore.Signal(QtCore.QPoint)
    clicked = QtCore.Signal(QtCore.QPoint)

    def __init__(self, widget):
        super().__init__(widget)
        self._widget = widget
        self.set_enabled(True)

    @property
    def widget(self):
        return self._widget

    def set_enabled(self, enabled):
        self.widget.setMouseTracking(enabled)
        self.widget.setAttribute(QtCore.Qt.WA_Hover, enabled)
        if enabled:
            self.widget.installEventFilter(self)
        else:
            self.widget.removeEventFilter(self)

    def eventFilter(self, o, e):
        if o is self.widget:
            if e.type() == QtCore.QEvent.MouseMove:
                self.positionChanged.emit(e.pos())
            elif e.type() == QtCore.QEvent.MouseButtonPress and e.button() == QtCore.Qt.LeftButton:
                self.clicked.emit(e.pos())
        return super().eventFilter(o, e)
