# Lesson 2 Worksheet: Weights in the Graph

**Name:** ________________________
**Date:** ________________________

---

## Part 1: `weight()`

```python
SLOW_EDGES = []

def add_slow_edge(a, b, cost):
    SLOW_EDGES.append((a, b, cost))

def weight(a, b):
    for (x, y, cost) in SLOW_EDGES:
        if (a == x and b == y) or (a == y and b == x):
            return cost
    return 1
```

After `add_slow_edge((0, 1), (0, 2), 5)`:

| Call | Returns |
|---|---|
| `weight((0, 1), (0, 2))` | ______ |
| `weight((0, 2), (0, 1))` | ______ |
| `weight((1, 1), (1, 2))` | ______ |
| `weight((0, 1), (1, 1))` | ______ |

1. Your partner deletes `or (a == y and b == x)`. Which row of the table changes, and what would that do to a robot driving the segment westward?

______________________________________________________________

2. Why does the function end with `return 1`?

______________________________________________________________

## Part 2: `path_cost()`

```python
def path_cost(position, path):
    total = 0
    here = position
    for step in path:
        total = total + weight(here, step)
        here = step
    return total
```

Trace `path_cost((0, 0), [(0, 1), (0, 2), (0, 3)])` with the slow edge at 5:

| pass | `here` | `step` | `weight(here, step)` | `total` after |
|---|---|---|---|---|
| 1 | (0, 0) | (0, 1) | ____ | ____ |
| 2 | ______ | ______ | ____ | ____ |
| 3 | ______ | ______ | ____ | ____ |

3. A classmate starts with `here = path[0]`. What does their function return for the same path, and which segment did they lose?

______________________________________________________________

## Part 3: The cost check

```
PASS: open row - cost 3
FAIL: slow row - cost 7 but the cheapest route costs 5
      path: [(0, 1), (0, 2), (0, 3)]
```

4. Where did the number 5 in the FAIL line come from -- the program, or you? Why does that matter?

______________________________________________________________

5. Which of the Module 5 properties (starts next to the start, ends at the destination, every step a neighbor, no step blocked, open-grid length) does this BFS path fail? ______________

6. So, in one sentence, what exactly is BFS's limitation?

______________________________________________________________

## Part 4: Your own slow edge

7. Add a second slow edge: `add_slow_edge(( __ , __ ), ( __ , __ ), ____ )`. Pick a start and destination where it is on the fewest-steps route: from ( __ , __ ) to ( __ , __ ).

8. By hand, the cheapest route is ______________________________ with cost ______. BFS's path costs ______. Does the check pass or fail? ______

## Exit ticket

Why does BFS pass the cost check on the open grid and fail it on the slow one?

______________________________________________________________
