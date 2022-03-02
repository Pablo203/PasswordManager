import pymysql

class DatabaseOperations:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost', 
            user = 'root',
            password = '',
            database = 'passes'
        )


    def addPass(self, app, url, username, password):
        mycursor = self.connection.cursor()
        query = "INSERT INTO Apps (App, URL, Username, Password) VALUES (%s, %s, %s, %s)"
        mycursor.execute(query, (app, url, username, password))
        self.connection.commit()


    def getPassByApp(self, appName):
        mycursor = self.connection.cursor()
        query = "SELECT App, URL, Username, Password FROM Apps WHERE App = %s"
        mycursor.execute(query, (appName))
        result = mycursor.fetchone()
        for data in result:
            print(data)
        self.connection.commit()

    def getPassByUrl(self, URL):
        mycursor = self.connection.cursor()
        query = "SELECT App, URL, Username, Password FROM Apps WHERE URL = %s"
        mycursor.execute(query, (URL))
        result = mycursor.fetchone()
        for data in result:
            print(data)
        self.connection.commit()

    def getPassByUsername(self, Username):
        mycursor = self.connection.cursor()
        query = "SELECT App, URL, Username, Password FROM Apps WHERE Username = %s"
        mycursor.execute(query, (Username))
        result = mycursor.fetchone()
        for data in result:
            print(data)
        self.connection.commit()



    def test(self):
        mycursor = self.connection.cursor()
        query = "SELECT * FROM Apps"
        print(mycursor.execute(query))
        self.connection.commit()