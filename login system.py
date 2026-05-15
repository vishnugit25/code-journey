correct_username = "admin"
correct_password = "12345"

attempts = 3

# while True:
while attempts > 0:
    
    username = input("username: ")
    password = input("password: ")

    if username == correct_username and password == correct_password:
        print("login successful")
        print("Welcome user")
        break
    
    else:
        attempts -= 1 
        print("invalid cred")
        print("attempts left:", attempts)

        if attempts == 1:
           print("final attempt!")

if attempts == 0:
    print("acc locked");
