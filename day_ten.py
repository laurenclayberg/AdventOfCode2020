adaptors = [0]

with open('project_files/day10-puzzle1.txt', 'r') as f:
    while True:
        line = f.readline()
        if line.isspace():
            continue
        if not line:
            break
        
        adaptors.append(int(line.strip()))

adaptors = sorted(adaptors)

count_diff_1 = 0
count_diff_3 = 1  # my device is 3 above the highest adaptor
for i in range(len(adaptors) - 1):
    difference = adaptors[i+1] - adaptors[i]
    if difference == 1:
        count_diff_1 += 1
    elif difference == 3:
        count_diff_3 += 1

print("Puzzle 1 solution: ", count_diff_1 * count_diff_3)

# get full set of adaptors
adaptors.append(max(adaptors) + 3)

dp_solutions = [1, 1]
# get solution for third adaptor
if adaptors[2] <= 3:
    dp_solutions.append(2)
else:
    dp_solutions.append(1)

for i in range(3, len(adaptors)):
    cur = adaptors[i]

    cur_solution = 0
    if cur - adaptors[i-1] <= 3:
        cur_solution += dp_solutions[i-1]
    if cur - adaptors[i-2] <= 3:
        cur_solution += dp_solutions[i-2]
    if cur - adaptors[i-3] <= 3:
        cur_solution += dp_solutions[i-3]
    dp_solutions.append(cur_solution)

print("Puzzle 2 solution: ", dp_solutions[-1])