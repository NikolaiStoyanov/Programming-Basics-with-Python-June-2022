chicken_menus = int(input())
fish_menus = int(input())
vegan_menus = int(input())
chicken_menus_price = chicken_menus * 10.35
fish_menus_price = fish_menus * 12.40
vegan_menus_price = vegan_menus * 8.15
total_menus_price = chicken_menus_price + fish_menus_price + vegan_menus_price
desert_price = 0.2 * total_menus_price
delivery_price = 2.50
total_delivery_price = total_menus_price + desert_price + delivery_price
print(total_delivery_price)
