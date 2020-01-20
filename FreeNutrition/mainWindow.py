# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
#
# rawInput = queryLineEdit.string
# queryBase = 'SELECT Shrt_Desc FROM food_des WHERE '
# likeClause = 'Shrt_Desc LIKE %{}%'
# clauseList = [likeClause.format(i) for i in rawInput.split()]
# userQuery = queryBase + '(' + ' AND '.join(clauseList) + ');'


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow(object):
    # connect to sr28 database
    def loadData(self, rawInput):
        connection = sqlite3.connect('../database/sr28.db')
        connection.text_factory = str
        #query = 'SELECT Shrt_Desc FROM food_des'
        #result = connection.execute(query)
        
        rawInput = self.queryLineEdit.text()
        
        if len(rawInput) == 0:
            return
    
        queryBase = 'SELECT Shrt_Desc FROM food_des WHERE '
        likeClause = 'Long_Desc LIKE \'%{}%\''
        clauseList = [likeClause.format(i) for i in rawInput.split()]
        userQuery = queryBase + '(' + ' AND '.join(clauseList) + ');'

        result = connection.execute(userQuery)

        self.resultTableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.resultTableWidget.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.resultTableWidget.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data))) 

        connection.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1246, 647)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.queryLayout = QtWidgets.QVBoxLayout()
        self.queryLayout.setObjectName("queryLayout")
        self.foodQuerylabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.foodQuerylabel.setFont(font)
        self.foodQuerylabel.setObjectName("foodQuerylabel")
        self.queryLayout.addWidget(self.foodQuerylabel)
        self.queryInputLayout = QtWidgets.QHBoxLayout()
        self.queryInputLayout.setObjectName("queryInputLayout")
        self.queryLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.queryLineEdit.setObjectName("queryLineEdit")
        self.queryInputLayout.addWidget(self.queryLineEdit)
        self.foodGroupComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.foodGroupComboBox.setEnabled(True)
        self.foodGroupComboBox.setMinimumSize(QtCore.QSize(50, 0))
        self.foodGroupComboBox.setEditable(True)
        self.foodGroupComboBox.setObjectName("foodGroupComboBox")
        self.queryInputLayout.addWidget(self.foodGroupComboBox)
        self.queryLayout.addLayout(self.queryInputLayout)
        self.resultTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.resultTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.resultTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.resultTableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.resultTableWidget.setObjectName("resultTableWidget")
        self.resultTableWidget.setColumnCount(1)
        self.resultTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.resultTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultTableWidget.setHorizontalHeaderItem(2, item)
        self.queryLayout.addWidget(self.resultTableWidget)
        self.horizontalLayout.addLayout(self.queryLayout)
        self.foodRecordLayout = QtWidgets.QVBoxLayout()
        self.foodRecordLayout.setObjectName("foodRecordLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.foodRecordLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.removeFoodPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeFoodPushButton.setObjectName("removeFoodPushButton")
        self.horizontalLayout_2.addWidget(self.removeFoodPushButton)
        self.addFoodPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.addFoodPushButton.setObjectName("addFoodPushButton")
        self.horizontalLayout_2.addWidget(self.addFoodPushButton)
        self.foodRecordLayout.addLayout(self.horizontalLayout_2)
        self.recordedFoodTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.recordedFoodTableWidget.setObjectName("recordedFoodTableWidget")
        self.recordedFoodTableWidget.setColumnCount(4)
        self.recordedFoodTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.recordedFoodTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.recordedFoodTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.recordedFoodTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.recordedFoodTableWidget.setHorizontalHeaderItem(3, item)
        self.foodRecordLayout.addWidget(self.recordedFoodTableWidget)
        self.horizontalLayout.addLayout(self.foodRecordLayout)
        self.foodMetadataLayout = QtWidgets.QVBoxLayout()
        self.foodMetadataLayout.setObjectName("foodMetadataLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.foodMetadataLayout.addWidget(self.label_2)
        self.foodCalendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.foodCalendarWidget.setObjectName("foodCalendarWidget")
        self.foodMetadataLayout.addWidget(self.foodCalendarWidget)
        self.foodTimeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.foodTimeEdit.setObjectName("foodTimeEdit")
        self.foodMetadataLayout.addWidget(self.foodTimeEdit)
        self.horizontalLayout.addLayout(self.foodMetadataLayout)
        self.recipeLayout = QtWidgets.QVBoxLayout()
        self.recipeLayout.setObjectName("recipeLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.recipeLayout.addWidget(self.label_3)
        self.addRecipePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.addRecipePushButton.setObjectName("addRecipePushButton")
        self.recipeLayout.addWidget(self.addRecipePushButton)
        self.newRecipePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.newRecipePushButton.setObjectName("newRecipePushButton")
        self.recipeLayout.addWidget(self.newRecipePushButton)
        self.editRecipePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.editRecipePushButton.setObjectName("editRecipePushButton")
        self.recipeLayout.addWidget(self.editRecipePushButton)
        self.deleteRecipePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteRecipePushButton.setObjectName("deleteRecipePushButton")
        self.recipeLayout.addWidget(self.deleteRecipePushButton)
        self.recipeTreeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.recipeTreeWidget.setAcceptDrops(False)
        self.recipeTreeWidget.setObjectName("recipeTreeWidget")
        self.recipeTreeWidget.headerItem().setText(0, "1")
        self.recipeLayout.addWidget(self.recipeTreeWidget)
        self.horizontalLayout.addLayout(self.recipeLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1246, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAnalysis = QtWidgets.QMenu(self.menuFile)
        self.menuAnalysis.setObjectName("menuAnalysis")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExportData = QtWidgets.QAction(MainWindow)
        self.actionExportData.setObjectName("actionExportData")
        self.actionExport_data = QtWidgets.QAction(MainWindow)
        self.actionExport_data.setObjectName("actionExport_data")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionLie_to_Me = QtWidgets.QAction(MainWindow)
        self.actionLie_to_Me.setObjectName("actionLie_to_Me")
        self.actionDoc_Give_it_to_me_straight = QtWidgets.QAction(MainWindow)
        self.actionDoc_Give_it_to_me_straight.setObjectName("actionDoc_Give_it_to_me_straight")
        self.menuAnalysis.addAction(self.actionLie_to_Me)
        self.menuAnalysis.addAction(self.actionDoc_Give_it_to_me_straight)
        self.menuFile.addAction(self.menuAnalysis.menuAction())
        self.menuFile.addAction(self.actionExportData)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # upon user entry into queryLineEdit, search database for user strings
        self.queryLineEdit.textChanged.connect(self.loadData)

        # disable table editability 
        self.resultTableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        # resize column
        self.resultTableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.recordedFoodTableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.foodQuerylabel.setText(_translate("MainWindow", "Search for Foods:"))
        self.resultTableWidget.setSortingEnabled(True)
        item = self.resultTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Food Name"))
        self.label.setText(_translate("MainWindow", "Daily Food Record:"))
        self.removeFoodPushButton.setText(_translate("MainWindow", "Add Food"))
        self.addFoodPushButton.setText(_translate("MainWindow", "Remove Food "))
        item = self.recordedFoodTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time"))
        item = self.recordedFoodTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Food Name"))
        item = self.recordedFoodTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.recordedFoodTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Units"))
        self.label_2.setText(_translate("MainWindow", "Date of Consumption:"))
        self.label_3.setText(_translate("MainWindow", "Recipe Options:"))
        self.addRecipePushButton.setText(_translate("MainWindow", "Add Recipe to Daily Food Record"))
        self.newRecipePushButton.setText(_translate("MainWindow", "Create New Recipe"))
        self.editRecipePushButton.setText(_translate("MainWindow", "Edit Recipe"))
        self.deleteRecipePushButton.setText(_translate("MainWindow", "Delete Recipe"))
        self.recipeTreeWidget.setSortingEnabled(False)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis"))
        self.actionExportData.setText(_translate("MainWindow", "Export data"))
        self.actionExport_data.setText(_translate("MainWindow", "Export data"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionLie_to_Me.setText(_translate("MainWindow", "Lie to Me"))
        self.actionDoc_Give_it_to_me_straight.setText(_translate("MainWindow", "Doc. Give it to me straight."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

