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


# CALIBRATION PXRF DATA
# workbook, file = mf.open_xlsx_file_('data/calibration_pxrf.xlsx')
# HEAD_CALIBRATION_PXRF_DATA_VALUE, CALIBRATION_PXRF_DATA = mf.compile_xlsx_calibration_to_dict(workbook, file)
# print('en-tete: ', HEAD_CALIBRATION_PXRF_DATA_VALUE)
# print('donnee brute: ', CALIBRATION_PXRF_DATA)
# cb.calcul_correction_factor_for_each_sample(calibration_chemical_element, CALIBRATION_PXRF_DATA)
# print('---------------------------------')
# cb.correction_factor(CORRECTION_FACTOR_BY_SAMPLE)

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
