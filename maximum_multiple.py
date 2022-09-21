divisor = int(input())
boundary = int(input())
number1 = 0
for number in range(boundary, divisor, - 1):
    if number % divisor == 0:
        number1 += number
        break
print(number1)
