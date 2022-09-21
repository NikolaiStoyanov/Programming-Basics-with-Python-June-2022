number_of_int = int(input())

for i in range(number_of_int):
    number = int(input())

    if number % 2 != 0:
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")


