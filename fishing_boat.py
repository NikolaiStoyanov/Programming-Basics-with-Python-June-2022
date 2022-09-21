budget = int(input())
season = input()
marines = int(input())

rent = 0
if season == "Spring":
    if marines <= 6:
        rent = 3000 * 0.90
    elif 7 <= marines <= 11:
        rent = 3000 * 0.85
    elif marines >= 12:
        rent = 3000 * 0.75
elif season == "Summer":
    if marines <= 6:
        rent = 4200 * 0.90
    elif 7 <= marines <= 11:
        rent = 4200 * 0.85
    elif marines >= 12:
        rent = 4200 * 0.75
elif season == "Autumn":
    if marines <= 6:
        rent = 4200 * 0.90
    elif 7 <= marines <= 11:
        rent = 4200 * 0.85
    elif marines >= 12:
        rent = 4200 * 0.75
elif season == "Winter":
    if marines <= 6:
        rent = 2600 * 0.90
    elif 7 <= marines <= 11:
        rent = 2600 * 0.85
    elif marines >= 12:
        rent = 2600 * 0.75

if marines % 2 == 0 and season == "Spring":
    rent = rent * 0.95
elif marines % 2 == 0 and season == "Winter":
    rent = rent * 0.95
elif marines % 2 == 0 and season == "Summer":
    rent = rent * 0.95
left_money = abs(budget - rent)
if budget > rent:
    print(f"Yes! You have {left_money:.2f} leva left.")
elif budget < rent:
    print(f"Not enough money! You need {left_money:.2f} leva.")