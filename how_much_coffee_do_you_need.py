command = input()
coffees = 0
while command != "END":

    if command.lower() == "coding" or \
            command.lower() == "dog" or \
            command.lower() == "cat" or \
            command.lower() == "movie":
        if command.islower():
            coffees += 1
        else:
            coffees += 2
    command = input()
if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)
