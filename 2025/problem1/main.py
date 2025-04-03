from solver import Solver


##### Part 1 #####
with open("input.txt") as f:
    text = f.readlines()
solver = Solver(text)
answer = solver.Solve1()
print(f"Answer of part 1 = {answer}")

##### Part 2 #####
answer = solver.Solve2()
print(f"Answer of part 2 = {answer}")

##### Part 3 #####
answer = solver.Solve3()
print(f"Answer of part 3 = {answer}")
