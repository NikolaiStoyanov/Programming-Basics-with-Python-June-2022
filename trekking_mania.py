number_of_groups = int(input())
musala_people = 0
monblant_people = 0
kilimanjaro_people = 0
k2_people = 0
everest_people = 0
for i in range(1, number_of_groups + 1):
    number_of_people_in_groups = int(input())
    if number_of_people_in_groups <= 5:
        musala_people = musala_people + number_of_people_in_groups
    elif 6 <= number_of_people_in_groups <= 12:
        monblant_people = monblant_people + number_of_people_in_groups
    elif 13 <= number_of_people_in_groups <= 25:
        kilimanjaro_people = kilimanjaro_people + number_of_people_in_groups
    elif 26 <= number_of_people_in_groups <= 40:
        k2_people = k2_people + number_of_people_in_groups
    else:
        everest_people = everest_people + number_of_people_in_groups

total_people = musala_people\
               + monblant_people\
               + kilimanjaro_people\
               + k2_people\
               + everest_people

percent_musala_people = musala_people / total_people * 100
percent_monblant_people = monblant_people / total_people * 100
percent_kilimanjaro_people = kilimanjaro_people / total_people * 100
percent_k2_people = k2_people / total_people * 100
percent_everest_people = everest_people / total_people * 100



print(f"{percent_musala_people:.2f}%")
print(f"{percent_monblant_people:.2f}%")
print(f"{percent_kilimanjaro_people:.2f}%")
print(f"{percent_k2_people:.2f}%")
print(f"{percent_everest_people:.2f}%")











#print(musala_people, monblant_people, kilimanjaro_people, k2_people, everest_people)

