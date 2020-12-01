numbers_list = []
with open('project_files/day1-puzzle1.txt', 'r') as f:
	while True:
		line = f.readline()
		if not line:
			break
		numbers_list.append(int(line.strip()))
print(numbers_list)
for i in numbers_list:
	for j in numbers_list:
		for k in numbers_list:
			if i + j + k == 2020:
				print(i * j * k)
