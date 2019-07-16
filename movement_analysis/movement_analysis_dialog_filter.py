# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movement_analysis_dialog_filter.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
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
        self.label.setGeometry(QtCore.QRect(240, 30, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(AnimalMovementAnalysisDialogFilter)
        self.label_4.setGeometry(QtCore.QRect(30, 290, 134, 22))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(AnimalMovementAnalysisDialogFilter)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(170, 290, 137, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(AnimalMovementAnalysisDialogFilter)
        self.label_5.setGeometry(QtCore.QRect(30, 90, 170, 22))
        self.label_5.setObjectName("label_5")
        self.calculateButton = QtWidgets.QPushButton(AnimalMovementAnalysisDialogFilter)
        self.calculateButton.setGeometry(QtCore.QRect(450, 230, 93, 28))
        self.calculateButton.setObjectName("calculateButton")
        self.label_2 = QtWidgets.QLabel(AnimalMovementAnalysisDialogFilter)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 121, 22))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(AnimalMovementAnalysisDialogFilter)
        self.comboBox.setGeometry(QtCore.QRect(140, 90, 401, 22))
        self.comboBox.setObjectName("comboBox")
        self.mComboBox = QgsCheckableComboBox(AnimalMovementAnalysisDialogFilter)
        self.mComboBox.setGeometry(QtCore.QRect(170, 150, 160, 27))
        self.mComboBox.setObjectName("mComboBox")
        self.mComboBox.addItem("")
        self.mComboBox.addItem("")
        self.mComboBox.addItem("")
        self.mComboBox.addItem("")

        self.retranslateUi(AnimalMovementAnalysisDialogFilter)
        self.button_box.accepted.connect(AnimalMovementAnalysisDialogFilter.accept)
        self.button_box.rejected.connect(AnimalMovementAnalysisDialogFilter.reject)
        QtCore.QMetaObject.connectSlotsByName(AnimalMovementAnalysisDialogFilter)

    def retranslateUi(self, AnimalMovementAnalysisDialogFilter):
        _translate = QtCore.QCoreApplication.translate
        AnimalMovementAnalysisDialogFilter.setWindowTitle(_translate("AnimalMovementAnalysisDialogFilter", "Animal Movement Analysis"))
        self.label.setText(_translate("AnimalMovementAnalysisDialogFilter", "Filter dataset"))
        self.label_4.setText(_translate("AnimalMovementAnalysisDialogFilter", "Points found?        -"))
        self.label_5.setText(_translate("AnimalMovementAnalysisDialogFilter", "Birds to analyse"))
        self.calculateButton.setText(_translate("AnimalMovementAnalysisDialogFilter", "Calculate"))
        self.label_2.setText(_translate("AnimalMovementAnalysisDialogFilter", "Seasons to consider"))
        self.mComboBox.setItemText(0, _translate("AnimalMovementAnalysisDialogFilter", "Winter"))
        self.mComboBox.setItemText(1, _translate("AnimalMovementAnalysisDialogFilter", "Spring"))
        self.mComboBox.setItemText(2, _translate("AnimalMovementAnalysisDialogFilter", "Summer"))
        self.mComboBox.setItemText(3, _translate("AnimalMovementAnalysisDialogFilter", "Autumn"))

from qgscheckablecombobox import QgsCheckableComboBox
