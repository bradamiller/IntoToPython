# Lesson 5: Implementing the Manhattan Class

## Overview
Students translate the Manhattan algorithm they hand-traced in Lesson 4 into a working Python class. The `Manhattan` class has two key pieces: an `__init__` method that stores the robot's starting position, and a `compute_path` method that takes a destination and returns the complete list of grid positions from start to destination. Students build the class step by step -- first determining direction, then implementing the row while loop, then the column while loop, and finally assembling the complete path using `append()`. By the end of the lesson, students have a fully functional `Manhattan` class they can test with print statements.

## Learning Objectives
By the end of this lesson, students will be able to:
- Design a class with `__init__` that stores position as a tuple
- Write a method that accepts a parameter (destination) and returns a result (path)
- Use if/else to determine step direction (+1 or -1) based on comparing current and destination values
- Implement while loops that iterate until a condition is met (current != destination)
- Build a list incrementally using `append()`
- Extract individual values from a tuple using indexing (e.g., `position[0]`, `position[1]`)
- Test a class by creating an instance and calling its methods with print statements

## Key Concepts
- **Class Design**: Deciding what data goes in `__init__` (the starting position) and what behavior goes in methods (`compute_path`)
- **Tuple Indexing**: Accessing the row with `position[0]` and the column with `position[1]`
- **Conditional Direction**: Using if/else to choose between +1 and -1 based on whether the destination is greater or less than the current position
- **While Loop with Condition**: `while current_row != dest_row` -- the loop runs until the condition becomes false
- **Building a List with append()**: Starting with an empty (or initial) list and adding elements one at a time inside a loop
- **Return Value**: The `compute_path` method returns the completed path list to the caller

## Materials Required
- Computer with VS Code and Python installed
- Hand-traced paths from Lesson 4 worksheets (for verification)
- Whiteboard or projector for live coding
- No robot needed -- all testing is done with print statements

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Hook: From Paper to Code**
   - Hold up (or display) the hand-traced worksheets from Lesson 4
   - Ask: "You can all trace a Manhattan path by hand. But the robot cannot read your worksheet. How do we teach the robot to do what you did?"
   - Answer: We write the algorithm as a Python class that the robot can execute.

2. **Review the Algorithm**:
   - Write the plain-English algorithm on the board (from Lesson 4):
     ```
     1. Start at your current position. Add it to the path.
     2. Figure out row direction (+1 or -1).
     3. Figure out column direction (+1 or -1).
     4. While not in the correct row: move one row step, add to path.
     5. While not in the correct column: move one column step, add to path.
     6. Return the path.
     ```
   - Ask: "Which parts become `__init__`? Which parts become a method?"
   - `__init__` stores the starting position (step 1 setup)
   - `compute_path` does steps 2-6

3. **Preview the Class Structure**:
   - Show the skeleton on the board:
     ```python
     class Manhattan:
         def __init__(self, start):
             # Store the starting position
             pass

         def compute_path(self, destination):
             # Compute and return the path
             pass
     ```
   - Explain: The class is called `Manhattan` (CamelCase, like `LineSensor` from Module 2). It takes a starting position when created and has a method to compute a path to any destination.

### Guided Practice: Building the Manhattan Class (20 minutes)
**For 50-min classes:** 22 min
**For 3-hour sessions:** 30 min

1. **Step 1: The `__init__` Method**
   - Start with storing the position:
     ```python
     class Manhattan:
         def __init__(self, start):
             self.position = start
     ```
   - Explain each part:
     - `start` is a tuple like `(0, 0)` -- the robot's starting grid position
     - `self.position = start` saves it so other methods can use it
   - Test it immediately:
     ```python
     nav = Manhattan((0, 0))
     print(nav.position)       # Output: (0, 0)
     print(nav.position[0])    # Output: 0  (the row)
     print(nav.position[1])    # Output: 0  (the column)
     ```
   - Remind students: `(0, 0)` is a tuple. `[0]` gets the first element (row), `[1]` gets the second element (column).

2. **Step 2: Starting compute_path -- Setup Variables**
   - Begin the method by extracting the values we need:
     ```python
     def compute_path(self, destination):
         path = [self.position]
         current_row = self.position[0]
         current_col = self.position[1]
         dest_row = destination[0]
         dest_col = destination[1]
     ```
   - Walk through each line:
     - `path = [self.position]` -- Start the path list with our current position (remember, the path always includes where we start)
     - `current_row` and `current_col` -- Pull out the row and column from our position so we can modify them
     - `dest_row` and `dest_col` -- Pull out the destination row and column for comparison
   - Ask: "Why do we create separate variables instead of modifying `self.position` directly?" (Because we do not want to change our stored position -- we just want to calculate a path.)

3. **Step 3: Determine Direction**
   - Add the direction logic:
     ```python
         if dest_row > current_row:
             row_step = 1
         else:
             row_step = -1

         if dest_col > current_col:
             col_step = 1
         else:
             col_step = -1
     ```
   - Connect to Lesson 4: "This is exactly what you did on paper -- if the destination row is bigger, we move down (+1). If it is smaller, we move up (-1). Same logic for columns."
   - Ask: "What if dest_row equals current_row? What will row_step be?" (It will be -1 from the else branch, but it does not matter because the while loop will not execute -- we are already in the correct row.)

4. **Step 4: The Row While Loop**
   - Add the loop for row movement:
     ```python
         while current_row != dest_row:
             current_row = current_row + row_step
             path.append((current_row, current_col))
     ```
   - Explain each line:
     - `while current_row != dest_row:` -- Keep going as long as we have not reached the destination row
     - `current_row = current_row + row_step` -- Move one step in the row direction
     - `path.append((current_row, current_col))` -- Add our new position to the path
   - Trace through with (0,0) to (2,3):
     - current_row = 0, dest_row = 2, row_step = 1
     - Loop 1: current_row becomes 1, append (1, 0)
     - Loop 2: current_row becomes 2, append (2, 0)
     - Loop ends: current_row (2) equals dest_row (2)
   - Note the tuple syntax: `(current_row, current_col)` creates a new tuple. The parentheses inside `append()` are the tuple, not extra function parentheses.

5. **Step 5: The Column While Loop**
   - Add the loop for column movement:
     ```python
         while current_col != dest_col:
             current_col = current_col + col_step
             path.append((current_row, current_col))
     ```
   - This is nearly identical to the row loop but for columns.
   - Trace through the continuation of (0,0) to (2,3):
     - current_col = 0, dest_col = 3, col_step = 1
     - Loop 1: current_col becomes 1, append (2, 1)
     - Loop 2: current_col becomes 2, append (2, 2)
     - Loop 3: current_col becomes 3, append (2, 3)
     - Loop ends: current_col (3) equals dest_col (3)

6. **Step 6: Return the Path**
   - Add the return statement:
     ```python
         return path
     ```
   - Explain: The caller gets back the complete list of positions.

7. **Step 7: The Complete Class**
   - Show the entire class together:
     ```python
     class Manhattan:
         def __init__(self, start):
             self.position = start

         def compute_path(self, destination):
             path = [self.position]
             current_row = self.position[0]
             current_col = self.position[1]
             dest_row = destination[0]
             dest_col = destination[1]

             if dest_row > current_row:
                 row_step = 1
             else:
                 row_step = -1

             if dest_col > current_col:
                 col_step = 1
             else:
                 col_step = -1

             while current_row != dest_row:
                 current_row = current_row + row_step
                 path.append((current_row, current_col))

             while current_col != dest_col:
                 current_col = current_col + col_step
                 path.append((current_row, current_col))

             return path
     ```
   - Ask students: "Can you see the paper algorithm in this code? Each step from the worksheet maps directly to a section of the code."

8. **Step 8: Test with Print Statements**
   - Add test code below the class:
     ```python
     nav = Manhattan((0, 0))
     path = nav.compute_path((2, 3))
     print("Path from (0,0) to (2,3):")
     print(path)
     ```
   - Run it. Expected output:
     ```
     Path from (0,0) to (2,3):
     [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]
     ```
   - Compare to the hand-traced result from Lesson 4. They should match exactly!
   - Test a second path:
     ```python
     path2 = nav.compute_path((1, 1))
     print("Path from (0,0) to (1,1):")
     print(path2)
     ```
   - Ask: "Wait -- we created `nav` at position (0,0). Does calling `compute_path` change `nav.position`?" (No! We used local variables `current_row` and `current_col`. `self.position` is unchanged.)

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise: Implement and Test the Manhattan Class**
- Students type the complete `Manhattan` class from scratch (or with minimal reference to the board)
- Write test code that computes and prints paths for at least 4 different start/destination pairs:

1. `(0, 0)` to `(2, 3)` -- both directions positive
2. `(2, 3)` to `(0, 1)` -- both directions negative
3. `(3, 0)` to `(1, 2)` -- row negative, column positive
4. `(1, 3)` to `(3, 1)` -- row positive, column negative

- For each test, compare the printed output to their hand-traced worksheets from Lesson 4
- Expected test program:
  ```python
  class Manhattan:
      def __init__(self, start):
          self.position = start

      def compute_path(self, destination):
          path = [self.position]
          current_row = self.position[0]
          current_col = self.position[1]
          dest_row = destination[0]
          dest_col = destination[1]

          if dest_row > current_row:
              row_step = 1
          else:
              row_step = -1

          if dest_col > current_col:
              col_step = 1
          else:
              col_step = -1

          while current_row != dest_row:
              current_row = current_row + row_step
              path.append((current_row, current_col))

          while current_col != dest_col:
              current_col = current_col + col_step
              path.append((current_row, current_col))

          return path

  # Test 1: Both directions positive
  nav = Manhattan((0, 0))
  path = nav.compute_path((2, 3))
  print("(0,0) to (2,3):", path)

  # Test 2: Both directions negative
  nav2 = Manhattan((2, 3))
  path = nav2.compute_path((0, 1))
  print("(2,3) to (0,1):", path)

  # Test 3: Row negative, column positive
  nav3 = Manhattan((3, 0))
  path = nav3.compute_path((1, 2))
  print("(3,0) to (1,2):", path)

  # Test 4: Row positive, column negative
  nav4 = Manhattan((1, 3))
  path = nav4.compute_path((3, 1))
  print("(1,3) to (3,1):", path)
  ```

- **Bonus: Test the edge cases**
  ```python
  # Same row
  nav5 = Manhattan((1, 0))
  print("(1,0) to (1,3):", nav5.compute_path((1, 3)))

  # Same column
  nav6 = Manhattan((0, 2))
  print("(0,2) to (3,2):", nav6.compute_path((3, 2)))

  # Same position
  nav7 = Manhattan((2, 1))
  print("(2,1) to (2,1):", nav7.compute_path((2, 1)))
  ```

## Assessment

**Formative (during lesson)**:
- Can students explain what `self.position` stores and why it is a tuple?
- Can students trace through the while loop and predict when it will stop?
- Can students explain why `append()` is used to build the path list?
- Does the student's code produce output that matches their hand-traced paths from Lesson 4?

**Summative (worksheet/exit ticket)**:
1. What does `self.position[0]` return? What about `self.position[1]`?
2. If `current_row` is 3 and `dest_row` is 1, what will `row_step` be? How many times will the row while loop execute?
3. Why does the path list start with `[self.position]` instead of an empty list `[]`?
4. What would happen if you wrote `while current_row < dest_row` instead of `while current_row != dest_row`? When would it fail?
5. Write the `compute_path` method from memory (or with minimal hints).

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "I need to modify `self.position` as the algorithm runs" | Never modify `self.position` inside `compute_path`. Use local variables (`current_row`, `current_col`) instead. The object's stored position should stay unchanged so you can compute multiple paths from the same start. |
| "The path starts as an empty list" | The path starts with `[self.position]` -- the starting position is always the first element. If you start with `[]`, you will be missing the first position in every path. |
| "`append` replaces the list" | `append` adds one element to the END of the existing list. It modifies the list in place and does not create a new list. |
| "I need two separate classes for rows and columns" | One class handles both. The `compute_path` method has two while loops -- one for rows, one for columns -- in sequence. |
| "`while current_row < dest_row` works the same as `while current_row != dest_row`" | Using `<` only works when moving to a larger row. If `dest_row` is smaller (moving up), the condition is immediately false and the loop never runs. Use `!=` because it works in both directions. |
| "The parentheses in `path.append((current_row, current_col))` are doubled by mistake" | The outer parentheses are for the `append()` function call. The inner parentheses create the tuple `(current_row, current_col)`. Both are necessary. |

## Differentiation

**For struggling students**:
- Provide the class skeleton with comments indicating what goes where:
  ```python
  class Manhattan:
      def __init__(self, start):
          # Store start as self.position

      def compute_path(self, destination):
          # Create path list with starting position
          # Extract row and col from self.position
          # Extract row and col from destination
          # Determine row_step (+1 or -1)
          # Determine col_step (+1 or -1)
          # While loop for rows
          # While loop for columns
          # Return path
  ```
- Have them fill in one section at a time, testing after each addition
- Keep Lesson 4 worksheets open side-by-side for reference
- Pair with a partner who can help with syntax while they focus on logic
- Allow reference to the complete code on the board

**For advanced students**:
- Add a `get_distance()` method that returns the Manhattan distance without computing the full path
- Add a `__str__` method so `print(nav)` shows the current position nicely
- Modify `compute_path` to also update `self.position` to the destination after computing the path (discuss: is this a good idea? when might you want this vs. not?)
- Add a `compute_path_columns_first()` method that does columns before rows and compare the results
- Think about: Could you combine the two while loops into one? What would that look like?

## Materials & Code Examples

### Complete Manhattan Class
```python
class Manhattan:
    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        path = [self.position]
        current_row = self.position[0]
        current_col = self.position[1]
        dest_row = destination[0]
        dest_col = destination[1]

        if dest_row > current_row:
            row_step = 1
        else:
            row_step = -1

        if dest_col > current_col:
            col_step = 1
        else:
            col_step = -1

        while current_row != dest_row:
            current_row = current_row + row_step
            path.append((current_row, current_col))

        while current_col != dest_col:
            current_col = current_col + col_step
            path.append((current_row, current_col))

        return path
```

### Test Program
```python
class Manhattan:
    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        path = [self.position]
        current_row = self.position[0]
        current_col = self.position[1]
        dest_row = destination[0]
        dest_col = destination[1]

        if dest_row > current_row:
            row_step = 1
        else:
            row_step = -1

        if dest_col > current_col:
            col_step = 1
        else:
            col_step = -1

        while current_row != dest_row:
            current_row = current_row + row_step
            path.append((current_row, current_col))

        while current_col != dest_col:
            current_col = current_col + col_step
            path.append((current_row, current_col))

        return path

# --- Test cases ---
print("=== Manhattan Path Tests ===")
print()

# Test 1: Down and right
nav = Manhattan((0, 0))
path = nav.compute_path((2, 3))
print("(0,0) to (2,3):")
print("  Path:", path)
print("  Moves:", len(path) - 1)
print()

# Test 2: Up and left
nav2 = Manhattan((2, 3))
path = nav2.compute_path((0, 1))
print("(2,3) to (0,1):")
print("  Path:", path)
print("  Moves:", len(path) - 1)
print()

# Test 3: Up and right
nav3 = Manhattan((3, 0))
path = nav3.compute_path((1, 2))
print("(3,0) to (1,2):")
print("  Path:", path)
print("  Moves:", len(path) - 1)
print()

# Test 4: Down and left
nav4 = Manhattan((1, 3))
path = nav4.compute_path((3, 1))
print("(1,3) to (3,1):")
print("  Path:", path)
print("  Moves:", len(path) - 1)
print()

# Edge case: Same row
nav5 = Manhattan((1, 0))
print("(1,0) to (1,3):", nav5.compute_path((1, 3)))

# Edge case: Same column
nav6 = Manhattan((0, 2))
print("(0,2) to (3,2):", nav6.compute_path((3, 2)))

# Edge case: Same position
nav7 = Manhattan((2, 1))
print("(2,1) to (2,1):", nav7.compute_path((2, 1)))
```

### Expected Output
```
=== Manhattan Path Tests ===

(0,0) to (2,3):
  Path: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]
  Moves: 5

(2,3) to (0,1):
  Path: [(2, 3), (1, 3), (0, 3), (0, 2), (0, 1)]
  Moves: 4

(3,0) to (1,2):
  Path: [(3, 0), (2, 0), (1, 0), (1, 1), (1, 2)]
  Moves: 4

(1,3) to (3,1):
  Path: [(1, 3), (2, 3), (3, 3), (3, 2), (3, 1)]
  Moves: 4

(1,0) to (1,3): [(1, 0), (1, 1), (1, 2), (1, 3)]
(0,2) to (3,2): [(0, 2), (1, 2), (2, 2), (3, 2)]
(2,1) to (2,1): [(2, 1)]
```

### Building the Class Step by Step (for Board Reference)
```python
# Step 1: Just __init__
class Manhattan:
    def __init__(self, start):
        self.position = start

# Step 2: compute_path skeleton
    def compute_path(self, destination):
        path = [self.position]
        current_row = self.position[0]
        current_col = self.position[1]
        dest_row = destination[0]
        dest_col = destination[1]
        # ... more to come
        return path

# Step 3: Add direction logic
        if dest_row > current_row:
            row_step = 1
        else:
            row_step = -1

        if dest_col > current_col:
            col_step = 1
        else:
            col_step = -1

# Step 4: Add row while loop
        while current_row != dest_row:
            current_row = current_row + row_step
            path.append((current_row, current_col))

# Step 5: Add column while loop
        while current_col != dest_col:
            current_col = current_col + col_step
            path.append((current_row, current_col))
```

## Teaching Notes
- **Live-code the class one step at a time.** Do not show the complete class and expect students to absorb it. Build it piece by piece, testing after each addition. Students should type along with you.
- **Test after every step.** After writing `__init__`, create an instance and print. After adding the direction logic, add a temporary print to show `row_step` and `col_step`. After each while loop, print the path so far. Immediate feedback prevents errors from accumulating.
- **The double parentheses in `path.append((row, col))` will confuse students.** Spend time on this. Show that `(current_row, current_col)` creates a tuple, and `append(...)` adds it to the list. Draw it out: `append( (2, 1) )` -- the outer parens are the function call, the inner parens are the tuple.
- **Connect every line of code to the paper algorithm.** Keep the Lesson 4 pseudocode visible on the board and point to the corresponding code as you write it. Students should see that the code IS the algorithm, just written in Python syntax.
- **Watch for `!=` vs `<` confusion.** Some students will instinctively write `while current_row < dest_row`, which only works when moving to larger row numbers. Demonstrate the failure: trace (2,3) to (0,1) with `<` and show that the loop never executes. `!=` works in both directions.
- **Tuple indexing is new for some students.** If students have not seen `position[0]` and `position[1]` before, spend a few extra minutes on this. Show that tuples work like lists for reading values: index 0 is the first element, index 1 is the second.
- **Do not worry about efficiency.** The algorithm visits every cell along the L-shaped path, which is optimal for Manhattan distance. There is nothing to optimize here, and students should not be distracted by performance concerns.

## Connections to Next Lessons
- **Lesson 6** will focus on systematic testing of the `Manhattan` class -- students will write a dedicated test program and compare output to their Lesson 4 hand-traced paths.
- **Later lessons** will integrate the `Manhattan` class with the robot's drivetrain to execute the computed paths on the physical grid.
- **The pattern of "compute first, then execute"** is a key software design principle that will recur throughout the course -- separating the planning (path computation) from the action (robot movement).
