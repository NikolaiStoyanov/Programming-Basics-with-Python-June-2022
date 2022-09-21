wall_height = int(input())
wall_width = int(input())
non_painted_percent = int(input())
all_is_painted = False
area_for_painting = wall_height * wall_width * 4
area_for_painting = area_for_painting * (100 - non_painted_percent) / 100
command = input()

while command != "Tired!":
    paint = int(command)
    area_for_painting -= paint
    if area_for_painting <= 0:
        all_is_painted = True
        break
    command = input()
if all_is_painted:
    if area_for_painting < 0:
        print(f"All walls are painted and you have {abs(area_for_painting)} lpaint left!")

else:
    pass







