# Lesson 1 Worksheet: Coordinates on the Grid — ANSWER KEY

---

## Part 1: Label the Grid

```
         Col 0       Col 1       Col 2       Col 3
          |           |           |           |
Row 0 ---[(0,0)]-----[(0,1)]-----[(0,2)]-----[(0,3)]---
          |           |           |           |
Row 1 ---[(1,0)]-----[(1,1)]-----[(1,2)]-----[(1,3)]---
          |           |           |           |
Row 2 ---[(2,0)]-----[(2,1)]-----[(2,2)]-----[(2,3)]---
          |           |           |           |
Row 3 ---[(3,0)]-----[(3,1)]-----[(3,2)]-----[(3,3)]---
```

**How many total intersections are on a 4x4 grid?** **16** (4 rows x 4 columns = 16)

---

## Part 2: Reading Coordinates

| Description | Coordinate (row, col) |
|---|---|
| Top-left corner | **(0, 0)** |
| Bottom-right corner | **(3, 3)** |
| Second row, third column | **(1, 2)** |
| Top-right corner | **(0, 3)** |
| Third row, first column | **(2, 0)** |
| Bottom-left corner | **(3, 0)** |

---

## Part 3: Identifying Positions

| Coordinate | Description |
|---|---|
| (0, 0) | **Top-left corner** |
| (1, 2) | **Second row, third column** |
| (3, 3) | **Bottom-right corner** |
| (0, 3) | **Top-right corner** |
| (2, 1) | **Third row, second column** |

---

## Part 4: Row vs. Column

1. **In the coordinate (2, 3), which number is the row?** **2**

2. **In the coordinate (2, 3), which number is the column?** **3**

3. **Which comes first in our convention — row or column?** **Row**

4. **Does the row number tell you how far DOWN or how far RIGHT?** **DOWN**

5. **Does the column number tell you how far DOWN or how far RIGHT?** **RIGHT**

6. **Are (2, 3) and (3, 2) the same position?** **NO**

7. **If they are different, explain how:**

   **(2, 3) is at the third row down and fourth column across (right). (3, 2) is at the fourth row down and third column across (right). The row and column values are swapped, so they are two different positions on the grid. Order matters in coordinates.**

---

## Part 5: Neighbors on the Grid

**Position (1, 2) on a 4x4 grid:**

| Direction | Neighbor Coordinate |
|---|---|
| Above (one row up) | **(0, 2)** |
| Below (one row down) | **(2, 2)** |
| Left (one column left) | **(1, 1)** |
| Right (one column right) | **(1, 3)** |

**Position (0, 0) on a 4x4 grid:**

| Direction | Neighbor Coordinate |
|---|---|
| Above | **NONE** |
| Below | **(1, 0)** |
| Left | **NONE** |
| Right | **(0, 1)** |

**Position (3, 3) on a 4x4 grid:**

| Direction | Neighbor Coordinate |
|---|---|
| Above | **(2, 3)** |
| Below | **NONE** |
| Left | **(3, 2)** |
| Right | **NONE** |

---

## Part 6: Movement on the Grid

| Step | Direction | New Coordinate |
|---|---|---|
| Start | — | (0, 0) |
| 1 | Move one row down | **(1, 0)** |
| 2 | Move one row down | **(2, 0)** |
| 3 | Move one column right | **(2, 1)** |
| 4 | Move one column right | **(2, 2)** |
| 5 | Move one column right | **(2, 3)** |

**Where did you end up?** **(2, 3)**

**How many rows did you move?** **2**

**How many columns did you move?** **3**

**Total steps taken:** **5**

---

## Part 7: Counting Steps Between Coordinates

| Start | End | Row Steps | Column Steps | Total Steps |
|---|---|---|---|---|
| (0, 0) | (2, 3) | **2** | **3** | **5** |
| (0, 0) | (3, 0) | **3** | **0** | **3** |
| (1, 1) | (3, 3) | **2** | **2** | **4** |
| (2, 3) | (0, 0) | **2** | **3** | **5** |
| (0, 0) | (0, 0) | **0** | **0** | **0** |

**How do you calculate total steps from two coordinates?**

**Find the absolute difference between the two row values, then find the absolute difference between the two column values, and add them together. This is called the Manhattan distance: |row1 - row2| + |col1 - col2|.**

---

## Part 8: Real-World Connections

1. **Name another system that uses coordinates (like Battleship, chess, maps, etc.):**

   **Answers will vary. Acceptable examples: Battleship (letter + number), chess (file + rank), maps (latitude + longitude), spreadsheets (column letter + row number), seating charts (row + seat).**

2. **In that system, what are the two values that identify a position?**

   **Answers will vary by system chosen. For example:**
   - **Battleship: a. Letter (column)  b. Number (row)**
   - **Chess: a. File (column, a-h)  b. Rank (row, 1-8)**
   - **Maps: a. Latitude (north/south)  b. Longitude (east/west)**

3. **Why do we start counting at 0 instead of 1 in our grid?**

   **Because that is the convention used in programming and computer science. In Python (and most programming languages), lists and arrays are indexed starting at 0. Starting at 0 means the coordinate value directly tells you how many steps from the origin you are.**

---

## Reflection

**Why is a coordinate system useful for a robot navigating on a grid?**

**A coordinate system gives the robot a precise, numerical way to describe any position on the grid. Instead of vague directions like "go over there," the robot can work with exact (row, col) pairs. This makes it possible to calculate how far apart two positions are using Manhattan distance, plan a step-by-step path from one position to another, and write code that tells the robot exactly where to go. Without coordinates, the robot would have no way to keep track of where it is or figure out how to reach its destination.**
