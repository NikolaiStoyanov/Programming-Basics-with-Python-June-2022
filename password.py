name = input()
password = input()
password_entrance = ""
while True:
    if password_entrance == password:
        print(f"Welcome {name}!")
        break
    else:
        password_entrance = input()

