safe = 0
total = 0

with open("input.txt", "r") as file:
    for line in file:
        levels = line.split(" ")
        diffs = [int(levels[i - 1]) - int(levels[i]) for i in range(len(levels))[1:]]
        if set(diffs) <= {-1,-2,-3} or set(diffs) <= {1, 2, 3}:
            safe += 1
        total += 1

print(f"{safe}/{total}")