import sys
import db
passwordMatch = False
masterPass = "test"

def getMasterPassword():
    masterPasswordInput = input("Please type master password: ")
    if(masterPass == masterPasswordInput):
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
                pass

            elif(option == 2):
                appName = input("From which app you want password? ")
                database.getPassByApp(appName)
                input("\nPress any key to continue...")

            elif(option == 3):
                url = input("From which URL you want password? ")
                database.getPassByUrl(url)
                input("\nPress any key to continue...")

            elif(option == 4):
                Username = input("From which Username you want password? ")
                database.getPassByUsername(Username)
                input("\nPress any key to continue...")

        except ValueError:
            print("You gave wrong option\n")
