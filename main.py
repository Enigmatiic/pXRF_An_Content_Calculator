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

# UNKNOWN DATA
# workbook, file = mf.open_xlsx_file_('data/data.xlsx')
# HEAD_DATAS_VALUE, UNKNOWN_DATA = mf.compile_xlsx_to_dict(workbook, file)
# UNKNOWN_DATA = pxrf.format_data(UNKNOWN_DATA)
# UNKNOWN_DATA_ELEMENTS = extract_elements(UNKNOWN_DATA)




# corrected_data = PxrfCalcul.correct_data(UNKNOWN_DATA_ELEMENTS)

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
