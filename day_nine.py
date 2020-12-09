def check_if_sum_in_list(list_values, sum_value):
    for v in range(len(list_values)):
        if sum_value - list_values[v] in [list_values[i] for i in range(len(list_values)) if i != v]:
            return True
    return False


def first_invalid_xmas_number(filename, preamble_size):
    preamble = []
    preamble_start = 0
    
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if line.isspace():
                continue
            if not line:
                break
            
            if len(preamble) < preamble_size:
                preamble.append(int(line.strip()))
            else:
                current_preamble = preamble[preamble_start:]
                current_value = int(line.strip())

                if not check_if_sum_in_list(current_preamble, current_value):
                    return current_value

                preamble_start += 1
                preamble.append(current_value)

toy_solution = first_invalid_xmas_number('project_files/day9-toy.txt', 5)
print(toy_solution)
solution = first_invalid_xmas_number('project_files/day9-puzzle1.txt', 25)
print(solution)

def contiguous_sum(filename, sum_value):
    numbers = []
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if line.isspace():
                continue
            if not line:
                break
            
            numbers.append(int(line.strip()))

    size = 2
    while True:
        for i in range(len(numbers) - size):
            if min(numbers[i:i+size]) > sum_value:
                break
            if sum(numbers[i:i+size]) == sum_value:
                return min(numbers[i:i+size]) + max(numbers[i:i+size])
        size += 1
        if size > len(numbers):
            break

def contiguous_sum_faster(filename, sum_value):
    numbers = []
    cumsums = {}
    cumsums_list = []
    total = 0
    idx = -1
    with open(filename, 'r') as f: # O(n)
        while True:
            line = f.readline()
            if line.isspace():
                continue
            if not line:
                break
            number = int(line.strip())
            total += number
            idx += 1
            numbers.append(number) # O(1)
            cumsums[total] = idx # O(1)
            cumsums_list.append(total) # O(1)

    for i in range(len(numbers)): # O(n)
        min_val = cumsums_list[i]
        if min_val + sum_value in cumsums: # O(1)
            max_idx = cumsums[min_val + sum_value] # O(1)
            # add 1 because the current cumsum is not part of the contiguous group
            return min(numbers[i+1:max_idx+1]) + max(numbers[i+1:max_idx+1]) # O(n) but only happens once


print(contiguous_sum('project_files/day9-toy.txt', toy_solution))
print(contiguous_sum('project_files/day9-puzzle1.txt', solution))

print("Faster:")
print(contiguous_sum_faster('project_files/day9-toy.txt', toy_solution))
print(contiguous_sum_faster('project_files/day9-puzzle1.txt', solution))