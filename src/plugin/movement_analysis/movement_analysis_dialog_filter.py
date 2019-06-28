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
        AnimalMovementAnalysisDialogFilter.resize(569, 313)
        self.button_box = QtWidgets.QDialogButtonBox(AnimalMovementAnalysisDialogFilter)
        self.button_box.setGeometry(QtCore.QRect(190, 230, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.label = QtWidgets.QLabel(AnimalMovementAnalysisDialogFilter)
        self.label.setGeometry(QtCore.QRect(220, 20, 151, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AnimalMovementAnalysisDialogFilter)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AnimalMovementAnalysisDialogFilter)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(AnimalMovementAnalysisDialogFilter)
        self.label_4.setGeometry(QtCore.QRect(320, 70, 81, 21))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(AnimalMovementAnalysisDialogFilter)
        self.comboBox.setGeometry(QtCore.QRect(130, 80, 73, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(AnimalMovementAnalysisDialogFilter)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 130, 73, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.checkBox = QtWidgets.QCheckBox(AnimalMovementAnalysisDialogFilter)
        self.checkBox.setGeometry(QtCore.QRect(410, 70, 81, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(AnimalMovementAnalysisDialogFilter)
        self.checkBox_2.setGeometry(QtCore.QRect(410, 100, 81, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(AnimalMovementAnalysisDialogFilter)
        self.checkBox_3.setGeometry(QtCore.QRect(410, 130, 81, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(AnimalMovementAnalysisDialogFilter)
        self.checkBox_4.setGeometry(QtCore.QRect(410, 160, 81, 20))
        self.checkBox_4.setObjectName("checkBox_4")

        self.retranslateUi(AnimalMovementAnalysisDialogFilter)
        self.button_box.accepted.connect(AnimalMovementAnalysisDialogFilter.accept)
        self.button_box.rejected.connect(AnimalMovementAnalysisDialogFilter.reject)
        QtCore.QMetaObject.connectSlotsByName(AnimalMovementAnalysisDialogFilter)

    def retranslateUi(self, AnimalMovementAnalysisDialogFilter):
        _translate = QtCore.QCoreApplication.translate
        AnimalMovementAnalysisDialogFilter.setWindowTitle(_translate("AnimalMovementAnalysisDialogFilter", "Animal Movement Analysis"))
        self.label.setText(_translate("AnimalMovementAnalysisDialogFilter", "Filter dataset"))
        self.label_2.setText(_translate("AnimalMovementAnalysisDialogFilter", "Gender"))
        self.label_3.setText(_translate("AnimalMovementAnalysisDialogFilter", "Age"))
        self.label_4.setText(_translate("AnimalMovementAnalysisDialogFilter", "Seasons"))
        self.checkBox.setText(_translate("AnimalMovementAnalysisDialogFilter", "Winter"))
        self.checkBox_2.setText(_translate("AnimalMovementAnalysisDialogFilter", "Spring"))
        self.checkBox_3.setText(_translate("AnimalMovementAnalysisDialogFilter", "Summer"))
        self.checkBox_4.setText(_translate("AnimalMovementAnalysisDialogFilter", "Autumn"))

