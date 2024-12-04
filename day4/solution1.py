with open("input.txt", "r") as file:
    content = file.read().splitlines() 

total = 0

def bounds(y, x):
    return 0 <= y < len(content) and 0 <= x < len(content[y])

def check(y, x, dy, dx):
    if content[y][x] == "X":
        if bounds(y + dy * 3, x + dx * 3) and bounds(y + dy * 2, x + dx * 2) and bounds(y + dy, x + dx):
            if content[y + dy][x + dx] == "M":
                if content[y + dy * 2][x + dx * 2] == "A":
                    if content[y + dy * 3][x + dx * 3] == "S":
                        return True
    return False    

for y in range(len(content)):
    for x in range(len(content[y])):
        if check(y, x, -1, 0):
            total += 1
        if check(y, x, 1, 0):
            total += 1
        if check(y, x, 0, -1):
            total += 1
        if check(y, x, 0, 1):
            total += 1
        if check(y, x, -1, -1):
            total += 1
        if check(y, x, 1, 1):
            total += 1
        if check(y, x, -1, 1):
            total += 1
        if check(y, x, 1, -1):
            total += 1

print(total)