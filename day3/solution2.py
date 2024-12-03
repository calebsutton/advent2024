import re

with open("input.txt", "r") as file:
    content = file.read()

result = re.findall(r"(do\(\))|(don't\(\))|(mul\((\d{1,3}),(\d{1,3})\))", content)

total = 0
process = True

for a, b, c, d, e in result:
    if a:
        process = True
    elif b:
        process = False
    elif process:
        total += int(d) * int(e)
        
print(total)