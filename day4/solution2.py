with open("input.txt", "r") as file:
    content = file.read().splitlines() 

total = 0

def bounds(y, x):
    return 0 <= y < len(content) and 0 <= x < len(content[y])

def check(y, x):
    if content[y][x] == "A":
        matches = 0
        if bounds(y - 1, x - 1) and bounds(y + 1, x + 1) and bounds(y - 1, x + 1) and bounds(y + 1, x - 1):
            for dy in [-1, 1]:
                for dx in [-1, 1]:
                    if content[y + dy][x + dx] == "M" and content[y + dy * -1][x + dx * -1] == "S":
                        matches += 1
                    if content[y + dy][x + dx] == "S" and content[y + dy * -1][x + dx * -1] == "M":
                        matches += 1
        if matches == 4:
            return True
    return False    

for y in range(len(content)):
    for x in range(len(content[y])):
        if check(y, x):
            total += 1

print(total)