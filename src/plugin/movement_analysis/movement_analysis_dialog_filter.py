# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movement_analysis_dialog_filter.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AnimalMovementAnalysisDialogFilter(object):
    def setupUi(self, AnimalMovementAnalysisDialogFilter):
        AnimalMovementAnalysisDialogFilter.setObjectName("AnimalMovementAnalysisDialogFilter")
        AnimalMovementAnalysisDialogFilter.resize(574, 417)
        self.button_box = QtWidgets.QDialogButtonBox(AnimalMovementAnalysisDialogFilter)
        self.button_box.setGeometry(QtCore.QRect(200, 360, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.label = QtWidgets.QLabel(AnimalMovementAnalysisDialogFilter)
        self.label.setGeometry(QtCore.QRect(240, 30, 91, 21))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(AnimalMovementAnalysisDialogFilter)
        self.label_4.setGeometry(QtCore.QRect(30, 290, 134, 22))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(AnimalMovementAnalysisDialogFilter)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(170, 290, 137, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(AnimalMovementAnalysisDialogFilter)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 170, 22))
        self.label_5.setObjectName("label_5")
        self.calculateButton = QtWidgets.QPushButton(AnimalMovementAnalysisDialogFilter)
        self.calculateButton.setGeometry(QtCore.QRect(450, 190, 93, 28))
        self.calculateButton.setObjectName("calculateButton")
        self.label_2 = QtWidgets.QLabel(AnimalMovementAnalysisDialogFilter)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 94, 22))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AnimalMovementAnalysisDialogFilter)
        self.label_3.setGeometry(QtCore.QRect(340, 90, 21, 22))
        self.label_3.setObjectName("label_3")
        self.mDateTimeEdit_From = QgsDateTimeEdit(AnimalMovementAnalysisDialogFilter)
        self.mDateTimeEdit_From.setGeometry(QtCore.QRect(140, 90, 186, 22))
        self.mDateTimeEdit_From.setObjectName("mDateTimeEdit_From")
        self.mDateTimeEdit_To = QgsDateTimeEdit(AnimalMovementAnalysisDialogFilter)
        self.mDateTimeEdit_To.setGeometry(QtCore.QRect(370, 90, 171, 22))
        self.mDateTimeEdit_To.setObjectName("mDateTimeEdit_To")
        self.comboBox = QtWidgets.QComboBox(AnimalMovementAnalysisDialogFilter)
        self.comboBox.setGeometry(QtCore.QRect(140, 140, 401, 22))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(AnimalMovementAnalysisDialogFilter)
        self.button_box.accepted.connect(AnimalMovementAnalysisDialogFilter.accept)
        self.button_box.rejected.connect(AnimalMovementAnalysisDialogFilter.reject)
        QtCore.QMetaObject.connectSlotsByName(AnimalMovementAnalysisDialogFilter)

    def retranslateUi(self, AnimalMovementAnalysisDialogFilter):
        _translate = QtCore.QCoreApplication.translate
        AnimalMovementAnalysisDialogFilter.setWindowTitle(_translate("AnimalMovementAnalysisDialogFilter", "Animal Movement Analysis"))
        self.label.setText(_translate("AnimalMovementAnalysisDialogFilter", "Filter dataset"))
        self.label_4.setText(_translate("AnimalMovementAnalysisDialogFilter", "Total amount of points:"))
        self.label_5.setText(_translate("AnimalMovementAnalysisDialogFilter", "Birds to analyse"))
        self.calculateButton.setText(_translate("AnimalMovementAnalysisDialogFilter", "Calculate"))
        self.label_2.setText(_translate("AnimalMovementAnalysisDialogFilter", "Date range from"))
        self.label_3.setText(_translate("AnimalMovementAnalysisDialogFilter", "to"))

from qgsdatetimeedit import QgsDateTimeEdit
