# Lesson 2: Tuples — Packaging Coordinates Together - SOLUTION
# Instead of separate row/col variables, use a tuple: (row, col)
#
# A tuple groups values together:
#   position = (2, 3)    # row 2, col 3
#   position[0]          # gets the row (2)
#   position[1]          # gets the col (3)


# ===== PART 1: Creating Position Tuples =====
start = (0, 0)
destination = (2, 3)
print("Start:", start)
print("Destination:", destination)


# ===== PART 2: Accessing Row and Column =====
print("Destination row:", destination[0])
print("Destination col:", destination[1])


# ===== PART 3: Comparing Positions =====
current = (0, 0)
print("At start?", current == start)
print("At destination?", current == destination)


# ===== PART 4: Manhattan Distance with Tuples =====
row_dist = destination[0] - start[0]
col_dist = destination[1] - start[1]
total = row_dist + col_dist
print("Manhattan distance:", total)


# ===== PART 5: Multiple Destinations =====
dest_a = (1, 2)
dest_b = (3, 1)
dest_c = (2, 4)

dist_a = (dest_a[0] - start[0]) + (dest_a[1] - start[1])
print("Distance to", dest_a, "is", dist_a)

dist_b = (dest_b[0] - start[0]) + (dest_b[1] - start[1])
print("Distance to", dest_b, "is", dist_b)

dist_c = (dest_c[0] - start[0]) + (dest_c[1] - start[1])
print("Distance to", dest_c, "is", dist_c)
