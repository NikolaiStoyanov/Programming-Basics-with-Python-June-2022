needed_money = float(input())
available_money = float(input())
sequent_days = 0
past_days = 0
total_money = available_money

while total_money < needed_money:
    if sequent_days == 5:
        break

    type_of_action = input()
    used_money = float(input())
    past_days += 1

    if type_of_action == "save":
        total_money = total_money + used_money

        sequent_days = 0

    elif type_of_action == "spend":
        total_money = total_money - used_money
        sequent_days += 1
        if total_money <= 0:
            total_money = 0


if sequent_days == 5:
    print(f"You can't save the money.")
    print(f"{past_days}")
elif total_money >= needed_money:
    print(f"You saved the money for {past_days} days.")





