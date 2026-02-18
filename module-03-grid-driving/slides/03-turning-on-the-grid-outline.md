# Lesson 3 Slide Outline: Turning on the Grid

## Slide 1: Title & Learning Objectives
**Title:** Turning on the Grid

**Learning Objectives:**
- Sequence drive and turn operations on the grid
- Use turn_right() and turn_left() at intersections
- Navigate L-shaped paths on the grid
- Plan a path on paper before writing code

**Agenda:**
- Turns at intersections (10 min)
- The L-shape path (10 min)
- Planning paths on paper (10 min)
- Practice (15 min)

---

## Slide 2: Hook — Making Corners
**So far:** You can drive any number of intersections in a straight line.

**New challenge:** What if the destination isn't straight ahead?

**Question:** "How does the robot turn a corner on the grid?"

**Answer:** At an intersection, use turn_right() or turn_left() to switch to the perpendicular line!

---

## Slide 3: Turning at an Intersection
**The robot must be AT an intersection to turn:**

```
Before turn:        After turn_right():
      |                   |
  ────+────           ────+────
      |                   |
   [ROBOT]             [ROBOT] →
```

**What turn_right() does:**
1. Drives forward briefly (clears the intersection)
2. Spins right
3. Stops when sensors find the perpendicular line

**Key:** After turning, the robot is already past the intersection — no extra clearing!

---

## Slide 4: The L-Shape Path
**Drive 2 intersections forward, turn right, drive 2 more:**

```python
drive_intersections(tracker, 2)
tracker.turn_right()
drive_intersections(tracker, 2)
```

**Visual:**
```
Start → + → + ┐
              ↓
              +
              ↓
              + ← End
```

**Three lines of code, one L-shaped path!**

---

## Slide 5: No Clearing After Turns
**Important detail:**

```python
# After drive_intersections, robot is AT the intersection
drive_intersections(tracker, 2)

# turn_right() handles clearing internally
tracker.turn_right()

# Go straight into next drive — no extra clearing!
drive_intersections(tracker, 2)
```

**Why?** The turn method drives forward as part of the turn. The robot is already past the intersection.

**Compare:**
- Between intersections in a straight line → must clear manually
- After a turn → already cleared

---

## Slide 6: Planning Paths on Paper
**Before coding, draw your path:**

**Step 1:** Mark the grid on paper

**Step 2:** Draw the robot's path

**Step 3:** Write the sequence:
- Drive N intersections
- Turn left/right
- Drive M intersections
- Turn left/right
- ...

**Example plan:**
```
1. Drive 3 intersections forward
2. Turn left
3. Drive 2 intersections forward
4. Turn right
5. Drive 1 intersection forward
```

---

## Slide 7: More Path Examples
**U-Turn:**
```python
drive_intersections(tracker, 3)
tracker.turn_right()
drive_intersections(tracker, 1)
tracker.turn_right()
drive_intersections(tracker, 3)
```

**Z-Shape:**
```python
drive_intersections(tracker, 2)
tracker.turn_right()
drive_intersections(tracker, 2)
tracker.turn_left()
drive_intersections(tracker, 2)
```

**Staircase:**
```python
for i in range(3):
    drive_intersections(tracker, 1)
    tracker.turn_right()
    drive_intersections(tracker, 1)
    tracker.turn_left()
```

---

## Slide 8: Common Mistakes
**Mistake 1: Forgetting to be at intersection before turning**
```python
# WRONG — robot is in the middle of a line
tracker.turn_right()

# CORRECT — drive to intersection first, then turn
tracker.track_until_cross()
tracker.turn_right()
```

**Mistake 2: Clearing after a turn**
```python
# WRONG — double clearing causes skipped intersection
tracker.turn_right()
tracker.drivetrain.set_effort(0.3, 0.3)  # Not needed!
time.sleep(0.3)
```

**Mistake 3: Wrong turn direction**
- Plan on paper first!
- Remember: turn_right() goes clockwise, turn_left() goes counterclockwise

---

## Slide 9: Your Turn!
**Activity:**
1. Plan an L-shape on paper: 2 forward, right, 2 forward
2. Code it and test on the robot
3. Plan a different path (your choice) and code it
4. Challenge: Plan a path that returns to the starting position

**Path ideas to try:**
- L-shape (2 forward, turn, 2 forward)
- U-shape (3 forward, right, 1 right, right, 3 forward)
- Staircase (repeat: 1 forward, turn, 1 forward, turn)

**Checkpoints:**
- Does the robot follow your planned path?
- Do the turns line up with the grid?
- Can you predict where the robot will end up?

---

## Slide 10: Connection to Final Project
**What you did today:**
- Combined driving and turning on the grid
- Navigated L-shaped and custom paths
- Planned paths on paper before coding

**Next lesson (Lesson 4 — Final Project):**
- Drive a complete **square** on the grid
- 4 sides, 4 right turns, back to start
- Use a for loop to repeat the pattern
- The robot drives a closed path!

**Preview:** The square is just: `for i in range(4): drive + turn`
