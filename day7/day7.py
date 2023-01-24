comms = [com.strip("\n $").split() for com in open("day7\\test.txt", "r")]


fw = "cd"
bk = "cd .."

path =[]


opn = 0
for i in comms:
    main = []
    dirs = []
    files = []
    if i[0] == "cd":
        if i[-1] == "..":
            pass    
    main.append(i[-1])
    path.append(main)

print(path)
    
    






































'''
ls = "n"
for row in comms:
    print(row)
    if  ls == "y" and row[0] != "ls":
        parent = row[-1]
        paths.setdefault(parent, []).append(child)
        ls = "n"
    if row[0] == "cd":
        ls = "y"
'''        


