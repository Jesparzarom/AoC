with open("day5\\input.txt") as s:
    stk = [f.split() for f in s.readlines()]

stacks = {}
for box in stk[0:9]:
    stacks[int(box[0])] = box[1:]

steps = [(int(step[1]), int(step[3]), int(step[5])) for step in stk[10:512]]
    


def moves(q, from_, _to):
        stacks[_to] += reversed(stacks[from_][-q::])
        del stacks[from_][-q::]


def moves2(q, from_, _to):
        stacks[_to] += stacks[from_][-q::]
        del stacks[from_][-q::]     
  
        
for i in steps:
    q, from_, _to = i[0], i[1], i[2]
    moves2(q, from_, _to)


for stack in stacks.items():
    print(stack)
