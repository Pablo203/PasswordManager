import sys
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
        input("Here we are")