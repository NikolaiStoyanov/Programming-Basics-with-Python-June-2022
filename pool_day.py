number_of_people = int(input())
entrance_price = float(input())
price_per_sunbed = float(input())
price_per_beach_umbrella = float(input())

total_entrance_price = number_of_people * entrance_price
total_sunbed_price = (number_of_people * 75/100) * price_per_sunbed
total_beach_umbrella_price = (number_of_people * 50/100) * price_per_beach_umbrella
total_price = total_entrance_price + total_sunbed_price + total_beach_umbrella_price
print(total_price)

