budget = float(input())
season = input()
destination = ""
needed_money = 0
place = ""
if season == "summer":
    if budget <= 100:
        destination = "Bulgaria"
        needed_money = budget * 0.3
    elif budget <= 1000:
        destination = "Balkans"
        needed_money = budget * 0.4
    elif budget > 1000:
        destination = "Europe"
        needed_money = budget * 0.9
elif season == "winter":
    if budget <= 100:
        destination = "Bulgaria"
        needed_money = budget * 0.7
    elif budget <= 1000:
        destination = "Balkans"
        needed_money = budget * 0.8
    elif budget > 1000:
        destination = "Europe"
        needed_money = budget * 0.9

if (season == "summer" and destination == "Bulgaria") \
        or (season == "summer" and destination == "Balkans"):
    place = "Camp"
elif (season == "winter" and destination == "Bulgaria") \
        or (season == "winter" and destination == "Balkans") \
        or destination == "Europe":
    place = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place} - {needed_money:.2f}")