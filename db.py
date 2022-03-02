import pymysql
import base64

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
        encodedBytes = base64.b64encode(password.encode("utf-8"))
        password = str(encodedBytes, "utf-8")
        mycursor.execute(query, (app, url, username, password))
        self.connection.commit()


    def getPassByApp(self, appName):
        #Create cursor for operations on database
        mycursor = self.connection.cursor()
        #Prepare query
        query = "SELECT App, URL, Username, Password FROM Apps WHERE App = %s"
        #Execute query
        mycursor.execute(query, (appName))
        #Write returned data into list
        result = mycursor.fetchone()
        data = []
        for info in result:
            data.append(info)

        for i in range(3):
            print(data[i])
        #Decode encrypted password and display it
        data[3] = base64.b64decode(data[3]).decode("utf-8")
        print(data[3])
        self.connection.commit()

    def getPassByUrl(self, URL):
        #Create cursor for operations on database
        mycursor = self.connection.cursor()
        #Prepare query
        query = "SELECT App, URL, Username, Password FROM Apps WHERE URL = %s"
        #Execute query
        mycursor.execute(query, (URL))
        #Write returned data into list
        result = mycursor.fetchone()
        data = []
        for info in result:
            data.append(info)

        for i in range(3):
            print(data[i])
        #Decode encrypted password and display it
        data[3] = base64.b64decode(data[3]).decode("utf-8")
        print(data[3])
        self.connection.commit()

    def getPassByUsername(self, Username):
        #Create cursor for operations on database
        mycursor = self.connection.cursor()
        #Prepare query
        query = "SELECT App, URL, Username, Password FROM Apps WHERE Username = %s"
        #Execute query
        mycursor.execute(query, (Username))
        #Write returned data into list
        result = mycursor.fetchone()
        data = []
        for info in result:
            data.append(info)

        for i in range(3):
            print(data[i])
        #Decode encrypted password and display it
        data[3] = base64.b64decode(data[3]).decode("utf-8")
        print(data[3])
        self.connection.commit()