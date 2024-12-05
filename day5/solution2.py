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

def fix_job(job):
    for rule in rules:
        lower, upper = rule.split("|")
        pages = job.split(",")
        if not check_rule(rule, job):
            target_index = 0 if pages.index(upper) == 0 else pages.index(upper) - 1
            pages.remove(lower)
            pages.insert(target_index, lower)
        job = ",".join(pages)
    return job

invalid_jobs = [ job for job in print_jobs if not validate_job(job)]

total = 0
for job in invalid_jobs:
    while not validate_job(job):
        job = fix_job(job)

    pages = job.split(",")
    total += return_middle(pages)

print(total)