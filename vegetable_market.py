per_kilogram_vegetables = float(input())
per_kilogram_fruits = float(input())
total_kilogram_vegetables = int(input())
total_kilogram_fruits = int(input())

vegetables_price = per_kilogram_vegetables * total_kilogram_vegetables
fruits_price = per_kilogram_fruits * total_kilogram_fruits

total_price = (vegetables_price + fruits_price) / 1.94

print("{:.2f}".format(total_price))
