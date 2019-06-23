# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movement_analysis_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AnimalMovementAnalysisDialogBase(object):
    def setupUi(self, AnimalMovementAnalysisDialogBase):
        AnimalMovementAnalysisDialogBase.setObjectName("AnimalMovementAnalysisDialogBase")
        AnimalMovementAnalysisDialogBase.resize(400, 255)
        self.button_box = QtWidgets.QDialogButtonBox(AnimalMovementAnalysisDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 190, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.label = QtWidgets.QLabel(AnimalMovementAnalysisDialogBase)
        self.label.setGeometry(QtCore.QRect(20, 30, 151, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AnimalMovementAnalysisDialogBase)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 151, 21))
        self.label_2.setObjectName("label_2")
        self.mQgsFileWidget1 = QgsFileWidget(AnimalMovementAnalysisDialogBase)
        self.mQgsFileWidget1.setGeometry(QtCore.QRect(20, 60, 331, 27))
        self.mQgsFileWidget1.setObjectName("mQgsFileWidget1")
        self.mQgsFileWidget2 = QgsFileWidget(AnimalMovementAnalysisDialogBase)
        self.mQgsFileWidget2.setGeometry(QtCore.QRect(20, 150, 331, 27))
        self.mQgsFileWidget2.setObjectName("mQgsFileWidget2")

        self.retranslateUi(AnimalMovementAnalysisDialogBase)
        self.button_box.accepted.connect(AnimalMovementAnalysisDialogBase.accept)
        self.button_box.rejected.connect(AnimalMovementAnalysisDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(AnimalMovementAnalysisDialogBase)

    def retranslateUi(self, AnimalMovementAnalysisDialogBase):
        _translate = QtCore.QCoreApplication.translate
        AnimalMovementAnalysisDialogBase.setWindowTitle(_translate("AnimalMovementAnalysisDialogBase", "Animal Movement Analysis"))
        self.label.setText(_translate("AnimalMovementAnalysisDialogBase", "Select input shapefile"))
        self.label_2.setText(_translate("AnimalMovementAnalysisDialogBase", "Select temperature CSV"))

from qgsfilewidget import QgsFileWidget
