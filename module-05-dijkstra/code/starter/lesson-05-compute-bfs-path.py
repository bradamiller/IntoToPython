# Lesson 5: Implementing compute_bfs_path()
# The ripples-out-from-the-start algorithm from Lesson 3, written as a
# function you can call from any program. No robot needed to run this file.
#
# Team: ________________________
# Date: ________________________
#
# How BFS finds the shortest path:
#   1. Start at the robot's position. It is the only place reached so far.
#   2. Look at every unreached neighbor of the places you reached last;
#      remember which place you came from to reach each one.
#   3. Repeat, one ring further out each time, until you reach the destination.
#   4. Walk the "previous" dictionary backwards from the destination.


# ===== The grid and the blocked list (Lesson 4) =====

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


# ===== The planner =====

def compute_bfs_path(position, destination):
    """
    Shortest path from position to destination, avoiding BLOCKED.

    Returns a list of (row, col) intersections to drive TO, in order.
    The robot's own position is not in the list; an empty list means
    "already there" (or "no way to get there").
    """
    # Step 1: build the graph fresh from BLOCKED, so a wall the robot just
    # found is already missing from it
    graph = build_graph(ROWS, COLS, BLOCKED)
    if position not in graph or destination not in graph:
        return []

    # Step 2: the start is reached (from nowhere) and is the only place to
    # look around so far
    previous = {position: None}
    to_visit = [position]

    # Step 3: spread out one ring at a time
    while len(to_visit) > 0:
        # TODO: take the OLDEST intersection off the FRONT of to_visit
        # current = to_visit.pop(???)

        # TODO: if current is the destination, stop looking
        # if current == ???:
        #     break

        # TODO: for each neighbor we have never reached, record where we came
        #       from and add it to the list of places to look around
        # for neighbor in graph[current]:
        #     if neighbor not in ???:
        #         previous[neighbor] = ???
        #         to_visit.append(???)
        pass

    # Step 4: if we never reached the destination, there is no way through
    if destination not in previous:
        return []

    # Step 5: walk back from the destination to the start, then flip the list.
    # The start itself is NOT in the path -- the robot is already there.
    path = []
    current = destination
    # TODO:
    # while current != ???:
    #     path.append(current)
    #     current = previous[???]
    # path.reverse()
    return path


# ===== Paper tests (no robot) =====
# Uncomment one at a time. The expected step counts are given; the exact
# path may differ from a classmate's and still be right.

# print("=== Test 1: no obstacles, (0,0) to (3,3) ===")
# path = compute_bfs_path((0, 0), (3, 3))
# print("Path:", path)
# print("Steps:", len(path), "(expect 6)")
# print()

# print("=== Test 2: straight line, (0,0) to (0,3) ===")
# path = compute_bfs_path((0, 0), (0, 3))
# print("Path:", path)
# print("Steps:", len(path), "(expect 3)")
# print()

# print("=== Test 3: already there, (2,2) to (2,2) ===")
# path = compute_bfs_path((2, 2), (2, 2))
# print("Path:", path)
# print("Steps:", len(path), "(expect 0)")
# print()

# print("=== Test 4: wall across the grid, (0,0) to (3,0) ===")
# add_blocked((1, 0))
# add_blocked((1, 1))
# print("Blocked:", BLOCKED)
# path = compute_bfs_path((0, 0), (3, 0))
# print("Path:", path)
# print("Steps:", len(path), "(expect 7 -- around the wall)")
# print()

# print("=== Test 5: destination walled off ===")
# add_blocked((1, 2))
# add_blocked((1, 3))
# path = compute_bfs_path((0, 0), (3, 0))
# print("Path:", path)
# print("Steps:", len(path), "(expect 0 -- no way through)")
# clear_blocked()
