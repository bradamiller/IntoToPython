# Lesson 6 Slide Outline: Testing and Swapping

## Slide 1: Title & Learning Objectives
**Title:** Testing and Swapping

**Learning Objectives:**
- Test Dijkstra with no blocked nodes and verify it matches Manhattan output
- Test Dijkstra with blocked nodes and verify correct rerouting
- Explain why a shared interface (compute_path returning list of tuples) enables swapping
- Swap Dijkstra into the Module 4 navigation program with minimal code changes

**Agenda:**
- Testing with no obstacles (5 min)
- Testing with obstacles (10 min)
- Shared interface: why it works (10 min)
- Swapping in the Module 4 program (10 min)
- Side-by-side comparison (5 min)
- Practice exercise (10 min)

---

## Slide 2: Hook — The Two-Minute Swap
**Imagine you're a mechanic.** A customer has a car with a flat tire. You could:
- Redesign the entire car to handle flat tires
- OR just swap in a new tire that fits the same wheel

**Our Navigator class is the car. Manhattan and Dijkstra are the tires.**

Because both pathfinders have the same interface — `compute_path` returning a list of tuples — swapping is quick and painless.

**Today:** We'll test Dijkstra thoroughly, then swap it into our Module 4 program. It should take about two minutes.

---

## Slide 3: Test 1 — No Blocked Nodes
**If nothing is blocked, Dijkstra should find a path the same length as Manhattan.**

```python
from manhattan import Manhattan
from dijkstra import Dijkstra

m = Manhattan((0, 0))
d = Dijkstra((0, 0), [])

destinations = [(3, 3), (0, 3), (3, 0), (2, 1)]

for dest in destinations:
    m_path = m.compute_path(dest)
    d_path = d.compute_path(dest)
    print(f"To {dest}:")
    print(f"  Manhattan: {m_path}  ({len(m_path)-1} steps)")
    print(f"  Dijkstra:  {d_path}  ({len(d_path)-1} steps)")
    print(f"  Same length? {len(m_path) == len(d_path)}")
    print()
```

**Expected:** Same number of steps for every destination. The actual nodes in the path may differ, but the length must match.

**Why might the paths differ?** Manhattan always goes rows-first, columns-second. Dijkstra may choose a different shortest path depending on which node it visits first.

---

## Slide 4: Test 2 — With Blocked Nodes
**Now the real test. Block some intersections and see Dijkstra route around them.**

```python
blocked = [(1, 0), (1, 1)]
d = Dijkstra((0, 0), blocked)

path = d.compute_path((3, 0))
print("Path:", path)
print("Steps:", len(path) - 1)
```

**Verify by hand:**
```
(0,0) --- (0,1) --- (0,2) --- (0,3)
                       |         |
                     (1,2) --- (1,3)
  |                    |         |
(2,0) --- (2,1) --- (2,2) --- (2,3)
  |         |         |         |
(3,0) --- (3,1) --- (3,2) --- (3,3)
```

**Check:** Does the path avoid (1,0) and (1,1)? Does it reach (3,0)? Is it the shortest path around the obstacles?

**Try blocking more nodes.** What's the minimum number of blocked nodes that makes (3,3) unreachable from (0,0)?

---

## Slide 5: The Shared Interface
**Both Manhattan and Dijkstra have a `compute_path` method that returns a list of tuples.**

| Feature | Manhattan | Dijkstra |
|---|---|---|
| Constructor | `Manhattan(start)` | `Dijkstra(start, blocked)` |
| Method | `compute_path(dest)` | `compute_path(dest)` |
| Returns | list of tuples | list of tuples |
| Handles obstacles | No | Yes |
| Path format | `[(0,0), (1,0), ...]` | `[(0,0), (0,1), ...]` |

**The Navigator class only cares about:**
1. Calling `compute_path(destination)` on the pathfinder
2. Getting back a list of tuples representing the path

**Navigator doesn't know or care** whether Manhattan or Dijkstra computed the path. This is the power of a shared interface.

---

## Slide 6: Swapping in the Module 4 Program
**Your Module 4 program probably looks something like this:**

```python
from manhattan import Manhattan
from navigator import Navigator

pathfinder = Manhattan((0, 0))
nav = Navigator(pathfinder)

destinations = [(2, 3), (0, 1), (3, 3)]
for dest in destinations:
    nav.go_to(dest)
```

**To swap in Dijkstra, change just two lines:**

```python
from dijkstra import Dijkstra
from navigator import Navigator

pathfinder = Dijkstra((0, 0), [(1, 1), (2, 2)])
nav = Navigator(pathfinder)

destinations = [(2, 3), (0, 1), (3, 3)]
for dest in destinations:
    nav.go_to(dest)
```

**That's it.** The Navigator code, the destination list, and the `go_to` calls all stay exactly the same.

---

## Slide 7: Side-by-Side Comparison
**Running both pathfinders on the same destinations with blocked nodes [(1,1), (2,2)]:**

| Destination | Manhattan Path | Dijkstra Path | Notes |
|---|---|---|---|
| (2, 3) | (0,0)→(1,0)→(2,0)→(2,1)→(2,2)→(2,3) | (0,0)→(0,1)→(0,2)→(0,3)→(1,3)→(2,3) | Manhattan hits blocked (1,1) or (2,2)! |
| (0, 3) | (0,0)→(0,1)→(0,2)→(0,3) | (0,0)→(0,1)→(0,2)→(0,3) | Same — no obstacles on this path |
| (3, 0) | (0,0)→(1,0)→(2,0)→(3,0) | (0,0)→(1,0)→(2,0)→(3,0) | Same — no obstacles on this path |

**Key takeaway:** When obstacles are not in the way, both produce paths of the same length. When obstacles block the Manhattan path, Dijkstra finds a working alternative.

---

## Slide 8: What Navigator Needs from a Pathfinder
**Let's look at how Navigator uses the pathfinder:**

```python
class Navigator:
    def __init__(self, pathfinder):
        self.pathfinder = pathfinder

    def go_to(self, destination):
        path = self.pathfinder.compute_path(destination)
        for i in range(len(path) - 1):
            current = path[i]
            next_node = path[i + 1]
            self.drive_segment(current, next_node)
```

**Navigator calls `self.pathfinder.compute_path(destination)` and expects a list of tuples back.** That's the entire contract.

- Manhattan fulfills this contract
- Dijkstra fulfills this contract
- Any future pathfinder that returns a list of tuples will also work!

**This is called programming to an interface** — one of the most important ideas in software design.

---

## Slide 9: Handling Edge Cases
**What should we test beyond the happy path?**

| Test Case | Expected Behavior |
|---|---|
| Start equals destination | Returns `[start]` — a one-element list |
| Adjacent destination | Returns `[start, dest]` — two elements |
| All nodes blocked except path | Still finds the only available route |
| Destination is blocked | Should handle gracefully (path doesn't exist) |
| Start is blocked | Should handle gracefully (can't begin) |

**Defensive check you can add:**
```python
def compute_path(self, destination):
    if destination not in self.graph:
        print("Destination is blocked or invalid!")
        return []
    # ... rest of algorithm
```

**Good programmers test the unusual cases, not just the obvious ones.**

---

## Slide 10: Your Turn!
**Activity: Swap Dijkstra into Your Module 4 Program**

1. Make a copy of your Module 4 navigation program
2. Replace Manhattan with Dijkstra:
   - Change the import statement
   - Change the constructor call, adding a blocked list
3. Test with **no blocked nodes** — verify the robot visits all destinations correctly
4. Test with **blocked nodes** — verify the robot takes alternate routes
5. Try these scenarios:
   - Block one intersection on the direct path
   - Block two adjacent intersections to force a longer detour
   - Block intersections that don't affect any paths (should make no difference)

**Checkpoints:**
- Did you only need to change 2 lines of code to swap pathfinders?
- Does the robot still visit all destinations correctly?
- With blocked nodes, does the robot avoid those intersections?
- Do both pathfinders produce the same results when nothing is blocked?

---

## Slide 11: Connection to Next Lesson
**What you did today:**
- Tested Dijkstra with and without obstacles
- Verified that Dijkstra matches Manhattan when no obstacles exist
- Swapped Dijkstra into the Module 4 program with minimal changes
- Understood why a shared interface makes swapping easy

**Next lesson (Lesson 7):**
- Use the XRP robot's **ultrasonic rangefinder** to detect real obstacles
- Read distance measurements from the sensor
- Decide when to treat an intersection as blocked

**Key insight:** Right now, we hard-code the blocked list. Next lesson, the robot will discover blocked intersections on its own using its rangefinder sensor.
