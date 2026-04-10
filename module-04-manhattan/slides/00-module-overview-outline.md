# Lesson 0 Slide Outline: Module 4 Overview — The Big Picture

## Slide 1: Title & Learning Objectives
**Title:** Module 4 Overview — The Big Picture

**Learning Objectives:**
- See the complete system we are building in this module
- Understand what the Manhattan and Navigator classes do
- Learn what "top-down design" means and why it helps
- Know which lesson builds which piece

**Agenda:**
- The mission (5 min)
- Peeling back the layers (10 min)
- Your roadmap (5 min)

---

## Slide 2: The Mission
**By the end of this module, your robot will do this:**

The robot starts at (0, 0) on the grid. You give it a list of destinations. It visits each one in order — computing the path, turning at intersections, following lines — all by itself.

**No remote control. No manual steering. The robot figures it out.**

Visual: Grid diagram with a path drawn through 3 destinations, arrows showing the route from (0,0) → (2,0) → (2,3) → (0,3).

**Question:** "That sounds complicated. How would you start building this?"

---

## Slide 3: Top-Down Design
**Strategy:** Start with the big picture. Break it into smaller pieces. Keep breaking until each piece is something you can build.

**The big problem:** Robot visits multiple destinations on a grid.

**Break it down:**
- How does it know the route? → Need a **path planner**
- How does it physically drive there? → Need a **robot driver**
- How does it handle multiple destinations? → Need a **loop**

**That gives us two classes and a main program.**

---

## Slide 4: The Main Program
**This is the ENTIRE main program:**

```python
manhattan = Manhattan((0, 0))
navigator = Navigator((0, 0), 0)
destinations = [(2, 0), (2, 3), (0, 3)]

for dest in destinations:
    path = manhattan.compute_path(dest)
    navigator.drive_path(path)
    manhattan.position = navigator.position
```

**Seven lines.** It is short because the classes do the work.

**In plain English:**
- Create a path planner and a robot driver
- For each destination: compute the path, drive it, update your position

---

## Slide 5: Two Classes, Two Jobs

**Manhattan class — "Where do I go?"**
- Input: current position + destination
- Output: a list of intersections to visit
- Example: (0,0) to (2,3) → `[(1,0), (2,0), (2,1), (2,2), (2,3)]`

**Navigator class — "How do I get there?"**
- Input: a list of intersections (the path)
- Output: the robot physically drives there

**Manhattan never touches the robot. Navigator never computes routes.**

Each class has one job. This is called **separation of concerns**.

---

## Slide 6: What Does Manhattan Compute?
**Given a start and destination, compute the path:**

Visual: Grid with path from (0,0) to (2,3) highlighted — go down 2 rows, then right 3 columns.

**The path is a list of intersections:**
```
[(1,0), (2,0), (2,1), (2,2), (2,3)]
```
The path lists only the intersections to drive to (the robot is already at the start).

**The rule:** Rows first, then columns — like walking city blocks in Manhattan, NYC.

**Lessons 4-5 will teach you how to build this.**

---

## Slide 7: What Does Navigator Do?
**At each intersection, the robot must:**

1. **Figure out which direction to face**
   - Headings are numbers: 0=North, 1=East, 2=South, 3=West
   - Compare coordinates to determine heading

2. **Turn to face that direction**
   - Keep turning right until facing the right way
   - Uses a simple while loop

3. **Drive forward to the next intersection**
   - Follow the line until detecting a cross
   - This is LineTrack from Module 2 — you already built it!

**Lessons 7-8 will teach you how to build this.**

---

## Slide 8: Building on What You Know
**You are not starting from scratch.**

**Module 2 gave you:**
- LineSensor — reads the line sensors
- LineTrack — follows lines and turns at intersections
  - `track_until_cross()` — drive to the next intersection
  - `turn_right()` — turn right until finding the next line

**Module 4 adds:**
- Manhattan — plan the path (which intersections to visit)
- Navigator — execute the path (calls LineTrack to move)

**Each module builds on the last. That is the power of reusable code.**

---

## Slide 9: Your Roadmap

| Lesson | What You Build |
|---|---|
| 1 | Coordinates on the grid — the (row, col) system |
| 2 | Tuples — store positions like (2, 3) |
| 3 | Lists — store paths as lists of positions |
| 4-5 | Manhattan algorithm — compute the path |
| 6 | Testing without a robot — verify before driving |
| 7 | Turning logic — headings as numbers, counting right turns |
| 8 | Navigator class — turn_to() and drive_path() |
| 9 | Final project — put it all together! |

**Every lesson builds one piece. Nothing is random.**

---

## Slide 10: The Payoff

**Show the main program one more time:**

```python
manhattan = Manhattan((0, 0))
navigator = Navigator((0, 0), 0)
destinations = [(2, 0), (2, 3), (0, 3)]

for dest in destinations:
    path = manhattan.compute_path(dest)
    navigator.drive_path(path)
    manhattan.position = navigator.position
```

**By Lesson 9, you will understand every line of this code — because you will have written every piece yourself.**

Let's get started.
