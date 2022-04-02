import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QSplashScreen, QMainWindow

from modules.pxrfAnCalculator import PxrfAnCalculator

# if __name__ == '__main__':
# mf = ManageFile()
# cb = Calibration()
# pxrf = PxrfCalcul()


# ratios = pxrf.calcul_ratios(corrected_data)
# an_content = pxrf.calcul_an_content(ratios)
# print('An Content: ', an_content)

app = QtWidgets.QApplication(sys.argv)

pixmap = QPixmap("ui/img/logo.png")
splash = QSplashScreen(pixmap)
splash.show()
app.processEvents()
AnCalculator = PxrfAnCalculator()
splash.finish(AnCalculator)
app.exec()
