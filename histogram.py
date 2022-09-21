number = int(input())
p1_sum = 0
p2_sum = 0
p3_sum = 0
p4_sum = 0
p5_sum = 0
for num in range(1, number + 1):
    n = int(input())
    if n < 200:
        p1_sum += 1
    elif n <= 399:
        p2_sum += 1
    elif n <= 599:
        p3_sum += 1
    elif n <= 799:
        p4_sum += 1
    else:
        p5_sum += 1

p1_percent = p1_sum / number * 100
p2_percent = p2_sum / number * 100
p3_percent = p3_sum / number * 100
p4_percent = p4_sum / number * 100
p5_percent = p5_sum / number * 100
print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
print(f"{p4_percent:.2f}%")
print(f"{p5_percent:.2f}%")






