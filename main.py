import actions
passwordMatch = False




while True:
    if(passwordMatch == False):
        passwordMatch = actions.getMasterPassword()
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
            if(option > 4 or option < 1):
                print("You gave wrong option\n")
            elif(option == 1):
                pass
            elif(option == 2):
                pass
            elif(option == 3):
                pass
            elif(option == 4):
                pass
        except ValueError:
            print("You gave wrong option\n")
