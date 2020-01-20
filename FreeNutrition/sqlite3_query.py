import sqlite3
import sys

rawInput = sys.argv[1].upper()
queryBase = 'SELECT Shrt_Desc, NDB_No FROM food_des WHERE '
likeClause = 'Shrt_Desc LIKE \'%{}%\''
clauseList = [likeClause.format(i) for i in rawInput.split()]
userQuery = queryBase + '(' + ' AND '.join(clauseList) + ');'

print(userQuery)
