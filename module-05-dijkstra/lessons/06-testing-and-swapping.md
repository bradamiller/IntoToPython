# Lesson 6: Testing and Swapping

## Overview
Students learn to verify their Dijkstra class by writing systematic tests, then experience the power of a shared interface by swapping Dijkstra into the Module 4 navigation program with only two lines of code changed. This lesson is where all the careful design work from Lessons 4-5 pays off: because the Dijkstra class and the Manhattan class both implement a `compute_path()` method that accepts a start and destination tuple and returns a list of (row, column) tuples, the Navigator class does not care which pathfinder it uses. Students first test Dijkstra in isolation -- verifying that paths on an obstacle-free grid match Manhattan distance, and that paths on a grid with blocked nodes correctly reroute around obstacles. Then they swap the Dijkstra class into the full Navigator program by changing just the import statement and the constructor call. The robot drives exactly as before, but now it can handle obstacles. This lesson introduces the concept of **polymorphism through a shared interface** -- one of the most powerful ideas in software engineering -- without requiring students to learn formal object-oriented terminology.

This lesson bridges the gap between building the Dijkstra class (Lessons 4-5) and using it with real sensors (Lessons 7-8). Before students add rangefinder-based obstacle detection, they need confidence that the pathfinding itself works correctly. The side-by-side comparison tests also reinforce the idea that good software design -- specifically, consistent interfaces -- makes code flexible and easy to change.

## Learning Objectives
By the end of this lesson, students will be able to:
- Write test cases that verify Dijkstra produces correct paths on an obstacle-free grid
- Write test cases that verify Dijkstra correctly reroutes around blocked nodes
- Explain what a shared interface is and why it matters
- Swap the Dijkstra class into a Module 4 Navigator program by changing only the import and constructor lines
- Run the Navigator with both Manhattan and Dijkstra pathfinders and observe identical behavior on a clear grid
- Compare Manhattan and Dijkstra output side-by-side and explain the differences when obstacles are present

## Key Concepts
- **Testing**: Running code with known inputs and checking that the output matches expected results. Testing builds confidence that code works before deploying it on hardware (the robot).
- **Test case**: A specific combination of inputs and expected outputs used to verify that code behaves correctly. For example: "On a 4x4 grid with no obstacles, the path from (0,0) to (3,3) should be 6 steps long."
- **Shared interface**: When two or more classes provide the same method names, accept the same parameters, and return the same types of data. The Manhattan class and Dijkstra class both have `compute_path(start, destination)` that returns a list of (row, col) tuples -- this is their shared interface.
- **Polymorphism (through shared interface)**: The ability to swap one class for another without changing the code that uses it, because both classes provide the same interface. The Navigator does not care whether it is using Manhattan or Dijkstra -- it just calls `compute_path()`.
- **Drop-in replacement**: A component that can replace another with minimal or no changes to surrounding code. Dijkstra is a drop-in replacement for Manhattan because it shares the same interface.
- **Regression testing**: Running your existing tests after making a change to ensure the change did not break anything that was previously working.

## Materials Required
- Computers with Python and Thonny (or preferred IDE)
- Completed Dijkstra class from Lessons 4-5 (`dijkstra.py`)
- Manhattan class from Module 4 (`manhattan.py`)
- Navigator class from Module 4 (`navigator.py`)
- XRP robot and grid (for the swap demonstration)
- Whiteboard or projector for side-by-side comparison
- Test output worksheet (for recording expected vs. actual results)

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 10-12 min

1. **Hook: Would You Trust Untested Code to Drive Your Car?**
   - Ask: "Imagine you wrote the software for a self-driving car. Would you put a passenger in it without testing it first?"
   - Discussion: Of course not. You would test it in simulation, on a closed course, with edge cases and unusual scenarios before letting anyone ride in it.
   - "Our robot is the same. We built the Dijkstra class, but we haven't proven it works yet. Today we test it -- and then we put it in the robot."
   - "And here's the cool part: because we designed Dijkstra with the same interface as Manhattan, swapping it in takes just TWO lines of code."

2. **What Makes a Good Test?**
   - A good test has:
     - **Known input**: A specific grid size, blocked list, start, and destination
     - **Expected output**: The path you calculated by hand (or know from Manhattan distance)
     - **A check**: Code that compares the actual output to the expected output
   - "We'll write tests for two scenarios: grids with NO obstacles (where Dijkstra should match Manhattan) and grids WITH obstacles (where Dijkstra should find a detour)."

3. **What Is a Shared Interface?**
   - Write on the board:
     ```
     Manhattan:   compute_path(start, destination) -> list of tuples
     Dijkstra:    compute_path(start, destination) -> list of tuples
     ```
   - "Both classes take the same inputs and return the same type of output. This means any code that works with Manhattan also works with Dijkstra -- no changes needed."
   - "This idea has a name in computer science: **polymorphism**. It means 'many forms.' The Navigator works with many forms of pathfinder, as long as they share the same interface."

### Guided Practice (15 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 20 min

1. **Test 1: No Obstacles -- Dijkstra Should Match Manhattan Distance**
   - Walk through writing the test together:
     ```python
     from dijkstra import Dijkstra

     # Test 1: No obstacles on a 4x4 grid
     pathfinder = Dijkstra(4, 4, [])
     path = pathfinder.compute_path((0, 0), (3, 3))
     print("Path:", path)
     print("Path length:", len(path) - 1, "steps")
     print("Expected steps (Manhattan distance):", 6)
     ```
   - Run the code. The path length (number of steps, which is `len(path) - 1`) should equal the Manhattan distance: |3-0| + |3-0| = 6.
   - Note: The exact path may differ from Manhattan's path (Dijkstra might go a different route of the same length), but the NUMBER of steps must be the same.
   - Ask: "Why do we check the number of steps and not the exact path?" (Because there can be multiple shortest paths of the same length.)

2. **Test 2: Blocked Node -- Dijkstra Should Reroute**
   - Add a blocked node and test again:
     ```python
     # Test 2: Block (1, 0) -- force a detour
     pathfinder_blocked = Dijkstra(4, 4, [(1, 0)])
     path_blocked = pathfinder_blocked.compute_path((0, 0), (3, 0))
     print("Path with (1,0) blocked:", path_blocked)
     print("Path length:", len(path_blocked) - 1, "steps")
     print("Manhattan distance (no obstacles):", 3)
     ```
   - Run the code. The path should avoid (1, 0) entirely. The path length should be longer than the Manhattan distance of 3.
   - Ask: "Does (1, 0) appear in the path?" (No -- it is blocked.)
   - Ask: "Is the path longer than 3 steps?" (Yes -- the detour costs extra steps.)

3. **Test 3: Verify the Blocked Node Is Not in the Path**
   - Add an explicit check:
     ```python
     # Test 3: Make sure blocked nodes never appear in the path
     blocked = [(1, 0), (2, 2)]
     pathfinder_multi = Dijkstra(4, 4, blocked)
     path_multi = pathfinder_multi.compute_path((0, 0), (3, 3))

     for node in path_multi:
         if node in blocked:
             print("ERROR: Path goes through blocked node", node)
             break
     else:
         print("PASS: Path avoids all blocked nodes")
     ```
   - Run the code. The output should say "PASS."
   - Explain the `for/else` construct: the `else` block runs only if the loop completes without `break`.

4. **The Swap: Dijkstra into the Navigator**
   - Show the Module 4 Navigator code (simplified):
     ```python
     # Module 4 version -- uses Manhattan
     from manhattan import Manhattan

     pathfinder = Manhattan(4, 4)
     # Navigator uses pathfinder.compute_path(start, dest) to get paths
     ```
   - Now change TWO lines:
     ```python
     # Module 5 version -- uses Dijkstra
     from dijkstra import Dijkstra

     pathfinder = Dijkstra(4, 4, [])
     # Navigator uses pathfinder.compute_path(start, dest) to get paths
     # NOTHING ELSE CHANGES
     ```
   - "That's it. The Navigator calls `pathfinder.compute_path()` exactly the same way. It doesn't know or care whether it's talking to Manhattan or Dijkstra."

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

**Exercise 1: Write a Complete Test Suite**
- Goal: Create a file `test_dijkstra.py` with at least 5 test cases
- Required tests:
  1. No obstacles, short path (e.g., (0,0) to (1,1) on a 3x3 grid) -- verify step count equals Manhattan distance
  2. No obstacles, long path (e.g., (0,0) to (3,3) on a 4x4 grid) -- verify step count equals Manhattan distance
  3. One blocked node on the direct path -- verify rerouting and no blocked nodes in path
  4. Multiple blocked nodes -- verify path avoids all of them
  5. Start and destination are the same -- verify path is just the start node
- For each test, print "PASS" or "FAIL" with a description

**Exercise 2: Side-by-Side Comparison**
- Goal: Run both Manhattan and Dijkstra on the same inputs and compare
- Steps:
  1. Create both pathfinders for a 4x4 grid (Dijkstra with empty blocked list)
  2. Test 3 different start/destination pairs
  3. Print both paths and their lengths side-by-side
  4. Verify that on a clear grid, both produce paths of the same length
- Key question: Are the paths always identical? Why or why not?

**Exercise 3: The Two-Line Swap**
- Goal: Modify your Module 4 navigation program to use Dijkstra
- Steps:
  1. Copy your Module 4 main program file
  2. Change the import from `manhattan` to `dijkstra`
  3. Change the constructor from `Manhattan(rows, cols)` to `Dijkstra(rows, cols, [])`
  4. Run the program on the robot -- it should behave identically on a clear grid
  5. Now add a blocked node and run again -- the robot should detour around it
- Reflection: How many lines did you change? Why did so few changes work?

**Exercise 4: Challenge -- Automated Pass/Fail Testing**
- Goal: Write a test function that automatically checks results
- Create a function:
  ```python
  def test_path(name, pathfinder, start, dest, blocked_list):
      path = pathfinder.compute_path(start, dest)
      # Check 1: path starts at start
      # Check 2: path ends at dest
      # Check 3: no blocked nodes in path
      # Check 4: each step moves to an adjacent node
      # Print PASS or FAIL for each check
  ```
- Run it with at least 3 different test scenarios

### Assessment

**Formative (during lesson)**:
- Can students write a test case with known inputs and expected outputs?
- Can students explain why Dijkstra's path length matches Manhattan distance on a clear grid?
- Can students identify the two lines that need to change to swap pathfinders?
- Can students explain what a shared interface is in their own words?
- Can students predict what will happen when the Navigator uses Dijkstra instead of Manhattan?

**Summative (worksheet/exit ticket)**:
1. Write a test case that verifies Dijkstra finds a path of length 4 from (0,0) to (2,2) on a 3x3 grid with no obstacles.
2. If (1,1) is blocked on a 3x3 grid, what is the shortest path from (0,0) to (2,2)? How many steps? Write a test case that checks this.
3. What two lines of code do you change to swap Manhattan for Dijkstra in the Navigator program? Write both the old and new versions.
4. Explain in your own words: What is a shared interface? Why does it make the swap possible?
5. The Navigator class works with both Manhattan and Dijkstra without modification. What is this property called, and why is it useful?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "Dijkstra and Manhattan should return the exact same path on a clear grid" | They should return paths of the same LENGTH, but the exact route may differ. There are often multiple shortest paths between two points, and the two algorithms may choose differently. |
| "Testing means running the program and seeing if it looks right" | Testing means comparing actual output to a specific expected result. Visual inspection misses subtle bugs. Automated checks catch errors reliably. |
| "The swap works because Dijkstra is better than Manhattan" | The swap works because both classes share the same INTERFACE -- the same method name, parameters, and return type. Quality does not matter for swappability; interface compatibility does. |
| "You need to rewrite the Navigator to use Dijkstra" | You change only the import and the constructor -- two lines. The Navigator's code that calls `compute_path()` does not change at all. This is the whole point of a shared interface. |
| "Polymorphism is an advanced concept I don't need to understand" | Students are already using polymorphism when they swap one pathfinder for another. The concept is simple: if two things work the same way from the outside, you can use either one. The formal name is just a label for what they are already doing. |
| "If all tests pass, the code is bug-free" | Passing tests means the code works for the cases you tested. There may be edge cases you did not think of. More tests give more confidence, but testing can never prove the complete absence of bugs. |

## Differentiation

**For struggling students**:
- Provide a test template with blanks to fill in (the inputs and expected values) rather than writing tests from scratch
- Start with the simplest possible test: a 2x2 grid, no obstacles, (0,0) to (1,1) -- the path should be 2 steps
- Walk through the swap step-by-step: first show the old import, then the new import, then run and compare
- Use a checklist: (1) write the input, (2) calculate the expected output by hand, (3) run the code, (4) compare
- Pair with a partner for the side-by-side comparison exercise

**For advanced students**:
- Write a function that generates random blocked lists and tests Dijkstra on them, checking that no blocked node appears in any path
- Add timing to tests: how long does Dijkstra take vs. Manhattan on larger grids? (Use `import time`)
- Research: What is "duck typing" in Python? How does it relate to the shared interface concept?
- Create a test that verifies Dijkstra's path is actually the SHORTEST path (not just a valid path) by checking that no shorter path exists
- Write tests for edge cases: What if the start is blocked? What if the destination is blocked? What if all paths are blocked?

## Materials & Code Examples

### Test Program: Comparing Manhattan and Dijkstra
```python
# test_compare.py
# Side-by-side comparison of Manhattan and Dijkstra pathfinders

from manhattan import Manhattan
from dijkstra import Dijkstra

# Setup
rows = 4
cols = 4

manhattan_pf = Manhattan(rows, cols)
dijkstra_pf = Dijkstra(rows, cols, [])  # No obstacles

# Test cases: (start, destination, description)
test_cases = [
    ((0, 0), (3, 3), "Corner to corner"),
    ((0, 0), (0, 3), "Top-left to top-right"),
    ((1, 1), (3, 2), "Interior to edge"),
]

print("=" * 60)
print("COMPARISON: Manhattan vs. Dijkstra (no obstacles)")
print("=" * 60)

for start, dest, description in test_cases:
    m_path = manhattan_pf.compute_path(start, dest)
    d_path = dijkstra_pf.compute_path(start, dest)

    m_steps = len(m_path) - 1
    d_steps = len(d_path) - 1

    print(f"\nTest: {description}")
    print(f"  Start: {start}  Destination: {dest}")
    print(f"  Manhattan path: {m_path}")
    print(f"  Dijkstra path:  {d_path}")
    print(f"  Manhattan steps: {m_steps}")
    print(f"  Dijkstra steps:  {d_steps}")

    if m_steps == d_steps:
        print(f"  PASS: Both produce {m_steps}-step paths")
    else:
        print(f"  FAIL: Step counts differ! Manhattan={m_steps}, Dijkstra={d_steps}")
```

### Test Program: Dijkstra with Obstacles
```python
# test_obstacles.py
# Test that Dijkstra correctly handles blocked nodes

from dijkstra import Dijkstra

print("=" * 60)
print("TESTING: Dijkstra with obstacles")
print("=" * 60)

# Test 1: Single blocked node
blocked = [(1, 0)]
pf = Dijkstra(4, 4, blocked)
path = pf.compute_path((0, 0), (3, 0))

print("\nTest 1: (1,0) blocked, path from (0,0) to (3,0)")
print(f"  Path: {path}")
print(f"  Steps: {len(path) - 1}")

blocked_in_path = [node for node in path if node in blocked]
if len(blocked_in_path) == 0:
    print("  PASS: No blocked nodes in path")
else:
    print(f"  FAIL: Blocked nodes in path: {blocked_in_path}")

# Test 2: Multiple blocked nodes
blocked = [(1, 0), (1, 1), (2, 2)]
pf = Dijkstra(4, 4, blocked)
path = pf.compute_path((0, 0), (3, 3))

print("\nTest 2: Three blocked nodes, path from (0,0) to (3,3)")
print(f"  Path: {path}")
print(f"  Steps: {len(path) - 1}")

blocked_in_path = [node for node in path if node in blocked]
if len(blocked_in_path) == 0:
    print("  PASS: No blocked nodes in path")
else:
    print(f"  FAIL: Blocked nodes in path: {blocked_in_path}")

# Test 3: Path should start at start and end at destination
start = (0, 0)
dest = (3, 3)
if path[0] == start and path[-1] == dest:
    print("  PASS: Path starts and ends correctly")
else:
    print(f"  FAIL: Path starts at {path[0]}, ends at {path[-1]}")

# Test 4: Each step should move to an adjacent node
all_adjacent = True
for i in range(len(path) - 1):
    r1, c1 = path[i]
    r2, c2 = path[i + 1]
    distance = abs(r1 - r2) + abs(c1 - c2)
    if distance != 1:
        print(f"  FAIL: Non-adjacent step from {path[i]} to {path[i+1]}")
        all_adjacent = False
        break

if all_adjacent:
    print("  PASS: All steps are to adjacent nodes")

# Test 5: Start equals destination
pf = Dijkstra(3, 3, [])
path = pf.compute_path((1, 1), (1, 1))
print(f"\nTest 5: Start equals destination")
print(f"  Path: {path}")
if path == [(1, 1)]:
    print("  PASS: Path is just the start node")
else:
    print(f"  FAIL: Expected [(1, 1)], got {path}")
```

### The Two-Line Swap
```python
# ========================================
# BEFORE (Module 4 version -- Manhattan)
# ========================================
from manhattan import Manhattan

pathfinder = Manhattan(4, 4)
# ... rest of program uses pathfinder.compute_path(start, dest)


# ========================================
# AFTER (Module 5 version -- Dijkstra)
# ========================================
from dijkstra import Dijkstra

pathfinder = Dijkstra(4, 4, [])
# ... rest of program uses pathfinder.compute_path(start, dest)
# NOTHING ELSE CHANGES -- Navigator works exactly the same way
```

### Full Navigator Swap Example
```python
# main_navigation.py
# This program works with EITHER pathfinder -- just change the two lines below

# OPTION A: Manhattan (Module 4)
# from manhattan import Manhattan
# pathfinder = Manhattan(4, 4)

# OPTION B: Dijkstra (Module 5)
from dijkstra import Dijkstra
pathfinder = Dijkstra(4, 4, [(1, 0), (2, 2)])  # Can include obstacles!

from navigator import Navigator

nav = Navigator(pathfinder)

# The Navigator uses pathfinder.compute_path() internally
# It does not know or care which class it is talking to
destinations = [(0, 3), (3, 3), (3, 0)]

for dest in destinations:
    print(f"Navigating to {dest}...")
    nav.go_to(dest)
    print(f"Arrived at {dest}")
```

### Automated Test Function (Challenge Exercise)
```python
# test_automated.py
# Reusable test function for any pathfinder

from dijkstra import Dijkstra

def test_path(name, pathfinder, start, dest, blocked_list):
    """Run a series of checks on a computed path."""
    print(f"\n--- {name} ---")
    path = pathfinder.compute_path(start, dest)
    print(f"  Path: {path}")
    passed = 0
    total = 4

    # Check 1: Path starts at start
    if path[0] == start:
        print(f"  PASS: Starts at {start}")
        passed += 1
    else:
        print(f"  FAIL: Should start at {start}, starts at {path[0]}")

    # Check 2: Path ends at destination
    if path[-1] == dest:
        print(f"  PASS: Ends at {dest}")
        passed += 1
    else:
        print(f"  FAIL: Should end at {dest}, ends at {path[-1]}")

    # Check 3: No blocked nodes in path
    blocked_found = [n for n in path if n in blocked_list]
    if len(blocked_found) == 0:
        print(f"  PASS: No blocked nodes in path")
        passed += 1
    else:
        print(f"  FAIL: Blocked nodes in path: {blocked_found}")

    # Check 4: Each step is to an adjacent node
    all_ok = True
    for i in range(len(path) - 1):
        r1, c1 = path[i]
        r2, c2 = path[i + 1]
        if abs(r1 - r2) + abs(c1 - c2) != 1:
            print(f"  FAIL: Non-adjacent step {path[i]} -> {path[i+1]}")
            all_ok = False
            break
    if all_ok:
        print(f"  PASS: All steps adjacent")
        passed += 1

    print(f"  Result: {passed}/{total} checks passed")
    return passed == total


# Run the tests
blocked = [(1, 0), (2, 2)]
pf = Dijkstra(4, 4, blocked)

test_path("Short path, no obstacle in way", pf, (0, 0), (0, 3), blocked)
test_path("Path must reroute around (1,0)", pf, (0, 0), (3, 0), blocked)
test_path("Path must reroute around (2,2)", pf, (0, 0), (3, 3), blocked)
```

## Teaching Notes
- **This lesson is the payoff for good design.** Students spent Lessons 4-5 building the Dijkstra class with a specific interface. Now they see why: the two-line swap is a powerful, concrete demonstration that good design decisions have practical benefits. Make the swap moment dramatic -- show the old code, make the change live, and run it.
- **Spend time on testing before the swap.** Students are often eager to get to the "cool part" (the swap), but testing teaches a critical skill. Emphasize that professional software developers spend as much time testing as they do writing code.
- **Let students discover that paths can differ.** When Manhattan and Dijkstra return different paths of the same length, use this as a teaching moment: there are often multiple correct answers, and different algorithms may find different ones. What matters is that the path length is optimal.
- **The polymorphism discussion should be light.** Do not get bogged down in formal OOP terminology. Students only need to understand: "If two things work the same way from the outside, you can use either one." The word "polymorphism" is optional vocabulary; the concept is what matters.
- **Connect to real-world examples.** USB-C is a shared interface -- many different devices use the same connector. Electrical outlets are a shared interface -- any appliance with a plug works in any outlet. These analogies make the concept concrete.
- **Save test files.** Students will reuse their test cases in Lessons 7-8 when they add obstacle detection, and again in the capstone (Lesson 9).

## Connections to Next Lessons
- **Lesson 7** will add **obstacle detection** using the XRP rangefinder sensor. Instead of pre-programming the blocked list, the robot will discover obstacles during navigation and feed them to the Dijkstra class for real-time rerouting.
- **Lesson 8** will introduce **obstacle memory** -- saving discovered obstacles between runs so the robot improves over time. The test infrastructure built here will help students verify that the obstacle memory system works correctly.
- **Lesson 9** (Capstone) will combine everything: Dijkstra pathfinding, the Navigator, rangefinder detection, and obstacle memory into a complete autonomous navigation system. The testing skills from this lesson are essential for debugging the capstone project.
- The shared interface concept introduced here applies broadly in programming -- students will encounter it again whenever they use libraries, APIs, or frameworks that expect components to follow a specific interface.
