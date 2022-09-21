import sys


min_number = sys.maxsize

while True:
    numbers = input()

    if numbers == "Stop":
        break

    numbers = int(numbers)

    if numbers < min_number:
        min_number = numbers


print(min_number)
