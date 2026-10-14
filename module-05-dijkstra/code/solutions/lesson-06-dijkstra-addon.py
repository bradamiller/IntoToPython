# Lesson 6 Optional Extension: Dijkstra's Algorithm - SOLUTION
# A THIRD planner, made by copying compute_bfs_path() and changing two things.
# No robot needed to run this file.
#
# BFS counts steps. Every step costs the same, so the path with the fewest
# steps is the fastest. But what if one segment of the grid is slow -- the
# tape takes a long winding detour between two intersections, so that "one
# block" takes as long as three? Then the fewest steps is no longer the
# fastest route, and BFS will happily send the robot down the slow road.
#
# Dijkstra's algorithm fixes that. It is BFS with two changes:
#   1. Instead of taking the OLDEST intersection off to_visit, take the one
#      with the SMALLEST distance so far.
#   2. Instead of "+1 step" use "+ the weight of this edge", and keep the
#      smaller total if you reach the same place a second time.
# Everything else -- the graph, add_blocked, previous, the walk-back -- is
# exactly the BFS code.
#
# To do this extension: copy your Lesson 5 file, rename the function
# compute_dijkstra_path, make the two changes marked NEW/CHANGED below, and
# add it to the Lesson 6 harness as a third planner.


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
    for (x, y, cost) in SLOW_EDGES:
        if (a == x and b == y) or (a == y and b == x):
            return cost
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


# ===== Planner 3: Dijkstra -- a copy of BFS with two changes =====

def closest(intersections, distance):
    """CHANGED (helper): of the intersections still to visit, the one with
    the smallest distance so far."""
    best = intersections[0]
    for node in intersections:
        if distance[node] < distance[best]:
            best = node
    return best


def compute_dijkstra_path(position, destination):
    graph = build_graph(ROWS, COLS, BLOCKED)
    if position not in graph or destination not in graph:
        return []

    previous = {position: None}
    distance = {position: 0}                 # NEW: best total cost found so far
    to_visit = [position]

    while len(to_visit) > 0:
        current = closest(to_visit, distance)    # CHANGED: was to_visit.pop(0)
        to_visit.remove(current)
        if current == destination:
            break
        for neighbor in graph[current]:
            new_distance = distance[current] + weight(current, neighbor)   # CHANGED: was "+1 step"
            if neighbor not in distance or new_distance < distance[neighbor]:  # CHANGED: keep the cheaper way
                distance[neighbor] = new_distance
                previous[neighbor] = current
                if neighbor not in to_visit:
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
    for step in path:
        total = total + weight(here, step)
        here = step
    return total


# ===== Compare BFS and Dijkstra =====

def compare(test_name, position, destination):
    print("--- " + test_name + " ---")
    for (name, planner) in [("BFS     ", compute_bfs_path), ("Dijkstra", compute_dijkstra_path)]:
        path = planner(position, destination)
        print("  " + name + "  steps:", len(path), " cost:", path_cost(position, path), " ", path)
    print()


print("========== No slow edges: they agree ==========")
compare("open (0,0) to (3,3)", (0, 0), (3, 3))
add_blocked((1, 0))
add_blocked((1, 1))
compare("wall at (1,0),(1,1): (0,0) to (3,0)", (0, 0), (3, 0))
clear_blocked()

print("========== A slow edge between (0,1) and (0,2), cost 5 ==========")
add_slow_edge((0, 1), (0, 2), 5)
compare("(0,0) to (0,3)", (0, 0), (0, 3))
print("BFS takes the fewest STEPS (3) but drives the slow road: cost 7.")
print("Dijkstra takes more steps (5) but gets there sooner: cost 5.")
clear_slow_edges()
