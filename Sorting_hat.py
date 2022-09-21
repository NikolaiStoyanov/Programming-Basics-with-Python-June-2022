command = input()


while True:

    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")

    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    elif len(command) > 6 and command != "Voldemort" and command != "Welcome!":
        print(f"{command} goes to Hufflepuff.")

    if command == "Voldemort":
        print("You must not speak of that name!" )
        break
    if command == "Welcome!":
        print("Welcome to Hogwarts.")
        break

    command = input()