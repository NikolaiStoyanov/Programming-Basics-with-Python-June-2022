stage = input()
ticket_type = input()
number_of_tickets = int(input())
photo = input()
ticket_price = 0

if stage == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = 55.50
    elif ticket_type == "Premium":
        ticket_price = 105.20
    elif ticket_type == "VIP":
        ticket_price = 118.90
elif stage == "Semi final":
    if ticket_type == "Standard":
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    elif ticket_type == "VIP":
        ticket_price = 300.40
elif stage == "Final":
    if ticket_type == "Standard":
        ticket_price = 110.10
    elif ticket_type == "Premium":
        ticket_price = 160.66
    elif ticket_type == "VIP":
        ticket_price = 400

total_price = number_of_tickets * ticket_price

if total_price > 4000:
    total_price = total_price * 0.75

else:
    if total_price > 2500:
        total_price = total_price * 0.90

    if photo == "Y":
        total_price += number_of_tickets * 40 # total_price = total_price + number_of_tickets * 40


print(f"{total_price:.2f}")
