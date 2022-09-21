actor_name = input()
academy_points = float(input())
number_of_jury = int(input())
is_valid = False
total_points = 0
for _ in range(1, number_of_jury + 1):
    jury_name = input()
    jury_points = float(input())
    total_points += (len(jury_name) * jury_points) / 2
    all_points = total_points + academy_points
    if all_points > 1250.5:
        is_valid = True
        break
if is_valid:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {all_points:.1f}!")
else:
    needed_points = abs(1250.5 - all_points)
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")



