length = int(input())
width = int(input())
height = int(input())
percent = float(input())

capacity = length * width * height

capacity_in_lt = capacity / 1000

needed_lt = capacity_in_lt * (1 - (percent/100))
print(needed_lt)
   