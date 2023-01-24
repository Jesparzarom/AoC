FILE = "day2\input.txt"
with open(FILE) as f:
    r = f.readlines()
rounds = [game.strip().split(" ") for game in r]

draw = [["A", "X"], ["B", "Y"], ["C", "Z"]]
elf_wins = [["A", "Z"], ["B", "X"], ["C", "Y"]]
me_wins = [["C", "X"], ["A", "Y"], ["B", "Z"]]


def total_points(strategy):
    my_points = 0
    elf_points = 0

    for elf, me in strategy:
        # My POINTS
        my_points += me.count("X") * 1
        my_points += me.count("Y") * 2
        my_points += me.count("Z") * 3
        if [elf, me] in me_wins:
            my_points += 6

        # Elf POINTS
        elf_points += elf.count("A") * 1
        elf_points += elf.count("B") * 2
        elf_points += elf.count("C") * 3
        if [elf, me] in elf_wins:
            elf_points += 6

        # DRAW POINTS
        if [elf, me] in draw:
            my_points += 3
            elf_points += 3

    return my_points, elf_points


new_strategy = []
for choice in rounds:
    # ELF WINS
    if choice == draw[0]:
        new_strategy.append(elf_wins[0])
    elif choice == me_wins[0]:
        new_strategy.append(elf_wins[2])

    # ME WINS
    elif choice == elf_wins[0]:
        new_strategy.append(me_wins[1])
    elif choice == draw[2]:
        new_strategy.append(me_wins[0])

    # DRAW
    elif choice == elf_wins[2]:
        new_strategy.append(draw[2])
    elif choice == me_wins[1]:
        new_strategy.append(draw[0])

    # ELSE
    else:
        new_strategy.append(choice)


# PART 1
me, elf = total_points(rounds)
print(me)

# PART 2
me, elf = total_points(new_strategy)
print(me)
