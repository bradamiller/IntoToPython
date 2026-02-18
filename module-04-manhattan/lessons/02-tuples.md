# Lesson 2: Tuples

## Overview
Students learn about tuples — Python's data type for storing an ordered, immutable pair of values. After building a strong mental model of coordinates in Lesson 1, students now represent those coordinates in code using tuples. They learn to create tuples, access individual elements with indexing, understand why immutability makes tuples ideal for coordinates, and compare tuples for equality. The lesson ends with a preview of Manhattan distance calculation, connecting the paper-based distance counting from Lesson 1 to actual Python arithmetic.

This is the first lesson in Module 4 where students write Python code. The exercises are designed to be run in a standard Python environment (VS Code or the Python interactive shell) — no robot hardware is needed.

## Learning Objectives
By the end of this lesson, students will be able to:
- Create tuples to represent (row, column) coordinate pairs
- Access individual tuple elements using `[0]` and `[1]` indexing
- Explain what immutability means and why it is appropriate for coordinates
- Compare two tuples for equality using `==`
- Calculate the Manhattan distance between two coordinate tuples using arithmetic
- Use `print()` to display tuples and their individual elements

## Key Concepts
- **Tuple**: An ordered, immutable collection of values, written with parentheses: `(2, 3)`
- **Indexing**: Accessing a specific element of a tuple using square brackets — `position[0]` gives the first element (row), `position[1]` gives the second (column)
- **Immutability**: Once created, a tuple's values cannot be changed — you must create a new tuple instead
- **Tuple comparison**: Two tuples are equal (`==`) if and only if all their elements match, in order
- **Manhattan distance**: The total number of grid steps between two positions, calculated as the sum of the absolute row difference and the absolute column difference

## Materials Required
- VS Code with Python configured (or Python interactive shell)
- Completed grid worksheet from Lesson 1
- Projector or screen for live coding demonstrations
- Student computers with Python installed

## Lesson Flow

### Introduction (10 minutes)

1. **Hook: The Two-Variable Problem**
   - Recall Lesson 1: "We used (row, column) to describe every position on the grid. Now we need to store those positions in Python."
   - Show the awkward approach:
     ```python
     row = 2
     col = 3
     ```
   - Ask: "This works for one position. But what if the robot needs to remember 10 positions? That's 20 separate variables — `row1`, `col1`, `row2`, `col2`... Is there a better way?"
   - Reveal: "Python has a data type called a **tuple** that packages two values into one."
     ```python
     position = (2, 3)
     ```
   - "One variable, one position. Clean and simple."

2. **What Is a Tuple?**
   - A tuple is an ordered collection of values written inside parentheses
   - The values are separated by commas
   - Pronunciation: "tuh-pull" or "too-pull" — both are accepted
   - Creating tuples:
     ```python
     start = (0, 0)
     destination = (3, 2)
     corner = (0, 3)
     ```
   - Each of these is a single value that holds two numbers — perfect for coordinates

3. **Accessing Elements with Indexing**
   - Use square brackets with an index number to get a specific element:
     ```python
     position = (2, 3)
     print(position[0])   # 2  (the row)
     print(position[1])   # 3  (the column)
     ```
   - Index 0 is the first element, index 1 is the second
   - This matches Python's zero-indexing — the same reason our grid starts at row 0, column 0
   - Common pattern:
     ```python
     row = position[0]
     col = position[1]
     ```

### Guided Practice (15 minutes)

1. **Creating and Printing Tuples**
   - Live code together — students type along:
     ```python
     home = (0, 0)
     school = (3, 2)
     store = (1, 4)

     print("Home:", home)
     print("School:", school)
     print("Store:", store)
     ```
   - Run and observe the output:
     ```
     Home: (0, 0)
     School: (3, 2)
     Store: (1, 4)
     ```
   - Notice: Python prints tuples with parentheses automatically

2. **Indexing Practice**
   - Add to the program:
     ```python
     print("School is at row", school[0], "column", school[1])
     print("Store is at row", store[0], "column", store[1])
     ```
   - Ask students: "What will `home[0]` print?" (0) "What about `home[1]`?" (0)
   - Emphasize: `[0]` is always the row, `[1]` is always the column

3. **Immutability Demonstration**
   - Try to change a tuple:
     ```python
     position = (2, 3)
     position[0] = 5       # What happens?
     ```
   - Run it: `TypeError: 'tuple' object does not support item assignment`
   - Explain: "Tuples are **immutable** — once created, they cannot be changed."
   - Ask: "Why is this actually a good thing for coordinates?"
   - Answer: "A coordinate represents a fixed point on the grid. (2, 3) is always row 2, column 3. It would be a bug if we could accidentally change it."
   - Analogy: "A street address doesn't change. '123 Main St' is always the same place. If you move, you get a NEW address — you don't modify the old one."
   - To represent a new position, create a new tuple:
     ```python
     old_position = (2, 3)
     new_position = (2, 4)   # One column to the right — a new tuple
     ```

4. **Comparing Tuples**
   - Show how `==` works with tuples:
     ```python
     current = (1, 2)
     target = (1, 2)
     print(current == target)    # True — same row, same column

     other = (2, 1)
     print(current == other)     # False — different positions!
     ```
   - Emphasize: "Two tuples are equal only if BOTH elements match. (1, 2) and (2, 1) are NOT equal — order matters, just like we learned in Lesson 1."
   - This will be important later: the Manhattan algorithm needs to check "have we reached the destination?"

5. **Manhattan Distance Preview**
   - Connect to Lesson 1's distance counting, now with Python:
     ```python
     start = (0, 0)
     destination = (2, 3)

     row_distance = destination[0] - start[0]    # 2 - 0 = 2
     col_distance = destination[1] - start[1]    # 3 - 0 = 3
     total_steps = row_distance + col_distance    # 2 + 3 = 5

     print("Rows to travel:", row_distance)
     print("Columns to travel:", col_distance)
     print("Total steps:", total_steps)
     ```
   - "This is the same calculation you did on paper in Lesson 1 — now Python does it for you."
   - Note: For now, assume the destination row and column are always greater than or equal to the start. Lesson 4 will handle all directions.

### Independent Practice (20 minutes)

**Exercise 1: Create and Print Coordinates**
- Goal: Create tuples for five positions from your grid worksheet and display them
- Steps:
  1. Create a new file: `coordinates.py`
  2. Choose five intersections from your Lesson 1 grid worksheet
  3. Store each as a tuple with a descriptive variable name
  4. Print each tuple and its individual row and column values
- Starter code:
  ```python
  # My grid positions
  home = (0, 0)
  park = (1, 3)
  # TODO: Add 3 more positions from your grid worksheet

  # Print each position
  print("Home:", home)
  print("  Row:", home[0], "Column:", home[1])

  print("Park:", park)
  print("  Row:", park[0], "Column:", park[1])

  # TODO: Print your other 3 positions the same way
  ```
- Success criteria:
  - Five tuples created with valid grid coordinates
  - Each tuple printed with its full value and individual row/column elements

**Exercise 2: Compare Positions**
- Goal: Use `==` to check whether two positions are the same
- Steps:
  1. Create pairs of tuples and compare them
  2. Predict the result before running
  3. Print the comparison result with a descriptive message
- Code:
  ```python
  pos_a = (2, 3)
  pos_b = (2, 3)
  pos_c = (3, 2)

  print("Is pos_a equal to pos_b?", pos_a == pos_b)
  print("Is pos_a equal to pos_c?", pos_a == pos_c)

  # TODO: Create two more tuples and compare them
  # TODO: Can you find a pair that is NOT equal but has the same numbers?
  ```
- Discussion point: Why does `(2, 3) == (3, 2)` return `False` even though both contain the numbers 2 and 3?

**Exercise 3: Calculate Manhattan Distance** (Challenge)
- Goal: Calculate the Manhattan distance between multiple pairs of positions
- Steps:
  1. Pick three pairs of positions from your grid
  2. For each pair, calculate row distance, column distance, and total steps
  3. Determine which pair of positions is closest
- Code:
  ```python
  # Pair 1
  start1 = (0, 0)
  end1 = (3, 2)
  dist1 = (end1[0] - start1[0]) + (end1[1] - start1[1])
  print("Distance from", start1, "to", end1, "is", dist1, "steps")

  # TODO: Calculate distance for two more pairs
  # TODO: Which pair is closest?
  ```
- Challenge: What happens if the destination has a smaller row or column than the start? (e.g., from (3, 2) to (1, 0)). You get a negative distance! How could you fix this? (Preview: `abs()` function or careful subtraction — covered in Lesson 4)

### Assessment

**Formative (during lesson)**:
- Can students create a tuple with correct syntax (parentheses, comma)?
- Can students access the row with `[0]` and the column with `[1]` without mixing them up?
- Do students understand why tuples cannot be modified?
- Can students use `==` to compare two tuples?

**Summative (worksheet/exit ticket)**:
1. Create a tuple that represents row 4, column 1. Write the Python code.
2. Given `position = (3, 5)`, what does `position[0]` return? What about `position[1]`?
3. What error do you get if you try `position[0] = 7`? Why?
4. Are `(1, 4)` and `(4, 1)` equal? Explain why or why not.
5. Calculate the Manhattan distance from (1, 1) to (4, 3). Show your work.

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "Index 1 gives the first element" | Python uses zero-indexing: index 0 is the first element (row), index 1 is the second (column) |
| "I can change a tuple after creating it" | Tuples are immutable. To represent a new position, create a new tuple. |
| "(2, 3) and (3, 2) are the same" | Order matters! (2, 3) is row 2, col 3. (3, 2) is row 3, col 2. These are different positions. |
| "Tuples use square brackets" | Tuples use parentheses `()` for creation. Square brackets `[]` are only used for indexing. |
| "A tuple is the same as two separate variables" | A tuple packages two values into one unit. This makes it easy to pass around, store in lists, and compare as a whole. |

## Differentiation

**For struggling students**:
- Provide a reference card: "position[0] = row, position[1] = column"
- Start with only creating and printing tuples — skip distance calculation
- Use the interactive Python shell (REPL) so students see results immediately after each line
- Pair with a student who completed the grid mapping confidently in Lesson 1

**For advanced students**:
- Calculate distances where the start has a larger row or column than the destination (introduces the need for `abs()`)
- Create a tuple with three values `(row, col, heading)` — what would `[2]` access?
- Write a program that asks for row and column input and creates a tuple: `position = (int(input("Row: ")), int(input("Col: ")))`
- Explore: Can a tuple hold other types? Try `("home", 0, 0)` — what does `[0]` return now?

## Materials & Code Examples

### Creating and Indexing Tuples
```python
# Create coordinate tuples
home = (0, 0)
school = (3, 2)
store = (1, 4)

# Access individual elements
print("School row:", school[0])      # 3
print("School column:", school[1])   # 2

# Print the full tuple
print("Store position:", store)      # (1, 4)
```

### Tuple Comparison
```python
# Comparing tuples with ==
pos_a = (2, 3)
pos_b = (2, 3)
pos_c = (3, 2)

print(pos_a == pos_b)   # True  — same position
print(pos_a == pos_c)   # False — different positions
```

### Manhattan Distance Calculation
```python
# Calculate distance between two positions
start = (0, 0)
destination = (2, 3)

row_distance = destination[0] - start[0]     # 2
col_distance = destination[1] - start[1]     # 3
total = row_distance + col_distance           # 5

print("From", start, "to", destination)
print("Row distance:", row_distance)
print("Col distance:", col_distance)
print("Total Manhattan distance:", total, "steps")
```

### Immutability Demonstration
```python
position = (2, 3)

# This will cause an error:
# position[0] = 5
# TypeError: 'tuple' object does not support item assignment

# Instead, create a new tuple:
new_position = (5, 3)
print("Old:", position)
print("New:", new_position)
```

## Teaching Notes
- **Pronounce it both ways**: Students may hear "tuh-pull" or "too-pull" from different sources. Acknowledge both are correct and move on — do not let pronunciation become a distraction.
- **Index confusion is expected**: Students will mix up `[0]` and `[1]` frequently in the first few exercises. A posted reference ("`[0]` = row, `[1]` = column") on the wall or whiteboard helps.
- **Immutability payoff comes later**: Students may wonder "why can't I just change it?" The real benefit shows up when tuples are stored in lists (Lesson 3) and used in the algorithm (Lesson 4). For now, the analogy of a street address is sufficient.
- **Interactive shell is powerful here**: For this lesson, consider having students type code into the Python REPL (interactive shell) rather than writing full scripts. Immediate feedback accelerates understanding.
- **Connect to Lesson 1**: Frequently refer back to the grid worksheet. "Find (2, 3) on your worksheet. Now you've stored that same position in Python."
- **Negative distances**: If a student tries calculating distance from a larger position to a smaller one (e.g., (3, 2) to (1, 0)), they will get negative values. Acknowledge it, note it is a real issue, and say "Lesson 4 handles this with `abs()`. For now, just make sure the destination is down and to the right of the start."

## Connections to Next Lessons
- **Lesson 3** will introduce lists, allowing students to store multiple tuples as a path: `[(0,0), (1,0), (2,0)]`
- **Lesson 4** will use tuple indexing and arithmetic to implement the Manhattan algorithm — computing an entire path from start to destination
- **Lesson 5** will use tuple comparison (`==`) to check whether the robot has reached its destination
- The `position[0]` / `position[1]` pattern will be used throughout the rest of Modules 4 and 5
