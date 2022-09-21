days = int(input())
type_room = input()
rate = input()
days = days - 1
room_for_one_person_price_night = 18
apartment_price_night = 25
president_apartment_price_night = 35

total_price_for_one_person = room_for_one_person_price_night * days
total_apartment_price = apartment_price_night * days
total_president_apartment_price = president_apartment_price_night * days

if type_room == "room for one person":
    if days < 10:
        total_price_for_one_person = room_for_one_person_price_night * days
    elif 10 < days < 15:
        total_price_for_one_person = room_for_one_person_price_night * days
    elif days > 15:
        total_price_for_one_person = room_for_one_person_price_night * days
    if rate == "positive":
        total_price_for_one_person = total_price_for_one_person * 1.25
    else:
        total_price_for_one_person = total_price_for_one_person * 0.90
    print(f"{total_price_for_one_person:.2f}")
elif type_room == "apartment":
    if days < 10:
        total_apartment_price = total_apartment_price * 0.70
    elif 10 < days < 15:
        total_apartment_price = total_apartment_price * 0.65
    elif days > 15:
        total_apartment_price = total_apartment_price * 0.50
    if rate == "positive":
        total_apartment_price = total_apartment_price * 1.25
    else:
        total_apartment_price = total_apartment_price * 0.90
    print(f"{total_apartment_price:.2f}")
elif type_room == "president apartment":
    if days < 10:
        total_president_apartment_price = total_president_apartment_price * 0.90
    elif 10 < days < 15:
        total_president_apartment_price = total_president_apartment_price * 0.85
    elif days > 15:
        total_president_apartment_price = total_president_apartment_price * 0.80
    if rate == "positive":
        total_president_apartment_price = total_president_apartment_price * 1.25
    else:
        total_president_apartment_price = total_president_apartment_price * 0.90
    print(f"{total_president_apartment_price:.2f}")



