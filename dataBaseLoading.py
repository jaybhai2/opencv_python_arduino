import mysql.connector

class dbConnectModule:

    def __init__(self,hostname,userId,password,database):
        self.hostname = hostname
        self.userId = userId
        self.password = password
        self.database = databases
        self.mydb = mysql.connector.connect (host=self.hostname, 
                                        user=self.userId, passwd = self.password, 
                                        database = self.database)
        
        self.cursor = self.mydb.cursor()

    def insertIntoTable(self, tableName, valueTuple):
        
        length = len(valueTuple)
        Str1 = "%s"
        for i in range(length-1):
            Str2 += ",%s"
        sqlCommand = 'INSERT INTO ' + tableName + ' VALUES ('+ Str2 +')' 
       
        self.cursor.execute(sqlCommand,valueTuple)

        self.mydb.commit()

#establish connectiong to mysql database
mydbconnect = dbConnectModule('localhost','root','123456','pydb')  

#testing 
mydbconnect.insertIntoTable('PE',("mang","65489"))
