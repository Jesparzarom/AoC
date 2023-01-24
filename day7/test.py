with open("day7\\test.txt", "r") as f:
    input_ = f.read()
signal = [comm.strip("\n") for comm in input_.splitlines()]