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
        AnimalMovementAnalysisDialogBase.resize(949, 926)
        self.button_box = QtWidgets.QDialogButtonBox(AnimalMovementAnalysisDialogBase)
        self.button_box.setGeometry(QtCore.QRect(730, 880, 201, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.label = QtWidgets.QLabel(AnimalMovementAnalysisDialogBase)
        self.label.setGeometry(QtCore.QRect(380, 30, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.statsLabel = QtWidgets.QLabel(AnimalMovementAnalysisDialogBase)
        self.statsLabel.setGeometry(QtCore.QRect(70, 230, 831, 591))
        self.statsLabel.setText("")
        self.statsLabel.setObjectName("statsLabel")
        self.scatterplotButton = QtWidgets.QPushButton(AnimalMovementAnalysisDialogBase)
        self.scatterplotButton.setGeometry(QtCore.QRect(650, 190, 251, 28))
        self.scatterplotButton.setObjectName("scatterplotButton")
        self.textEdit_2 = QtWidgets.QTextEdit(AnimalMovementAnalysisDialogBase)
        self.textEdit_2.setEnabled(True)
        self.textEdit_2.setGeometry(QtCore.QRect(630, 90, 261, 71))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_4 = QtWidgets.QLabel(AnimalMovementAnalysisDialogBase)
        self.label_4.setGeometry(QtCore.QRect(510, 100, 111, 20))
        self.label_4.setObjectName("label_4")
        self.showPlotButton = QtWidgets.QPushButton(AnimalMovementAnalysisDialogBase)
        self.showPlotButton.setEnabled(False)
        self.showPlotButton.setGeometry(QtCore.QRect(740, 840, 191, 31))
        self.showPlotButton.setObjectName("showPlotButton")
        self.textEdit = QtWidgets.QTextEdit(AnimalMovementAnalysisDialogBase)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(160, 90, 271, 71))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(AnimalMovementAnalysisDialogBase)
        self.label_5.setGeometry(QtCore.QRect(60, 100, 111, 20))
        self.label_5.setObjectName("label_5")
        self.distTempButton = QtWidgets.QPushButton(AnimalMovementAnalysisDialogBase)
        self.distTempButton.setGeometry(QtCore.QRect(340, 190, 261, 28))
        self.distTempButton.setObjectName("distTempButton")
        self.monthlyStatsButton = QtWidgets.QPushButton(AnimalMovementAnalysisDialogBase)
        self.monthlyStatsButton.setGeometry(QtCore.QRect(70, 190, 221, 28))
        self.monthlyStatsButton.setObjectName("monthlyStatsButton")

        self.retranslateUi(AnimalMovementAnalysisDialogBase)
        self.button_box.accepted.connect(AnimalMovementAnalysisDialogBase.accept)
        self.button_box.rejected.connect(AnimalMovementAnalysisDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(AnimalMovementAnalysisDialogBase)

    def retranslateUi(self, AnimalMovementAnalysisDialogBase):
        _translate = QtCore.QCoreApplication.translate
        AnimalMovementAnalysisDialogBase.setWindowTitle(_translate("AnimalMovementAnalysisDialogBase", "Animal Movement Analysis"))
        self.label.setText(_translate("AnimalMovementAnalysisDialogBase", "Visual Analysis of Data"))
        self.scatterplotButton.setText(_translate("AnimalMovementAnalysisDialogBase", "Display distance/temperature scatterplot"))
        self.textEdit_2.setHtml(_translate("AnimalMovementAnalysisDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("AnimalMovementAnalysisDialogBase", "Chosen seasons:"))
        self.showPlotButton.setText(_translate("AnimalMovementAnalysisDialogBase", "Show Plot in Popup"))
        self.textEdit.setHtml(_translate("AnimalMovementAnalysisDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("AnimalMovementAnalysisDialogBase", "Chosen birds"))
        self.distTempButton.setText(_translate("AnimalMovementAnalysisDialogBase", "Display distance/temperature boxplots"))
        self.monthlyStatsButton.setText(_translate("AnimalMovementAnalysisDialogBase", "Display monthly bar charts "))

