# Lesson 1 Slide Outline: Coordinates on the Grid

## Slide 1: Title & Learning Objectives
**Title:** Coordinates on the Grid

**Learning Objectives:**
- Understand the (row, column) coordinate system
- Map physical grid positions to coordinate pairs
- Count intersections to determine robot position
- Read and write coordinates accurately

**Agenda:**
- What is a coordinate system? (10 min)
- The grid and (row, col) convention (10 min)
- Mapping exercise (25 min)

---

## Slide 2: Hook — How Does a Robot Know Where It Is?
**Question:** "You can look around a room and know where you are. How does a robot know its position?"

**Discussion:** GPS uses coordinates (latitude, longitude). Street addresses use a grid (5th Ave & 3rd Street).

**Today:** We'll create a coordinate system for our robot's grid — so it always knows where it is.

---

## Slide 3: What Is a Coordinate System?
**Definition:** A way to describe any position using numbers

**Examples Students Know:**
- Battleship: "B4" = column B, row 4
- Chess: "e5" = column e, row 5
- Maps: latitude and longitude
- Spreadsheets: cell A1, B3, etc.

**Key Idea:** Two numbers uniquely identify any position on a 2D surface.

---

## Slide 4: Our Grid Convention — (row, col)
**The XRP grid uses (row, column):**

| | Col 0 | Col 1 | Col 2 | Col 3 |
|---|---|---|---|---|
| Row 0 | (0,0) | (0,1) | (0,2) | (0,3) |
| Row 1 | (1,0) | (1,1) | (1,2) | (1,3) |
| Row 2 | (2,0) | (2,1) | (2,2) | (2,3) |
| Row 3 | (3,0) | (3,1) | (3,2) | (3,3) |

**Convention:**
- First number = row (how far down)
- Second number = column (how far right)
- Start at (0, 0) in the top-left corner

---

## Slide 5: Reading Coordinates
**Practice: What are the coordinates?**

- Top-left corner: (0, 0)
- One row down, two columns right: (1, 2)
- Bottom-right of a 4x4 grid: (3, 3)
- Third row, first column: (2, 0)

**Common Mistake:** Mixing up row and column order!
- (2, 3) means row 2, column 3
- (3, 2) means row 3, column 2
- These are DIFFERENT positions!

---

## Slide 6: The Physical Grid
**Your robot drives on a physical grid:**
- Black tape lines form a grid on the floor
- Each intersection is a coordinate
- The robot uses line-following (Module 2) to travel between intersections

**How to count:**
- Start at (0, 0) — the home position
- Moving forward increases the row
- Moving right increases the column

**Show:** Photo/diagram of taped grid with labeled intersections

---

## Slide 7: Why Coordinates Matter for Navigation
**Without coordinates:**
- "Go forward, turn right, go forward, turn left..."
- Hard to plan, hard to change destination

**With coordinates:**
- "Go from (0, 0) to (2, 3)"
- The robot can CALCULATE the path
- Change destination? Just change the numbers!

**This is the foundation for Modules 4 and 5:**
- Module 4: Manhattan pathfinding using coordinates
- Module 5: Dijkstra's algorithm using coordinates

---

## Slide 8: Coordinates in Python
**We'll represent positions as pairs of numbers:**
```python
row = 2
col = 3
print("Position: row", row, "col", col)
```

**Next lesson preview — Tuples:**
```python
position = (2, 3)
print("Position:", position)
print("Row:", position[0])
print("Col:", position[1])
```

**Key Idea:** Python has a data type called a "tuple" that's perfect for storing coordinates. That's Lesson 2!

---

## Slide 9: Your Turn!
**Activity: Map the Grid**
1. Look at the physical grid (or the diagram)
2. Label every intersection with its (row, col) coordinate
3. Answer these questions:
   - What is the coordinate of the bottom-right corner?
   - How many intersections are on a 4x4 grid?
   - If the robot is at (1, 2), what intersection is directly below it?
   - What is directly to the right of (0, 0)?

**Checkpoints:**
- Can you read any coordinate on the grid?
- Can you find the position given a coordinate?
- Do you know which number is row and which is column?

---

## Slide 10: Connection to Next Lesson
**What you did today:**
- Learned the (row, column) coordinate system
- Mapped physical grid positions to coordinates
- Practiced reading and writing coordinates

**Next lesson (Lesson 2):**
- Learn about **tuples** — Python's way to store coordinate pairs
- Write code that creates and uses coordinate tuples
- Build toward representing robot position in code

**Remember: Row first, column second — (row, col)!**
