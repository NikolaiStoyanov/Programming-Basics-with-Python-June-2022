number = int(input())
num = 0
total_sum = 0
while True:
    num = int(input())
    total_sum = total_sum + num
    if total_sum >= number:
        print(total_sum)
        break
    else:
        continue


