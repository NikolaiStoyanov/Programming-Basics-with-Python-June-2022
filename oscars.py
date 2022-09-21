name = input()
points = float(input())
number_judge = int(input())

total_points = points
for i in range(1, number_judge + 1):
    name_judge = input()
    points_judge = float(input())

    actor_points = (len(name) * points) / 2
    total_points = total_points + actor_points
    if total_points >= 1250.5:
        break

if total_points < 1250.5:
    needed_points = 1250.5 - total_points
    print(f"Sorry, {name} you need {needed_points:.1f} more!")
else:
    print(f"Congratulations, {name} got a nominee for leading role with {total_points:.1f}!")

