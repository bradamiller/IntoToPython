# Lesson 8 Slide Outline: Building Experience

## Slide 1: Title & Learning Objectives
**Title:** Building Experience

**Learning Objectives:**
- Explain how a robot can "learn" by remembering obstacles across multiple runs
- Save a list of discovered obstacles to a file using Python file I/O
- Load previously discovered obstacles at the start of a new run
- Compare robot performance between a first run and a second run

**Agenda:**
- How does a GPS app learn about traffic? (5 min)
- Run 1 vs. Run 2: the experience advantage (10 min)
- Saving obstacles to a file (10 min)
- Loading obstacles from a file (5 min)
- Comparing performance across runs (10 min)
- Practice exercise (10 min)

---

## Slide 2: Hook — How Does a GPS App Learn About Traffic?
**Question:** "When Waze tells you there's traffic on your usual route, how does it know?"

**Answer:** Other drivers reported it. The app **remembers** what happened before and uses that information for future trips.

**Our robot can do the same thing:**
- Run 1: The robot discovers obstacles it didn't know about
- Run 2: The robot starts with everything it learned in Run 1
- Each run makes the robot smarter

**Today:** We'll make the robot remember obstacles across runs — building experience just like a GPS app.

---

## Slide 3: Run 1 vs. Run 2 — The Experience Advantage
**Run 1: Discovery mode**
- Robot starts with an empty blocked list
- Drives toward destination using the shortest path
- Discovers obstacles along the way
- Reroutes each time — takes extra steps

```
Run 1: blocked_nodes starts as []
  → Discovers (1,1) is blocked → reroutes → 2 extra steps
  → Discovers (2,3) is blocked → reroutes → 3 extra steps
  → Total extra steps from rerouting: 5
```

**Run 2: Experienced mode**
- Robot starts with blocked list from Run 1: `[(1,1), (2,3)]`
- Plans the optimal route from the very beginning
- No surprises, no rerouting needed

```
Run 2: blocked_nodes starts as [(1,1), (2,3)]
  → Plans around both obstacles from the start
  → Takes the shortest possible path immediately
  → Extra steps from rerouting: 0
```

---

## Slide 4: The Strategy — Check, Record, Remember
**At each intersection during a run:**

1. **Check:** Use the rangefinder to look for obstacles
2. **Record:** If obstacle found, add to the blocked list
3. **Remember:** At end of run, save the blocked list to a file

**Between runs:**

4. **Load:** At start of next run, read the saved blocked list from the file
5. **Use:** Pass the loaded list to Dijkstra before computing any paths

```python
# End of Run 1:
save_obstacles(blocked_nodes)  # Write to file

# Start of Run 2:
blocked_nodes = load_obstacles()  # Read from file
pathfinder = Dijkstra((0, 0), blocked_nodes)  # Start smart!
```

---

## Slide 5: Saving Obstacles to a File
**Python can write data to a file that persists after the program ends.**

```python
def save_obstacles(blocked_nodes):
    file = open("obstacles.txt", "w")
    for node in blocked_nodes:
        row = node[0]
        col = node[1]
        file.write(str(row) + "," + str(col) + "\n")
    file.close()
    print(f"Saved {len(blocked_nodes)} obstacles to file")
```

**What the file looks like:**
```
1,1
2,3
0,2
```

**Key concepts:**
| Concept | Explanation |
|---|---|
| `open("obstacles.txt", "w")` | Opens file for writing ("w" = write mode) |
| `file.write(...)` | Writes a string to the file |
| `"\n"` | Newline character — each obstacle on its own line |
| `file.close()` | Closes the file — important! Data may not save without this |

---

## Slide 6: Loading Obstacles from a File
**At the start of a new run, read the saved obstacles back into a list.**

```python
def load_obstacles():
    blocked_nodes = []
    try:
        file = open("obstacles.txt", "r")
        for line in file:
            parts = line.strip().split(",")
            row = int(parts[0])
            col = int(parts[1])
            blocked_nodes.append((row, col))
        file.close()
        print(f"Loaded {len(blocked_nodes)} obstacles from file")
    except FileNotFoundError:
        print("No obstacle file found — starting fresh")
    return blocked_nodes
```

**Key concepts:**
| Concept | Explanation |
|---|---|
| `open("obstacles.txt", "r")` | Opens file for reading ("r" = read mode) |
| `line.strip()` | Removes the newline character from each line |
| `line.split(",")` | Splits "1,3" into ["1", "3"] |
| `int(parts[0])` | Converts string "1" to integer 1 |
| `try / except FileNotFoundError` | Handles the case where no file exists yet (first run) |

---

## Slide 7: The Complete Two-Run Pattern
**Run 1 — Discover and Save:**
```python
from dijkstra import Dijkstra
from XRPLib.rangefinder import Rangefinder

blocked_nodes = load_obstacles()  # Empty on first run
rangefinder = Rangefinder.get_default_rangefinder()
THRESHOLD = 15

current = (0, 0)
destinations = [(2, 3), (3, 1)]

for dest in destinations:
    pathfinder = Dijkstra(current, blocked_nodes)
    path = pathfinder.compute_path(dest)
    # Navigate with obstacle checking...
    # (add newly discovered obstacles to blocked_nodes)
    current = dest

save_obstacles(blocked_nodes)  # Save for next run
print("Run complete! Obstacles saved.")
```

**Run 2 — same program, but load_obstacles returns the saved list!**

The code is identical. The only difference is what `load_obstacles()` returns.

---

## Slide 8: Comparing Performance
**How to measure improvement:**

| Metric | Run 1 | Run 2 |
|---|---|---|
| Starting blocked list | `[]` | `[(1,1), (2,3)]` |
| Times rerouted | 2 | 0 |
| Total intersections visited | 14 | 10 |
| Obstacles discovered during run | 2 | 0 (already known) |
| Path efficiency | Good (with detours) | Optimal (no detours) |

**Tracking steps in code:**
```python
step_count = 0

# Each time the robot moves one intersection:
step_count = step_count + 1

# At the end:
print(f"Total steps this run: {step_count}")
```

**Challenge question:** Will Run 3 be even better than Run 2? (Only if new obstacles appear!)

---

## Slide 9: Your Turn!
**Activity: Add Experience to Your Navigation Program**

1. Write the `save_obstacles` function — saves blocked list to "obstacles.txt"
2. Write the `load_obstacles` function — reads blocked list from "obstacles.txt"
3. Modify your program:
   - At the start: call `load_obstacles()` to get the initial blocked list
   - During the run: detect and add new obstacles (from Lesson 7)
   - At the end: call `save_obstacles()` to save the full list
4. Run the program twice:
   - **Run 1:** Place obstacles on the grid. Watch the robot discover and reroute.
   - **Run 2:** Same obstacles. Watch the robot avoid them from the start.
5. Print the step count for each run and compare

**Checkpoints:**
- Does the obstacles.txt file get created after Run 1?
- Does Run 2 load the correct obstacles from the file?
- Does Run 2 take fewer steps (or equal) compared to Run 1?
- What happens if you delete the obstacles.txt file? (Robot starts fresh)

---

## Slide 10: Edge Cases and Extensions
**What could go wrong?**

| Situation | What Happens | Solution |
|---|---|---|
| File doesn't exist yet | `FileNotFoundError` | Use `try/except` to start with empty list |
| Obstacle was removed between runs | Robot avoids an intersection that is now clear | Periodically re-check known obstacles |
| Same obstacle added twice | Duplicate entries in list | Check `if node not in blocked_nodes` before adding |
| File gets corrupted | `load_obstacles` crashes | Add error handling for bad data |

**Extension ideas:**
- Add a "forget" function that clears the obstacle file
- Record timestamps: when was each obstacle discovered?
- Add a confidence score: obstacle seen on 3 runs = definitely blocked

---

## Slide 11: Connection to Next Lesson
**What you did today:**
- Made the robot remember obstacles across runs using file I/O
- Compared performance between first and subsequent runs
- Saw how experience makes the robot more efficient

**Next lesson (Lesson 9 — Capstone Project):**
- Combine everything: Dijkstra + Navigator + Rangefinder + obstacle memory
- Build a complete autonomous navigation system
- Demonstrate learning across multiple runs
- This is your graduation project!

**Key insight:** The robot doesn't just follow instructions — it builds knowledge over time. This is the foundation of how real autonomous systems learn from experience.
