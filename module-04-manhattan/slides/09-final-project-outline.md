# Lesson 9 Slide Outline: Module 4 Final Project

## Slide 1: Title & Learning Objectives
**Title:** Module 4 Final Project — Grid Navigation

**Learning Objectives:**
- Integrate `compute_manhattan_path()` and `drive_path()` into one program
- Navigate to a series of destinations on the grid
- Debug and refine the complete system
- Demonstrate separation of concerns in a working project

**Agenda:**
- Project overview (5 min)
- Main program design (10 min)
- Implementation and testing (25 min)
- Demo and reflection (5 min)

---

## Slide 2: Hook — The Complete Robot Navigator
**Where you started (Lesson 1):**
- Learned what (row, col) means

**What you've built (Lessons 2-8):**
- Tuples for coordinates
- Lists for paths
- `compute_manhattan_path()` to compute paths
- `drive_path()` to drive paths using the Module 2 toolkit

**Today:** Put it ALL together. Your robot will navigate to multiple destinations on the grid — automatically!

---

## Slide 3: The Main Program Structure
**Two functions, orchestrated by a loop:**

```python
# 1. compute_manhattan_path() — computes the path
# 2. drive_path() — drives the path

position = (0, 0)
heading = 0  # heading North

# 3. Main program — orchestrates everything
destinations = [(2, 3), (0, 1), (3, 3), (1, 0)]

for dest in destinations:
    path = compute_manhattan_path(position, dest)
    position, heading = drive_path(path, position, heading)
```

**The main program is simple because the functions do the work!**

**Why reassign `position, heading = drive_path(...)`?** `drive_path()` computes the new position and heading internally and returns them -- it doesn't change anything outside itself. Skip the reassignment and every leg starts from (0, 0) again.

---

## Slide 4: Complete Main Program
```python
from XRPLib.board import Board

HEADING_NAMES = ["N", "E", "S", "W"]

board = Board.get_default_board()

# Setup
position = (0, 0)
heading = 0  # heading North

# Destinations to visit
destinations = [(2, 3), (0, 1), (3, 3), (1, 0)]

board.wait_for_button()
print("Starting navigation!")

for dest in destinations:
    print("--- Navigating to", dest, "---")

    # Compute the path
    path = compute_manhattan_path(position, dest)
    print("  Path:", path)

    # Drive the path, capturing the updated position/heading
    position, heading = drive_path(path, position, heading)

    print("  Arrived at", position)
    print("  Heading:", HEADING_NAMES[heading])

print("All destinations reached!")
```

---

## Slide 5: Project Requirements
**Your final project must:**

1. Use `compute_manhattan_path()` to compute paths
2. Use `drive_path()` to drive paths
3. Visit at least 4 destinations
4. Start from (0, 0)
5. Print the path for each leg
6. Successfully navigate the physical grid

**Grading rubric:**

| Category | Points |
|---|---|
| `compute_manhattan_path()` works correctly | 10 |
| Driving functions turn and drive correctly | 15 |
| Main program visits 4+ destinations, reassigns position/heading | 10 |
| Robot completes the course | 10 |
| Planning & documentation | 5 |
| Total | 50 |

---

## Slide 6: Testing Strategy
**Step 1: Test `compute_manhattan_path()` alone (no robot)**
```python
position = (0, 0)
for dest in [(2,3), (0,1), (3,3), (1,0)]:
    path = compute_manhattan_path(position, dest)
    print(dest, "->", path)
    position = dest
```

**Step 2: Test `drive_path()` with one short path**
- Start with (0, 0) to (1, 0) — one step
- Then (0, 0) to (2, 0) — straight line
- Then (0, 0) to (1, 1) — requires one turn

**Step 3: Test full sequence**
- Run all 4 destinations
- Watch for accumulated heading errors

---

## Slide 7: Common Issues and Fixes
**Issue 1: Robot turns wrong direction**
- Check: Does physical starting heading match the code?
- Check: Is `turn_to()` returning `heading`?
- Fix: Print heading before and after each turn

**Issue 2: Robot drifts off the line**
- Check: Is the robot starting centered on a grid line?
- Fix: `track_until_cross()` follows the line, so starting position matters
- Fix: Make sure `clear_intersection()` clears the intersection fully

**Issue 3: Position not updating between legs**
- Check: `position, heading = drive_path(path, position, heading)` after each leg
- Without this, all paths start from (0, 0)!

**Issue 4: Path correct on screen, wrong on robot**
- This is usually a turning or line-following issue, not an algorithm issue
- Test `compute_manhattan_path()` output first, then debug `drive_path()` separately

---

## Slide 8: Extension Challenges
**If you finish early:**

**Challenge A: Return Home**
- After visiting all destinations, compute a path back to (0, 0)
- Add it as the final destination

**Challenge B: Round Trip**
- Visit destinations in order, then visit them in reverse order
- End up back at (0, 0)

**Challenge C: Custom Destinations**
- Let a partner choose 4 destinations
- Your robot navigates to them without any code changes (just update the list!)

**Challenge D: Distance Tracker**
- Count total intersections crossed
- Print a summary at the end: "Visited 4 destinations in 18 steps"

---

## Slide 9: Your Turn!
**Activity:**
1. Combine `compute_manhattan_path()` and the driving functions into one file
2. Write the main program with at least 4 destinations
3. Test path output on screen first (Step 1 from Slide 6)
4. Test with robot one leg at a time (Step 2)
5. Run the full sequence (Step 3)

**Destination suggestions for a 4x4 grid:**
- `[(2, 3), (0, 1), (3, 3), (1, 0)]`
- `[(3, 0), (3, 3), (0, 3), (0, 0)]` — rectangle tour
- `[(1, 1), (2, 2), (1, 3), (3, 1)]` — zigzag

**Checkpoints:**
- Does `compute_manhattan_path()` produce correct paths for all legs?
- Does the robot complete at least one leg correctly?
- Does the robot complete all 4 legs?

---

## Slide 10: Reflection and Looking Ahead
**What you accomplished in Module 4:**
- Coordinate systems and (row, col) convention
- Tuples for positions, lists for paths
- Manhattan algorithm for pathfinding
- Testing without hardware
- `drive_path()` for physical driving
- Separation of concerns: algorithm vs. action

**Looking ahead to Module 5:**
- What if an intersection is BLOCKED?
- `compute_manhattan_path()` can't handle obstacles — it always goes the same way
- Module 5 introduces **Dijkstra's algorithm** — finds the BEST path around obstacles
- Your `drive_path()` function stays the same — only the pathfinding changes!

**Big picture:** You built a modular system. Swapping one component (Manhattan → Dijkstra) is easy because of separation of concerns.

**Optional Extension:** Courses that also cover classes can see this same final project built on `Manhattan`/`Navigator` objects — see the lesson document.
