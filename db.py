from h11 import Data
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
    def test(self):
        mycursor = self.connection.cursor()
        query = "SELECT * FROM Apps"
        print(mycursor.execute(query))
        self.connection.commit()

x = DatabaseOperations()
x.addPass("Facebook", "www.facebook.com", "Pablo", "123xyz")