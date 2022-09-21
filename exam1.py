budget = float(input())
category = input()
people_per_group = int(input())
left_money = 0
needed_money = 0
if category == "VIP":
    if 1 <= people_per_group <= 4:
        budget = budget - budget * 0.75
    elif 5 <= people_per_group <= 9:
        budget = budget - budget * 0.60
    elif 10 <= people_per_group <= 24:
        budget = budget - budget * 0.50
    elif 25 <= people_per_group <= 49:
        budget = budget - budget * 0.40
    elif people_per_group >= 50:
        budget = budget - budget * 0.25
elif category == "Normal":
    if 1 <= people_per_group <= 4:
        budget = budget - budget * 0.75
    elif 5 <= people_per_group <= 9:
        budget = budget - budget * 0.60
    elif 10 <= people_per_group <= 24:
        budget = budget - budget * 0.50
    elif 25 <= people_per_group <= 49:
        budget = budget - budget * 0.40
    elif people_per_group >= 50:
        budget = budget - budget * 0.25
total_price = people_per_group * 499.99
total_price1 = people_per_group * 249.99
if category == "VIP" and budget >= total_price:
    left_money = abs(budget - 499.99 * people_per_group)
    print(f"Yes! You have {left_money:.2f} leva left.")
elif category == "VIP" and budget < total_price:
    needed_money = abs(499.99 * people_per_group - budget)
    print(f"Not enough money! You need {needed_money:.2f} leva.")

if category == "Normal" and budget >= total_price1:
    left_money = abs(budget - 249.99 * people_per_group)
    print(f"Yes! You have {left_money:.2f} leva left.")
elif category == "Normal" and budget < total_price1:
    needed_money = abs(249.99 * people_per_group - budget)
    print(f"Not enough money! You need {needed_money:.2f} leva.")



