# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceXymTIp.ui'
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
    QGraphicsView, QGridLayout, QGroupBox, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_interface_(object):
    def setupUi(self, interface_):
        if not interface_.objectName():
            interface_.setObjectName(u"interface_")
        interface_.setEnabled(True)
        interface_.resize(1063, 786)
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(9)
        interface_.setFont(font)
        self.centralwidget = QWidget(interface_)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_app_title = QFrame(self.centralwidget)
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
        self.label_app_title.setFont(font1)
        self.label_app_title.setScaledContents(True)
        self.label_app_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_app_title)


        self.gridLayout.addWidget(self.frame_app_title, 0, 0, 1, 3)

        self.gb_importFile = QGroupBox(self.centralwidget)
        self.gb_importFile.setObjectName(u"gb_importFile")
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(10)
        font2.setKerning(False)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.gb_importFile.setFont(font2)
        self.verticalLayout_6 = QVBoxLayout(self.gb_importFile)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.l_typeFile = QLabel(self.gb_importFile)
        self.l_typeFile.setObjectName(u"l_typeFile")

        self.verticalLayout_6.addWidget(self.l_typeFile)

        self.cb_chooseTypeFile = QComboBox(self.gb_importFile)
        self.cb_chooseTypeFile.addItem("")
        icon = QIcon()
        icon.addFile(u"img/xlsx_.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.cb_chooseTypeFile.addItem(icon, "")
        self.cb_chooseTypeFile.addItem(icon, "")
        self.cb_chooseTypeFile.addItem(icon, "")
        self.cb_chooseTypeFile.setObjectName(u"cb_chooseTypeFile")
        self.cb_chooseTypeFile.setCursor(QCursor(Qt.ArrowCursor))

        self.verticalLayout_6.addWidget(self.cb_chooseTypeFile)

        self.tb_browserFile = QPushButton(self.gb_importFile)
        self.tb_browserFile.setObjectName(u"tb_browserFile")
        self.tb_browserFile.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"img/import.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.tb_browserFile.setIcon(icon1)

        self.verticalLayout_6.addWidget(self.tb_browserFile)


        self.gridLayout.addWidget(self.gb_importFile, 1, 0, 1, 1)

        self.verticalLine_divider = QFrame(self.centralwidget)
        self.verticalLine_divider.setObjectName(u"verticalLine_divider")
        self.verticalLine_divider.setFrameShape(QFrame.VLine)
        self.verticalLine_divider.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.verticalLine_divider, 1, 1, 7, 1)

        self.gv_chart = QGraphicsView(self.centralwidget)
        self.gv_chart.setObjectName(u"gv_chart")
        self.gv_chart.viewport().setProperty("cursor", QCursor(Qt.CrossCursor))
        self.gv_chart.setFrameShape(QFrame.NoFrame)

        self.gridLayout.addWidget(self.gv_chart, 1, 2, 4, 1)

        self.gb_validation = QGroupBox(self.centralwidget)
        self.gb_validation.setObjectName(u"gb_validation")
        self.gb_validation.setFont(font2)
        self.verticalLayout_23 = QVBoxLayout(self.gb_validation)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.cb_probeReference = QCheckBox(self.gb_validation)
        self.cb_probeReference.setObjectName(u"cb_probeReference")
        self.cb_probeReference.setEnabled(True)
        self.cb_probeReference.setIcon(icon)
        self.cb_probeReference.setIconSize(QSize(16, 16))
        self.cb_probeReference.setCheckable(False)

        self.verticalLayout_23.addWidget(self.cb_probeReference)

        self.cb_pxrfCalibration = QCheckBox(self.gb_validation)
        self.cb_pxrfCalibration.setObjectName(u"cb_pxrfCalibration")
        self.cb_pxrfCalibration.setIcon(icon)
        self.cb_pxrfCalibration.setCheckable(False)

        self.verticalLayout_23.addWidget(self.cb_pxrfCalibration)

        self.cb_unknowAnalysis = QCheckBox(self.gb_validation)
        self.cb_unknowAnalysis.setObjectName(u"cb_unknowAnalysis")
        self.cb_unknowAnalysis.setIcon(icon)
        self.cb_unknowAnalysis.setCheckable(False)

        self.verticalLayout_23.addWidget(self.cb_unknowAnalysis)


        self.gridLayout.addWidget(self.gb_validation, 2, 0, 1, 1)

        self.gb_calibration = QGroupBox(self.centralwidget)
        self.gb_calibration.setObjectName(u"gb_calibration")
        self.gb_calibration.setFont(font2)
        self.verticalLayout_9 = QVBoxLayout(self.gb_calibration)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pb_formatProbe = QPushButton(self.gb_calibration)
        self.pb_formatProbe.setObjectName(u"pb_formatProbe")
        self.pb_formatProbe.setEnabled(False)
        self.pb_formatProbe.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"img/format.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_formatProbe.setIcon(icon2)

        self.verticalLayout_9.addWidget(self.pb_formatProbe)

        self.pb_formatPXRF = QPushButton(self.gb_calibration)
        self.pb_formatPXRF.setObjectName(u"pb_formatPXRF")
        self.pb_formatPXRF.setEnabled(False)
        self.pb_formatPXRF.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_formatPXRF.setIcon(icon2)

        self.verticalLayout_9.addWidget(self.pb_formatPXRF)


        self.gridLayout.addWidget(self.gb_calibration, 3, 0, 1, 1)

        self.gb_traitment = QGroupBox(self.centralwidget)
        self.gb_traitment.setObjectName(u"gb_traitment")
        self.gb_traitment.setFont(font2)
        self.verticalLayout_8 = QVBoxLayout(self.gb_traitment)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pb_calibrer = QPushButton(self.gb_traitment)
        self.pb_calibrer.setObjectName(u"pb_calibrer")
        self.pb_calibrer.setEnabled(False)
        self.pb_calibrer.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"img/gears.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_calibrer.setIcon(icon3)

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
        icon4 = QIcon()
        icon4.addFile(u"img/start.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_start.setIcon(icon4)
        self.pb_start.setFlat(True)

        self.verticalLayout_8.addWidget(self.pb_start)


        self.gridLayout.addWidget(self.gb_traitment, 4, 0, 2, 1)

        self.tw_tabs = QTabWidget(self.centralwidget)
        self.tw_tabs.setObjectName(u"tw_tabs")
        font4 = QFont()
        font4.setFamilies([u"Poppins"])
        font4.setPointSize(11)
        self.tw_tabs.setFont(font4)
        self.tab_calibration_probe = QWidget()
        self.tab_calibration_probe.setObjectName(u"tab_calibration_probe")
        self.tw_tabs.addTab(self.tab_calibration_probe, "")
        self.tab_calibration_pxrf = QWidget()
        self.tab_calibration_pxrf.setObjectName(u"tab_calibration_pxrf")
        self.tw_tabs.addTab(self.tab_calibration_pxrf, "")
        self.tab_correction_factor = QWidget()
        self.tab_correction_factor.setObjectName(u"tab_correction_factor")
        self.tw_tabs.addTab(self.tab_correction_factor, "")
        self.tab_pxrf_analysis = QWidget()
        self.tab_pxrf_analysis.setObjectName(u"tab_pxrf_analysis")
        self.tw_tabs.addTab(self.tab_pxrf_analysis, "")
        self.tab_results = QWidget()
        self.tab_results.setObjectName(u"tab_results")
        self.tw_tabs.addTab(self.tab_results, "")

        self.gridLayout.addWidget(self.tw_tabs, 5, 2, 3, 1)

        self.gb_project = QGroupBox(self.centralwidget)
        self.gb_project.setObjectName(u"gb_project")
        self.gb_project.setEnabled(False)
        self.gb_project.setFont(font2)
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


        self.gridLayout.addWidget(self.gb_project, 6, 0, 1, 1)

        self.gb_resultCalcicite = QGroupBox(self.centralwidget)
        self.gb_resultCalcicite.setObjectName(u"gb_resultCalcicite")
        self.gb_resultCalcicite.setFont(font2)
        self.verticalLayout_15 = QVBoxLayout(self.gb_resultCalcicite)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.pb_extractResult = QPushButton(self.gb_resultCalcicite)
        self.pb_extractResult.setObjectName(u"pb_extractResult")
        self.pb_extractResult.setEnabled(False)
        self.pb_extractResult.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"img/save.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_extractResult.setIcon(icon5)
        self.pb_extractResult.setFlat(False)

        self.verticalLayout_15.addWidget(self.pb_extractResult)


        self.gridLayout.addWidget(self.gb_resultCalcicite, 7, 0, 1, 1)

        interface_.setCentralWidget(self.centralwidget)

        self.retranslateUi(interface_)

        self.pb_start.setDefault(True)
        self.tw_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(interface_)
    # setupUi

    def retranslateUi(self, interface_):
        interface_.setWindowTitle(QCoreApplication.translate("interface_", u"Calcicit\u00e9 Plagioclase par Fluorescence X Portative", None))
        self.label_app_title.setText(QCoreApplication.translate("interface_", u"FLUROSCENCE X PORTATIVE - An Calculator", None))
        self.gb_importFile.setTitle(QCoreApplication.translate("interface_", u"Importer un fichier", None))
        self.l_typeFile.setText(QCoreApplication.translate("interface_", u"Type de donn\u00e9es", None))
        self.cb_chooseTypeFile.setItemText(0, QCoreApplication.translate("interface_", u"- Choisir un type de donn\u00e9e -", None))
        self.cb_chooseTypeFile.setItemText(1, QCoreApplication.translate("interface_", u"Microsonde - Donn\u00e9es de ref\u00e9rence", None))
        self.cb_chooseTypeFile.setItemText(2, QCoreApplication.translate("interface_", u"Analyses pXRF - Donn\u00e9es de calibration", None))
        self.cb_chooseTypeFile.setItemText(3, QCoreApplication.translate("interface_", u"Analyses pXRF - Donn\u00e9es inconnues", None))

        self.tb_browserFile.setText(QCoreApplication.translate("interface_", u"Parcourir ...", None))
        self.gb_validation.setTitle(QCoreApplication.translate("interface_", u"Validation", None))
        self.cb_probeReference.setText(QCoreApplication.translate("interface_", u"Donn\u00e9es de Ref\u00e9rence - Microsonde", None))
        self.cb_pxrfCalibration.setText(QCoreApplication.translate("interface_", u"Donn\u00e9es de Calibration - pXRF", None))
        self.cb_unknowAnalysis.setText(QCoreApplication.translate("interface_", u"Donn\u00e9es d'analyses inconnu - pXRF", None))
        self.gb_calibration.setTitle(QCoreApplication.translate("interface_", u"Calibration", None))
        self.pb_formatProbe.setText(QCoreApplication.translate("interface_", u"Format -microsonde", None))
        self.pb_formatPXRF.setText(QCoreApplication.translate("interface_", u"Format - pXRF", None))
        self.gb_traitment.setTitle(QCoreApplication.translate("interface_", u"Traitement", None))
        self.pb_calibrer.setText(QCoreApplication.translate("interface_", u"Calibrer", None))
        self.pb_start.setText(QCoreApplication.translate("interface_", u"LANCER LE TRAITEMENT", None))
        self.tw_tabs.setTabText(self.tw_tabs.indexOf(self.tab_calibration_probe), QCoreApplication.translate("interface_", u"Calibration Microsonde", None))
        self.tw_tabs.setTabText(self.tw_tabs.indexOf(self.tab_calibration_pxrf), QCoreApplication.translate("interface_", u"Calibration pXRF", None))
        self.tw_tabs.setTabText(self.tw_tabs.indexOf(self.tab_correction_factor), QCoreApplication.translate("interface_", u"Facteur de correction", None))
        self.tw_tabs.setTabText(self.tw_tabs.indexOf(self.tab_pxrf_analysis), QCoreApplication.translate("interface_", u"Analyses pXRF", None))
        self.tw_tabs.setTabText(self.tw_tabs.indexOf(self.tab_results), QCoreApplication.translate("interface_", u"R\u00e9sultats", None))
        self.gb_project.setTitle(QCoreApplication.translate("interface_", u"Projets", None))
        self.pb_openProject.setText(QCoreApplication.translate("interface_", u"Ouvrir un projet", None))
        self.pb_saveProject.setText(QCoreApplication.translate("interface_", u"Enregistrer", None))
        self.pb_newProject.setText(QCoreApplication.translate("interface_", u"Nouveau projet", None))
        self.gb_resultCalcicite.setTitle(QCoreApplication.translate("interface_", u"R\u00e9sultat calcicit\u00e9", None))
        self.pb_extractResult.setText(QCoreApplication.translate("interface_", u"Extraire - Excel", None))
    # retranslateUi

