import numpy as np 
import re

airplane = [ [ 0 for _ in range(8) ] for _ in range(128)]

airplane_row = []
airplane_col = []

def convert_ticket_to_row_col(ticket):
    row = int(re.sub("B", "1", re.sub("F", "0", ticket[:7])), 2)
    col = int(re.sub("R", "1", re.sub("L", "0", ticket[7:])), 2)
    return (row, col)

with open('project_files/day5-puzzle1.txt', 'r') as f:
    while True:
        line = f.readline()
        if line.isspace():
            continue
        if not line:
            break
        row, col = convert_ticket_to_row_col(line.strip())
        airplane_row.append(row)
        airplane_col.append(col)
        airplane[row - 1][col - 1] = 1

seat_ids = set()

def get_seat_id(row, col):
    return row * 8 + col

# what is the max seat?
max_seat = 0
for i in range(len(airplane_row)):
    seat = get_seat_id(airplane_row[i], airplane_col[i])
    max_seat = max(max_seat, seat)
    seat_ids.add(seat)

# what is my seat?
for i in range(128):
    for j in range(8):
        if airplane[i][j] == 0:
            seat = get_seat_id(i+1, j+1)
            if seat + 1 in seat_ids and seat - 1 in seat_ids:
                print(seat)
