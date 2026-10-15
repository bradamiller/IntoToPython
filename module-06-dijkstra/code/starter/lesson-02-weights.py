# Module 6, Lesson 2: Weights in the Graph
#
# Team: ________________________
# Date: ________________________
# The slow segment becomes a number, and the harness learns to add up the
# cost of a path. BFS still plans by steps, so it fails the new check -- on
# paper, before anyone touches a robot. No robot needed to run this file.
#
# A weight is "how many normal blocks' worth of time". Measure it with a
# stopwatch in Lesson 1: if a normal block takes 4 seconds and the slow
# segment takes 12, its weight is 3.


# ===== The grid, the blocked list, and (NEW) the slow edges =====

ROWS = 4
COLS = 4
BLOCKED = []
SLOW_EDGES = []      # NEW: each entry is (intersection_a, intersection_b, cost)


def add_blocked(intersection):
    if intersection not in BLOCKED:
        BLOCKED.append(intersection)


def clear_blocked():
    while len(BLOCKED) > 0:
        BLOCKED.pop()


def add_slow_edge(a, b, cost):
    """NEW: the segment between a and b takes 'cost' blocks' worth of time.
    Measure it with a stopwatch: if a normal block takes 4 seconds and this
    one takes 12, its cost is 3."""
    SLOW_EDGES.append((a, b, cost))


def clear_slow_edges():
    while len(SLOW_EDGES) > 0:
        SLOW_EDGES.pop()


def weight(a, b):
    """NEW: how much the segment from a to b costs. 1 unless it is slow."""
    # TODO: look through SLOW_EDGES for an entry that joins a and b
    #       (in either order!) and return its cost
    # TODO: if none matches, return 1
    return 1


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


# ===== Planner 2: BFS, unchanged from Lesson 5 (for comparison) =====

def compute_bfs_path(position, destination):
    graph = build_graph(ROWS, COLS, BLOCKED)
    if position not in graph or destination not in graph:
        return []

    previous = {position: None}
    to_visit = [position]

    while len(to_visit) > 0:
        current = to_visit.pop(0)
        if current == destination:
            break
        for neighbor in graph[current]:
            if neighbor not in previous:
                previous[neighbor] = current
                to_visit.append(neighbor)

    if destination not in previous:
        return []

    path = []
    current = destination
    while current != position:
        path.append(current)
        current = previous[current]
    path.reverse()
    return path


# ===== One more property for the harness: total cost =====

def path_cost(position, path):
    """NEW: add up the weight of every segment the path drives."""
    total = 0
    here = position
    # TODO: for each step in the path, add weight(here, step) to total,
    #       then move 'here' forward to that step
    return total


# ===== The Module 5 harness, plus one property: cost =====

# The expected cost is worked out BY HAND for Lesson 2 (trace the cheapest
# route on the grid and add up its weights). Lesson 3 writes the planner
# that finds it.

def check_cost(test_name, position, destination, path, expected_cost):
    cost = path_cost(position, path)
    if cost == expected_cost:
        print("PASS:", test_name, "- cost", cost)
    else:
        print("FAIL:", test_name, "- cost", cost, "but the cheapest route costs", expected_cost)
        print("      path:", path)


# ===== Try it =====

print("=== No slow edges: BFS passes the cost check ===")
path = compute_bfs_path((0, 0), (0, 3))
check_cost("open row, (0,0) to (0,3)", (0, 0), (0, 3), path, 3)
print()

print("=== Slow segment between (0,1) and (0,2), weight 5 ===")
add_slow_edge((0, 1), (0, 2), 5)
path = compute_bfs_path((0, 0), (0, 3))
print("BFS path:", path, " steps:", len(path), " cost:", path_cost((0, 0), path))
# By hand: go round through row 1 instead -- 5 steps, every one a normal block.
# TODO: work out the cheapest route's cost by hand and put it in place of ???
EXPECTED = 0   # <-- replace 0 with the cost of the cheapest route
check_cost("slow row, (0,0) to (0,3)", (0, 0), (0, 3), path, EXPECTED)
print()
print("BFS counts steps. 3 steps beat 5 steps, so it picks the slow road and")
print("pays 7 blocks' worth of time for a trip that could cost 5.")
print("That is the limitation Lesson 3 fixes.")
