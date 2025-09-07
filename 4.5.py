correct_username = "SimonRo"
correct_password = "Khatra Barz"
i = 0
while i < 5:
    username = input("enter your username: ")
    password = input("enter your password: ")
    if username == correct_username and password == correct_password:
        print("welcome")
        break
    else:
        i += 1
        print("enter again")
else:
    print("Access denied")
