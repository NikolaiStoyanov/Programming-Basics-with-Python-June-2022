age = int(input())
price_wash_machine = float(input())
price_per_toy = int(input())

brother_count = 0
count_toys = 0
total_sum = 0
current_money = 10
for i in range(1, age + 1):
    if i % 2 != 0:
        count_toys = count_toys + 1
    else:
        brother_count = brother_count + 1
        total_sum = total_sum + current_money
        current_money = current_money + 10


result = total_sum + (count_toys * price_per_toy) - brother_count
diff = abs(result - price_wash_machine)
if result >= price_wash_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")


