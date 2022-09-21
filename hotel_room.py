month = input()
nights = int(input())
night_price = 0
studio_price = 0
apartment_price = 0
if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
total_studio_price = nights * studio_price
total_apartment_price = nights * apartment_price
if (month == "May" or month == "October") and nights > 14:
    total_studio_price = total_studio_price * 0.70
else:
    if (month == "May" or month == "October") and nights > 7:
        total_studio_price = total_studio_price * 0.95
if (month == "June" or month == "September") and nights > 14:
    total_studio_price = total_studio_price * 0.80
if nights > 14:
    total_apartment_price = total_apartment_price * 0.90

print(f"Apartment: {total_apartment_price:.2f} lv.")
print(f"Studio: {total_studio_price:.2f} lv.")
