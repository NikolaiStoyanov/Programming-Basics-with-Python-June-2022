type_shoot = input()
rows = int(input())
columns = int(input())
ticket = 0

if type_shoot == "Premiere":
    ticket = 12
elif type_shoot == "Normal":
    ticket = 7.5
elif type_shoot == "Discount":
    ticket = 5

total_price = (rows * columns) * ticket

print(f"{total_price:.2f} leva")
