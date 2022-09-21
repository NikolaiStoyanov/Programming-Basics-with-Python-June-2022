open_browsers = int(input())
salary = float(input())
taxes = 0
for i in range(1, open_browsers + 1):
    website_name = input()
    if website_name == "Facebook":
        taxes = taxes + 150
    elif website_name == "Instagram":
        taxes = taxes + 100
    elif website_name == "Reddit":
        taxes = taxes + 50

result = salary - taxes

if result <= 0:
    print("You have lost your salary.")
else:
    print(f"{result:.0f}")


