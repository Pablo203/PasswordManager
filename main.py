import sys
import db
import pymysql
import hashlib
passwordMatch = False

def getMasterPassword():
    masterPasswordInput = input("Please type master password: ")

    connection = pymysql.connect(
            host = 'localhost', 
            user = 'root',
            password = '',
            database = 'passes'
        )
    #Hash inputed phrase
    hashedPass = hashlib.md5(masterPasswordInput.encode())
    hashedPass = hashedPass.hexdigest()
    print(hashedPass)

    #Get hash from db
    mycursor = connection.cursor()
    query = "SELECT Pass FROM Pass WHERE ID = 1"
    mycursor.execute(query)
    result = mycursor.fetchone()
    dbHash = []
    for i in result:
        dbHash.append(i)
    print(dbHash[0])

    if(hashedPass == dbHash[0]):
        print("Please come in")
        return True
    else:
        sys.exit("Password given by you is wrong")


while True:
    if(passwordMatch == False):
        passwordMatch = getMasterPassword()
    else:
        print("Welcome \nWhat would you want to do?")
        print("1 - Add new password")
        print("Get password:")
        print("\t2 - By app name")
        print("\t3 - By URL")
        print("\t4 - By Username")
        option = input()
        try:
            option = int(option)
            database = db.DatabaseOperations()
            if(option > 4 or option < 1):
                print("You gave wrong option\n")
            elif(option == 1):
                app = input("Give app name: ")
                url = input("Give url name: ")
                username = input("Give username: ")
                password = input("Give password: ")

                input("\nPress enter to continue...")
                database.addPass(app, url, username, password)

            elif(option == 2):
                appName = input("From which app you want password? ")
                database.getPassByApp(appName)
                input("\nPress enter to continue...")

            elif(option == 3):
                url = input("From which URL you want password? ")
                database.getPassByUrl(url)
                input("\nPress enter to continue...")

            elif(option == 4):
                Username = input("From which Username you want password? ")
                database.getPassByUsername(Username)
                input("\nPress enter to continue...")

        except ValueError:
            print("You gave wrong option\n")
