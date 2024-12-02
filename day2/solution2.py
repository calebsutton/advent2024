import re
safe = 0
total = 0

def check(diffs):
    return set(diffs) <= {-1,-2,-3} or set(diffs) <= {1, 2, 3}

with open("input.txt", "r") as file:
    for line in file:
        levels = line.split(" ")
        dropped_lists = [ levels[:i] + levels[i + 1:] for i in range(len(levels)) ]
        if any([ check([int(list[i - 1]) - int(list[i]) for i in range(len(list))[1:]]) for list in dropped_lists]):
            safe += 1
        total += 1

print(f"{safe}/{total}")
