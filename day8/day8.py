maps = [row.strip("\n") for row in open("day8/input.txt", "r").readlines()]
#maps = ["30373", "25512", "65332", "33549", "35390"]

length = len(maps)
rows = [trees for trees in maps]
cols = []
v = 0

for m in range(length):
    col = []
    for i in range(length):
        col.append(maps[i][v])
    cols.append(col)
    v += 1




def outside():
    externals = [((len(cols) * 2) - 4) + ((len(rows) * 2))]
    print("EXTERNS:", externals[0])
    return externals[0]


def inside():
    visibles = []
    cont = 0

    for x in range(1, (length - 1)):
        for y in range(1, (len(maps[x]) - 1)):

            pos = int(maps[x][y])
            above, below = int(maps[x - 1][y]), int(maps[x + 1][y])
            before, after = int(maps[x][y - 1]), int(maps[x][y + 1])

            if (
                (int(max(maps[x][:y])) < pos)
                or (int(max(maps[x][y:])) < pos)
                or (int(max(cols[x][:y])) < pos)
                or (int(max(cols[x][-y:])) < pos)
            ):
                visibles.append(pos)
                #print(f"row: {x} col: {y} ==> {pos}")
    
            #print(cols[:x][-1], cols[-2])
            #print(cols[x][-y:])
        cont += 1



        
    print("VISIBLES", len(visibles))
    return visibles


print("TOTAL:", len(inside()) + outside())
