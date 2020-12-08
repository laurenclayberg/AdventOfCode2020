import re

bag_lookup = {}

class Bag:
    def __init__(self, color, first_parent=None):
        if first_parent == None:
            self.parents = []
        else:
            self.parents = [first_parent]
        self.children = {}
        self.color = color

    def add_parent(self, parent):
        self.parents.append(parent)

    def add_child(self, child, count):
        self.children[child] = count

def parse_line(line):
    line = line.strip()
    line_split = line.split(" bags contain ")

    current = line_split[0]

    if "no other bags" in line_split[1]:
        return (current, [], [])

    numbers = re.findall("\d+ ", line_split[1])

    line = re.sub(" bags\.", "", line_split[1])
    line = re.sub(" bag\.", "", line)
    line = re.sub("\d ", "", line)
    line = re.sub(" bag, ", "&", line)
    line = re.sub(" bags, ", "&", line)

    children = line.split("&")
    return (current, children, numbers)

def init_bags(current, children, numbers):
    if current not in bag_lookup:
        bag_lookup[current] = Bag(current)
    for c in range(len(children)):
        child = children[c]
        count = int(numbers[c].strip())
        bag_lookup[current].add_child(child, count)
        if child in bag_lookup:
            bag_lookup[child].add_parent(current)
        else:
            bag_lookup[child] = Bag(child, current)

with open('project_files/day7-puzzle1.txt', 'r') as f:
    while True:
        line = f.readline()
        if line.isspace():
            continue
        if not line:
            break
        current, children, numbers = parse_line(line)
        init_bags(current, children, numbers)

solution = set()
solution.add("shiny gold")
def solve_puzzle_1(color):
    for parent in bag_lookup[color].parents:
        if parent not in solution:
            solution.add(parent)
            solve_puzzle_1(parent)

solve_puzzle_1("shiny gold")
print("Puzzle 1: ", len(solution) - 1)

def solve_puzzle_2(color):
    global total
    current_total = 1 # self
    current = bag_lookup[color]
    for child, count in current.children.items():
        current_total += count * solve_puzzle_2(child)
    return current_total

total = solve_puzzle_2("shiny gold")
print("Puzzle 2: ", total - 1)
