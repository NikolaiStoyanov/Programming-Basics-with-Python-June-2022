start = int(input())
final = int(input())
magic_number = int(input())
combination_counter = 0
total_sum = 0
is_valid = False

for first_number in range(start, final + 1):
    for second_number in range(start, final + 1):
        combination_counter += 1
        if first_number + second_number == magic_number:
            is_valid = True

            break
    if is_valid:
        break
if is_valid:
    print(f"Combination N:{combination_counter} \n({first_number} + {second_number} = {magic_number})")
else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")








