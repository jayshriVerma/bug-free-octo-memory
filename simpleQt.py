import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    textLabel = QLabel(widget)
    textLabel.setText("Hello World!")
    textLabel.move(90, 85)

    widget.setGeometry(50, 50, 320, 200)
    widget.setWindowTitle("My first PyQt5 project")
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()

sys.exit(app.exec_())
#PyQT5 integrates well with native OS APIs. A great benefit of PYQT5 is the QT Designer, a tool that lets you visually compose UI with QT widgets.
#PyQt5 is a framework built around QT. QT (and PYQT5) supports cross-functional development. It supports Windows, Mac, Linux, and mobile platforms such as iOS and Android.
