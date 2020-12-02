min_list = []
max_list = []
char_list = []
password_list = []
with open('project_files/day2-puzzle1.txt', 'r') as f:
    while True:
        line = f.readline()
        if line == " ":
            continue
        if not line:
            break
        line_split = line.strip().split(" ")
        numbers = line_split[0]
        character = line_split[1]
        password = line_split[2]
        min_list.append(int(numbers.split("-")[0]))
        max_list.append(int(numbers.split("-")[1]))
        char_list.append(character.split(":")[0])
        password_list.append(password)

def password_match(minimum, maximum, character, pw):
    total = 0
    for c in pw:
        if c == character:
            total += 1
    if total <= maximum and total >= minimum:
        return True
    return False

def password_match_problem2(loc1, loc2, character, pw):
    idx1 = loc1 - 1
    idx2 = loc2 - 1
    a = pw[idx1] == character 
    b = pw[idx2] == character 
    if (a and not b) or (b and not a):
        return True
    return False

# count = 0
# for i in range(len(password_list)):
#     if (password_match(min_list[i], max_list[i], char_list[i], password_list[i])):
#         count += 1

count = 0
for i in range(len(password_list)):
    if (password_match_problem2(min_list[i], max_list[i], char_list[i], password_list[i])):
        count += 1

print(count)