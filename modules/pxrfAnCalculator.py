from PySide6 import QtGui, QtCore, QtWidgets
from ui.ui_interface import Ui_Form
from modules.calibration import Calibration
from modules.manageFiles import ManageFile
from modules.pxrfCalcul import PxrfCalcul
from modules.projectManagment import ProjectManagment
from functools import partial
from modules.utils import *


class PxrfAnCalculator(Ui_Form, QtWidgets.QWidget, ManageFile, Calibration, PxrfCalcul, ProjectManagment):
    def __init__(self):
        super(PxrfAnCalculator, self).__init__()
        # Init Window
        self.setupUi(self)
        self.modification_setup_ui()
        self.setup_connections()
        self.show()

    def modification_setup_ui(self):
        pass

    def setup_connections(self):
        pass

    @staticmethod
    def import_files():
        pass

    def format_probe(self):
        pass

    def format_pxrf(self):
        pass

    def correction_factor_calculate(self):
        pass

    def start(self):
        pass

    def extract_result(self):
        pass

    def draw_chart(self):
        pass

    def draw_table(self, dataset):
        pass
