# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceiAAfgl.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1203, 793)
        Form.setMinimumSize(QSize(1203, 793))
        Form.setMaximumSize(QSize(1203, 793))
        self.gridLayout_11 = QGridLayout(Form)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_app_title = QFrame(Form)
        self.frame_app_title.setObjectName(u"frame_app_title")
        self.frame_app_title.setStyleSheet(u"border-color: rgba(255, 255, 255, 0);")
        self.frame_app_title.setFrameShape(QFrame.NoFrame)
        self.frame_app_title.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_app_title)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_app_title = QLabel(self.frame_app_title)
        self.label_app_title.setObjectName(u"label_app_title")
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        self.label_app_title.setFont(font)
        self.label_app_title.setStyleSheet(u"font: 700 24pt \"Poppins\";\n"
"color: rgb(42, 42, 42);")
        self.label_app_title.setScaledContents(True)
        self.label_app_title.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_app_title, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_app_title, 0, 2, 1, 1)

        self.gb_importFile = QGroupBox(Form)
        self.gb_importFile.setObjectName(u"gb_importFile")
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(10)
        font1.setKerning(False)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.gb_importFile.setFont(font1)
        self.verticalLayout_6 = QVBoxLayout(self.gb_importFile)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.l_typeFile = QLabel(self.gb_importFile)
        self.l_typeFile.setObjectName(u"l_typeFile")

        self.verticalLayout_6.addWidget(self.l_typeFile)

        self.select_chooseTypeFile = QComboBox(self.gb_importFile)
        self.select_chooseTypeFile.addItem("")
        icon = QIcon()
        icon.addFile(u"ui/img/xlsx_.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.select_chooseTypeFile.addItem(icon, "")
        self.select_chooseTypeFile.addItem(icon, "")
        self.select_chooseTypeFile.addItem(icon, "")
        self.select_chooseTypeFile.setObjectName(u"select_chooseTypeFile")
        self.select_chooseTypeFile.setCursor(QCursor(Qt.ArrowCursor))

        self.verticalLayout_6.addWidget(self.select_chooseTypeFile)

        self.pb_browserFile = QPushButton(self.gb_importFile)
        self.pb_browserFile.setObjectName(u"pb_browserFile")
        self.pb_browserFile.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"ui/img/import.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_browserFile.setIcon(icon1)

        self.verticalLayout_6.addWidget(self.pb_browserFile)


        self.gridLayout_11.addWidget(self.gb_importFile, 2, 0, 1, 1)

        self.gb_project = QGroupBox(Form)
        self.gb_project.setObjectName(u"gb_project")
        self.gb_project.setEnabled(False)
        self.gb_project.setFont(font1)
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


        self.gridLayout_11.addWidget(self.gb_project, 6, 0, 1, 1)

        self.gb_validation = QGroupBox(Form)
        self.gb_validation.setObjectName(u"gb_validation")
        self.gb_validation.setFont(font1)
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

        self.cb_unknownAnalysis = QCheckBox(self.gb_validation)
        self.cb_unknownAnalysis.setObjectName(u"cb_unknownAnalysis")
        self.cb_unknownAnalysis.setIcon(icon)
        self.cb_unknownAnalysis.setCheckable(False)

        self.verticalLayout_23.addWidget(self.cb_unknownAnalysis)


        self.gridLayout_11.addWidget(self.gb_validation, 3, 0, 1, 1)

        self.verticalLine_divider = QFrame(Form)
        self.verticalLine_divider.setObjectName(u"verticalLine_divider")
        self.verticalLine_divider.setFrameShape(QFrame.VLine)
        self.verticalLine_divider.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.verticalLine_divider, 1, 1, 7, 1)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.l_img_logo = QLabel(self.frame_3)
        self.l_img_logo.setObjectName(u"l_img_logo")
        self.l_img_logo.setLayoutDirection(Qt.LeftToRight)
        self.l_img_logo.setPixmap(QPixmap(u"ui/img/logo_1.png"))
        self.l_img_logo.setScaledContents(False)
        self.l_img_logo.setAlignment(Qt.AlignCenter)
        self.l_img_logo.setWordWrap(True)

        self.gridLayout_4.addWidget(self.l_img_logo, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_3, 0, 0, 2, 1)

        self.gb_calibration = QGroupBox(Form)
        self.gb_calibration.setObjectName(u"gb_calibration")
        self.gb_calibration.setFont(font1)
        self.verticalLayout_9 = QVBoxLayout(self.gb_calibration)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pb_formatProbe = QPushButton(self.gb_calibration)
        self.pb_formatProbe.setObjectName(u"pb_formatProbe")
        self.pb_formatProbe.setEnabled(False)
        self.pb_formatProbe.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"ui/img/format.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_formatProbe.setIcon(icon2)

        self.verticalLayout_9.addWidget(self.pb_formatProbe)

        self.pb_formatPXRF = QPushButton(self.gb_calibration)
        self.pb_formatPXRF.setObjectName(u"pb_formatPXRF")
        self.pb_formatPXRF.setEnabled(False)
        self.pb_formatPXRF.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_formatPXRF.setIcon(icon2)

        self.verticalLayout_9.addWidget(self.pb_formatPXRF)


        self.gridLayout_11.addWidget(self.gb_calibration, 4, 0, 1, 1)

        self.gb_resultCalcicite = QGroupBox(Form)
        self.gb_resultCalcicite.setObjectName(u"gb_resultCalcicite")
        self.gb_resultCalcicite.setFont(font1)
        self.verticalLayout_15 = QVBoxLayout(self.gb_resultCalcicite)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.pb_extractResult = QPushButton(self.gb_resultCalcicite)
        self.pb_extractResult.setObjectName(u"pb_extractResult")
        self.pb_extractResult.setEnabled(False)
        self.pb_extractResult.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"ui/img/save.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_extractResult.setIcon(icon3)
        self.pb_extractResult.setFlat(False)

        self.verticalLayout_15.addWidget(self.pb_extractResult)


        self.gridLayout_11.addWidget(self.gb_resultCalcicite, 7, 0, 1, 1)

        self.gb_traitment = QGroupBox(Form)
        self.gb_traitment.setObjectName(u"gb_traitment")
        self.gb_traitment.setFont(font1)
        self.verticalLayout_8 = QVBoxLayout(self.gb_traitment)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pb_calibrer = QPushButton(self.gb_traitment)
        self.pb_calibrer.setObjectName(u"pb_calibrer")
        self.pb_calibrer.setEnabled(False)
        self.pb_calibrer.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"ui/img/gears.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_calibrer.setIcon(icon4)

        self.verticalLayout_8.addWidget(self.pb_calibrer)

        self.pb_start = QPushButton(self.gb_traitment)
        self.pb_start.setObjectName(u"pb_start")
        self.pb_start.setEnabled(False)
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setKerning(False)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.pb_start.setFont(font2)
        self.pb_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_start.setStyleSheet(u"color: rgb(44, 202, 57);\n"
"background-color: rgb(85, 255, 127);")
        icon5 = QIcon()
        icon5.addFile(u"ui/img/start.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_start.setIcon(icon5)
        self.pb_start.setFlat(True)

        self.verticalLayout_8.addWidget(self.pb_start)


        self.gridLayout_11.addWidget(self.gb_traitment, 5, 0, 1, 1)

        self.frame_tabs = QFrame(Form)
        self.frame_tabs.setObjectName(u"frame_tabs")
        self.frame_tabs.setStyleSheet(u"background-color: rgba(217, 217, 217, .4);")
        self.frame_tabs.setFrameShape(QFrame.StyledPanel)
        self.frame_tabs.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_tabs)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tw_tabs = QTabWidget(self.frame_tabs)
        self.tw_tabs.setObjectName(u"tw_tabs")
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setPointSize(11)
        self.tw_tabs.setFont(font3)
        self.tw_tabs.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tab_calibration_probe = QWidget()
        self.tab_calibration_probe.setObjectName(u"tab_calibration_probe")
        self.gridLayout_6 = QGridLayout(self.tab_calibration_probe)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.table_calibration_probe = QTableWidget(self.tab_calibration_probe)
        self.table_calibration_probe.setObjectName(u"table_calibration_probe")
        self.table_calibration_probe.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_calibration_probe.setDragDropOverwriteMode(False)

        self.gridLayout_6.addWidget(self.table_calibration_probe, 0, 0, 1, 1)

        self.tw_tabs.addTab(self.tab_calibration_probe, "")
        self.tab_calibration_pxrf = QWidget()
        self.tab_calibration_pxrf.setObjectName(u"tab_calibration_pxrf")
        self.gridLayout_5 = QGridLayout(self.tab_calibration_pxrf)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.table_calibration_pxrf = QTableWidget(self.tab_calibration_pxrf)
        self.table_calibration_pxrf.setObjectName(u"table_calibration_pxrf")
        self.table_calibration_pxrf.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_5.addWidget(self.table_calibration_pxrf, 0, 0, 1, 1)

        self.tw_tabs.addTab(self.tab_calibration_pxrf, "")
        self.tab_correction_factor = QWidget()
        self.tab_correction_factor.setObjectName(u"tab_correction_factor")
        self.gridLayout_7 = QGridLayout(self.tab_correction_factor)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.table_correction_factor = QTableWidget(self.tab_correction_factor)
        self.table_correction_factor.setObjectName(u"table_correction_factor")
        self.table_correction_factor.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_7.addWidget(self.table_correction_factor, 0, 0, 1, 1)

        self.tw_tabs.addTab(self.tab_correction_factor, "")
        self.tab_pxrf_analysis = QWidget()
        self.tab_pxrf_analysis.setObjectName(u"tab_pxrf_analysis")
        self.gridLayout_8 = QGridLayout(self.tab_pxrf_analysis)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.table_pxrf_analysis = QTableWidget(self.tab_pxrf_analysis)
        self.table_pxrf_analysis.setObjectName(u"table_pxrf_analysis")
        self.table_pxrf_analysis.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_8.addWidget(self.table_pxrf_analysis, 0, 0, 1, 1)

        self.tw_tabs.addTab(self.tab_pxrf_analysis, "")
        self.tab_results = QWidget()
        self.tab_results.setObjectName(u"tab_results")
        self.gridLayout_9 = QGridLayout(self.tab_results)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.table_results = QTableWidget(self.tab_results)
        self.table_results.setObjectName(u"table_results")
        self.table_results.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_9.addWidget(self.table_results, 0, 0, 1, 1)

        self.tw_tabs.addTab(self.tab_results, "")

        self.gridLayout_3.addWidget(self.tw_tabs, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_tabs, 1, 2, 7, 1)


        self.retranslateUi(Form)

        self.pb_start.setDefault(True)
        self.tw_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"pXRF An Calculator", None))
        self.label_app_title.setText(QCoreApplication.translate("Form", u"An Content Calculator by Portable X-Ray", None))
        self.gb_importFile.setTitle(QCoreApplication.translate("Form", u"Importer un fichier", None))
        self.l_typeFile.setText(QCoreApplication.translate("Form", u"Type de donn\u00e9es", None))
        self.select_chooseTypeFile.setItemText(0, QCoreApplication.translate("Form", u"- Choisir un type de donn\u00e9e -", None))
        self.select_chooseTypeFile.setItemText(1, QCoreApplication.translate("Form", u"Microsonde - Donn\u00e9es de ref\u00e9rence", None))
        self.select_chooseTypeFile.setItemText(2, QCoreApplication.translate("Form", u"Analyses pXRF - Donn\u00e9es de calibration", None))
        self.select_chooseTypeFile.setItemText(3, QCoreApplication.translate("Form", u"Analyses pXRF - Donn\u00e9es inconnues", None))

        self.pb_browserFile.setText(QCoreApplication.translate("Form", u"Parcourir ...", None))
        self.gb_project.setTitle(QCoreApplication.translate("Form", u"Projets", None))
        self.pb_openProject.setText(QCoreApplication.translate("Form", u"Ouvrir un projet", None))
        self.pb_saveProject.setText(QCoreApplication.translate("Form", u"Enregistrer", None))
        self.pb_newProject.setText(QCoreApplication.translate("Form", u"Nouveau projet", None))
        self.gb_validation.setTitle(QCoreApplication.translate("Form", u"Validation", None))
        self.cb_probeReference.setText(QCoreApplication.translate("Form", u"Donn\u00e9es de Ref\u00e9rence - Microsonde", None))
        self.cb_pxrfCalibration.setText(QCoreApplication.translate("Form", u"Donn\u00e9es de Calibration - pXRF", None))
        self.cb_unknownAnalysis.setText(QCoreApplication.translate("Form", u"Donn\u00e9es d'analyses inconnu - pXRF", None))
        self.l_img_logo.setText("")
        self.gb_calibration.setTitle(QCoreApplication.translate("Form", u"Calibration", None))
        self.pb_formatProbe.setText(QCoreApplication.translate("Form", u"Format -microsonde", None))
        self.pb_formatPXRF.setText(QCoreApplication.translate("Form", u"Format - pXRF", None))
        self.gb_resultCalcicite.setTitle(QCoreApplication.translate("Form", u"R\u00e9sultat calcicit\u00e9", None))
        self.pb_extractResult.setText(QCoreApplication.translate("Form", u"Extraire - Excel", None))
        self.gb_traitment.setTitle(QCoreApplication.translate("Form", u"Traitement", None))
        self.pb_calibrer.setText(QCoreApplication.translate("Form", u"Corriger les donn\u00e9es", None))
        self.pb_start.setText(QCoreApplication.translate("Form", u"LANCER LE TRAITEMENT", None))
        self.tw_tabs.setTabText(self.tw_tabs.indexOf(self.tab_calibration_probe), QCoreApplication.translate("Form", u"Calibration Microsonde", None))
        self.tw_tabs.setTabText(self.tw_tabs.indexOf(self.tab_calibration_pxrf), QCoreApplication.translate("Form", u"Calibration pXRF", None))
        self.tw_tabs.setTabText(self.tw_tabs.indexOf(self.tab_correction_factor), QCoreApplication.translate("Form", u"Facteur de correction", None))
        self.tw_tabs.setTabText(self.tw_tabs.indexOf(self.tab_pxrf_analysis), QCoreApplication.translate("Form", u"Analyses pXRF corrig\u00e9es", None))
        self.tw_tabs.setTabText(self.tw_tabs.indexOf(self.tab_results), QCoreApplication.translate("Form", u"R\u00e9sultats", None))
    # retranslateUi

