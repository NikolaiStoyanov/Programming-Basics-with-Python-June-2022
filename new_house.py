type_of_flowers = input()
flowers = int(input())
budget = int(input())
final_price = 0
if type_of_flowers == "Roses":
    final_price = flowers * 5
    if flowers > 80:
        final_price = (flowers * 5) * 0.90
elif type_of_flowers == "Dahlias":
    final_price = flowers * 3.80
    if flowers > 90:
        final_price = (flowers * 3.80) * 0.85
elif type_of_flowers == "Tulips":
    final_price = flowers * 2.80
    if flowers > 80:
        final_price = (flowers * 2.80) * 0.85
elif type_of_flowers == "Narcissus":
    final_price = flowers * 3
    if flowers < 120:
        final_price = (flowers * 3) * 1.15
elif type_of_flowers == "Gladiolus":
    final_price = flowers * 2.50
    if flowers < 80:
        final_price = (flowers * 2.50) * 1.20


if budget > final_price:
    left_money = budget - final_price
    print(f"Hey, you have a great garden with {flowers} {type_of_flowers} and {left_money:.2f} leva left.")
elif budget < final_price:
    left_money = abs(budget - final_price)
    print(f"Not enough money, you need {left_money:.2f} leva more.")

