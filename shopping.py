budget = int(input())
command = input()
total_sum = 0
while command != "End":
    prices = int(command)
    total_sum += prices
    if total_sum > budget:
        break
    command = input()
if command == "End":
    print(f"You bought everything needed.")
elif total_sum > budget:
    print(f"You went in overdraft!")