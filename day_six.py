# how many questions did anyone respond yes to?
answer_sets = []

with open('project_files/day6-puzzle1.txt', 'r') as f:
    answers = set()
    while True:
        line = f.readline()
        if line.isspace():
            answer_sets.append(answers)
            answers = set()
            continue
        if not line:
            break
        line_split = line.strip()
        for answer in line_split:
            answers.add(answer)
    answer_sets.append(answers)

print(sum(len(val) for val in answer_sets))

# how many questions did everyone respond yes to?
answer_sets = []

with open('project_files/day6-puzzle1.txt', 'r') as f:
    answers = set(l for l in 'abcdefghijklmnopqrstuvwxyz')
    while True:
        line = f.readline()
        if line.isspace():
            answer_sets.append(answers)
            answers = set(l for l in 'abcdefghijklmnopqrstuvwxyz')
            continue
        if not line:
            break
        line_split = line.strip()
        answers = answers & set(l for l in line_split)
    answer_sets.append(answers)

print(sum(len(val) for val in answer_sets))