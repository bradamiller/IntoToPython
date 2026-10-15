# Lesson 8 Worksheet: Building Experience

**Name:** ________________________
**Date:** ________________________

---

## Part A: Run 1 vs Run 2 Comparison

The robot navigates from (0, 0) to (3, 3) on a 4x4 grid. There are obstacles at (1, 1) and (2, 2), but the robot does not know about them at the start. It discovers them using its rangefinder.

**Run 1: Starting with blocked = []**

The robot computes a path with no obstacles. Trace what happens:

Initial path (no obstacles): (0,0) -> __________ -> __________ -> __________ -> __________ -> __________ -> (3,3)

The robot starts moving along this path.

At intersection (0, 0), robot checks ahead toward (1, 1). Rangefinder reads 8 cm.

- Obstacle detected at: __________
- Updated blocked list: __________
- Robot recomputes path. New path: ____________________________________________________

Robot follows new path. At (0, 1), checks ahead toward (0, 2). Rangefinder reads 40 cm.

- Obstacle? __________

Robot continues. Eventually reaches (1, 2), checks ahead toward (2, 2). Rangefinder reads 6 cm.

- Obstacle detected at: __________
- Updated blocked list: __________
- Robot recomputes path. New path from (1, 2): ____________________________________________________

**Total obstacles discovered in Run 1:** __________

**Run 2: Starting with blocked = [(1, 1), (2, 2)]**

Now the robot remembers obstacles from Run 1.

Initial path (with known obstacles): ____________________________________________________

Does the robot discover any new obstacles? __________

**How many times did the robot recompute its path in Run 1?** __________

**How many times did the robot recompute its path in Run 2?** __________

---

## Part B: Performance Analysis

Count the total steps (edges traveled) for each run.

**Run 1 Performance:**

| Segment | Path | Steps |
|---|---|---|
| Start to first obstacle discovery | ______________________ | ______ |
| After recompute to second obstacle | ______________________ | ______ |
| After second recompute to destination | ______________________ | ______ |
| **Total steps** | | ______ |

**Run 2 Performance:**

| Segment | Path | Steps |
|---|---|---|
| Start to destination (no surprises) | ______________________ | ______ |
| **Total steps** | | ______ |

**How many fewer steps did Run 2 take?** __________

**Why is Run 2 more efficient?**

____________________________________________________________________

____________________________________________________________________

**Will Run 3 be even better than Run 2?** __________ Why?

____________________________________________________________________

---

## Part C: Code Reading

Trace through this obstacle-updating code:

```python
blocked = [(1, 1)]
new_obstacle = (2, 2)

# Check if we already know about this obstacle
if new_obstacle not in blocked:
    blocked.append(new_obstacle)
    print("New obstacle at", new_obstacle)
    print("Blocked list:", blocked)
else:
    print("Already known")
```

**Output:**

```
__________________________________________
__________________________________________
```

Now trace what happens if we run the same code again with the SAME `new_obstacle`:

```python
new_obstacle = (2, 2)  # Same obstacle

if new_obstacle not in blocked:
    blocked.append(new_obstacle)
    print("New obstacle at", new_obstacle)
else:
    print("Already known")
```

**Output:**

```
__________________________________________
```

**Why is the `not in` check important?**

____________________________________________________________________

Now trace this multi-run code:

```python
blocked = []

# Run 1: discover obstacles
discovered_run1 = [(1, 1), (2, 2)]
for obs in discovered_run1:
    if obs not in blocked:
        blocked.append(obs)

print("After Run 1:", blocked)

# Run 2: discover one new obstacle, rediscover one old one
discovered_run2 = [(2, 2), (0, 3)]
for obs in discovered_run2:
    if obs not in blocked:
        blocked.append(obs)

print("After Run 2:", blocked)
```

**Output:**

```
After Run 1: __________________________________________
After Run 2: __________________________________________
```

---

## Part D: Design Question

**How would you save the obstacle list between program runs so the robot remembers obstacles even after being turned off?**

**Option 1: Save to a file**

Write pseudocode for saving the blocked list to a file:

```
# Saving
____________________________________________________________________
____________________________________________________________________
____________________________________________________________________
```

Write pseudocode for loading the blocked list from a file:

```
# Loading
____________________________________________________________________
____________________________________________________________________
____________________________________________________________________
```

**Option 2: Hard-code known obstacles**

What are the advantages and disadvantages?

Advantages: ____________________________________________________________________

Disadvantages: ____________________________________________________________________

**Which option would you choose and why?**

____________________________________________________________________

____________________________________________________________________

**Bonus: What would happen if the obstacle moves (someone removes it)?**

____________________________________________________________________

____________________________________________________________________

**How could the robot handle obstacles that might move?**

____________________________________________________________________

____________________________________________________________________

---

## Answer Key

### Part A:
- Run 1 initial path (no obstacles): (0,0) -> (1,0) -> (1,1) -> (2,1) -> (2,2) -> (3,2) -> (3,3) or similar diagonal path through (1,1)
- At (0,0) facing (1,1) — but actually the robot would detect (1,0) or (0,1) depending on facing direction. Assuming it detects (1,1) when approaching:
  - blocked = [(1,1)]
  - Recompute: path goes around via (0,1), (0,2) etc.
- At (1,2) facing (2,2): blocked = [(1,1), (2,2)], recompute path from (1,2) going (1,3), (2,3), (3,3) or via (2,1), (3,1), (3,2), (3,3)
- Total obstacles discovered: 2
- Run 2 starts with blocked=[(1,1),(2,2)], computes optimal path immediately
- Run 1 recomputes: 2 times. Run 2 recomputes: 0 times.

### Part B:
- Run 2 takes fewer steps because it knows about obstacles from the start and plans the optimal route immediately. Run 1 wastes steps going toward obstacles, then backtracking.
- Run 3 would be the same as Run 2 (unless new obstacles appear) because the robot already knows all the obstacles.

### Part C:
- First trace: "New obstacle at (2, 2)" then "Blocked list: [(1, 1), (2, 2)]"
- Second trace: "Already known"
- The `not in` check prevents duplicate entries in the blocked list.
- Multi-run trace: After Run 1: [(1, 1), (2, 2)]. After Run 2: [(1, 1), (2, 2), (0, 3)]. (2,2) was already known so it was not added again.

### Part D:
- File approach: Save each blocked coordinate to a text file, read it back at program start.
- Hard-code: Advantages — simple, no file handling. Disadvantages — cannot update automatically, requires editing code.
- If obstacle moves, the robot would still think it is blocked and route around it unnecessarily. The robot could re-check known obstacles periodically, or only remember obstacles for a limited time.
