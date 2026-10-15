# Module 6, Lesson 5 Optional Extension: Three Planners, One Harness - SOLUTION
# Classes-track reference: the Module 5 Lesson 6 class harness with a third
# planner, Dijkstra, added. Swap by changing one name. No robot needed.
#
# The harness is the same as the functions version except that it calls
# planner.compute_path(...) and planner.add_blocked(...) instead of
# compute_xxx_path(...) and add_blocked(...). Because every planner class has
# those two methods, the harness never needs to know which planner it holds.
#
# Dijkstra is a copy of the BFS class with the two changes marked NEW/CHANGED,
# plus add_slow_edge() and weight() (Module 6 Lessons 2-3).


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


class Manhattan:
    def __init__(self):
        pass

    def add_blocked(self, intersection):
        # Manhattan cannot route around obstacles; this exists so every
        # planner can be tested the same way. It deliberately does nothing.
        pass

    def clear_blocked(self):
        pass

    def compute_path(self, position, destination):
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


class BFS:
    def __init__(self, rows=4, cols=4):
        self.rows = rows
        self.cols = cols
        self.blocked = []

    def add_blocked(self, intersection):
        if intersection not in self.blocked:
            self.blocked.append(intersection)

    def clear_blocked(self):
        self.blocked = []

    def compute_path(self, position, destination):
        graph = build_graph(self.rows, self.cols, self.blocked)
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


class Dijkstra:
    """A copy of BFS with two changes (see lesson-06-dijkstra-addon.py)."""

    def __init__(self, rows=4, cols=4):
        self.rows = rows
        self.cols = cols
        self.blocked = []
        self.slow_edges = []                     # NEW

    def add_blocked(self, intersection):
        if intersection not in self.blocked:
            self.blocked.append(intersection)

    def clear_blocked(self):
        self.blocked = []

    def add_slow_edge(self, a, b, cost):         # NEW
        self.slow_edges.append((a, b, cost))

    def weight(self, a, b):                      # NEW
        for (x, y, cost) in self.slow_edges:
            if (a == x and b == y) or (a == y and b == x):
                return cost
        return 1

    def closest(self, intersections, distance):  # CHANGED (helper)
        best = intersections[0]
        for node in intersections:
            if distance[node] < distance[best]:
                best = node
        return best

    def compute_path(self, position, destination):
        graph = build_graph(self.rows, self.cols, self.blocked)
        if position not in graph or destination not in graph:
            return []
        previous = {position: None}
        distance = {position: 0}                 # NEW
        to_visit = [position]
        while len(to_visit) > 0:
            current = self.closest(to_visit, distance)   # CHANGED
            to_visit.remove(current)
            if current == destination:
                break
            for neighbor in graph[current]:
                new_distance = distance[current] + self.weight(current, neighbor)   # CHANGED
                if neighbor not in distance or new_distance < distance[neighbor]:   # CHANGED
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


# ===== The harness, now taking a planner OBJECT =====

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def is_neighbor(a, b):
    return manhattan_distance(a, b) == 1


def check_path(planner, path, position, destination):
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
        if step in blocked_for_test:
            problems.append("drives through blocked intersection " + str(step))
    return problems


blocked_for_test = []     # the harness's own record of what it has blocked


def block(planner, intersection):
    planner.add_blocked(intersection)
    blocked_for_test.append(intersection)


def unblock_all(planner):
    planner.clear_blocked()
    while len(blocked_for_test) > 0:
        blocked_for_test.pop()


def run_test(test_name, planner, position, destination, expected_steps):
    path = planner.compute_path(position, destination)
    problems = check_path(planner, path, position, destination)
    if expected_steps is not None and len(path) != expected_steps:
        problems.append("expected " + str(expected_steps) + " steps, got " + str(len(path)))
    if len(problems) == 0:
        print("  PASS  " + test_name + "  " + str(path))
        return True
    print("  FAIL  " + test_name + "  " + str(path))
    for p in problems:
        print("          - " + p)
    return False


def run_no_path_test(test_name, planner, position, destination):
    path = planner.compute_path(position, destination)
    if len(path) == 0:
        print("  PASS  " + test_name + "  [] (no path, correctly)")
        return True
    print("  FAIL  " + test_name + "  " + str(path))
    print("          - there is no way through, so the path should be empty")
    return False


def run_all_tests(name, planner):
    print("========== " + name + " ==========")
    passed = 0
    total = 0

    unblock_all(planner)
    for (start, dest) in [((0, 0), (3, 3)), ((0, 0), (0, 3)), ((2, 1), (0, 3)), ((1, 1), (1, 1))]:
        total = total + 1
        if run_test("open " + str(start) + " to " + str(dest), planner,
                    start, dest, manhattan_distance(start, dest)):
            passed = passed + 1

    unblock_all(planner)
    block(planner, (1, 0))
    block(planner, (1, 1))
    total = total + 1
    if run_test("wall at (1,0),(1,1): (0,0) to (3,0)", planner, (0, 0), (3, 0), 7):
        passed = passed + 1

    unblock_all(planner)
    for node in [(1, 0), (1, 1), (1, 2), (1, 3)]:
        block(planner, node)
    total = total + 1
    if run_no_path_test("walled off: (0,0) to (3,0)", planner, (0, 0), (3, 0)):
        passed = passed + 1

    unblock_all(planner)
    print(name + ":", passed, "of", total, "passed")
    print()
    return passed == total


# ===== The swap: three planners, one harness =====

run_all_tests("Manhattan", Manhattan())
run_all_tests("BFS", BFS())
run_all_tests("Dijkstra", Dijkstra())


# ===== Where BFS and Dijkstra part ways =====

def path_cost(planner, position, path):
    total = 0
    here = position
    for step in path:
        total = total + planner.weight(here, step)
        here = step
    return total


print("========== Slow edge (0,1)-(0,2), cost 5: (0,0) to (0,3) ==========")
bfs = BFS()
dij = Dijkstra()
dij.add_slow_edge((0, 1), (0, 2), 5)
bfs_path = bfs.compute_path((0, 0), (0, 3))
dij_path = dij.compute_path((0, 0), (0, 3))
print("BFS:      steps", len(bfs_path), " cost", path_cost(dij, (0, 0), bfs_path), " ", bfs_path)
print("Dijkstra: steps", len(dij_path), " cost", path_cost(dij, (0, 0), dij_path), " ", dij_path)
