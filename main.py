from FreeNutrition.ingredientQuantityDialog import Ui_ingredientQuantityDialog
from FreeNutrition.recipeDialog import Ui_recipeDialog
from FreeNutrition.mainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDialog
import sqlite3
import sys

class ingredQuantDialogLogic(QDialog, Ui_ingredientQuantityDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        # upon user entry into queryLineEdit, search database for user strings
        self.queryLineEdit.textChanged.connect(self.loadData)

        # upon user entry into foodGroupComboBox, filter database for FdGroup_Cd
        self.loadFdGrp()

        # upon user selection of item in resultTableWidget, record the selection.
        self.resultTableWidget.itemSelectionChanged.connect(self.getWeights)

        # disable table editability
        self.resultTableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        #self.unitComboBox.currentIndexChanged.connect(
        self.currentNDB_No = None




    # load FdGrp_Desc
    def loadFdGrp(self):
        connection = sqlite3.connect('./database/sr28.db')
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
        '''sr28 query is executed upon changed character string in queryLineEdit.
        Searches the Long_Desc column for each space delimited string in queryLineEdit.
        Implemented a hacky work around using like clauses as sqlite3 does not have a
        REGEXP function.'''

        # do not query if search box is devoid of non whitespace characters.
        if len(self.queryLineEdit.text().strip()) == 0:
            return

        connection = sqlite3.connect('./database/sr28.db')
        connection.text_factory = str

        rawInput = self.queryLineEdit.text().strip()
        FdGrp_Desc = str(self.foodGroupComboBox.currentText())

        queryBase = 'SELECT Long_Desc,NDB_No FROM food_des WHERE '
        likeClause = 'Long_Desc LIKE \'%{}%\''
        clauseList = [likeClause.format(i) for i in rawInput.split()]

        # filter by food group
        FdGrpFilter = 'FdGrp_Cd == \'{}\' AND '.format(self.FdGrpDict[FdGrp_Desc])

        # omit query food group condition if foodGroupCombo box is empty.
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

    def getWeights(self):
        '''list available measurements of selected row in resultTableWidget
        pull rows from weight table where NDB_No matches.
        send available measurements to unitComboBox.
        test for cases where NDB_No is not found in weight table.'''

        self.unitComboBox.clear()

        # ugly. should build in innate behaviorial fix rather than error catching.
        try:
            self.currentNDB_No = self.foodDesBuffer[ self.resultTableWidget.currentRow() ]
        except:
            # print(self.foodDesBuffer, self.resultTableWidget.currentRow())
            return

        connection = sqlite3.connect('./database/sr28.db')
        connection.text_factory = str

        query = 'SELECT  Msre_Desc FROM weight WHERE NDB_No == \'{}\';'
        result  = connection.execute(query.format(self.currentNDB_No))

        measureList = ['']
        for i in result:
            measureList.append(i[0][1:-1])

        connection.close()
        if len(measureList) == 1:
            self.unitComboBox.addItems(['gram'])
        else:
            self.unitComboBox.addItems(measureList)


class recipeDialogLogic(QDialog, Ui_recipeDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        # upon user entry into queryLineEdit, search database for user strings
        self.queryLineEdit.textChanged.connect(self.loadData)

        # upon user entry into foodGroupComboBox, filter database for FdGroup_Cd
        self.loadFdGrp()

        # upon user selection of item in resultTableWidget, record the selection.
        self.resultTableWidget.itemSelectionChanged.connect(self.getWeights)


        #self.unitComboBox.currentIndexChanged.connect(
        self.currentNDB_No = None

        self.addFoodPushButton.clicked.connect(self.addFoodButtonClicked)

        # on Remove Food call, delete selected recordedFoodTableWidget entry from food_history
        self.removeFoodPushButton.clicked.connect(self.removeFoodButtonClicked)
       

        self.recordedFoodBuffer = []

        # if user has entered quantity and measurement unit, allow save. 
        self.quantitySpinBox.valueChanged.connect(self.addFoodButtonEnable)
        self.unitComboBox.currentIndexChanged.connect(self.addFoodButtonEnable)

        self.recipeDict = {'ingredients' : [], 'servings' : 0}

    def loadRecipe(self):
        for row, ingredientData in enumerate(self.recipeDict['ingredient']):
            for col, col_data in enumerate(ingredient)



    def addFoodButtonEnable(self):
        if self.quantitySpinBox.value() == 0.0 or self.unitComboBox.currentText() == '':
            self.addFoodPushButton.setEnabled(False)
        else:
            self.addFoodPushButton.setEnabled(True)

    def addFoodButtonClicked(self):
        '''Loads ingredientQuantityDialog. Upon confirmation, saves '''


        ingredientData = (self.currentNDB_No, 
                            self.quantitySpinBox.value(),
                            self.unitComboBox.currentText())

        self.recipeDict['ingredients'] = ingredientData

            
    def removeFoodButtonClicked(self):
        
        if self.recordedFoodTableWidget.currentRow() < 0:
            return        

        deleteQuery = 'DELETE from diet_history WHERE _ROWID_ = {}'
        recipeNDB_No = self.recordedFoodBuffer[self.recordedFoodTableWidget.currentRow()]
        #print(self.recordedFoodTableWidget.currentRow())
        connection = sqlite3.connect('./diet_history/diet_history.db')
        c = connection.cursor()
        c.execute(deleteQuery.format(str(rowID)))
        connection.commit()

        connection.close()

        self.loadDietHistory()
        
        self.recordedFoodTableWidget.clearSelection()

        #print(self.recordedFoodTableWidget.currentRow())


    # load FdGrp_Desc
    def loadFdGrp(self):
        connection = sqlite3.connect('./database/sr28.db')
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
        '''sr28 query is executed upon changed character string in queryLineEdit.
        Searches the Long_Desc column for each space delimited string in queryLineEdit.
        Implemented a hacky work around using like clauses as sqlite3 does not have a
        REGEXP function.'''

        # do not query if search box is devoid of non whitespace characters.
        if len(self.queryLineEdit.text().strip()) == 0:
            return

        connection = sqlite3.connect('./database/sr28.db')
        connection.text_factory = str

        rawInput = self.queryLineEdit.text().strip()
        FdGrp_Desc = str(self.foodGroupComboBox.currentText())

        queryBase = 'SELECT Long_Desc,NDB_No FROM food_des WHERE '
        likeClause = 'Long_Desc LIKE \'%{}%\''
        clauseList = [likeClause.format(i) for i in rawInput.split()]

        # filter by food group
        FdGrpFilter = 'FdGrp_Cd == \'{}\' AND '.format(self.FdGrpDict[FdGrp_Desc])

        # omit query food group condition if foodGroupCombo box is empty.
        if len(FdGrp_Desc) != 0:
            userQuery = queryBase + '(' + FdGrpFilter  + ' AND '.join(clauseList) + ');'
        else:
            userQuery = queryBase + '(' + ' AND '.join(clauseList) + ');'

        result = connection.execute(userQuery)

        # Save NDB_No for mapping to other tables in sr28.db
        self.foodDesBuffer = []

        self.resultTableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.resultTableWidget.insertRow(row_number)

            self.resultTableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(row_data[0][1:-1]))

            self.foodDesBuffer.append(row_data[1])

        connection.close()


class mainWindowLogic(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
        # display today's diet history
        self.loadDietHistory()

        # on user's change of selected day, display available diet history
        self.foodCalendarWidget.clicked.connect(self.loadDietHistory)
        self.foodCalendarWidget.selectionChanged.connect(self.loadDietHistory)

        # on user's change of selected month, clear displayed diet history
        self.foodCalendarWidget.currentPageChanged.connect(self.clearDietHistory)

        # on Add Food call, open ingredientQuantityDialog
        self.addFoodPushButton.clicked.connect(self.addFoodButtonClicked)

        # on Remove Food call, delete selected recordedFoodTableWidget entry from food_history
        self.removeFoodPushButton.clicked.connect(self.removeFoodButtonClicked)
        
    
        self.addFoodDialog = None


    def addFoodButtonClicked(self):
        '''Loads ingredientQuantityDialog. Upon confirmation, saves '''

        if self.addFoodDialog is not None:
            return
        
        entryDate = self.foodCalendarWidget.selectedDate().toString('yyyy-MM-dd')
        self.addFoodDialog = ingredQuantDialogLogic()
        self.addFoodDialog.show()

        rsp = self.addFoodDialog.exec_()

        if rsp == QtWidgets.QDialog.Accepted:
            #self.addFoodDialog.time, self.addFoodDialog.currentNDB_No, self.addFoodDialog.quantity, self.addFoodDialog.units.
            diet_historyEntry = (entryDate,
                                    self.addFoodDialog.consumptionTimeEdit.time().toString('hh:mm AP'), 
                                    self.addFoodDialog.currentNDB_No, 
                                    self.addFoodDialog.quantitySpinBox.value(),
                                    self.addFoodDialog.unitComboBox.currentText())

            

            insertData = 'INSERT INTO diet_history (Date, Time, NDB_No, Quantity, Units) VALUES  (?,?,?,?,?)'
            connection = sqlite3.connect('./diet_history/diet_history.db')
            c = connection.cursor()
            c.execute(insertData, diet_historyEntry)
            connection.commit()
            connection.close()
            self.loadDietHistory()
     
        self.addFoodDialog = None

    def removeFoodButtonClicked(self):
        
        if self.addFoodDialog is not None or self.dietHistoryBuffer == [] or self.recordedFoodTableWidget.currentRow() < 0:
            return        

        deleteQuery = 'DELETE from diet_history WHERE _ROWID_ = {}'
        rowID = self.dietHistoryBuffer[self.recordedFoodTableWidget.currentRow()]
        #print(self.recordedFoodTableWidget.currentRow())
        connection = sqlite3.connect('./diet_history/diet_history.db')
        c = connection.cursor()
        c.execute(deleteQuery.format(str(rowID)))
        connection.commit()

        connection.close()

        self.loadDietHistory()
        
        self.recordedFoodTableWidget.clearSelection()

        #print(self.recordedFoodTableWidget.currentRow())

    def loadDietHistory(self):
        '''Queries user diet history for date displayed on foodCalendarWidget.
        diet_history.db contains columns Date, Time, NDB_No, Quantity, Units.
        diet_history.db will be created if none exists.'''

        self.recordedFoodTableWidget.setRowCount(0)
        createTable = 'CREATE TABLE IF NOT EXISTS diet_history (Date TEXT, Time TEXT, NDB_No TEXT, Quantity REAL, Units TEXT);'
        diet_historyConnection = sqlite3.connect('./diet_history/diet_history.db')
        diet_historyConnection.execute(createTable)

        queryBase = 'SELECT _ROWID_,* FROM diet_history WHERE Date == \'{}\''
        queryQDate = self.foodCalendarWidget.selectedDate()
        queryDate = queryQDate.toString('yyyy-MM-dd')
        query = queryBase.format(queryDate)
        diet_historyResult = diet_historyConnection.execute(query)

        
        sr28Connection = sqlite3.connect('./database/sr28.db')
        food_desQuery = 'SELECT Long_Desc FROM food_des WHERE NDB_No == \'{}\''

        self.dietHistoryBuffer = []
    
        for row_number, row_data in enumerate(diet_historyResult):
            self.recordedFoodTableWidget.insertRow(row_number)

            recordedFoodVals = list(row_data[2:])
            self.dietHistoryBuffer.append(row_data[0])
            sr28Result = sr28Connection.execute(food_desQuery.format(row_data[3]))
            sr28Result = [i for i in sr28Result][0][0]
            recordedFoodVals[1] = sr28Result[1:-1]
            
            for col_number, col_data in enumerate(recordedFoodVals):
                self.recordedFoodTableWidget.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(col_data)))


        sr28Connection.close()
        diet_historyConnection.close()


    def clearDietHistory(self):
        '''Removes displayed rows in recordedFoodTableWidget'''

        self.dietHistoryBuffer = []
        self.recordedFoodTableWidget.setRowCount(0)

    
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mainWindowLogic()
    w.show()
    sys.exit(app.exec_())
