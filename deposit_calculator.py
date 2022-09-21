deposit_value = int(input())
months = int(input())
annual_percent = float(input())

interest = deposit_value * (annual_percent/100)
per_month = interest / 12
total_sum = deposit_value + months * per_month
print(total_sum)