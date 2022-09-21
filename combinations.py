number = int(input())
number_of_combinations = 0

for x1 in range(number + 1):
    for x2 in range(number + 1):
        for x3 in range(number + 1):
            if x1 + x2 + x3 == number:
                number_of_combinations += 1

print(number_of_combinations)
