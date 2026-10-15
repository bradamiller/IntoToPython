# Lesson 5 Optional Extension: The BFS Class (and a Manhattan class to match)
# Classes-track reference: compute_bfs_path() and add_blocked() from
# lesson-05-compute-bfs-path.py, repackaged as a class. Robot behavior is
# identical either way. No robot needed to run this file.
#
# Same four changes as every extension so far:
#   - the functions move inside "class BFS:" and gain self
#   - the shared variables (ROWS, COLS, BLOCKED) move into __init__ as self.rows,
#     self.cols, self.blocked
#   - inside the methods, shared values and sibling calls gain "self."
#   - from outside, calls go through the object: planner.compute_path(...)
#
# Why BFS is a class: it has setup to hold (the grid size and the blocked
# list). Why Manhattan is a class: ONLY so it has the same shape as BFS, so
# the same test harness and the same main program work with either. That is
# the point of the swap in Lesson 6.
#
# Neither planner remembers where the robot is. The Navigator does that (Module
# 4). A planner is TOLD the position every time it is asked for a path.


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
    """The Module 4 planner, with the same shape as BFS."""

    def __init__(self):
        pass        # Manhattan has no setup -- it is a class only to match BFS

    def add_blocked(self, intersection):
        # Manhattan cannot route around obstacles. This method exists so every
        # planner can be tested the same way; it deliberately does nothing.
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
    """Shortest path by breadth-first search, avoiding blocked intersections."""

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


# ===== Paper tests (no robot) =====

planner = BFS()

print("=== (0,0) to (3,3), open grid ===")
print(planner.compute_path((0, 0), (3, 3)))

print("=== wall at (1,0),(1,1): (0,0) to (3,0) ===")
planner.add_blocked((1, 0))
planner.add_blocked((1, 1))
print("BFS:      ", planner.compute_path((0, 0), (3, 0)))

# Same calls, different object: Manhattan ignores the wall.
other = Manhattan()
other.add_blocked((1, 0))
other.add_blocked((1, 1))
print("Manhattan:", other.compute_path((0, 0), (3, 0)), " <- drives through the wall")
