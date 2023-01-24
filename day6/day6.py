with open("day6\\input.txt", "r") as f:
    input_ = f.read()
signal = [comm.strip("\n") for comm in input_.split()]

# PACKET'S
packet1 = [signal[0][index : 4 + index] for index in range(len(signal[0]))] # pack = 4
packet2 = [signal[0][index : 14 + index] for index in range(len(signal[0]))] # pack = 14


# PART 1
combos1 = [
    combination
    for combination in packet1
    if len(set(combination)) == len(combination) and len(combination) == 4
]

print([f"{combos1[0]} -----> {[packet1.index(i) + 4]}" for i in combos1[0:1]])


# PART 2
combos2 = [
    combination
    for combination in packet2
    if len(set(combination)) == len(combination) and len(combination) == 14
]

print([f"{combos2[0]} -----> {[packet2.index(i) + 14]}" for i in combos2[0:1]])
