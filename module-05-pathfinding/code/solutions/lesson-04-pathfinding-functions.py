# Lesson 4: The Pathfinding Functions - SOLUTION
# Organizing the pathfinding code into a small toolkit, the way Lesson 2-8
# organized the sensor code. No robot needed to run this file.
#
# The toolkit has one job: answer "how do I get from here to there?" while
# remembering which intersections are blocked. Three pieces:
#   build_graph()         -- the grid as a dictionary (Lessons 1-2)
#   add_blocked()         -- remember a blocked intersection
#   compute_bfs_path()    -- the planner (a placeholder today; Lesson 5 fills it in)
#
# Two rules every planner in this course follows:
#   - compute_xxx_path(position, destination) is TOLD where the robot is.
#     A planner never remembers position; the driving code owns that.
#   - The path it returns is the list of intersections to drive TO. The robot's
#     own position is not in it, so len(path) is the number of steps.


# ===== The grid and the blocked list =====

ROWS = 4
COLS = 4
BLOCKED = []     # every planner that cares about obstacles reads this list


def add_blocked(intersection):
    """Remember that an intersection is blocked. On the robot, the rangefinder
    loop calls this when it sees an obstacle (Lesson 7). In a test, you call it
    yourself to set up an obstacle course on paper."""
    if intersection not in BLOCKED:
        BLOCKED.append(intersection)


def clear_blocked():
    """Forget every blocked intersection."""
    while len(BLOCKED) > 0:
        BLOCKED.pop()


def build_graph(rows, cols, blocked):
    """Build the graph dictionary for a rows x cols grid.
    Blocked intersections are left out, and nothing connects to them."""
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


def compute_bfs_path(position, destination):
    """Shortest path from position to destination, avoiding BLOCKED.
    (Placeholder -- Lesson 5 writes the real one.)"""
    graph = build_graph(ROWS, COLS, BLOCKED)      # rebuilt every call, so it
    print("compute_bfs_path is not written yet!")  # always matches BLOCKED
    return []


# ===== PART 1: Build a Graph =====
graph = build_graph(ROWS, COLS, BLOCKED)
print("Number of intersections in the graph:", len(graph))


# ===== PART 2: Examine the Graph =====
print("\n===== Graph =====")
for node in graph:
    print(node, "->", graph[node])


# ===== PART 3: Block an intersection and rebuild =====
add_blocked((1, 1))
graph = build_graph(ROWS, COLS, BLOCKED)
print("\n===== Graph with (1,1) blocked =====")
print("Blocked:", BLOCKED)
print("Number of intersections:", len(graph))
print("(1,1) in graph?", (1, 1) in graph)
print("Neighbors of (0,1):", graph[(0, 1)], " <- (1,1) is gone from the list")

# Adding the same one twice does nothing
add_blocked((1, 1))
print("Blocked after adding (1,1) again:", BLOCKED)


# ===== PART 4: Call the planner (placeholder) =====
path = compute_bfs_path((0, 0), (3, 3))
print("\nPath:", path)
clear_blocked()
