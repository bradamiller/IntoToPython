# Lesson 6: Testing and Swapping - SOLUTION
# One test harness, two planners (three if you did the Dijkstra extension).
# No robot needed to run this file.
#
# Both planners have exactly the same shape:
#     path = compute_manhattan_path(position, destination)
#     path = compute_bfs_path(position, destination)
# so the SAME tests can run against either one. You hand the harness the
# planner you want to test, the way you would hand it a number or a list.
#
# The tests do not compare against one "expected" path. On an open grid there
# are many equally short paths and any of them is correct. Instead they check
# what MUST be true of a correct answer:
#   - the first step is next to where the robot is
#   - the last step is the destination
#   - every step is next to the one before it
#   - no step is a blocked intersection
#   - when nothing is blocked, the number of steps is the Manhattan distance


# ===== The grid and the blocked list =====

ROWS = 4
COLS = 4
BLOCKED = []


def add_blocked(intersection):
    if intersection not in BLOCKED:
        BLOCKED.append(intersection)


def clear_blocked():
    while len(BLOCKED) > 0:
        BLOCKED.pop()


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


# ===== Planner 1: Manhattan (from Module 4) =====
# Manhattan does not know about BLOCKED. It never looks at it. That is the
# whole reason Module 5 exists, and the tests below will show it.

def compute_manhattan_path(position, destination):
    path = []
    current_row, current_col = position
    dest_row, dest_col = destination

    while current_row < dest_row:
        current_row = current_row + 1
        path.append((current_row, current_col))
    while current_row > dest_row:
        current_row = current_row - 1
        path.append((current_row, current_col))
    while current_col < dest_col:
        current_col = current_col + 1
        path.append((current_row, current_col))
    while current_col > dest_col:
        current_col = current_col - 1
        path.append((current_row, current_col))

    return path


# ===== Planner 2: BFS (from Lesson 5) =====

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


# ===== The test harness =====

def manhattan_distance(a, b):
    """How many steps apart two intersections are on an open grid."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def is_neighbor(a, b):
    """True when a and b are exactly one step apart."""
    return manhattan_distance(a, b) == 1


def check_path(path, position, destination):
    """Check everything that must be true of a correct path.
    Returns a list of problems. An empty list means the path is good."""
    problems = []

    if len(path) == 0:
        if position != destination:
            problems.append("empty path, but the robot is not at the destination")
        return problems

    if not is_neighbor(position, path[0]):
        problems.append("first step " + str(path[0]) + " is not next to the start " + str(position))
    if path[-1] != destination:
        problems.append("last step " + str(path[-1]) + " is not the destination " + str(destination))
    for i in range(1, len(path)):
        if not is_neighbor(path[i - 1], path[i]):
            problems.append("step " + str(path[i]) + " is not next to " + str(path[i - 1]))
    for step in path:
        if step in BLOCKED:
            problems.append("drives through blocked intersection " + str(step))

    return problems


def run_test(test_name, planner, position, destination, expected_steps):
    """Run one planner on one case and report PASS or FAIL.
    expected_steps is None when more than one length could be right."""
    path = planner(position, destination)
    problems = check_path(path, position, destination)
    if expected_steps is not None and len(path) != expected_steps:
        problems.append("expected " + str(expected_steps) + " steps, got " + str(len(path)))

    if len(problems) == 0:
        print("  PASS  " + test_name + "  " + str(path))
        return True
    else:
        print("  FAIL  " + test_name + "  " + str(path))
        for p in problems:
            print("          - " + p)
        return False


def run_no_path_test(test_name, planner, position, destination):
    """For a destination that is walled off, the only right answer is an
    empty list. (check_path cannot tell "walled off" from "forgot to look",
    so this case gets its own test.)"""
    path = planner(position, destination)
    if len(path) == 0:
        print("  PASS  " + test_name + "  [] (no path, correctly)")
        return True
    else:
        print("  FAIL  " + test_name + "  " + str(path))
        print("          - there is no way through, so the path should be empty")
        return False


def run_all_tests(name, planner):
    """Run the whole test suite against one planner. The planner is handed in
    as an argument, so the same suite serves every planner we write."""
    print("========== " + name + " ==========")
    passed = 0
    total = 0

    # --- Open grid: the number of steps is the Manhattan distance ---
    clear_blocked()
    for (start, dest) in [((0, 0), (3, 3)), ((0, 0), (0, 3)), ((2, 1), (0, 3)), ((1, 1), (1, 1))]:
        total = total + 1
        if run_test("open " + str(start) + " to " + str(dest), planner,
                    start, dest, manhattan_distance(start, dest)):
            passed = passed + 1

    # --- A wall in the way: must route around it ---
    clear_blocked()
    add_blocked((1, 0))
    add_blocked((1, 1))
    total = total + 1
    if run_test("wall at (1,0),(1,1): (0,0) to (3,0)", planner, (0, 0), (3, 0), 7):
        passed = passed + 1

    # --- Walled off completely: the only right answer is "no path" ---
    clear_blocked()
    add_blocked((1, 0))
    add_blocked((1, 1))
    add_blocked((1, 2))
    add_blocked((1, 3))
    total = total + 1
    if run_no_path_test("walled off: (0,0) to (3,0)", planner, (0, 0), (3, 0)):
        passed = passed + 1

    clear_blocked()
    print(name + ":", passed, "of", total, "passed")
    print()
    return passed == total


# ===== The swap: same harness, different planner =====

run_all_tests("Manhattan", compute_manhattan_path)
run_all_tests("BFS", compute_bfs_path)

# Did the Dijkstra extension? Paste compute_dijkstra_path above and add:
# run_all_tests("Dijkstra", compute_dijkstra_path)


# ===== The swap in a main program =====
# A navigate function that is handed its planner works with any of them.

def navigate(planner, position, destination):
    path = planner(position, destination)
    print("  Path from", position, "to", destination, ":", path, " Steps:", len(path))
    return destination       # where the robot would be after driving it


print("========== Same main program, different planner ==========")
clear_blocked()
add_blocked((2, 0))
print("Blocked:", BLOCKED)

print("With Manhattan:")
position = navigate(compute_manhattan_path, (0, 0), (3, 3))
position = navigate(compute_manhattan_path, position, (0, 2))

print("With BFS -- only the planner's name changed:")
position = navigate(compute_bfs_path, (0, 0), (3, 3))
position = navigate(compute_bfs_path, position, (0, 2))
clear_blocked()
