row_offsets = [1,1,1,1,2]
col_offsets = [1,3,5,7,1]

def count_trees(row_offset, col_offset):
    row = -1
    col = 0

    trees = 0
    with open('project_files/day3-puzzle1.txt', 'r') as f:
        while True:
            line = f.readline()
            if line == " ":
                continue
            if not line:
                break
            row += 1

            if row == 0:
                continue

            line = line.strip()
            if row % row_offset is 0:
                col = (col + col_offset) % len(line)
                if line[col] == '#':
                    trees += 1
                    line = line[:col] + 'X' + line[col+1:]
                else:
                    line = line[:col] + '0' + line[col+1:]

    return trees

answer = 1
for i in range(5):
    answer *= count_trees(row_offsets[i], col_offsets[i])

print(answer)