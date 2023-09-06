# what should I make
def sign_up():
    log_sign = input("login or sign up:\n")
    if log_sign == "sign up":
        name = input("please enter our name:\n")
        while True:
            password = input("please enter a 5 digit password:\n")
            conform = input("please conform password:\n")
            try:
                if password == conform:
                    print("you have successfully signed up!!!!!!")
                    break
                else:
                    print("Error please try again")
            except:
                pass


def login():
    log_sign = input("login or sign up:\n")
    if log_sign == "login":
        user_name=input("please enter your user name:\n")
        password = input("please enter your password:\n")
        if password == "12345" and user_name == "bertlomewos fissha":
            print("you have logged in successfully!!!")
        else:
            print("you have input a wrong pin or wrong user name, please try again")
            choose = input("would you like to sign up or try again:\n")
            if choose == "sign up":
                sign_up()
            else:
                login()


login()
sign_up()