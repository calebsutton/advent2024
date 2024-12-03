import re

with open("input.txt", "r") as file:
    content = file.read()

result = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", content)
print(sum([int(a) * int(b) for a, b in result]))