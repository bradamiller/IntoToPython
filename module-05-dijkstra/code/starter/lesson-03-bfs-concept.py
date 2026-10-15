# Lesson 3: Breadth-First Search -- The Concept
# Watch the algorithm spread out from the start one ring at a time.
# No robot needed to run this file.
#
# Team: ________________________
# Date: ________________________
#
# On paper you wrote 0 on the start, 1 on everything one step away, 2 on
# every NEW intersection one step from a 1, and so on. The first number you
# wrote on the destination is the length of the shortest path. In code:
#   to_visit  -- the ring you are working on (a list; oldest first)
#   previous  -- where you came from to reach each intersection (a dictionary)
#   ring      -- the number you wrote on each intersection (a dictionary)


# ===== HELPER: Build a Graph (Lessons 1-2) =====
def build_graph(rows, cols, blocked):
    graph = {}
    for r in range(rows):
        for c in range(cols):
            if (r, c) in blocked:
                continue
            neighbors = []
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in blocked:
                    neighbors.append((nr, nc))
            graph[(r, c)] = neighbors
    return graph


def print_grid(rows, cols, blocked, numbers):
    """Draw the grid: X for a blocked intersection, otherwise the number in
    the numbers dictionary (a ring number, a distance, ...), or . if none."""
    print("     ", end="")
    for c in range(cols):
        print(str(c).rjust(3), end="")
    print()
    print("    " + "-" * (3 * cols + 1))
    for r in range(rows):
        print(str(r).rjust(2) + " | ", end="")
        for c in range(cols):
            if (r, c) in blocked:
                print("  X", end="")
            elif (r, c) in numbers:
                print(str(numbers[(r, c)]).rjust(3), end="")
            else:
                print("  .", end="")
        print()


# ===== PART 1: Explore the Graph =====
print("===== 3x3 Grid Graph (no obstacles) =====")
graph = build_graph(3, 3, [])
for node in graph:
    print(node, "->", graph[node])
print()


# ===== PART 2: Graph with a Blocked Node =====
print("===== Graph with (1,1) blocked =====")
# TODO: build the 3x3 graph with (1,1) blocked and print it
# graph = build_graph(3, 3, [???])
# for node in graph:
#     print(node, "->", graph[node])
print()


# ===== PART 3: Set up the trace =====
print("===== BFS Trace: (0,0) to (2,2) with (1,1) blocked =====")
graph = build_graph(3, 3, [(1, 1)])
start = (0, 0)
destination = (2, 2)

previous = {start: None}     # the start is reached; it came from nowhere
ring = {start: 0}            # the start is ring 0
to_visit = [start]           # the only place to look around so far

print("Ring 0:", [start])
print()


# ===== PART 4: Run the Algorithm Step by Step =====
step = 0
while len(to_visit) > 0:
    # TODO: take the OLDEST intersection off the front of to_visit
    # current = to_visit.pop(???)
    step = step + 1
    print("--- Step", step, ": looking around", current, "(ring", ring[current], ") ---")

    # TODO: if current is the destination, print a message and break
    # if current == ???:
    #     print("Reached the destination!")
    #     break

    for neighbor in graph[current]:
        if neighbor not in previous:             # never reached before
            # TODO: record where we came from, give it a ring number one
            #       bigger than current's, and add it to to_visit
            # previous[neighbor] = ???
            # ring[neighbor] = ring[???] + 1
            # to_visit.append(???)
            print("  Reached", neighbor, "for the first time -- ring", ring[neighbor], ", came from", current)
        else:
            print("  Already reached", neighbor, "-- ignore")
    print("  Still to look around:", to_visit)
    print()


# ===== PART 5: Walk the Path Back =====
print("===== Path Reconstruction =====")
path = []
current = destination
# TODO: walk back through previous until you reach the start, collecting
#       each intersection along the way. The start itself is NOT part of the
#       path (the robot is already there).
# while current != ???:
#     print("  At", current, ", came from", previous[current])
#     path.append(current)
#     current = previous[???]

# TODO: the list is backwards -- flip it
# path.reverse()

print()
print("Shortest path (the intersections to drive TO):", path)
print("Steps:", len(path))
print("Ring number on the destination:", ring[destination], "-- the same thing")

# ===== PART 6: The Picture =====
# The ring numbers, drawn on the grid. X is the blocked intersection. Compare
# this with the numbers you wrote on paper.
print()
print_grid(3, 3, [(1, 1)], ring)
