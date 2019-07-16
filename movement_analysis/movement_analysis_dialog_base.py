# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movement_analysis_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AnimalMovementAnalysisDialogBase(object):
    def setupUi(self, AnimalMovementAnalysisDialogBase):
        AnimalMovementAnalysisDialogBase.setObjectName("AnimalMovementAnalysisDialogBase")
        AnimalMovementAnalysisDialogBase.resize(400, 215)
        self.button_box = QtWidgets.QDialogButtonBox(AnimalMovementAnalysisDialogBase)
        self.button_box.setGeometry(QtCore.QRect(40, 140, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.label = QtWidgets.QLabel(AnimalMovementAnalysisDialogBase)
        self.label.setGeometry(QtCore.QRect(20, 40, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.mQgsFileWidget1 = QgsFileWidget(AnimalMovementAnalysisDialogBase)
        self.mQgsFileWidget1.setGeometry(QtCore.QRect(20, 80, 361, 27))
        self.mQgsFileWidget1.setObjectName("mQgsFileWidget1")

        self.retranslateUi(AnimalMovementAnalysisDialogBase)
        self.button_box.accepted.connect(AnimalMovementAnalysisDialogBase.accept)
        self.button_box.rejected.connect(AnimalMovementAnalysisDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(AnimalMovementAnalysisDialogBase)

    def retranslateUi(self, AnimalMovementAnalysisDialogBase):
        _translate = QtCore.QCoreApplication.translate
        AnimalMovementAnalysisDialogBase.setWindowTitle(_translate("AnimalMovementAnalysisDialogBase", "Animal Movement Analysis"))
        self.label.setText(_translate("AnimalMovementAnalysisDialogBase", "Select input shapefile"))

from qgsfilewidget import QgsFileWidget
