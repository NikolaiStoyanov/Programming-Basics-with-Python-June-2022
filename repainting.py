nylon = int(input())
lit = int(input())
number_of_lit = int(input())
hours = int(input())
nylon_sum = (nylon + 2) * 1.50
paint_sum = (lit * 0.1 + lit) * 14.50
raz = number_of_lit * 5.00
total_sum_materials = nylon_sum + paint_sum + raz + 0.40

master_sum = (total_sum_materials * 0.3) * hours
final_sum = total_sum_materials + master_sum
print(final_sum)
