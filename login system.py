correct_username = "admin"
correct_password = "12345"

attempts = 3

# while True:
while attempts > 0:
    
    username = input("username: ")
    password = input("password: ")

    if username == correct_username and password == correct_password:
        print("login successful")
        break
    else:
        print("invalid cred")
        attempts -= 1 
        print("attempts left:", attempts)

if attempts == 0:
    print("acc locked");
