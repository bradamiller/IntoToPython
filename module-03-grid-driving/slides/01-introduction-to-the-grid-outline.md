# Lesson 1 Slide Outline: Introduction to the Grid

## Slide 1: Title & Learning Objectives
**Title:** Introduction to the Grid

**Learning Objectives:**
- Describe the physical grid layout and how intersections are formed
- Explain how cross detection from Module 2 maps to grid intersections
- Use the LineTrack class to drive to the first intersection
- Reuse existing code on a new surface

**Agenda:**
- From circle to grid (10 min)
- Review: LineTrack methods (5 min)
- Guided: Drive to first intersection (15 min)
- Practice (15 min)

---

## Slide 2: Hook — From Circle to Grid
**Remember Module 2?**
- You built a `LineTrack` class that follows lines and detects crosses

**Now look at this grid:**
- Lines running horizontally and vertically
- Where they cross = intersection
- Each intersection looks just like the cross on the circle!

**Question:** "Can your Module 2 code work on this grid without changes?"

**Answer:** Yes! That's the power of code reuse.

---

## Slide 3: The Grid Layout
**A grid is a network of taped lines:**

| | Col 0 | Col 1 | Col 2 | Col 3 |
|---|---|---|---|---|
| Row 0 | + | + | + | + |
| Row 1 | + | + | + | + |
| Row 2 | + | + | + | + |
| Row 3 | + | + | + | + |

**Each "+" is an intersection:**
- Lines connecting them horizontally and vertically
- The robot follows lines between intersections
- Cross detection tells the robot it has arrived

---

## Slide 4: Why the Grid Matters
**The grid is a stepping stone:**
- Module 2: Follow a circle, detect one cross
- Module 3 (now): Navigate a GRID of crosses
- Module 4: Use COORDINATES on the grid for pathfinding

**Grid navigation = line following + cross detection + turns**
- You already have all three from Module 2!

---

## Slide 5: Review — LineTrack Methods
**Your LineTrack class from Module 2 has three key methods:**

```python
tracker = LineTrack()

# Follow the line until an intersection
tracker.track_until_cross()

# Turn right onto perpendicular line
tracker.turn_right()

# Turn left onto perpendicular line
tracker.turn_left()
```

**These three methods are ALL you need for grid navigation!**

---

## Slide 6: Driving to the First Intersection
**Setup:** Place robot on a grid line, behind an intersection

**Program:**
```python
board = Board.get_default_board()
tracker = LineTrack()

board.wait_for_button()
print("Driving to first intersection...")
tracker.track_until_cross()
print("Intersection reached!")
```

**What happens:**
1. Robot follows the line using proportional control
2. When both sensors detect the cross → stops
3. Robot is now AT the intersection

---

## Slide 7: Drive and Turn
**After reaching an intersection, you can turn:**

```python
board.wait_for_button()

tracker.track_until_cross()
print("At intersection!")

tracker.turn_right()
print("Turned right - now on perpendicular line!")

tracker.track_until_cross()
print("At next intersection!")
```

**The robot:**
1. Follows the line to the first intersection
2. Turns right onto the crossing line
3. Follows THAT line to the next intersection

---

## Slide 8: Code Reuse in Action
**Module 2 code → Module 3 application:**

| Module 2 | Module 3 |
|---|---|
| Follow circle | Follow grid lines |
| Detect cross on circle | Detect grid intersection |
| Turn at cross | Turn at intersection |
| `track_until_cross()` | Same method, same code! |
| `turn_right()` | Same method, same code! |

**Key insight:** Good code works in new situations without modification.

---

## Slide 9: Your Turn!
**Activity:**
1. Copy your LineSensor and LineTrack classes from Module 2
2. Write a program that drives to the first intersection and stops
3. Verify the robot stops at the right place
4. Add a turn_right() after reaching the intersection
5. Add another track_until_cross() to drive to the next intersection

**Checkpoints:**
- Does the robot stop at the first intersection?
- Does the turn line up with the perpendicular line?
- Does the robot reach the second intersection after turning?

---

## Slide 10: Connection to Next Lesson
**What you did today:**
- Saw how the grid relates to Module 2's cross detection
- Drove to the first intersection using LineTrack
- Added a turn at the intersection

**Next lesson (Lesson 2):**
- Drive PAST an intersection to reach the next one
- Learn the "clear the intersection" technique
- Use for loops to drive multiple intersections

**Challenge:** What if you need to go 3 intersections forward? That's next!
