# Lesson 3: Breadth-First Search -- The Concept - SOLUTION
# Watch the algorithm spread out from the start one ring at a time, the way
# you traced it on paper. No robot needed to run this file.
#
# The idea: stand at the start and write 0 on it. Every intersection you can
# reach in one step gets a 1. Every NEW intersection you can reach from a 1
# gets a 2. Keep going. The first time you write a number on the destination,
# that number is the length of the shortest path -- and if you also wrote
# down WHERE YOU CAME FROM each time, you can walk the numbers back down to
# the start to get the path itself.
#
# In code, "the ring you are working on" is a list called to_visit, and
# "where you came from" is a dictionary called previous.


# ===== HELPER: Build a Graph (Lessons 1-2) =====
def build_graph(rows, cols, blocked):
    """Build a graph dictionary for a rows x cols grid, excluding blocked nodes."""
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


# ===== PART 1: Explore the Graph =====
print("===== 3x3 Grid Graph (no obstacles) =====")
graph = build_graph(3, 3, [])
for node in graph:
    print(node, "->", graph[node])
print()


# ===== PART 2: Graph with a Blocked Node =====
print("===== Graph with (1,1) blocked =====")
graph = build_graph(3, 3, [(1, 1)])
for node in graph:
    print(node, "->", graph[node])
print()


# ===== PART 3: Trace BFS by Hand =====
print("===== BFS Trace: (0,0) to (2,2) with (1,1) blocked =====")
graph = build_graph(3, 3, [(1, 1)])
start = (0, 0)
destination = (2, 2)

previous = {start: None}     # start is reached; it came from nowhere
ring = {start: 0}            # the number you wrote on each intersection
to_visit = [start]

print("Ring 0:", [start])
print()


# ===== PART 4: Run the Algorithm Step by Step =====
step = 0
while len(to_visit) > 0:
    current = to_visit.pop(0)        # the OLDEST one in the list
    step = step + 1
    print("--- Step", step, ": looking around", current, "(ring", ring[current], ") ---")

    if current == destination:
        print("Reached the destination!")
        break

    for neighbor in graph[current]:
        if neighbor not in previous:             # never reached before
            previous[neighbor] = current
            ring[neighbor] = ring[current] + 1
            to_visit.append(neighbor)
            print("  Reached", neighbor, "for the first time -- ring", ring[neighbor], ", came from", current)
        else:
            print("  Already reached", neighbor, "-- ignore")
    print("  Still to look around:", to_visit)
    print()


# ===== PART 5: Walk the Path Back =====
print("===== Path Reconstruction =====")
path = []
current = destination
while current != start:
    print("  At", current, ", came from", previous[current])
    path.append(current)
    current = previous[current]

path.reverse()
print()
print("Shortest path (the intersections to drive TO):", path)
print("Steps:", len(path))
print("Ring number on the destination:", ring[destination], "-- the same thing")
