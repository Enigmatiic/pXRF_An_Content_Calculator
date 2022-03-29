# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceLPypnd.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
                               QGraphicsView, QGridLayout, QGroupBox, QHeaderView,
                               QLabel, QPushButton, QSizePolicy, QTabWidget,
                               QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1061, 782)
        Form.setMinimumSize(QSize(1061, 782))
        Form.setMaximumSize(QSize(1061, 782))
        self.gridLayout_4 = QGridLayout(Form)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gb_calibration = QGroupBox(Form)
        self.gb_calibration.setObjectName(u"gb_calibration")
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(10)
        font.setKerning(False)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.gb_calibration.setFont(font)
        self.verticalLayout_9 = QVBoxLayout(self.gb_calibration)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pb_formatProbe = QPushButton(self.gb_calibration)
        self.pb_formatProbe.setObjectName(u"pb_formatProbe")
        self.pb_formatProbe.setEnabled(False)
        self.pb_formatProbe.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"img/format.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_formatProbe.setIcon(icon)

        self.verticalLayout_9.addWidget(self.pb_formatProbe)

        self.pb_formatPXRF = QPushButton(self.gb_calibration)
        self.pb_formatPXRF.setObjectName(u"pb_formatPXRF")
        self.pb_formatPXRF.setEnabled(False)
        self.pb_formatPXRF.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_formatPXRF.setIcon(icon)

        self.verticalLayout_9.addWidget(self.pb_formatPXRF)

        self.gridLayout_4.addWidget(self.gb_calibration, 3, 0, 1, 1)

        self.verticalLine_divider = QFrame(Form)
        self.verticalLine_divider.setObjectName(u"verticalLine_divider")
        self.verticalLine_divider.setFrameShape(QFrame.VLine)
        self.verticalLine_divider.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.verticalLine_divider, 1, 1, 7, 1)

        self.frame_app_title = QFrame(Form)
        self.frame_app_title.setObjectName(u"frame_app_title")
        self.frame_app_title.setStyleSheet(u"border-color: rgba(255, 255, 255, 0);")
        self.frame_app_title.setFrameShape(QFrame.NoFrame)
        self.frame_app_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_app_title)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_app_title = QLabel(self.frame_app_title)
        self.label_app_title.setObjectName(u"label_app_title")
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_app_title.setFont(font1)
        self.label_app_title.setStyleSheet(u"font: 700 24pt \"Poppins\";\n"
                                           "color: rgb(42, 42, 42);")
        self.label_app_title.setScaledContents(True)
        self.label_app_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_app_title)

        self.gridLayout_4.addWidget(self.frame_app_title, 0, 0, 1, 3)

        self.gb_project = QGroupBox(Form)
        self.gb_project.setObjectName(u"gb_project")
        self.gb_project.setEnabled(False)
        self.gb_project.setFont(font)
        self.gridLayout_2 = QGridLayout(self.gb_project)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pb_openProject = QPushButton(self.gb_project)
        self.pb_openProject.setObjectName(u"pb_openProject")
        self.pb_openProject.setCursor(QCursor(Qt.ForbiddenCursor))

        self.gridLayout_2.addWidget(self.pb_openProject, 2, 0, 1, 1)

        self.pb_saveProject = QPushButton(self.gb_project)
        self.pb_saveProject.setObjectName(u"pb_saveProject")
        self.pb_saveProject.setCursor(QCursor(Qt.ForbiddenCursor))

        self.gridLayout_2.addWidget(self.pb_saveProject, 3, 0, 1, 1)

        self.pb_newProject = QPushButton(self.gb_project)
        self.pb_newProject.setObjectName(u"pb_newProject")
        self.pb_newProject.setCursor(QCursor(Qt.ForbiddenCursor))

        self.gridLayout_2.addWidget(self.pb_newProject, 0, 0, 1, 1)

        self.gridLayout_4.addWidget(self.gb_project, 6, 0, 1, 1)

        self.gb_resultCalcicite = QGroupBox(Form)
        self.gb_resultCalcicite.setObjectName(u"gb_resultCalcicite")
        self.gb_resultCalcicite.setFont(font)
        self.verticalLayout_15 = QVBoxLayout(self.gb_resultCalcicite)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.pb_extractResult = QPushButton(self.gb_resultCalcicite)
        self.pb_extractResult.setObjectName(u"pb_extractResult")
        self.pb_extractResult.setEnabled(False)
        self.pb_extractResult.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"img/save.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_extractResult.setIcon(icon1)
        self.pb_extractResult.setFlat(False)

        self.verticalLayout_15.addWidget(self.pb_extractResult)

        self.gridLayout_4.addWidget(self.gb_resultCalcicite, 7, 0, 1, 1)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgba(217, 217, 217, .4);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tw_tabs = QTabWidget(self.frame_2)
        self.tw_tabs.setObjectName(u"tw_tabs")
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(11)
        self.tw_tabs.setFont(font2)
        self.tw_tabs.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tab_calibration_probe = QWidget()
        self.tab_calibration_probe.setObjectName(u"tab_calibration_probe")
        self.gridLayout_6 = QGridLayout(self.tab_calibration_probe)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tableWidget = QTableWidget(self.tab_calibration_probe)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_6.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.tw_tabs.addTab(self.tab_calibration_probe, "")
        self.tab_calibration_pxrf = QWidget()
        self.tab_calibration_pxrf.setObjectName(u"tab_calibration_pxrf")
        self.gridLayout_5 = QGridLayout(self.tab_calibration_pxrf)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tableWidget_2 = QTableWidget(self.tab_calibration_pxrf)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.gridLayout_5.addWidget(self.tableWidget_2, 0, 0, 1, 1)

        self.tw_tabs.addTab(self.tab_calibration_pxrf, "")
        self.tab_correction_factor = QWidget()
        self.tab_correction_factor.setObjectName(u"tab_correction_factor")
        self.gridLayout_7 = QGridLayout(self.tab_correction_factor)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.tableWidget_3 = QTableWidget(self.tab_correction_factor)
        self.tableWidget_3.setObjectName(u"tableWidget_3")

        self.gridLayout_7.addWidget(self.tableWidget_3, 0, 0, 1, 1)

        self.tw_tabs.addTab(self.tab_correction_factor, "")
        self.tab_pxrf_analysis = QWidget()
        self.tab_pxrf_analysis.setObjectName(u"tab_pxrf_analysis")
        self.gridLayout_8 = QGridLayout(self.tab_pxrf_analysis)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.tableWidget_4 = QTableWidget(self.tab_pxrf_analysis)
        self.tableWidget_4.setObjectName(u"tableWidget_4")

        self.gridLayout_8.addWidget(self.tableWidget_4, 0, 0, 1, 1)

        self.tw_tabs.addTab(self.tab_pxrf_analysis, "")
        self.tab_results = QWidget()
        self.tab_results.setObjectName(u"tab_results")
        self.gridLayout_9 = QGridLayout(self.tab_results)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.tableWidget_5 = QTableWidget(self.tab_results)
        self.tableWidget_5.setObjectName(u"tableWidget_5")

        self.gridLayout_9.addWidget(self.tableWidget_5, 0, 0, 1, 1)

        self.tw_tabs.addTab(self.tab_results, "")

        self.gridLayout_3.addWidget(self.tw_tabs, 0, 0, 1, 1)

        self.gridLayout_4.addWidget(self.frame_2, 5, 2, 3, 1)

        self.gb_importFile = QGroupBox(Form)
        self.gb_importFile.setObjectName(u"gb_importFile")
        self.gb_importFile.setFont(font)
        self.verticalLayout_6 = QVBoxLayout(self.gb_importFile)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.l_typeFile = QLabel(self.gb_importFile)
        self.l_typeFile.setObjectName(u"l_typeFile")

        self.verticalLayout_6.addWidget(self.l_typeFile)

        self.cb_chooseTypeFile = QComboBox(self.gb_importFile)
        self.cb_chooseTypeFile.addItem("")
        icon2 = QIcon()
        icon2.addFile(u"img/xlsx_.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.cb_chooseTypeFile.addItem(icon2, "")
        self.cb_chooseTypeFile.addItem(icon2, "")
        self.cb_chooseTypeFile.addItem(icon2, "")
        self.cb_chooseTypeFile.setObjectName(u"cb_chooseTypeFile")
        self.cb_chooseTypeFile.setCursor(QCursor(Qt.ArrowCursor))

        self.verticalLayout_6.addWidget(self.cb_chooseTypeFile)

        self.tb_browserFile = QPushButton(self.gb_importFile)
        self.tb_browserFile.setObjectName(u"tb_browserFile")
        self.tb_browserFile.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"img/import.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.tb_browserFile.setIcon(icon3)

        self.verticalLayout_6.addWidget(self.tb_browserFile)

        self.gridLayout_4.addWidget(self.gb_importFile, 1, 0, 1, 1)

        self.gb_validation = QGroupBox(Form)
        self.gb_validation.setObjectName(u"gb_validation")
        self.gb_validation.setFont(font)
        self.verticalLayout_23 = QVBoxLayout(self.gb_validation)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.cb_probeReference = QCheckBox(self.gb_validation)
        self.cb_probeReference.setObjectName(u"cb_probeReference")
        self.cb_probeReference.setEnabled(True)
        self.cb_probeReference.setIcon(icon2)
        self.cb_probeReference.setIconSize(QSize(16, 16))
        self.cb_probeReference.setCheckable(False)

        self.verticalLayout_23.addWidget(self.cb_probeReference)

        self.cb_pxrfCalibration = QCheckBox(self.gb_validation)
        self.cb_pxrfCalibration.setObjectName(u"cb_pxrfCalibration")
        self.cb_pxrfCalibration.setIcon(icon2)
        self.cb_pxrfCalibration.setCheckable(False)

        self.verticalLayout_23.addWidget(self.cb_pxrfCalibration)

        self.cb_unknowAnalysis = QCheckBox(self.gb_validation)
        self.cb_unknowAnalysis.setObjectName(u"cb_unknowAnalysis")
        self.cb_unknowAnalysis.setIcon(icon2)
        self.cb_unknowAnalysis.setCheckable(False)

        self.verticalLayout_23.addWidget(self.cb_unknowAnalysis)

        self.gridLayout_4.addWidget(self.gb_validation, 2, 0, 1, 1)

        self.gb_traitment = QGroupBox(Form)
        self.gb_traitment.setObjectName(u"gb_traitment")
        self.gb_traitment.setFont(font)
        self.verticalLayout_8 = QVBoxLayout(self.gb_traitment)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pb_calibrer = QPushButton(self.gb_traitment)
        self.pb_calibrer.setObjectName(u"pb_calibrer")
        self.pb_calibrer.setEnabled(False)
        self.pb_calibrer.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"img/gears.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_calibrer.setIcon(icon4)

        self.verticalLayout_8.addWidget(self.pb_calibrer)

        self.pb_start = QPushButton(self.gb_traitment)
        self.pb_start.setObjectName(u"pb_start")
        self.pb_start.setEnabled(False)
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setKerning(False)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.pb_start.setFont(font3)
        self.pb_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_start.setStyleSheet(u"color: rgb(44, 202, 57);\n"
                                    "background-color: rgb(85, 255, 127);")
        icon5 = QIcon()
        icon5.addFile(u"img/start.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_start.setIcon(icon5)
        self.pb_start.setFlat(True)

        self.verticalLayout_8.addWidget(self.pb_start)

        self.gridLayout_4.addWidget(self.gb_traitment, 4, 0, 2, 1)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(217, 217, 217, .4);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gv_chart = QGraphicsView(self.frame)
        self.gv_chart.setObjectName(u"gv_chart")
        self.gv_chart.viewport().setProperty("cursor", QCursor(Qt.CrossCursor))
        self.gv_chart.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gv_chart.setFrameShape(QFrame.NoFrame)

        self.gridLayout.addWidget(self.gv_chart, 0, 0, 1, 1)

        self.gridLayout_4.addWidget(self.frame, 1, 2, 4, 1)

        self.retranslateUi(Form)

        self.tw_tabs.setCurrentIndex(0)
        self.pb_start.setDefault(True)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"FLUROSCENCE X PORTATIVE - AN CALCULATOR", None))
        self.gb_calibration.setTitle(QCoreApplication.translate("Form", u"Calibration", None))
        self.pb_formatProbe.setText(QCoreApplication.translate("Form", u"Format - microsonde", None))
        self.pb_formatPXRF.setText(QCoreApplication.translate("Form", u"Format - pXRF", None))
        self.label_app_title.setText(QCoreApplication.translate("Form", u"FLUROSCENCE X PORTATIVE - AN CALCULATOR", None))
        self.gb_project.setTitle(QCoreApplication.translate("Form", u"Projets", None))
        self.pb_openProject.setText(QCoreApplication.translate("Form", u"Ouvrir un projet", None))
        self.pb_saveProject.setText(QCoreApplication.translate("Form", u"Enregistrer", None))
        self.pb_newProject.setText(QCoreApplication.translate("Form", u"Nouveau projet", None))
        self.gb_resultCalcicite.setTitle(QCoreApplication.translate("Form", u"R\u00e9sultat calcicit\u00e9", None))
        self.pb_extractResult.setText(QCoreApplication.translate("Form", u"Extraire - Excel", None))
        self.tw_tabs.setTabText(self.tw_tabs.indexOf(self.tab_calibration_probe), QCoreApplication.translate("Form", u"Calibration Microsonde", None))
        self.tw_tabs.setTabText(self.tw_tabs.indexOf(self.tab_calibration_pxrf), QCoreApplication.translate("Form", u"Calibration pXRF", None))
        self.tw_tabs.setTabText(self.tw_tabs.indexOf(self.tab_correction_factor), QCoreApplication.translate("Form", u"Facteur de correction", None))
        self.tw_tabs.setTabText(self.tw_tabs.indexOf(self.tab_pxrf_analysis), QCoreApplication.translate("Form", u"Analyses pXRF", None))
        self.tw_tabs.setTabText(self.tw_tabs.indexOf(self.tab_results), QCoreApplication.translate("Form", u"R\u00e9sultats", None))
        self.gb_importFile.setTitle(QCoreApplication.translate("Form", u"Importer un fichier", None))
        self.l_typeFile.setText(QCoreApplication.translate("Form", u"Type de donn\u00e9es", None))
        self.cb_chooseTypeFile.setItemText(0, QCoreApplication.translate("Form", u"- Choisir un type de donn\u00e9e -", None))
        self.cb_chooseTypeFile.setItemText(1, QCoreApplication.translate("Form", u"Microsonde - Donn\u00e9es de ref\u00e9rence", None))
        self.cb_chooseTypeFile.setItemText(2, QCoreApplication.translate("Form", u"Analyses pXRF - Donn\u00e9es de calibration", None))
        self.cb_chooseTypeFile.setItemText(3, QCoreApplication.translate("Form", u"Analyses pXRF - Donn\u00e9es inconnues", None))

        self.tb_browserFile.setText(QCoreApplication.translate("Form", u"Parcourir ...", None))
        self.gb_validation.setTitle(QCoreApplication.translate("Form", u"Validation", None))
        self.cb_probeReference.setText(QCoreApplication.translate("Form", u"Donn\u00e9es de Ref\u00e9rence - Microsonde", None))
        self.cb_pxrfCalibration.setText(QCoreApplication.translate("Form", u"Donn\u00e9es de Calibration - pXRF", None))
        self.cb_unknowAnalysis.setText(QCoreApplication.translate("Form", u"Donn\u00e9es d'analyses inconnu - pXRF", None))
        self.gb_traitment.setTitle(QCoreApplication.translate("Form", u"Traitement", None))
        self.pb_calibrer.setText(QCoreApplication.translate("Form", u"Facteur de correction", None))
        self.pb_start.setText(QCoreApplication.translate("Form", u"LANCER LE TRAITEMENT", None))
    # retranslateUi
