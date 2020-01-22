# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ingredientQuantityWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_ingredientQuantityDialog(object):

    # load FdGrp_Desc
    def loadFdGrp(self):
        connection = sqlite3.connect('../database/sr28.db')
        connection.text_factory = str
        query = 'SELECT FdGrp_Desc, FdGrp_Cd FROM fd_group;'
        result = connection.execute(query)

        result = [(FdGrp_Desc[1:-1], FdGrp_Cd) for FdGrp_Desc, FdGrp_Cd in result]
        self.FdGrpDict = dict(result)     
        self.FdGrpDict[''] = ''
        connection.close()

        self.foodGroupComboBox.addItems(sorted(self.FdGrpDict.keys()))

    # connect to sr28 database
    def loadData(self):
        connection = sqlite3.connect('../database/sr28.db')
        connection.text_factory = str
        #query = 'SELECT Shrt_Desc FROM food_des'
        #result = connection.execute(query)
        
        rawInput = self.queryLineEdit.text().strip()
        FdGrp_Desc = str(self.foodGroupComboBox.currentText())
        
        if len(rawInput) == 0:
            return
    
        queryBase = 'SELECT Long_Desc,NDB_No FROM food_des WHERE '
        likeClause = 'Long_Desc LIKE \'%{}%\''
        clauseList = [likeClause.format(i) for i in rawInput.split()]
        FdGrpFilter = 'FdGrp_Cd == \'{}\' AND '.format(self.FdGrpDict[FdGrp_Desc])
        if len(FdGrp_Desc) != 0:
            userQuery = queryBase + '(' + FdGrpFilter  + ' AND '.join(clauseList) + ');'
        else:
            userQuery = queryBase + '(' + ' AND '.join(clauseList) + ');'

        result = connection.execute(userQuery)

        # Save NDB_No for mapping to other tables in sr28.db
        # Long_Desc = key, NDB_No = value
        self.foodDesBuffer = [] 

        self.resultTableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.resultTableWidget.insertRow(row_number)
            
            self.resultTableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(row_data[0][1:-1]))
            
            self.foodDesBuffer.append(row_data[1])

        connection.close()

    # list available measurements of selected row in resultTableWidget
    # pull rows from weight table where NDB_No matches.
    # send available measurements to unitComboBox.
    # test for cases where NDB_No is not found in weight table.
    def getWeights(self):

        self.unitComboBox.clear()

        try:
            self.currentNDB_No = self.foodDesBuffer[ self.resultTableWidget.currentRow() ]
        except:
            # print(self.foodDesBuffer, self.resultTableWidget.currentRow())
            return

        connection = sqlite3.connect('../database/sr28.db')
        connection.text_factory = str

        query = 'SELECT  Msre_Desc FROM weight WHERE NDB_No == \'{}\';'
        result  = connection.execute(query.format(self.currentNDB_No))

        measureList = []
        for i in result:
            measureList.append(i[0][1:-1])
        if len(measureList) == 0:
            print(self.currentNDB_No)
        
        connection.close()
        if len(measureList) == 0:
            self.unitComboBox.addItems(['oz (weight)', 'gram', 'cup', 'tsp', 'tbsp', 'serving'])
        else:
            self.unitComboBox.addItems(measureList)
        
    def setupUi(self, ingredientQuantityDialog):
        ingredientQuantityDialog.setObjectName("ingredientQuantityDialog")
        ingredientQuantityDialog.resize(1002, 533)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(ingredientQuantityDialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.queryLayout = QtWidgets.QVBoxLayout()
        self.queryLayout.setObjectName("queryLayout")
        self.foodQuerylabel = QtWidgets.QLabel(ingredientQuantityDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.foodQuerylabel.setFont(font)
        self.foodQuerylabel.setObjectName("foodQuerylabel")
        self.queryLayout.addWidget(self.foodQuerylabel)
        self.queryInputLayout = QtWidgets.QHBoxLayout()
        self.queryInputLayout.setObjectName("queryInputLayout")
        self.queryLineEdit = QtWidgets.QLineEdit(ingredientQuantityDialog)
        self.queryLineEdit.setObjectName("queryLineEdit")
        self.queryInputLayout.addWidget(self.queryLineEdit)
        self.foodGroupComboBox = QtWidgets.QComboBox(ingredientQuantityDialog)
        self.foodGroupComboBox.setEnabled(True)
        self.foodGroupComboBox.setMinimumSize(QtCore.QSize(50, 0))
        self.foodGroupComboBox.setEditable(True)
        self.foodGroupComboBox.setObjectName("foodGroupComboBox")
        self.queryInputLayout.addWidget(self.foodGroupComboBox)
        self.queryLayout.addLayout(self.queryInputLayout)
        self.resultTableWidget = QtWidgets.QTableWidget(ingredientQuantityDialog)
        self.resultTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.resultTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.resultTableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.resultTableWidget.setObjectName("resultTableWidget")
        self.resultTableWidget.setColumnCount(1)
        self.resultTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.resultTableWidget.setHorizontalHeaderItem(0, item)
        self.resultTableWidget.horizontalHeader().setStretchLastSection(True)
        self.queryLayout.addWidget(self.resultTableWidget)
        self.horizontalLayout_2.addLayout(self.queryLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.timeLabel = QtWidgets.QLabel(ingredientQuantityDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.timeLabel.setFont(font)
        self.timeLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.timeLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.timeLabel.setObjectName("timeLabel")
        self.verticalLayout_2.addWidget(self.timeLabel)
        self.consumptionTimeEdit = QtWidgets.QTimeEdit(ingredientQuantityDialog)
        self.consumptionTimeEdit.setObjectName("consumptionTimeEdit")
        self.verticalLayout_2.addWidget(self.consumptionTimeEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.quantityLabel = QtWidgets.QLabel(ingredientQuantityDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.quantityLabel.setFont(font)
        self.quantityLabel.setObjectName("quantityLabel")
        self.verticalLayout_2.addWidget(self.quantityLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.quantitySpinBox = QtWidgets.QDoubleSpinBox(ingredientQuantityDialog)
        self.quantitySpinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.quantitySpinBox.setObjectName("quantitySpinBox")
        self.horizontalLayout.addWidget(self.quantitySpinBox)
        self.unitComboBox = QtWidgets.QComboBox(ingredientQuantityDialog)
        self.unitComboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.unitComboBox.setObjectName("unitComboBox")
        self.horizontalLayout.addWidget(self.unitComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.confirmButtonBox = QtWidgets.QDialogButtonBox(ingredientQuantityDialog)
        self.confirmButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.confirmButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.confirmButtonBox.setObjectName("confirmButtonBox")
        self.verticalLayout_2.addWidget(self.confirmButtonBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.retranslateUi(ingredientQuantityDialog)
        self.confirmButtonBox.accepted.connect(ingredientQuantityDialog.accept)
        self.confirmButtonBox.rejected.connect(ingredientQuantityDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ingredientQuantityDialog)

        # upon user entry into queryLineEdit, search database for user strings
        self.queryLineEdit.textChanged.connect(self.loadData)

        # upon user entry into foodGroupComboBox, filter database for FdGroup_Cd
        self.loadFdGrp()

        # upon user selection of item in resultTableWidget, record the selection.
        self.resultTableWidget.itemSelectionChanged.connect(self.getWeights)

        # disable table editability 
        self.resultTableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)



    def retranslateUi(self, ingredientQuantityDialog):
        _translate = QtCore.QCoreApplication.translate
        ingredientQuantityDialog.setWindowTitle(_translate("ingredientQuantityDialog", "Dialog"))
        self.foodQuerylabel.setText(_translate("ingredientQuantityDialog", "Search for Foods:"))
        self.resultTableWidget.setSortingEnabled(False)
        item = self.resultTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ingredientQuantityDialog", "Food Name"))
        self.timeLabel.setText(_translate("ingredientQuantityDialog", "Time of Consumption:"))
        self.quantityLabel.setText(_translate("ingredientQuantityDialog", "Quantity:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ingredientQuantityDialog = QtWidgets.QDialog()
    ui = Ui_ingredientQuantityDialog()
    ui.setupUi(ingredientQuantityDialog)
    ingredientQuantityDialog.show()
    sys.exit(app.exec_())

