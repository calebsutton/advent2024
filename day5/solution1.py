import re

with open("input.txt", "r") as file:
    content = file.readlines()


# with open("test.txt", "r") as file:
#     content = file.readlines()

rules = []
print_jobs = []

parse_flag = True

for lines in content:
    if lines == "\n":
        parse_flag = False
        continue
    if parse_flag:
        rules.append(lines.strip())
    else:
        print_jobs.append(lines.strip())

def check_rule(rule, job):
    lower, upper = rule.split("|")
    if lower not in job or upper not in job:
        return True
    return bool(re.search(f"{lower}.*{upper}", job))


def validate_job(job):
    return all([check_rule(rule, job) for rule in rules])

def return_middle(pages):
    return int(pages[int((len(pages) - 1) / 2)])   

total = 0
for job in print_jobs:
    if validate_job(job):
        pages = job.split(",")
        total += return_middle(pages)

print(total)