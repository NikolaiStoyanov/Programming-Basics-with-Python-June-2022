start = int(input())
end = int(input())
magic_number = int(input())
combinations = 0
combination_is_found = False
for first_number in range(start, end + 1):
    for second_number in range(start, end + 1):
        combinations += 1
        if first_number + second_number == magic_number:
            combination_is_found = True
            break

    if combination_is_found:
        break
if combination_is_found:
    print(f"Combination N:{combinations} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{combinations} combinations - neither equals {magic_number}")


