with open("input.txt") as f:
    food = f.readlines()
inventory = [calories for calories in food]


elf = []
cal_per_elf = []
for calories in inventory:
    if calories != "\n":
        cal_per_elf.append(int(calories.strip())) 
    else:
        cal_per_elf = []
    elf.append(cal_per_elf)


total_calories = []
for cal in elf:
    if cal not in total_calories:
        total_calories.append(cal)


# PART 1
totals = [sum(i) for i in total_calories]
print(max(totals))

# PART 2
totals.sort(reverse=True)
print(sum(totals[:3]))
