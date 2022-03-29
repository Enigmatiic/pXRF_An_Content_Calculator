from PySide6 import QtGui, QtCore, QtWidgets
from ui.ui_interface import Ui_Form
from functools import partial
from modules.calibration import Calibration
from modules.manageFiles import ManageFile
from modules.pxrfCalcul import PxrfCalcul
from modules.utils import *


class PxrfAnCalculator(Ui_Form, QtWidgets.QWidget, ManageFile, Calibration, PxrfCalcul):
    def __init__(self):
        super(PxrfAnCalculator, self).__init__()
        # Init Window
        self.setupUi(self)
        # self.modificationSetupUi()
        # self.setupConnections()
        # self.setupRaccourcisClaviers()
        self.show()


# if __name__ == '__main__':
# mf = ManageFile()
# cb = Calibration()
# pxrf = PxrfCalcul()

# UNKNOWN DATA
# workbook, file = mf.open_xlsx_file_('data/data.xlsx')
# HEAD_DATAS_VALUE, UNKNOWN_DATA = mf.compile_xlsx_to_dict(workbook, file)
# UNKNOWN_DATA = pxrf.format_data(UNKNOWN_DATA)
# UNKNOWN_DATA_ELEMENTS = extract_elements(UNKNOWN_DATA)

# REFERENCE PROBE DATA
# workbook, file = mf.open_xlsx_file_('data/probe_data.xlsx')
# HEAD_PROBE_REFERENCE_DATA_VALUE, PROBE_REFERENCE_DATA = mf.compile_xlsx_to_dict(workbook, file)
# print(HEAD_PROBE_REFERENCE_DATA_VALUE)
# print(PROBE_REFERENCE_DATA)
# calibration_chemical_element, non_convertible_oxid = cb.convert_oxid_to_element(PROBE_REFERENCE_DATA)
# print('---------------------------------')
# print('Chemical: ', calibration_chemical_element)
# print('Non-convertible: ', non_convertible_oxid)

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

MainWindow = QtWidgets.QApplication([])
AnCalculator = PxrfAnCalculator()
MainWindow.exec()
