# Lesson 5: Implementing the Manhattan Class

## Overview
Students convert the `compute_path` function they wrote in Lesson 4 into a `Manhattan` class. The focus of this lesson is on understanding why classes are useful and how to mechanically transform a standalone function into a method inside a class. Students learn that `__init__` stores the robot's starting position, and `compute_path` becomes a method that uses `self.position` instead of accepting a start parameter. The algorithm itself -- four while loops that build a path list -- is already familiar from Lesson 4. By the end of the lesson, students have a fully functional `Manhattan` class they can test with print statements.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain why wrapping a function in a class is useful (bundles data with behavior, reusable object)
- Design a class with `__init__` that stores position as a tuple
- Convert a standalone function into a method by adding `self` and using `self.position`
- Write a method that accepts a parameter (destination) and returns a result (path)
- Use tuple unpacking to extract row and column values
- Test a class by creating an instance and calling its methods with print statements

## Key Concepts
- **Why Classes?**: A class bundles data (the robot's position) with behavior (computing a path). Instead of passing the start position every time you call the function, the object remembers it.
- **From Function to Method**: The function's `start` parameter disappears -- the class stores it as `self.position` in `__init__`, and the method reads it from there.
- **The `self` Prefix**: Inside a method, `self.position` accesses the data stored in `__init__`. Local variables like `current_row` do NOT need `self` because they are temporary.
- **Tuple Unpacking**: `current_row, current_col = self.position` extracts both values in one line -- cleaner than indexing with `[0]` and `[1]`.
- **Building a List with append()**: Starting with an empty list `[]` and adding each new position one at a time inside the while loops.
- **Return Value**: The `compute_path` method returns the completed path list to the caller.

## Materials Required
- Computer with VS Code and Python installed
- Working `compute_path` function from Lesson 4 (students should have this in their files)
- Hand-traced paths from Lesson 4 worksheets (for verification)
- Whiteboard or projector for live coding
- No robot needed -- all testing is done with print statements

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Hook: The Problem with Functions**
   - Display (or have students open) their `compute_path` function from Lesson 4
   - Ask students to write code that computes three paths from the same starting position:
     ```python
     path1 = compute_path((0, 0), (2, 3))
     path2 = compute_path((0, 0), (1, 1))
     path3 = compute_path((0, 0), (3, 2))
     ```
   - Point out the repetition: "We typed `(0, 0)` three times. What if the robot starts at a different position? We would have to change it in every single call."
   - Now show the class version:
     ```python
     nav = Manhattan((0, 0))
     path1 = nav.compute_path((2, 3))
     path2 = nav.compute_path((1, 1))
     path3 = nav.compute_path((3, 2))
     ```
   - Ask: "Which version is easier to read? Which is easier to change if the start position changes?"
   - Key idea: A class lets us store the starting position once and reuse it across multiple method calls.

2. **What Changes, What Stays the Same**:
   - Write on the board:
     ```
     Function version:  compute_path(start, destination)
     Class version:     nav.compute_path(destination)
     ```
   - Ask: "Where did the `start` parameter go?" (It is stored inside the object when we create it.)
   - The algorithm inside `compute_path` stays exactly the same. The only changes are:
     - `start` becomes `self.position`
     - The function moves inside a class
     - We add `self` as the first parameter

3. **Preview the Class Structure**:
   - Show the skeleton on the board:
     ```python
     class Manhattan:
         def __init__(self, start):
             # Store the starting position
             pass

         def compute_path(self, destination):
             # Same algorithm as Lesson 4, but uses self.position
             pass
     ```
   - Explain: The class is called `Manhattan` (CamelCase, like `LineSensor` from Module 2). It takes a starting position when created and has a method to compute a path to any destination.

### Guided Practice: Converting the Function to a Class (20 minutes)
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
     ```
   - Ask: "Where does `(0, 0)` end up?" (It goes into the `start` parameter, then gets stored as `self.position`.)

2. **Step 2: Starting compute_path -- Setup Variables**
   - Begin the method by extracting the values we need:
     ```python
     def compute_path(self, destination):
         path = []
         current_row, current_col = self.position
         dest_row, dest_col = destination
     ```
   - Walk through each line:
     - `path = []` -- Start with an empty path list. We will add each position the robot moves TO.
     - `current_row, current_col = self.position` -- Tuple unpacking! If `self.position` is `(0, 0)`, then `current_row` gets `0` and `current_col` gets `0`.
     - `dest_row, dest_col = destination` -- Same unpacking for the destination.
   - Compare to the Lesson 4 function: "In the function, you wrote `current_row, current_col = start`. Now `start` is replaced by `self.position`. That is the only difference."
   - Ask: "Why do we create separate variables instead of modifying `self.position` directly?" (Because we do not want to change our stored position -- we just want to calculate a path.)

3. **Step 3: The Four While Loops**
   - Add the while loops -- students should recognize these from Lesson 4:
     ```python
         # Move south (rows increase)
         while current_row < dest_row:
             current_row = current_row + 1
             path.append((current_row, current_col))

         # Move north (rows decrease)
         while current_row > dest_row:
             current_row = current_row - 1
             path.append((current_row, current_col))

         # Move east (columns increase)
         while current_col < dest_col:
             current_col = current_col + 1
             path.append((current_row, current_col))

         # Move west (columns decrease)
         while current_col > dest_col:
             current_col = current_col - 1
             path.append((current_row, current_col))
     ```
   - Ask: "Do you recognize these loops?" (They are the same four while loops from the Lesson 4 function -- nothing changed.)
   - Briefly trace through (0,0) to (2,3) to confirm:
     - South loop: current_row goes 0 -> 1 -> 2, appending (1,0) and (2,0)
     - North loop: skipped (current_row is not greater than dest_row)
     - East loop: current_col goes 0 -> 1 -> 2 -> 3, appending (2,1), (2,2), (2,3)
     - West loop: skipped
   - Note the tuple syntax: `(current_row, current_col)` creates a new tuple. The parentheses inside `append()` are the tuple, not extra function parentheses.

4. **Step 4: Return the Path**
   - Add the return statement:
     ```python
         return path
     ```
   - Explain: The caller gets back the list of positions the robot visits. The starting position is NOT in the path -- only the positions the robot moves to.

5. **Step 5: The Complete Class**
   - Show the entire class together:
     ```python
     class Manhattan:
         def __init__(self, start):
             self.position = start

         def compute_path(self, destination):
             path = []
             current_row, current_col = self.position
             dest_row, dest_col = destination

             while current_row < dest_row:
                 current_row = current_row + 1
                 path.append((current_row, current_col))
             while current_row > dest_row:
                 current_row = current_row - 1
                 path.append((current_row, current_col))
             while current_col < dest_col:
                 current_col = current_col + 1
                 path.append((current_row, current_col))
             while current_col > dest_col:
                 current_col = current_col - 1
                 path.append((current_row, current_col))

             return path
     ```
   - Ask: "What is different from the Lesson 4 function?" Students should identify: (1) it is inside a class, (2) `self` is the first parameter, (3) `start` was replaced by `self.position`.

6. **Step 6: Test with Print Statements**
   - Add test code below the class:
     ```python
     nav = Manhattan((0, 0))
     path = nav.compute_path((2, 3))
     print("Path from (0,0) to (2,3):")
     print(path)
     print("Steps:", len(path))
     ```
   - Run it. Expected output:
     ```
     Path from (0,0) to (2,3):
     [(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]
     Steps: 5
     ```
   - Compare to the hand-traced result from Lesson 4. They should match!
   - Test a second path:
     ```python
     path2 = nav.compute_path((1, 1))
     print("Path from (0,0) to (1,1):")
     print(path2)
     ```
   - Ask: "We created `nav` at position (0,0). Does calling `compute_path` change `nav.position`?" (No! We used local variables `current_row` and `current_col`. `self.position` is unchanged.)
   - Ask: "How many steps is the path from (0,0) to (2,3)?" (5 -- just `len(path)` since the path only contains positions the robot moves to.)

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise: Implement and Test the Manhattan Class**
- Students convert their Lesson 4 `compute_path` function into a `Manhattan` class (or type it from scratch with minimal reference to the board)
- Write test code that computes and prints paths for at least 4 different start/destination pairs:

1. `(0, 0)` to `(2, 3)` -- south then east
2. `(2, 3)` to `(0, 1)` -- north then west
3. `(3, 0)` to `(1, 2)` -- north then east
4. `(1, 3)` to `(3, 1)` -- south then west

- For each test, compare the printed output to their hand-traced worksheets from Lesson 4
- Expected test program:
  ```python
  class Manhattan:
      def __init__(self, start):
          self.position = start

      def compute_path(self, destination):
          path = []
          current_row, current_col = self.position
          dest_row, dest_col = destination

          while current_row < dest_row:
              current_row = current_row + 1
              path.append((current_row, current_col))
          while current_row > dest_row:
              current_row = current_row - 1
              path.append((current_row, current_col))
          while current_col < dest_col:
              current_col = current_col + 1
              path.append((current_row, current_col))
          while current_col > dest_col:
              current_col = current_col - 1
              path.append((current_row, current_col))

          return path

  # Test 1: South then east
  nav = Manhattan((0, 0))
  path = nav.compute_path((2, 3))
  print("(0,0) to (2,3):", path)

  # Test 2: North then west
  nav2 = Manhattan((2, 3))
  path = nav2.compute_path((0, 1))
  print("(2,3) to (0,1):", path)

  # Test 3: North then east
  nav3 = Manhattan((3, 0))
  path = nav3.compute_path((1, 2))
  print("(3,0) to (1,2):", path)

  # Test 4: South then west
  nav4 = Manhattan((1, 3))
  path = nav4.compute_path((3, 1))
  print("(1,3) to (3,1):", path)
  ```

- **Bonus: Test the edge cases**
  ```python
  # Same row (only column movement)
  nav5 = Manhattan((1, 0))
  print("(1,0) to (1,3):", nav5.compute_path((1, 3)))

  # Same column (only row movement)
  nav6 = Manhattan((0, 2))
  print("(0,2) to (3,2):", nav6.compute_path((3, 2)))

  # Same position (no movement needed)
  nav7 = Manhattan((2, 1))
  print("(2,1) to (2,1):", nav7.compute_path((2, 1)))
  ```

## Assessment

**Formative (during lesson)**:
- Can students explain why wrapping the function in a class is useful?
- Can students identify the three changes needed to convert the function to a method? (`self` parameter, `self.position` replaces `start`, function moves inside a class)
- Can students explain what `self.position` stores and why it is a tuple?
- Does the student's code produce output that matches their hand-traced paths from Lesson 4?

**Summative (worksheet/exit ticket)**:
1. What is the advantage of using a `Manhattan` class over a standalone `compute_path` function?
2. In the class version, the function parameter `start` disappears. Where does that information come from instead?
3. What does `current_row, current_col = self.position` do? What is this called?
4. If we call `nav.compute_path((2, 1))` and `nav` was created with `Manhattan((2, 1))`, what does the method return? Why?
5. Write the `compute_path` method from memory (or with minimal hints).

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "I need to modify `self.position` as the algorithm runs" | Never modify `self.position` inside `compute_path`. Use local variables (`current_row`, `current_col`) instead. The object's stored position should stay unchanged so you can compute multiple paths from the same start. |
| "`append` replaces the list" | `append` adds one element to the END of the existing list. It modifies the list in place and does not create a new list. |
| "I need to add `self.` to every variable in the method" | Only data that needs to persist between method calls uses `self.` (like `self.position`). Temporary variables like `current_row`, `path`, and `dest_col` are local to the method and do not need `self.`. |
| "The parentheses in `path.append((current_row, current_col))` are doubled by mistake" | The outer parentheses are for the `append()` function call. The inner parentheses create the tuple `(current_row, current_col)`. Both are necessary. |
| "I need two separate classes for rows and columns" | One class handles both. The `compute_path` method has four while loops -- two for rows (south and north), two for columns (east and west) -- in sequence. For any given path, only the relevant loops actually execute. |

## Differentiation

**For struggling students**:
- Have them open their working Lesson 4 function side-by-side with the class skeleton
- Walk them through the conversion one change at a time: (1) add the class wrapper and `__init__`, (2) indent the function inside the class, (3) add `self` as the first parameter, (4) replace `start` with `self.position`
- Provide the class skeleton with comments indicating what goes where:
  ```python
  class Manhattan:
      def __init__(self, start):
          # Store start as self.position

      def compute_path(self, destination):
          # Create empty path list
          # Unpack self.position into current_row, current_col
          # Unpack destination into dest_row, dest_col
          # Four while loops (same as Lesson 4)
          # Return path
  ```
- Have them fill in one section at a time, testing after each addition
- Keep Lesson 4 worksheets open side-by-side for reference
- Allow reference to the complete code on the board

**For advanced students**:
- Add a `get_distance()` method that returns the Manhattan distance without computing the full path
- Add a `__str__` method so `print(nav)` shows the current position nicely
- Modify `compute_path` to also update `self.position` to the destination after computing the path (discuss: is this a good idea? when might you want this vs. not?)
- Add a `compute_path_columns_first()` method that does columns before rows and compare the results
- Think about: What other data or methods might a Manhattan navigation class need for a real robot?

## Materials & Code Examples

### Complete Manhattan Class
```python
class Manhattan:
    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        path = []
        current_row, current_col = self.position
        dest_row, dest_col = destination

        while current_row < dest_row:
            current_row = current_row + 1
            path.append((current_row, current_col))
        while current_row > dest_row:
            current_row = current_row - 1
            path.append((current_row, current_col))
        while current_col < dest_col:
            current_col = current_col + 1
            path.append((current_row, current_col))
        while current_col > dest_col:
            current_col = current_col - 1
            path.append((current_row, current_col))

        return path
```

### Test Program
```python
class Manhattan:
    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        path = []
        current_row, current_col = self.position
        dest_row, dest_col = destination

        while current_row < dest_row:
            current_row = current_row + 1
            path.append((current_row, current_col))
        while current_row > dest_row:
            current_row = current_row - 1
            path.append((current_row, current_col))
        while current_col < dest_col:
            current_col = current_col + 1
            path.append((current_row, current_col))
        while current_col > dest_col:
            current_col = current_col - 1
            path.append((current_row, current_col))

        return path

# --- Test cases ---
print("=== Manhattan Path Tests ===")
print()

# Test 1: South then east
nav = Manhattan((0, 0))
path = nav.compute_path((2, 3))
print("(0,0) to (2,3):")
print("  Path:", path)
print("  Steps:", len(path))
print()

# Test 2: North then west
nav2 = Manhattan((2, 3))
path = nav2.compute_path((0, 1))
print("(2,3) to (0,1):")
print("  Path:", path)
print("  Steps:", len(path))
print()

# Test 3: North then east
nav3 = Manhattan((3, 0))
path = nav3.compute_path((1, 2))
print("(3,0) to (1,2):")
print("  Path:", path)
print("  Steps:", len(path))
print()

# Test 4: South then west
nav4 = Manhattan((1, 3))
path = nav4.compute_path((3, 1))
print("(1,3) to (3,1):")
print("  Path:", path)
print("  Steps:", len(path))
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
  Path: [(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]
  Steps: 5

(2,3) to (0,1):
  Path: [(1, 3), (0, 3), (0, 2), (0, 1)]
  Steps: 4

(3,0) to (1,2):
  Path: [(2, 0), (1, 0), (1, 1), (1, 2)]
  Steps: 4

(1,3) to (3,1):
  Path: [(2, 3), (3, 3), (3, 2), (3, 1)]
  Steps: 4

(1,0) to (1,3): [(1, 1), (1, 2), (1, 3)]
(0,2) to (3,2): [(1, 2), (2, 2), (3, 2)]
(2,1) to (2,1): []
```

### Side-by-Side Comparison: Function vs. Class (for Board Reference)
```python
# LESSON 4: Standalone function
def compute_path(start, destination):
    path = []
    current_row, current_col = start          # <-- uses start parameter
    dest_row, dest_col = destination

    while current_row < dest_row:
        current_row = current_row + 1
        path.append((current_row, current_col))
    while current_row > dest_row:
        current_row = current_row - 1
        path.append((current_row, current_col))
    while current_col < dest_col:
        current_col = current_col + 1
        path.append((current_row, current_col))
    while current_col > dest_col:
        current_col = current_col - 1
        path.append((current_row, current_col))

    return path

# Calling:
path = compute_path((0, 0), (2, 3))


# LESSON 5: Class version
class Manhattan:
    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        path = []
        current_row, current_col = self.position  # <-- uses self.position
        dest_row, dest_col = destination

        while current_row < dest_row:
            current_row = current_row + 1
            path.append((current_row, current_col))
        while current_row > dest_row:
            current_row = current_row - 1
            path.append((current_row, current_col))
        while current_col < dest_col:
            current_col = current_col + 1
            path.append((current_row, current_col))
        while current_col > dest_col:
            current_col = current_col - 1
            path.append((current_row, current_col))

        return path

# Calling:
nav = Manhattan((0, 0))
path = nav.compute_path((2, 3))
```

## Teaching Notes
- **Frame this lesson as a conversion, not a blank-page exercise.** Students already wrote and tested the algorithm in Lesson 4. The cognitive load here should be on the class mechanics (self, __init__, method), not on the algorithm. Keep the algorithm familiar so students can focus on what is new.
- **Use the side-by-side comparison.** Put the Lesson 4 function and the Lesson 5 class on the board next to each other. Highlight the three differences: (1) class wrapper + `__init__`, (2) `self` parameter, (3) `self.position` replaces `start`. Students should see that the algorithm inside is identical.
- **Live-code the class one step at a time.** Do not show the complete class and expect students to absorb it. Build it piece by piece, testing after each addition. Students should type along with you.
- **Test after every step.** After writing `__init__`, create an instance and print `nav.position`. After adding the while loops, print the path. Immediate feedback prevents errors from accumulating.
- **The double parentheses in `path.append((row, col))` will confuse students.** Spend time on this. Show that `(current_row, current_col)` creates a tuple, and `append(...)` adds it to the list. Draw it out: `append( (2, 1) )` -- the outer parens are the function call, the inner parens are the tuple.
- **Emphasize that `self.` is only for persistent data.** Students will want to put `self.` in front of every variable. Clarify: `self.position` persists because other methods (or future code) need it. `current_row`, `path`, `dest_col` are temporary -- they exist only while `compute_path` is running.
- **The empty path for same-position is correct.** If a student asks "what if start equals destination?", trace through: all four while-loop conditions are false, so no loops execute, and the method returns `[]`. That is correct -- the robot is already there, so there are zero steps to take.
- **Do not worry about efficiency.** The algorithm visits every cell along the L-shaped path, which is optimal for Manhattan distance. There is nothing to optimize here, and students should not be distracted by performance concerns.

## Connections to Next Lessons
- **Lesson 6** will focus on systematic testing of the `Manhattan` class -- students will write a dedicated test program and compare output to their Lesson 4 hand-traced paths.
- **Later lessons** will integrate the `Manhattan` class with the robot's drivetrain to execute the computed paths on the physical grid.
- **The pattern of "compute first, then execute"** is a key software design principle that will recur throughout the course -- separating the planning (path computation) from the action (robot movement).
