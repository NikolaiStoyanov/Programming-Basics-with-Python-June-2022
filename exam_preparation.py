poor_grades = int(input())
times_failed = 0
has_failed = True
grades_sum = 0
last_problem = ""
total_problems = 0
while times_failed < poor_grades:
    problem_name = input()

    if problem_name == "Enough":
        has_failed = False
        break

    grade = int(input())

    if grade <= 4:
        times_failed += 1

    grades_sum += grade
    last_problem = problem_name
    total_problems += 1

if has_failed:
    print(f"You need a break, {poor_grades} poor grades.")
else:
    print(f"Average score: {grades_sum / total_problems:.2f}")
    print(f"Number of problems: {total_problems}")
    print(f"Last problem: {last_problem}")



