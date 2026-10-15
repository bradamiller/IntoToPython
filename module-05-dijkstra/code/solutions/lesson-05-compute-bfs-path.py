# Lesson 5: Implementing compute_bfs_path() - SOLUTION
# Breadth-first search: the ripples-out-from-the-start algorithm from Lesson 3,
# written as code. No robot needed to run this file.
#
# How BFS finds the shortest path:
#   1. Start at the robot's position. It is the only place "visited" so far.
#   2. Look at every unvisited neighbor of the places you reached last;
#      remember which place you came from to reach each one.
#   3. Repeat, one ring further out each time, until you reach the destination.
#   4. Walk the "previous" dictionary backwards from the destination to get
#      the path.
# Because every ring is one step further than the last, the first time you
# reach the destination you have found a shortest path.


# ===== The grid and the blocked list (shared by every planner) =====

ROWS = 4
COLS = 4
BLOCKED = []     # intersections the robot must not drive through


def add_blocked(intersection):
    """Remember that an intersection is blocked. The robot calls this when the
    rangefinder sees an obstacle; tests call it to set up an obstacle course."""
    if intersection not in BLOCKED:
        BLOCKED.append(intersection)


def clear_blocked():
    """Forget every blocked intersection (used between tests)."""
    while len(BLOCKED) > 0:
        BLOCKED.pop()


def build_graph(rows, cols, blocked):
    """Build the graph dictionary for a rows x cols grid (Lesson 4).
    Every intersection maps to the list of its neighbors; blocked
    intersections are left out entirely, so nothing connects to them."""
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


# ===== The planner =====

def compute_bfs_path(position, destination):
    """
    Shortest path from position to destination, avoiding BLOCKED.

    Returns a list of (row, col) intersections to drive TO, in order.
    The robot's own position is not in the list; an empty list means
    "already there" (or "no way to get there").
    """
    # Build the graph fresh from the blocked list, so a wall the robot just
    # found is already missing from it.
    graph = build_graph(ROWS, COLS, BLOCKED)
    if position not in graph or destination not in graph:
        return []

    previous = {position: None}     # how we got to each place we have reached
    to_visit = [position]           # the places whose neighbors we still have to look at

    while len(to_visit) > 0:
        current = to_visit.pop(0)   # the oldest one first -- that is what makes it ripples
        if current == destination:
            break
        for neighbor in graph[current]:
            if neighbor not in previous:          # first time we have reached it
                previous[neighbor] = current
                to_visit.append(neighbor)

    if destination not in previous:
        return []                                 # walled off

    # Walk back from the destination to the start, then flip the list around.
    path = []
    current = destination
    while current != position:
        path.append(current)
        current = previous[current]
    path.reverse()
    return path


def bfs_rings(position):
    """Run the ripples all the way out (no stopping at a destination) and
    return a dictionary: intersection -> how many steps it is from position.
    Used only for the picture; compute_bfs_path() is the planner."""
    graph = build_graph(ROWS, COLS, BLOCKED)
    ring = {position: 0}
    to_visit = [position]
    while len(to_visit) > 0:
        current = to_visit.pop(0)
        for neighbor in graph[current]:
            if neighbor not in ring:
                ring[neighbor] = ring[current] + 1
                to_visit.append(neighbor)
    return ring


# ===== Paper tests (no robot) =====

print("=== Test 1: no obstacles, (0,0) to (3,3) ===")
path = compute_bfs_path((0, 0), (3, 3))
print("Path:", path)
print("Steps:", len(path), "(expect 6)")
print()

print("=== Test 2: straight line, (0,0) to (0,3) ===")
path = compute_bfs_path((0, 0), (0, 3))
print("Path:", path)
print("Steps:", len(path), "(expect 3)")
print()

print("=== Test 3: already there, (2,2) to (2,2) ===")
path = compute_bfs_path((2, 2), (2, 2))
print("Path:", path)
print("Steps:", len(path), "(expect 0)")
print()

print("=== Test 4: wall across the grid, (0,0) to (3,0) ===")
add_blocked((1, 0))
add_blocked((1, 1))
print("Blocked:", BLOCKED)
path = compute_bfs_path((0, 0), (3, 0))
print("Path:", path)
print("Steps:", len(path), "(expect 7 -- around the wall)")
print()

print("=== Test 5: destination walled off ===")
add_blocked((1, 2))
add_blocked((1, 3))
print("Blocked:", BLOCKED)
path = compute_bfs_path((0, 0), (3, 0))
print("Path:", path)
print("Steps:", len(path), "(expect 0 -- no way through)")
clear_blocked()


# ===== The picture =====
# Every intersection labeled with its distance from (0,0), around the wall.
# The path above is just one route down these numbers, 1, 2, 3 ... to the goal.
print()
print("=== Rings from (0,0) with (1,0) and (1,1) blocked ===")
add_blocked((1, 0))
add_blocked((1, 1))
print_grid(ROWS, COLS, BLOCKED, bfs_rings((0, 0)))
clear_blocked()
