import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QSplashScreen, QMainWindow
from modules.pxrfAnCalculator import PxrfAnCalculator

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    pixmap = QPixmap("ui/img/logo.png")
    splash = QSplashScreen(pixmap)
    splash.show()
    app.processEvents()
    AnCalculator = PxrfAnCalculator()
    splash.finish(AnCalculator)
    app.exec()
