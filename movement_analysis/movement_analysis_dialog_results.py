# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movement_analysis_dialog_results.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AnimalMovementAnalysisDialogResults(object):
    def setupUi(self, AnimalMovementAnalysisDialogResults):
        AnimalMovementAnalysisDialogResults.setObjectName("AnimalMovementAnalysisDialogResults")
        AnimalMovementAnalysisDialogResults.resize(794, 824)
        self.button_box = QtWidgets.QDialogButtonBox(AnimalMovementAnalysisDialogResults)
        self.button_box.setGeometry(QtCore.QRect(420, 770, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.label = QtWidgets.QLabel(AnimalMovementAnalysisDialogResults)
        self.label.setGeometry(QtCore.QRect(300, 30, 191, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AnimalMovementAnalysisDialogResults)
        self.label_2.setGeometry(QtCore.QRect(150, 110, 511, 321))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(AnimalMovementAnalysisDialogResults)
        self.button_box.accepted.connect(AnimalMovementAnalysisDialogResults.accept)
        self.button_box.rejected.connect(AnimalMovementAnalysisDialogResults.reject)
        QtCore.QMetaObject.connectSlotsByName(AnimalMovementAnalysisDialogResults)

    def retranslateUi(self, AnimalMovementAnalysisDialogResults):
        _translate = QtCore.QCoreApplication.translate
        AnimalMovementAnalysisDialogResults.setWindowTitle(_translate("AnimalMovementAnalysisDialogResults", "Animal Movement Analysis Results"))
        self.label.setText(_translate("AnimalMovementAnalysisDialogResults", "Distance/temperature statistics"))

