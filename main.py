import sys, os

from PySide6 import QtWidgets
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QSplashScreen, QMainWindow
from modules.pxrfAnCalculator import PxrfAnCalculator

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll
    myappid = 'itzadn.pxrfancalculator.v-0-1-0-alpha'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    pixmap = QPixmap(os.path.join(basedir, "ui/img/", "logo.png"))
    splash = QSplashScreen(pixmap)
    splash.show()
    app.processEvents()
    app.setWindowIcon(QIcon(os.path.join(basedir, "ui/img/", "logo_1.ico")))
    AnCalculator = PxrfAnCalculator()
    splash.finish(AnCalculator)
    app.exec()
