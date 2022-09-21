hall_rent = int(input())

statuettes_price = hall_rent * 0.70
service = statuettes_price * 0.85
sound = service * 0.50

total_sum = statuettes_price + service + sound
all_cost = total_sum + hall_rent

print(f"{all_cost:.2f}")