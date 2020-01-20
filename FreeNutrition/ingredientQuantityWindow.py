# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ingredientQuantityWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ingredientQuantityDialog(object):
    def setupUi(self, ingredientQuantityDialog):
        ingredientQuantityDialog.setObjectName("ingredientQuantityDialog")
        ingredientQuantityDialog.resize(378, 135)
        self.buttonBox = QtWidgets.QDialogButtonBox(ingredientQuantityDialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 90, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(ingredientQuantityDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 341, 61))
        self.groupBox.setObjectName("groupBox")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setGeometry(QtCore.QRect(20, 30, 71, 23))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(110, 30, 121, 22))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(ingredientQuantityDialog)
        self.buttonBox.accepted.connect(ingredientQuantityDialog.accept)
        self.buttonBox.rejected.connect(ingredientQuantityDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ingredientQuantityDialog)

    def retranslateUi(self, ingredientQuantityDialog):
        _translate = QtCore.QCoreApplication.translate
        ingredientQuantityDialog.setWindowTitle(_translate("ingredientQuantityDialog", "Dialog"))
        self.groupBox.setTitle(_translate("ingredientQuantityDialog", "Ingredient Amount"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ingredientQuantityDialog = QtWidgets.QDialog()
    ui = Ui_ingredientQuantityDialog()
    ui.setupUi(ingredientQuantityDialog)
    ingredientQuantityDialog.show()
    sys.exit(app.exec_())

