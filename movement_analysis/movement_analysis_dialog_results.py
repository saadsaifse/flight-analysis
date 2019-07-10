# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movement_analysis_dialog_results.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AnimalMovementAnalysisDialogBase(object):
    def setupUi(self, AnimalMovementAnalysisDialogBase):
        AnimalMovementAnalysisDialogBase.setObjectName("AnimalMovementAnalysisDialogBase")
        AnimalMovementAnalysisDialogBase.resize(946, 813)
        self.button_box = QtWidgets.QDialogButtonBox(AnimalMovementAnalysisDialogBase)
        self.button_box.setGeometry(QtCore.QRect(570, 750, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.label = QtWidgets.QLabel(AnimalMovementAnalysisDialogBase)
        self.label.setGeometry(QtCore.QRect(420, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.statsLabel = QtWidgets.QLabel(AnimalMovementAnalysisDialogBase)
        self.statsLabel.setGeometry(QtCore.QRect(90, 320, 731, 411))
        self.statsLabel.setText("")
        self.statsLabel.setObjectName("statsLabel")
        self.monthlyStatsButton = QtWidgets.QPushButton(AnimalMovementAnalysisDialogBase)
        self.monthlyStatsButton.setGeometry(QtCore.QRect(70, 270, 221, 28))
        self.monthlyStatsButton.setObjectName("monthlyStatsButton")
        self.distTempButton = QtWidgets.QPushButton(AnimalMovementAnalysisDialogBase)
        self.distTempButton.setGeometry(QtCore.QRect(360, 270, 261, 28))
        self.distTempButton.setObjectName("distTempButton")
        self.loadToMapButton = QtWidgets.QPushButton(AnimalMovementAnalysisDialogBase)
        self.loadToMapButton.setGeometry(QtCore.QRect(680, 270, 201, 28))
        self.loadToMapButton.setObjectName("loadToMapButton")
        self.textEdit = QtWidgets.QTextEdit(AnimalMovementAnalysisDialogBase)
        self.textEdit.setGeometry(QtCore.QRect(190, 80, 321, 171))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(AnimalMovementAnalysisDialogBase)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 121, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(AnimalMovementAnalysisDialogBase)
        self.textEdit_2.setGeometry(QtCore.QRect(680, 110, 201, 101))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_4 = QtWidgets.QLabel(AnimalMovementAnalysisDialogBase)
        self.label_4.setGeometry(QtCore.QRect(570, 140, 111, 20))
        self.label_4.setObjectName("label_4")
        self.showPlotButton = QtWidgets.QPushButton(AnimalMovementAnalysisDialogBase)
        self.showPlotButton.setEnabled(False)
        self.showPlotButton.setGeometry(QtCore.QRect(360, 740, 181, 28))
        self.showPlotButton.setObjectName("showPlotButton")

        self.retranslateUi(AnimalMovementAnalysisDialogBase)
        self.button_box.accepted.connect(AnimalMovementAnalysisDialogBase.accept)
        self.button_box.rejected.connect(AnimalMovementAnalysisDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(AnimalMovementAnalysisDialogBase)

    def retranslateUi(self, AnimalMovementAnalysisDialogBase):
        _translate = QtCore.QCoreApplication.translate
        AnimalMovementAnalysisDialogBase.setWindowTitle(_translate("AnimalMovementAnalysisDialogBase", "Animal Movement Analysis"))
        self.label.setText(_translate("AnimalMovementAnalysisDialogBase", "Statistics"))
        self.monthlyStatsButton.setText(_translate("AnimalMovementAnalysisDialogBase", "Display monthly statistics"))
        self.distTempButton.setText(_translate("AnimalMovementAnalysisDialogBase", "Dislpay distance/temperature distribution"))
        self.loadToMapButton.setText(_translate("AnimalMovementAnalysisDialogBase", "Load all the points to the map"))
        self.label_3.setText(_translate("AnimalMovementAnalysisDialogBase", "Chosen birds:"))
        self.label_4.setText(_translate("AnimalMovementAnalysisDialogBase", "Chosen seasons:"))
        self.showPlotButton.setText(_translate("AnimalMovementAnalysisDialogBase", "Show Plot in Popup"))

