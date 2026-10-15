# Lesson 6 Slide Outline: Testing and Swapping

## Slide 1: Title & Learning Objectives
**Title:** Testing and Swapping

**Learning Objectives:**
- Write test cases that verify Dijkstra produces correct paths on an obstacle-free grid
- Write test cases that verify Dijkstra correctly reroutes around blocked nodes
- Explain the shape mismatch between `compute_manhattan_path` and `compute_dijkstra_path`
- Write a `compute_path(algorithm, ...)` dispatch function that normalizes the two functions behind one call
- Swap which algorithm a program uses by changing one argument, not rewriting calling code

**Agenda:**
- Testing with no obstacles (5 min)
- Testing with obstacles (10 min)
- The shape mismatch (5 min)
- Building the dispatch function (10 min)
- The one-argument swap (10 min)
- Practice exercise (10 min)

---

## Slide 2: Hook — Would You Trust Untested Code to Drive Your Car?
**Question:** "Imagine you wrote the software for a self-driving car. Would you put a passenger in it without testing it first?"

Of course not. You'd test it in simulation, on a closed course, with edge cases and unusual scenarios first.

**Our robot is the same.** We built `build_dijkstra_graph()` and `compute_dijkstra_path()`, but we haven't proven they work yet.

**Today:** Test them thoroughly, then make it possible to switch between Manhattan and Dijkstra with a single argument.

---

## Slide 3: The Shape Mismatch
```
compute_manhattan_path(position, destination)         -> path, position NOT included
compute_dijkstra_path(position, destination, graph)   -> path, position included
```

**These aren't quite interchangeable.** Dijkstra needs a `graph`. And if you compare `len()` of the two outputs directly, you'll be off by one -- that's not a bug, it's just two different design choices that happened to land differently.

**So how do we make the rest of our program not care about this difference?**

---

## Slide 4: Test 1 — No Obstacles, Step Count Should Match Manhattan
```python
graph = build_dijkstra_graph(4, 4, [])
path = compute_dijkstra_path((0, 0), (3, 3), graph)
print("Path:", path)
print("Path length:", len(path) - 1, "steps")   # -1: Dijkstra includes the start
print("Expected steps (Manhattan distance):", 6)
```

**Run it.** The path length should equal the Manhattan distance: |3-0| + |3-0| = 6.

**Note:** The exact path may differ from Manhattan's path (Dijkstra might take a different route of the same length), but the NUMBER of steps must be the same.

---

## Slide 5: Test 2 — Blocked Node, Dijkstra Should Reroute
```python
graph_blocked = build_dijkstra_graph(4, 4, [(1, 0)])
path_blocked = compute_dijkstra_path((0, 0), (3, 0), graph_blocked)
print("Path with (1,0) blocked:", path_blocked)
print("Path length:", len(path_blocked) - 1, "steps")
print("Manhattan distance (no obstacles):", 3)
```

**Run it.** The path should avoid (1, 0) entirely, and the path length should be longer than the Manhattan distance of 3.

---

## Slide 6: Building the Dispatch Function
**One function that hides both algorithms' quirks behind a single, consistent call:**

```python
def compute_path(algorithm, position, destination, blocked):
    """Compute a path using the named algorithm.

    algorithm:   "manhattan" or "dijkstra"
    position:    (row, col) tuple, current position
    destination: (row, col) tuple, target
    blocked:     list of blocked (row, col) tuples (ignored by manhattan)

    Returns a list of (row, col) tuples, NOT including position,
    no matter which algorithm computed it.
    """
    if algorithm == "manhattan":
        return compute_manhattan_path(position, destination)
    else:
        graph = build_dijkstra_graph(4, 4, blocked)
        path = compute_dijkstra_path(position, destination, graph)
        return path[1:]  # drop the start position to match Manhattan's shape
```

**What it does:** picks the right underlying function, and for Dijkstra, slices off the first element so both branches return the *same shape* of result. Now `drive_path()` only ever calls `compute_path(...)` -- it never needs to know the differences exist.

---

## Slide 7: The One-Argument Swap
```python
# ========================================
# BEFORE (Module 4 style -- Manhattan only)
# ========================================
path = compute_manhattan_path(position, dest)
position, heading = drive_path(path, position, heading)


# ========================================
# AFTER (Module 5 -- either algorithm via one argument)
# ========================================
path = compute_path("dijkstra", position, dest, blocked)   # <- only this line changed
position, heading = drive_path(path, position, heading)
```

**That's it.** Everything downstream -- `drive_path(path, position, heading)` -- is completely unaware which algorithm ran.

---

## Slide 8: Side-by-Side Comparison
**Running `compute_path()` on the same destinations with blocked nodes [(1,1), (2,2)]:**

| Destination | Manhattan Path | Dijkstra Path | Notes |
|---|---|---|---|
| (2, 3) | (0,0)→(1,0)→(2,0)→(2,1)→(2,2)→(2,3) | (0,0)→(0,1)→(0,2)→(0,3)→(1,3)→(2,3) | Manhattan hits blocked (1,1) or (2,2)! |
| (0, 3) | (0,0)→(0,1)→(0,2)→(0,3) | (0,0)→(0,1)→(0,2)→(0,3) | Same — no obstacles on this path |
| (3, 0) | (0,0)→(1,0)→(2,0)→(3,0) | (0,0)→(1,0)→(2,0)→(3,0) | Same — no obstacles on this path |

**Key takeaway:** When obstacles are not in the way, both produce paths of the same length. When obstacles block the Manhattan path, Dijkstra finds a working alternative.

---

## Slide 9: Handling Edge Cases
**What should we test beyond the happy path?**

| Test Case | Expected Behavior |
|---|---|
| Start equals destination | Returns `[]` — no steps needed |
| Adjacent destination | Returns `[dest]` — one element |
| All nodes blocked except path | Still finds the only available route |
| Destination is blocked | Should handle gracefully (path doesn't exist) |
| Start is blocked | Should handle gracefully (can't begin) |

**Good programmers test the unusual cases, not just the obvious ones.**

---

## Slide 10: Your Turn!
**Activity: Swap Dijkstra into Your Module 4 Program**

1. Add the `compute_path()` dispatch function and `build_dijkstra_graph()`/`compute_dijkstra_path()` to your Module 4 navigation program
2. Change every `compute_manhattan_path(position, dest)` call to `compute_path("dijkstra", position, dest, blocked)`
3. Test with **no blocked nodes** — verify the robot visits all destinations correctly
4. Test with **blocked nodes** — verify the robot takes alternate routes
5. Try these scenarios:
   - Block one intersection on the direct path
   - Block two adjacent intersections to force a longer detour
   - Block intersections that don't affect any paths (should make no difference)

**Checkpoints:**
- Did you only need to change one line of code to swap pathfinders?
- Does the robot still visit all destinations correctly?
- With blocked nodes, does the robot avoid those intersections?
- Do both pathfinders produce the same-length results when nothing is blocked?

---

## Slide 11: What's Next
**Today:** Tested Dijkstra with and without obstacles, built a `compute_path(algorithm, ...)` dispatch function, and swapped Dijkstra into the Module 4 program by changing one argument.

**Next lesson (Lesson 7):**
- Use the XRP robot's **ultrasonic rangefinder** to detect real obstacles
- Read distance measurements from the sensor
- Decide when to treat an intersection as blocked

**Key insight:** Right now, we hard-code the blocked list. Next lesson, the robot will discover blocked intersections on its own using its rangefinder sensor.

**Optional Extension:** Courses that also cover classes can see how a shared method signature gives "true polymorphism" -- no dispatch function needed -- see the separate "True Polymorphism with Classes" deck.
