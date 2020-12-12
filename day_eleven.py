seats = []
with open('project_files/day11-puzzle1.txt', 'r') as f:
    while True:
        line = f.readline()
        if line.isspace():
            continue
        if not line:
            break

        row = list(line.strip())
        seats.append(row)

import numpy as np 
floor = set()
for row in range(len(seats)):
    for col in range(len(seats[row])):
        if seats[row][col] == '.':
            floor.add((row+1,col+1))


seats_binary = np.zeros((len(seats)+2,len(seats[0])+2), np.int32) # padded with 0s around the outside
while True:
    seats_swap = np.zeros(seats_binary.shape, np.int32)
    for row in range(1,seats_swap.shape[0]-1):
        for col in range(1,seats_swap.shape[1]-1):
            if (row,col) in floor:
                continue
            if np.sum(seats_binary[row-1:row+2,col-1:col+2]) == 0:
                seats_swap[row,col] = 1
            elif np.sum(seats_binary[row-1:row+2,col-1:col+2]) >= 5 and seats_binary[row,col] == 1:
                seats_swap[row,col] = 1
    if np.sum(seats_swap) == 0:
        break
    seats_binary = (seats_binary + seats_swap) % 2

print("Solution 1: ", np.sum(seats_binary))

closest_seats = [[[] for _ in range(len(seats[0])+2)] for _ in range(len(seats)+2)]
def get_closest_seats(row, col):
    result = []

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            r = row
            c = col
            while r > 0 and c > 0 and r < len(closest_seats) and c < len(closest_seats[0]):
                r += i
                c += j
                if (r,c) not in floor:
                    result.append((r,c))
                    break

    return result

for i in range(len(closest_seats)):
    for j in range(len(closest_seats[0])):
        closest_seats[i][j] = get_closest_seats(i, j)

seats_binary = np.zeros((len(seats)+2,len(seats[0])+2), np.int32) # padded with 0s around the outside
while True:
    seats_swap = np.zeros(seats_binary.shape, np.int32)
    for row in range(1,seats_swap.shape[0]-1):
        for col in range(1,seats_swap.shape[1]-1):
            count_seats = 0
            if (row,col) in floor:
                continue
            for i, j in closest_seats[row][col]:
                count_seats += seats_binary[i,j]
            if count_seats == 0 and seats_binary[row,col] == 0:
                seats_swap[row,col] = 1
            elif count_seats >= 5 and seats_binary[row,col] == 1:
                seats_swap[row,col] = 1
    if np.sum(seats_swap) == 0:
        break
    seats_binary = (seats_binary + seats_swap) % 2

print("Solution 2: ", np.sum(seats_binary))