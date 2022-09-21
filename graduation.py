name = input()
average_grade = 0
total_sum = 0

while True:

    grade = float(input())
    if grade >= 4:
        total_sum = total_sum + grade

        print(f"{name} graduated. Average grade: {average_grade}")

    if grade == 2:
        print(f"{name} has been excluded at {total_sum} grade")













    # total_sum = total_sum + grade
    # average_grade = total_sum / 12
