# Lesson 6: Testing and Swapping

## Overview
Students verify their Dijkstra functions with systematic tests, then confront a real design question: `compute_manhattan_path(position, destination)` and `compute_dijkstra_path(position, destination, graph)` are *almost* the same shape, but not quite -- Dijkstra needs an extra `graph` argument, and (as flagged in Lesson 5) its returned path includes the start position while Manhattan's doesn't. Students build a small `compute_path(algorithm, position, destination, blocked)` dispatch function that hides these differences behind one call, so the rest of the program -- particularly `drive_path()` -- can ask for a path without caring which algorithm computed it. Swapping algorithms becomes changing one argument, not rewriting the caller. Students first test Dijkstra in isolation, then wire the dispatch function into the Module 4 navigation program.

This lesson bridges the gap between building the Dijkstra functions (Lessons 4-5) and using them with real sensors (Lessons 7-8). Before students add rangefinder-based obstacle detection, they need confidence that the pathfinding itself works correctly. The dispatch function also sets up an honest comparison, in the Optional Extension, to what true object-oriented polymorphism buys you when two components share an identical interface.

## Learning Objectives
By the end of this lesson, students will be able to:
- Write test cases that verify Dijkstra produces correct paths on an obstacle-free grid
- Write test cases that verify Dijkstra correctly reroutes around blocked nodes
- Explain the shape mismatch between `compute_manhattan_path` and `compute_dijkstra_path`
- Write a `compute_path(algorithm, ...)` dispatch function that normalizes the two functions behind one call
- Swap which algorithm a program uses by changing one argument, not rewriting calling code
- Compare Manhattan and Dijkstra output side-by-side and explain the differences when obstacles are present

## Key Concepts
- **Testing**: Running code with known inputs and checking that the output matches expected results. Testing builds confidence that code works before deploying it on hardware (the robot).
- **Test case**: A specific combination of inputs and expected outputs used to verify that code behaves correctly. For example: "On a 4x4 grid with no obstacles, the path from (0,0) to (3,3) should be 6 steps long."
- **Interface mismatch**: Two functions doing a similar job but with different parameter lists or return formats. `compute_manhattan_path` takes two parameters and excludes the start from its output; `compute_dijkstra_path` takes three and includes it. Neither is wrong -- they just don't line up automatically.
- **Dispatch function**: A small function whose only job is to decide which of several other functions to call, and to smooth over their differences so the caller doesn't have to know about them. `compute_path(algorithm, position, destination, blocked)` is a dispatch function.
- **Regression testing**: Running your existing tests after making a change to ensure the change did not break anything that was previously working.

## Materials Required
- Computers with Python and Thonny (or preferred IDE)
- Completed Dijkstra functions from Lessons 4-5 (`dijkstra.py`)
- `compute_manhattan_path` from Module 4
- `drive_path` and the driving toolkit from Module 4 Lesson 8
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
   - "Our robot is the same. We built the Dijkstra functions, but we haven't proven they work yet. Today we test them -- and then we make it possible to switch between Manhattan and Dijkstra with a single argument."

2. **What Makes a Good Test?**
   - A good test has:
     - **Known input**: A specific grid size, blocked list, start, and destination
     - **Expected output**: The path you calculated by hand (or know from Manhattan distance)
     - **A check**: Code that compares the actual output to the expected output
   - "We'll write tests for two scenarios: grids with NO obstacles (where Dijkstra's step count should match Manhattan's) and grids WITH obstacles (where Dijkstra should find a detour)."

3. **The Shape Mismatch**
   - Write on the board:
     ```
     compute_manhattan_path(position, destination)         -> path, start NOT included
     compute_dijkstra_path(position, destination, graph)   -> path, start included
     ```
   - "These aren't quite interchangeable. Dijkstra needs a graph. And if you compare `len()` of the two outputs directly, you'll be off by one -- that's not a bug, it's just two different design choices that happened to land differently."
   - "So how do we make the rest of our program not care about this difference?"

### Guided Practice (15 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 20 min

1. **Test 1: No Obstacles -- Step Count Should Match Manhattan**
   - Walk through writing the test together:
     ```python
     graph = build_dijkstra_graph(4, 4, [])
     path = compute_dijkstra_path((0, 0), (3, 3), graph)
     print("Path:", path)
     print("Path length:", len(path) - 1, "steps")   # -1 because Dijkstra includes the start
     print("Expected steps (Manhattan distance):", 6)
     ```
   - Run the code. The path length should equal the Manhattan distance: |3-0| + |3-0| = 6.
   - Note: The exact path may differ from Manhattan's path (Dijkstra might go a different route of the same length), but the NUMBER of steps must be the same.
   - Ask: "Why do we check the number of steps and not the exact path?" (Because there can be multiple shortest paths of the same length.)

2. **Test 2: Blocked Node -- Dijkstra Should Reroute**
   - Add a blocked node and test again:
     ```python
     graph_blocked = build_dijkstra_graph(4, 4, [(1, 0)])
     path_blocked = compute_dijkstra_path((0, 0), (3, 0), graph_blocked)
     print("Path with (1,0) blocked:", path_blocked)
     print("Path length:", len(path_blocked) - 1, "steps")
     print("Manhattan distance (no obstacles):", 3)
     ```
   - Run the code. The path should avoid (1, 0) entirely. The path length should be longer than the Manhattan distance of 3.

3. **Building the Dispatch Function**
   - "Here's the trick: write one function that hides both algorithms' quirks behind a single, consistent call."
     ```python
     def compute_path(algorithm, position, destination, blocked):
         """Compute a path using the named algorithm.

         algorithm:   "manhattan" or "dijkstra"
         position:    (row, col) tuple, current position
         destination: (row, col) tuple, target
         blocked:     list of blocked (row, col) tuples (ignored by manhattan)

         Returns a list of (row, col) tuples, NOT including position,
         no matter which algorithm computed it.
         """
         if algorithm == "manhattan":
             return compute_manhattan_path(position, destination)
         else:
             graph = build_dijkstra_graph(4, 4, blocked)
             path = compute_dijkstra_path(position, destination, graph)
             return path[1:]  # drop the start position to match Manhattan's shape
     ```
   - Walk through what it does: picks the right underlying function, and for Dijkstra, slices off the first element (`path[1:]`) so both branches return the *same shape* of result.
   - "Now the rest of our program -- especially `drive_path()` -- only ever calls `compute_path(...)`. It never touches `compute_manhattan_path` or `compute_dijkstra_path` directly, so it doesn't need to know their differences exist."

4. **The Swap: One Argument, Not a Rewrite**
   - Show the Module 4 navigation program (simplified):
     ```python
     # Using Manhattan
     path = compute_path("manhattan", position, dest, [])
     ```
   - Now change ONE argument:
     ```python
     # Using Dijkstra
     path = compute_path("dijkstra", position, dest, blocked)
     ```
   - "That's it. Everything downstream -- `drive_path(path, position, heading)` -- is completely unaware which algorithm ran."

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
  5. Start and destination are the same -- verify path is `[start]`
- For each test, print "PASS" or "FAIL" with a description

**Exercise 2: Side-by-Side Comparison**
- Goal: Run both algorithms through `compute_path()` on the same inputs and compare
- Steps:
  1. Test 3 different position/destination pairs on a clear 4x4 grid
  2. Call `compute_path("manhattan", ...)` and `compute_path("dijkstra", ..., blocked=[])` for each
  3. Print both paths and their lengths (`len(path)` for both now, since the dispatch function normalizes the shape!) side-by-side
  4. Verify that on a clear grid, both produce paths of the same length
- Key question: Are the paths always identical? Why or why not?

**Exercise 3: The One-Argument Swap**
- Goal: Modify your Module 4 navigation program to use Dijkstra
- Steps:
  1. Copy your Module 4 main program file
  2. Add the `compute_path()` dispatch function and `dijkstra.py`'s two functions
  3. Change every `compute_manhattan_path(position, dest)` call to `compute_path("dijkstra", position, dest, blocked)`
  4. Run the program on the robot -- it should behave identically on a clear grid
  5. Now add a blocked node and run again -- the robot should detour around it
- Reflection: How many lines did you change? Why did so few changes work?

**Exercise 4: Challenge -- Automated Pass/Fail Testing**
- Goal: Write a test function that automatically checks results
- Create a function:
  ```python
  def test_path(name, algorithm, position, dest, blocked):
      path = compute_path(algorithm, position, dest, blocked)
      # Check 1: path ends at dest
      # Check 2: no blocked nodes in path
      # Check 3: each step moves to an adjacent node
      # Print PASS or FAIL for each check
  ```
- Run it with at least 3 different test scenarios, for both algorithms

### Assessment

**Formative (during lesson)**:
- Can students write a test case with known inputs and expected outputs?
- Can students explain why Dijkstra's path length matches Manhattan distance on a clear grid?
- Can students explain what `compute_path()`'s dispatch function is hiding from its caller?
- Can students identify the one line that needs to change to swap algorithms?
- Can students predict what will happen when `drive_path()` receives a Dijkstra-computed path?

**Summative (worksheet/exit ticket)**:
1. Write a test case that verifies Dijkstra finds a path of length 4 from (0,0) to (2,2) on a 3x3 grid with no obstacles.
2. If (1,1) is blocked on a 3x3 grid, what is the shortest path from (0,0) to (2,2)? How many steps? Write a test case that checks this.
3. What line of code do you change to swap Manhattan for Dijkstra using the dispatch function? Write both the old and new versions.
4. Why does the dispatch function need to slice off the first element of Dijkstra's path (`path[1:]`) but not Manhattan's?
5. What would happen to `drive_path()` if the dispatch function did NOT normalize the two algorithms' path shapes?

## Common Misconceptions

| Misconception | Reality |
|---|---|
| "Dijkstra and Manhattan should return the exact same path on a clear grid" | They should return paths of the same LENGTH, but the exact route may differ. There are often multiple shortest paths between two points, and the two algorithms may choose differently. |
| "Testing means running the program and seeing if it looks right" | Testing means comparing actual output to a specific expected result. Visual inspection misses subtle bugs. Automated checks catch errors reliably. |
| "The swap works because Dijkstra is better than Manhattan" | The swap works because the dispatch function normalizes their differences. Quality does not matter for swappability; a consistent call shape does. |
| "compute_manhattan_path and compute_dijkstra_path could always be swapped directly, with no dispatch function" | Not quite -- they take different numbers of parameters and return differently-shaped results. That's exactly why the dispatch function exists: to paper over those differences in one place instead of every call site. |
| "If all tests pass, the code is bug-free" | Passing tests means the code works for the cases you tested. There may be edge cases you did not think of. More tests give more confidence, but testing can never prove the complete absence of bugs. |

## Differentiation

**For struggling students**:
- Provide a test template with blanks to fill in (the inputs and expected values) rather than writing tests from scratch
- Start with the simplest possible test: a 2x2 grid, no obstacles, (0,0) to (1,1) -- the path should be 2 steps
- Walk through the dispatch function step-by-step: first show it calling Manhattan, then show it calling Dijkstra, then run and compare
- Use a checklist: (1) write the input, (2) calculate the expected output by hand, (3) run the code, (4) compare
- Pair with a partner for the side-by-side comparison exercise

**For advanced students**:
- Write a function that generates random blocked lists and tests Dijkstra on them, checking that no blocked node appears in any path
- Add timing to tests: how long does Dijkstra take vs. Manhattan on larger grids? (Use `import time`)
- Create a test that verifies Dijkstra's path is actually the SHORTEST path (not just a valid path) by checking that no shorter path exists
- Write tests for edge cases: What if the start is blocked? What if the destination is blocked? What if all paths are blocked?
- Work through the Optional Extension below and compare it to the dispatch-function approach

## Materials & Code Examples

### Test Program: Comparing Manhattan and Dijkstra
```python
test_cases = [
    ((0, 0), (3, 3), "Corner to corner"),
    ((0, 0), (0, 3), "Top-left to top-right"),
    ((1, 1), (3, 2), "Interior to edge"),
]

print("=" * 60)
print("COMPARISON: Manhattan vs. Dijkstra (no obstacles)")
print("=" * 60)

for position, dest, description in test_cases:
    m_path = compute_path("manhattan", position, dest, [])
    d_path = compute_path("dijkstra", position, dest, [])

    print(f"\nTest: {description}")
    print(f"  Position: {position}  Destination: {dest}")
    print(f"  Manhattan path: {m_path}  ({len(m_path)} steps)")
    print(f"  Dijkstra path:  {d_path}  ({len(d_path)} steps)")

    if len(m_path) == len(d_path):
        print(f"  PASS: Both produce {len(m_path)}-step paths")
    else:
        print(f"  FAIL: Step counts differ!")
```

### The Dispatch Function
```python
def compute_path(algorithm, position, destination, blocked):
    """Compute a path using the named algorithm. Always returns a path
    NOT including position, regardless of which algorithm ran."""
    if algorithm == "manhattan":
        return compute_manhattan_path(position, destination)
    else:
        graph = build_dijkstra_graph(4, 4, blocked)
        path = compute_dijkstra_path(position, destination, graph)
        return path[1:]
```

### The One-Argument Swap
```python
# ========================================
# BEFORE (Module 4 style -- Manhattan only)
# ========================================
path = compute_manhattan_path(position, dest)
position, heading = drive_path(path, position, heading)


# ========================================
# AFTER (Module 5 -- either algorithm via one argument)
# ========================================
path = compute_path("dijkstra", position, dest, blocked)   # <- only this line changed
position, heading = drive_path(path, position, heading)
```

### Automated Test Function (Challenge Exercise)
```python
def test_path(name, algorithm, position, dest, blocked):
    """Run a series of checks on a computed path."""
    print(f"\n--- {name} ---")
    path = compute_path(algorithm, position, dest, blocked)
    print(f"  Path: {path}")
    passed = 0
    total = 3

    # Check 1: Path ends at destination
    if (len(path) == 0 and position == dest) or (len(path) > 0 and path[-1] == dest):
        print(f"  PASS: Ends at {dest}")
        passed += 1
    else:
        print(f"  FAIL: Should end at {dest}")

    # Check 2: No blocked nodes in path
    blocked_found = [n for n in path if n in blocked]
    if len(blocked_found) == 0:
        print(f"  PASS: No blocked nodes in path")
        passed += 1
    else:
        print(f"  FAIL: Blocked nodes in path: {blocked_found}")

    # Check 3: Each step is to an adjacent node (from position, then along path)
    trace = [position] + path
    all_ok = True
    for i in range(len(trace) - 1):
        r1, c1 = trace[i]
        r2, c2 = trace[i + 1]
        if abs(r1 - r2) + abs(c1 - c2) != 1:
            print(f"  FAIL: Non-adjacent step {trace[i]} -> {trace[i+1]}")
            all_ok = False
            break
    if all_ok:
        print(f"  PASS: All steps adjacent")
        passed += 1

    print(f"  Result: {passed}/{total} checks passed")
    return passed == total


# Run the tests
blocked = [(1, 0), (2, 2)]
test_path("Short path, no obstacle in way", "dijkstra", (0, 0), (0, 3), blocked)
test_path("Path must reroute around (1,0)", "dijkstra", (0, 0), (3, 0), blocked)
test_path("Manhattan, same inputs", "manhattan", (0, 0), (0, 3), blocked)
```

## Teaching Notes
- **This lesson is the payoff for good design -- with an honest twist.** Students spent Lessons 4-5 building the Dijkstra functions. Now they discover the two algorithms don't line up perfectly, and they build the dispatch function to fix that in one place. Make the swap moment dramatic -- show the old code, make the change live, and run it.
- **Don't hide the shape mismatch -- it's the actual lesson.** Some students may expect Dijkstra to be a drop-in replacement automatically. Naming the mismatch explicitly (extra `graph` parameter, extra start-position in the output) and showing how the dispatch function papers over it is more honest, and more useful, than pretending it doesn't exist.
- **Spend time on testing before the swap.** Students are often eager to get to the "cool part" (the swap), but testing teaches a critical skill. Emphasize that professional software developers spend as much time testing as they do writing code.
- **Let students discover that paths can differ.** When Manhattan and Dijkstra return different paths of the same length, use this as a teaching moment: there are often multiple correct answers, and different algorithms may find different ones. What matters is that the path length is optimal.
- **Connect to real-world examples.** USB-C is a shared interface -- many different devices use the same connector, sometimes through an adapter. The dispatch function is like that adapter: it lets two things that don't quite match work together anyway.
- **Save test files.** Students will reuse their test cases in Lessons 7-8 when they add obstacle detection, and again in the capstone (Lesson 9).

## Connections to Next Lessons
- **Lesson 7** will add **obstacle detection** using the XRP rangefinder sensor. Instead of pre-programming the blocked list, the robot will discover obstacles during navigation and feed them to `compute_path("dijkstra", ...)` for real-time rerouting.
- **Lesson 8** will introduce **obstacle memory** -- saving discovered obstacles between runs so the robot improves over time.
- **Lesson 9** (Capstone) will combine everything into a complete autonomous navigation system.
- The interface-mismatch problem introduced here applies broadly in programming -- students will encounter it again whenever they connect two libraries or components that were built independently.

---

## Optional Extension: True Polymorphism with Classes

*For courses that also cover classes/objects. Skip this section entirely otherwise; nothing later in the course depends on it.*

### The Payoff
The dispatch function works, but it's still one function with an if/else inside -- every time a new algorithm gets added, `compute_path()` itself has to grow another branch. Classes solve the shape-mismatch problem differently: instead of normalizing the *call*, you design both classes to have an **identical method signature** from the start, so no dispatch function is needed at all.

```python
class Manhattan:
    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        # ... (from Module 4)
        ...

class Dijkstra:
    def __init__(self, start, blocked):
        self.position = start
        self.blocked = blocked
        self.graph = self.build_graph()

    def build_graph(self):
        ...

    def compute_path(self, destination):
        # ... (from this module's Optional Extensions)
        ...
```

Both classes have a `compute_path(destination)` method -- same name, same single parameter, same return type. This shared shape is called a **shared interface**, and code that uses it gets **polymorphism**: the ability to swap one object for another without changing the code that uses it, because both objects respond to the same calls.

```python
# Using Manhattan
pathfinder = Manhattan((0, 0))

# Using Dijkstra -- literally just this one line changes
pathfinder = Dijkstra((0, 0), blocked)

# Everything below is IDENTICAL for either pathfinder:
path = pathfinder.compute_path(dest)
```

Unlike the functions version, `Navigator.drive_path()` never needs to know which class `pathfinder` is -- it just calls `.compute_path()` and trusts whatever comes back. No dispatch function, no `if algorithm == "manhattan"` anywhere.

### Discussion Prompt
"The functions version needed `path[1:]` inside the dispatch function to normalize Dijkstra's output. Does the classes version have that problem?" (It still does, if `Dijkstra.compute_path()`'s reconstruction includes the start position the same way -- classes don't automatically fix an interface mismatch in *return values*, only in *how you call things*. A careful class design would still need `Dijkstra.compute_path()` to slice off the start position internally, to genuinely match `Manhattan.compute_path()`'s behavior.)

### Worksheet
See the "Optional Extension" section at the end of the Lesson 6 worksheet for matching exercises.
