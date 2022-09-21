first_number = input()
second_number = input()
first_number_first_digit = int(first_number[0])
first_number_second_digit = int(first_number[1])
first_number_third_digit = int(first_number[2])
first_number_fourth_digit = int(first_number[3])
second_number_first_digit = int(second_number[0])
second_number_second_digit = int(second_number[1])
second_number_third_digit = int(second_number[2])
second_number_fourth_digit = int(second_number[3])
for first_digit in range(first_number_first_digit, second_number_first_digit + 1):
    if first_digit % 2 == 0:
        continue
    for second_digit in range(first_number_second_digit, second_number_second_digit + 1):
        if second_digit % 2 == 0:
            continue
        for third_digit in range(first_number_third_digit, second_number_third_digit + 1):
            if third_digit % 2 == 0:
                continue
            for fourth_digit in range(first_number_fourth_digit, second_number_fourth_digit + 1):
                if fourth_digit % 2 == 0:
                    continue
                print(f"{first_digit}{second_digit}{third_digit}{fourth_digit}", end=" ")

