# Lesson 9 Slide Outline: Module 4 Final Project

## Slide 1: Title & Learning Objectives
**Title:** Module 4 Final Project — Manhattan Navigator

**Learning Objectives:**
- Integrate the Manhattan and Navigator classes into one program
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
- Manhattan class to compute paths
- Navigator class to drive paths

**Today:** Put it ALL together. Your robot will navigate to multiple destinations on the grid — automatically!

---

## Slide 3: The Main Program Structure
**Three components working together:**

```python
# 1. Manhattan class — computes the path
manhattan = Manhattan((0, 0))

# 2. Navigator class — drives the path
navigator = Navigator((0, 0), "N")

# 3. Main program — orchestrates everything
destinations = [(2, 3), (0, 1), (3, 3), (1, 0)]

for dest in destinations:
    path = manhattan.compute_path(dest)
    navigator.drive_path(path)
    manhattan.position = navigator.position
```

**The main program is simple because the classes do the work!**

---

## Slide 4: Complete Main Program
```python
from XRPLib.board import Board

# Import your classes (or define them above)

board = Board.get_default_board()

# Setup
start = (0, 0)
manhattan = Manhattan(start)
navigator = Navigator(start, "N")

# Destinations to visit
destinations = [(2, 3), (0, 1), (3, 3), (1, 0)]

board.wait_for_button()
print("Starting navigation!")

for i in range(len(destinations)):
    dest = destinations[i]
    print("Leg", i + 1, "- Going to", dest)

    # Compute the path
    path = manhattan.compute_path(dest)
    print("  Path:", path)

    # Drive the path
    navigator.drive_path(path)

    # Update Manhattan's position
    manhattan.position = navigator.position
    print("  Arrived at", dest)

print("All destinations reached!")
```

---

## Slide 5: Project Requirements
**Your final project must:**

1. Use the Manhattan class to compute paths
2. Use the Navigator class to drive paths
3. Visit at least 4 destinations
4. Start from (0, 0)
5. Print the path for each leg
6. Successfully navigate the physical grid

**Grading rubric:**

| Category | Points |
|---|---|
| Manhattan class works correctly | 15 |
| Navigator class turns and drives correctly | 15 |
| Main program visits 4+ destinations | 10 |
| Code is organized and readable | 5 |
| Robot completes the course | 5 |
| Total | 50 |

---

## Slide 6: Testing Strategy
**Step 1: Test Manhattan class alone (no robot)**
```python
manhattan = Manhattan((0, 0))
for dest in [(2,3), (0,1), (3,3), (1,0)]:
    path = manhattan.compute_path(dest)
    print(dest, "->", path)
    manhattan.position = dest
```

**Step 2: Test Navigator with one short path**
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
- Check: Is turn_to() updating self.heading?
- Fix: Print heading before and after each turn

**Issue 2: Robot overshoots intersections**
- Check: Is straight() distance correct for your grid?
- Fix: Measure actual distance between intersections, adjust parameter

**Issue 3: Manhattan position not updating between legs**
- Check: `manhattan.position = navigator.position` after each leg
- Without this, all paths start from (0, 0)!

**Issue 4: Path correct on screen, wrong on robot**
- This is usually a turning or distance issue, not an algorithm issue
- Test Manhattan class output first, then debug Navigator separately

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
1. Combine your Manhattan and Navigator classes into one file
2. Write the main program with at least 4 destinations
3. Test Manhattan output on screen first (Step 1 from Slide 6)
4. Test with robot one leg at a time (Step 2)
5. Run the full sequence (Step 3)

**Destination suggestions for a 4x4 grid:**
- `[(2, 3), (0, 1), (3, 3), (1, 0)]`
- `[(3, 0), (3, 3), (0, 3), (0, 0)]` — rectangle tour
- `[(1, 1), (2, 2), (1, 3), (3, 1)]` — zigzag

**Checkpoints:**
- Does Manhattan produce correct paths for all legs?
- Does the robot complete at least one leg correctly?
- Does the robot complete all 4 legs?

---

## Slide 10: Reflection and Looking Ahead
**What you accomplished in Module 4:**
- Coordinate systems and (row, col) convention
- Tuples for positions, lists for paths
- Manhattan algorithm for pathfinding
- Testing without hardware
- Navigator class for physical driving
- Separation of concerns: algorithm vs. action

**Looking ahead to Module 5:**
- What if an intersection is BLOCKED?
- Manhattan can't handle obstacles — it always goes the same way
- Module 5 introduces **Dijkstra's algorithm** — finds the BEST path around obstacles
- Your Navigator class stays the same — only the pathfinding changes!

**Big picture:** You built a modular system. Swapping one component (Manhattan → Dijkstra) is easy because of separation of concerns.
