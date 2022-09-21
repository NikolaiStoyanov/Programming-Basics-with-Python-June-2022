annual_tax = int(input())
basketball_shoes_price = annual_tax - (annual_tax * 0.4)
basketball_kit_price = basketball_shoes_price - (basketball_shoes_price * 0.2)
basketball_price = 1/4 * basketball_kit_price
accessories_pr = 1 / 5 * basketball_price
total_equipment_price = annual_tax + basketball_shoes_price + basketball_kit_price + basketball_price + accessories_pr
print(total_equipment_price)
