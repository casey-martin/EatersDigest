# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_des/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from ingredientQuantityWindow import Ui_ingredientQuantityDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow(object):

    def addFoodButtonClicked(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        ingredientQuantityDialog = QtWidgets.QDialog()
        ui = Ui_ingredientQuantityDialog()
        ui.setupUi(ingredientQuantityDialog)
        ingredientQuantityDialog.show()
        ingredientQuantityDialog.exec_()


    def loadDietHistory(self):
        '''Queries user diet history for date displayed on foodCalendarWidget.
        diet_history.db contains columns Date, Time, NDB_No, Quantity, Units.
        diet_history.db will be created if none exists.'''
        createTable = 'CREATE TABLE IF NOT EXISTS diet_history (Date TEXT, Time TEXT, NDB_No TEXT, Quantity REAL, Units TEXT);'
        connection = sqlite3.connect('../diet_history/diet_history.db')
        connection.execute(createTable)
        
        queryBase = 'SELECT * FROM diet_history WHERE Date == \'{}\''
        queryQDate = self.foodCalendarWidget.selectedDate()
        queryDate = queryQDate.toString('yyyy-MM-dd')
        query = queryBase.format(queryDate) 
        result = connection.execute(query)

        self.dietHistoryBuffer = []

        for row_number, row_data in enumerate(result):
            self.recordedFoodTableWidget.insertRow(row_number)

            self.resultTableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(row_data[0][1:-1]))

            self.foodDesBuffer.append(row_data[1])

 
        connection.close()
        print(queryDate)


    def clearDietHistory(self):
        '''Removes displayed rows in recordedFoodTableWidget'''

        self.dietHistoryBuffer = []
        self.recordedFoodTableWidget.setRowCount(0)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1246, 647)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
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
        self.addFoodPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.addFoodPushButton.setObjectName("addFoodPushButton")
        self.horizontalLayout_2.addWidget(self.addFoodPushButton)
        self.removeFoodPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeFoodPushButton.setObjectName("removeFoodPushButton")
        self.horizontalLayout_2.addWidget(self.removeFoodPushButton)
 
        self.foodRecordLayout.addLayout(self.horizontalLayout_2)
        self.recordedFoodTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.recordedFoodTableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.recordedFoodTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.recordedFoodTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
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
        self.recordedFoodTableWidget.horizontalHeader().setStretchLastSection(True)
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
        self.recipeListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.recipeListWidget.setAcceptDrops(False)
        self.recipeListWidget.setObjectName("recipeListWidget")
        self.recipeLayout.addWidget(self.recipeListWidget)
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

        # display today's diet history
        self.loadDietHistory()

        # on user's change of selected day, display available diet history
        self.foodCalendarWidget.clicked.connect(self.loadDietHistory)

        # on user's change of selected month, clear displayed diet history
        self.foodCalendarWidget.currentPageChanged.connect(self.clearDietHistory)

        # on Add Food call, open ingredientQuantityDialog
        self.addFoodPushButton.clicked.connect(self.addFoodButtonClicked)

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Daily Food Record:"))
        self.removeFoodPushButton.setText(_translate("MainWindow", "Remove Food"))
        self.addFoodPushButton.setText(_translate("MainWindow", "Add Food"))
        item = self.recordedFoodTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time"))
        item = self.recordedFoodTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Food Name"))
        item = self.recordedFoodTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.recordedFoodTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Units"))
        self.label_2.setText(_translate("MainWindow", "Date :"))
        self.label_3.setText(_translate("MainWindow", "Recipe Options:"))
        self.addRecipePushButton.setText(_translate("MainWindow", "Add Recipe to Daily Food Record"))
        self.newRecipePushButton.setText(_translate("MainWindow", "Create New Recipe"))
        self.editRecipePushButton.setText(_translate("MainWindow", "Edit Recipe"))
        self.deleteRecipePushButton.setText(_translate("MainWindow", "Delete Recipe"))
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
