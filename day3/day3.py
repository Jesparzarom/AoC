from more_itertools import grouper

with open("day3\input.txt") as f:
    bag = f.readlines()
st = [articles.strip('\n') for articles in bag]

lowrs = "abcdefghijklmnopqrstuvwxyz"
letters = lowrs + lowrs.upper()

# Priorities
priorities= {}
for ix, ltr in enumerate(letters):
    priorities[ltr] = ix+1
    
# Compartments
compartments = [(item[0:(len(item) // 2)], item[(len(item) // 2):]) for item in st]

# Same Article
found = [list(set(comp1).intersection(comp2))[0] for comp1, comp2 in compartments]

# Priorities values 
values = [priorities[art] for art in found if art in priorities.keys()]

# PART 1
print(sum(values))

# PART 2
b = list(grouper(st[:], 3))
group = [list(set(val[0]).intersection(val[1], val[2]))[0] for idx, val in enumerate(b)]
values2 = [priorities[art] for art in group if art in priorities.keys()]
print(sum(values2))
