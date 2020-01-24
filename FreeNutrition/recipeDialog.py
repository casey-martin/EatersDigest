# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_des_ui/recipeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_recipeDialog(object):
    def setupUi(self, recipeDialog):
        recipeDialog.setObjectName("recipeDialog")
        recipeDialog.resize(1009, 436)
        self.horizontalLayout = QtWidgets.QHBoxLayout(recipeDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.queryLayout = QtWidgets.QVBoxLayout()
        self.queryLayout.setObjectName("queryLayout")
        self.recipeNameLineEdit = QtWidgets.QLineEdit(recipeDialog)
        self.recipeNameLineEdit.setObjectName("recipeNameLineEdit")
        self.queryLayout.addWidget(self.recipeNameLineEdit)
        self.queryInputLayout = QtWidgets.QHBoxLayout()
        self.queryInputLayout.setObjectName("queryInputLayout")
        self.queryLineEdit = QtWidgets.QLineEdit(recipeDialog)
        self.queryLineEdit.setObjectName("queryLineEdit")
        self.queryInputLayout.addWidget(self.queryLineEdit)
        self.foodGroupComboBox = QtWidgets.QComboBox(recipeDialog)
        self.foodGroupComboBox.setEnabled(True)
        self.foodGroupComboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.foodGroupComboBox.setEditable(True)
        self.foodGroupComboBox.setObjectName("foodGroupComboBox")
        self.queryInputLayout.addWidget(self.foodGroupComboBox)
        self.queryLayout.addLayout(self.queryInputLayout)
        self.resultTableWidget = QtWidgets.QTableWidget(recipeDialog)
        self.resultTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.resultTableWidget.setAlternatingRowColors(True)
        self.resultTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.resultTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.resultTableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.resultTableWidget.setColumnCount(1)
        self.resultTableWidget.setObjectName("resultTableWidget")
        self.resultTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.resultTableWidget.setHorizontalHeaderItem(0, item)
        self.resultTableWidget.horizontalHeader().setStretchLastSection(True)
        self.queryLayout.addWidget(self.resultTableWidget)
        self.quantityLabel = QtWidgets.QLabel(recipeDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.quantityLabel.setFont(font)
        self.quantityLabel.setObjectName("quantityLabel")
        self.queryLayout.addWidget(self.quantityLabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.quantitySpinBox = QtWidgets.QDoubleSpinBox(recipeDialog)
        self.quantitySpinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.quantitySpinBox.setObjectName("quantitySpinBox")
        self.horizontalLayout_3.addWidget(self.quantitySpinBox)
        self.unitComboBox = QtWidgets.QComboBox(recipeDialog)
        self.unitComboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.unitComboBox.setEditable(True)
        self.unitComboBox.setObjectName("unitComboBox")
        self.horizontalLayout_3.addWidget(self.unitComboBox)
        self.queryLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.queryLayout)
        self.foodRecordLayout = QtWidgets.QVBoxLayout()
        self.foodRecordLayout.setObjectName("foodRecordLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addFoodPushButton = QtWidgets.QPushButton(recipeDialog)
        self.addFoodPushButton.setEnabled(False)
        self.addFoodPushButton.setObjectName("addFoodPushButton")
        self.horizontalLayout_2.addWidget(self.addFoodPushButton)
        self.removeFoodPushButton = QtWidgets.QPushButton(recipeDialog)
        self.removeFoodPushButton.setObjectName("removeFoodPushButton")
        self.horizontalLayout_2.addWidget(self.removeFoodPushButton)
        self.foodRecordLayout.addLayout(self.horizontalLayout_2)
        self.recordedFoodTableWidget = QtWidgets.QTableWidget(recipeDialog)
        self.recordedFoodTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.recordedFoodTableWidget.setAlternatingRowColors(True)
        self.recordedFoodTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.recordedFoodTableWidget.setObjectName("recordedFoodTableWidget")
        self.recordedFoodTableWidget.setColumnCount(3)
        self.recordedFoodTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.recordedFoodTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.recordedFoodTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.recordedFoodTableWidget.setHorizontalHeaderItem(2, item)
        self.recordedFoodTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.recordedFoodTableWidget.horizontalHeader().setStretchLastSection(True)
        self.foodRecordLayout.addWidget(self.recordedFoodTableWidget)
        self.horizontalLayout.addLayout(self.foodRecordLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.line = QtWidgets.QFrame(recipeDialog)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.servingSizeLabel = QtWidgets.QLabel(recipeDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.servingSizeLabel.setFont(font)
        self.servingSizeLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.servingSizeLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.servingSizeLabel.setObjectName("servingSizeLabel")
        self.verticalLayout.addWidget(self.servingSizeLabel)
        self.servingSizeSpinBox = QtWidgets.QSpinBox(recipeDialog)
        self.servingSizeSpinBox.setMinimum(0)
        self.servingSizeSpinBox.setProperty("value", 0)
        self.servingSizeSpinBox.setObjectName("servingSizeSpinBox")
        self.verticalLayout.addWidget(self.servingSizeSpinBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.saveRecipePushButton = QtWidgets.QPushButton(recipeDialog)
        self.saveRecipePushButton.setEnabled(False)
        self.saveRecipePushButton.setObjectName("saveRecipePushButton")
        self.verticalLayout.addWidget(self.saveRecipePushButton)
        self.cancelRecipePushButton = QtWidgets.QPushButton(recipeDialog)
        self.cancelRecipePushButton.setObjectName("cancelRecipePushButton")
        self.verticalLayout.addWidget(self.cancelRecipePushButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(recipeDialog)
        QtCore.QMetaObject.connectSlotsByName(recipeDialog)

    def retranslateUi(self, recipeDialog):
        _translate = QtCore.QCoreApplication.translate
        recipeDialog.setWindowTitle(_translate("recipeDialog", "Dialog"))
        self.recipeNameLineEdit.setText(_translate("recipeDialog", "Recipe Name"))
        self.resultTableWidget.setSortingEnabled(True)
        item = self.resultTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("recipeDialog", "Food Name"))
        self.quantityLabel.setText(_translate("recipeDialog", "Quantity:"))
        self.addFoodPushButton.setText(_translate("recipeDialog", "Add Food"))
        self.removeFoodPushButton.setText(_translate("recipeDialog", "Remove Food "))
        item = self.recordedFoodTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("recipeDialog", "Food Name"))
        item = self.recordedFoodTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("recipeDialog", "Quantity"))
        item = self.recordedFoodTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("recipeDialog", "Units"))
        self.servingSizeLabel.setText(_translate("recipeDialog", "Recipe Serving Size"))
        self.saveRecipePushButton.setText(_translate("recipeDialog", "Save Recipe"))
        self.cancelRecipePushButton.setText(_translate("recipeDialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    recipeDialog = QtWidgets.QDialog()
    ui = Ui_recipeDialog()
    ui.setupUi(recipeDialog)
    recipeDialog.show()
    sys.exit(app.exec_())