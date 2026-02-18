# Lesson 3: Lists

## Overview
Students learn how to store multiple values in a single variable using Python lists. Building on the previous lesson's tuples (which store a single coordinate), this lesson introduces lists as ordered, mutable collections that can grow and shrink. The key insight is that a path through the grid is naturally represented as a list of coordinate tuples — for example, `[(0,0), (1,0), (2,0), (2,1), (2,2), (2,3)]`. By the end of the lesson, students will be able to create lists, add items with `append()`, iterate through lists with `for` loops, and combine lists and tuples to represent paths.

This lesson bridges the gap between storing a single position (a tuple) and storing a sequence of positions (a list of tuples). Students will build lists both by writing them out directly and by constructing them step by step inside loops — a pattern that is essential for the Manhattan algorithm in Lesson 4, where the path is computed one step at a time.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain what a list is and how it differs from a tuple
- Create lists using square bracket notation `[]`
- Add items to a list using `append()`
- Determine the length of a list using `len()`
- Iterate through a list using a `for` loop
- Build a list step by step inside a loop
- Represent a path as a list of coordinate tuples
- Access individual elements and tuple components within a list of tuples

## Key Concepts
- **List**: An ordered, mutable collection of values enclosed in square brackets `[]`
- **Mutable**: Can be changed after creation — items can be added, removed, or modified
- **append()**: A method that adds a new item to the end of a list
- **len()**: A function that returns the number of items in a list
- **Iteration**: Visiting each item in a list one at a time using a `for` loop
- **List of tuples**: A list where each element is a tuple — used to represent a path as a sequence of coordinates

## Materials Required
- Computers with Python/Thonny installed
- Projector or shared screen for live coding
- Students' completed grid worksheets from Lesson 1
- Slide deck: `slides/03-lists-outline.md`

## Lesson Flow

### Introduction (8 minutes)

1. **Hook: One Position Is Not Enough**
   - Recap: "Last lesson we learned to store a single position using a tuple: `position = (2, 3)`"
   - Ask: "A path from (0, 0) to (2, 3) visits six positions: (0,0), (1,0), (2,0), (2,1), (2,2), (2,3). How would we store all of those in Python?"
   - Let students brainstorm — some may suggest six separate variables: `pos1 = (0,0)`, `pos2 = (1,0)`, etc.
   - Problem: "What if the path has 20 steps? 100 steps? We need a way to store a whole collection in one variable."
   - Reveal: "That's what a list does."

2. **What Is a List?**
   - A list is an ordered, mutable collection of values
   - Uses square brackets: `numbers = [1, 2, 3, 4, 5]`
   - Can hold any type of value — integers, strings, tuples
   - Can grow and shrink — unlike tuples, lists are mutable
   - Show the comparison table:

     | Feature | Tuple | List |
     |---|---|---|
     | Brackets | `( )` | `[ ]` |
     | Can change? | No (immutable) | Yes (mutable) |
     | Best for | Fixed data (coordinates) | Collections (paths) |

### Guided Practice (20 minutes)

1. **Creating Lists and Accessing Items** (5 minutes)
   - Live code together:
     ```python
     colors = ["red", "green", "blue"]
     print(colors[0])      # "red"
     print(colors[1])      # "green"
     print(len(colors))    # 3
     ```
   - Emphasize: Indexing starts at 0, just like row and column numbering
   - Try accessing `colors[3]` to show the `IndexError` — reinforce that a list of 3 items has indices 0, 1, 2

2. **Adding Items with append()** (5 minutes)
   - Live code together:
     ```python
     colors = ["red", "green"]
     colors.append("blue")
     print(colors)         # ["red", "green", "blue"]
     colors.append("yellow")
     print(colors)         # ["red", "green", "blue", "yellow"]
     print(len(colors))    # 4
     ```
   - Key point: `append()` always adds to the END of the list
   - Show starting from an empty list:
     ```python
     path = []
     path.append("first")
     path.append("second")
     print(path)           # ["first", "second"]
     ```

3. **Iterating with for Loops** (5 minutes)
   - Live code together:
     ```python
     colors = ["red", "green", "blue"]

     for color in colors:
         print(color)
     ```
   - Output: each color on its own line
   - With index numbers:
     ```python
     for i in range(len(colors)):
         print("Item", i, "is", colors[i])
     ```

4. **Building a List Step by Step** (5 minutes)
   - This pattern is critical for the Manhattan algorithm:
     ```python
     squares = []

     for i in range(5):
         squares.append(i * i)

     print(squares)    # [0, 1, 4, 9, 16]
     ```
   - Trace through the loop iteration by iteration:

     | Iteration | i | i * i | List after append |
     |---|---|---|---|
     | 1 | 0 | 0 | [0] |
     | 2 | 1 | 1 | [0, 1] |
     | 3 | 2 | 4 | [0, 1, 4] |
     | 4 | 3 | 9 | [0, 1, 4, 9] |
     | 5 | 4 | 16 | [0, 1, 4, 9, 16] |

   - Emphasize: "Start with an empty list, append inside a loop. This is exactly how we will build paths in the Manhattan algorithm."

### Independent Practice (17 minutes)

**Exercise 1: Create and Iterate a Path**
- Goal: Build a path as a list of tuples and iterate through it
- Steps:
  1. Create an empty list called `path`
  2. Use `append()` to add these coordinates in order: `(0, 0)`, `(0, 1)`, `(0, 2)`, `(1, 2)`, `(2, 2)`
  3. Print the full path
  4. Print how many steps the path has using `len()`
  5. Use a `for` loop to print each step with its row and column:
     ```python
     for step in path:
         print("Visit:", step)
         print("  Row:", step[0], "Col:", step[1])
     ```
- Success criteria: Output shows all 5 coordinates with correct row and column values

**Exercise 2: Build a Path with a Loop**
- Goal: Use a loop and `append()` to build a straight-line path
- Steps:
  1. Create an empty list called `path`
  2. Write a `for` loop that builds a path from `(0, 0)` down to `(4, 0)`:
     ```python
     path = []
     for row in range(5):
         path.append((row, 0))
     print(path)
     ```
  3. Verify the output: `[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]`
  4. Modify the loop to build a path from `(0, 0)` right to `(0, 4)` instead
- Success criteria: Both paths print correctly with the expected coordinates

**Exercise 3: Combine Two Segments** (Challenge)
- Goal: Build a path that goes down first, then right — just like the Manhattan algorithm will
- Steps:
  1. Start at `(0, 0)`, destination is `(2, 3)`
  2. First, append coordinates going down from row 0 to row 2 (column stays 0)
  3. Then, append coordinates going right from column 1 to column 3 (row stays 2)
  4. Print the complete path
  5. Verify: `[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]`
- Key insight: This is exactly what the Manhattan algorithm will do automatically in Lesson 4

### Assessment

**Formative (during lesson)**:
- Can students create a list and add items with `append()`?
- Can students iterate through a list with a `for` loop?
- Can students access tuple elements inside a list (e.g., `path[0][1]`)?
- Do students understand the "start empty, append in a loop" pattern?

**Summative (exit ticket)**:
1. What is the difference between a tuple and a list?
2. Write code to create an empty list and append the numbers 1, 2, and 3 to it.
3. Given `path = [(0, 0), (1, 0), (2, 0)]`, what does `path[2]` return?
4. Given `path = [(0, 0), (1, 0), (2, 0)]`, what does `path[2][1]` return?
5. Write a `for` loop that prints every item in a list called `path`.

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "Lists and tuples are the same thing" | Lists use `[]` and are mutable (can change). Tuples use `()` and are immutable (cannot change). Use tuples for fixed data like coordinates, lists for collections like paths. |
| "append() goes inside the parentheses of the list" | `append()` is called on the list using dot notation: `path.append((1, 0))`, not `path = [(1, 0).append()]`. |
| "append() inside a loop only adds the last item" | This happens when `append()` is accidentally placed outside the loop body (wrong indentation). It must be indented inside the loop to run each iteration. |
| "Square brackets and parentheses are interchangeable" | `[(0,0), (1,0)]` is a list of tuples (correct for paths). `((0,0), (1,0))` is a tuple of tuples — not what we want for a mutable path. |
| "A list of 3 items has index 3" | Indexing starts at 0. A list of 3 items has indices 0, 1, and 2. Accessing index 3 causes an `IndexError`. |

## Differentiation

**For struggling students**:
- Start with lists of simple values (integers, strings) before introducing lists of tuples
- Provide partially completed code where students only need to fill in the `append()` calls
- Use a visual trace table on paper to step through the loop, showing the list after each iteration
- Pair with a stronger student for Exercise 3

**For advanced students**:
- Challenge: Write code to build a path from any start to any destination (not just from (0,0)) using two loops — this is essentially the Manhattan algorithm
- Ask: What does `path[-1]` return? What about `path[-2]`? (Negative indexing)
- Explore: Can a list contain a mix of types? What about a list of lists?
- Challenge: Calculate the total Manhattan distance of a path by iterating through it and summing the row and column changes between consecutive steps

## Materials & Code Examples

### List Basics
```python
# Creating lists
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
empty = []

# Accessing items
print(numbers[0])     # 1
print(names[2])       # "Charlie"
print(len(numbers))   # 5

# Adding items
numbers.append(6)
print(numbers)        # [1, 2, 3, 4, 5, 6]
```

### Iterating Through a List
```python
colors = ["red", "green", "blue"]

# Simple iteration
for color in colors:
    print(color)

# Iteration with index
for i in range(len(colors)):
    print("Item", i, "is", colors[i])
```

### Building a List in a Loop
```python
squares = []
for i in range(5):
    squares.append(i * i)
print(squares)        # [0, 1, 4, 9, 16]
```

### Path as a List of Tuples
```python
# A path from (0,0) to (2,3)
path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]

print("Path has", len(path), "positions")
print("Start:", path[0])
print("End:", path[-1])

# Iterate and print each step
for step in path:
    print("Visit:", step)
    print("  Row:", step[0], "Col:", step[1])
```

### Building a Path with append()
```python
path = []

# Add the starting position
path.append((0, 0))

# Move down 2 rows
path.append((1, 0))
path.append((2, 0))

# Move right 3 columns
path.append((2, 1))
path.append((2, 2))
path.append((2, 3))

print("Path:", path)
# Path: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]
```

### Common Mistake: append() Outside the Loop
```python
# WRONG — only adds the last position
path = []
for i in range(3):
    position = (i, 0)
path.append(position)       # Outside the loop!
print(path)                 # [(2, 0)] — only the last one

# CORRECT — adds each position
path = []
for i in range(3):
    position = (i, 0)
    path.append(position)   # Inside the loop!
print(path)                 # [(0, 0), (1, 0), (2, 0)]
```

## Teaching Notes
- **Tuples vs. lists confusion is expected**: Students will mix up `()` and `[]` for the first several lessons. Reinforce the rule: "Parentheses for positions, brackets for collections." A coordinate is a tuple, a path is a list.
- **The "build in a loop" pattern is critical**: Spend extra time on Exercise 2 and the trace table. The Manhattan algorithm in Lesson 4 relies entirely on starting with an empty list and appending coordinates inside a loop. If students do not master this pattern, the next lesson will be very difficult.
- **Show the indentation error live**: Deliberately place `append()` outside the loop and show that only the last item is added. Then fix it and show the correct behavior. This is one of the most common bugs students will encounter.
- **Keep referring back to the grid**: When students build a path like `[(0,0), (1,0), (2,0)]`, have them trace it on their grid worksheet from Lesson 1. The connection between the code and the physical grid should always be visible.
- **Do not over-teach list features**: Students do not need `insert()`, `remove()`, `pop()`, slicing, or list comprehensions at this point. Keep the focus on `[]`, `append()`, `len()`, indexing, and `for` loops — these are the only operations needed for the Manhattan project.

## Connections to Next Lessons
- **Lesson 4** will use the "start empty, append in a loop" pattern to build paths automatically using the Manhattan algorithm
- **Lesson 5** will wrap the path-building code in a class method (`compute_path`) that returns a list of tuples
- **Lesson 8** will iterate through a path list to drive the robot one step at a time using `drive_path()`
- The list-of-tuples data structure introduced here is the core data format used throughout the rest of Modules 4 and 5
