goals = 0
total_goals = 0
player_name = ""
while True:
    command = input()
    if command == "END":
        break
    player_name = command
    goals = int(input())
    if goals >= 10:
        break
    total_goals += goals
    if goals < total_goals:
        total_goals -= goals
        continue
print(f"{player_name} is the best player!")
if goals >= 3:
    print(f"He has scored {goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goals} goals.")






