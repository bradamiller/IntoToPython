# Lesson 5 Worksheet (Optional Extension): Three Planners, One Harness

**Name:** ________________________
**Date:** ________________________

---

## Part 1: The third class

1. List everything `Dijkstra` has that `BFS` does not:

______________________________________________________________

2. Where does the slow-edge list live, and what is the only way anything outside the class can add to it?

______________________________________________________________

3. Fill in the method names every planner class answers to -- the "shape":

`__________________(position, destination)`   `__________________(intersection)`   `__________________()`   `__________________(a, b, cost)`

## Part 2: The empty method

```python
class BFS:
    def add_slow_edge(self, a, b, cost):
        pass
```

4. Why does `BFS` need this method when it never uses weights?

______________________________________________________________

5. What would the harness have to contain if `BFS` did not have it? Write the line:

```python
______________________________________________
```

6. Which Module 5 class already had a method that deliberately does nothing, and why?

______________________________________________________________

## Part 3: The cost check in the class harness

7. The harness calls `planner.add_slow_edge(...)` **and** records the edge in its own list. Why can't it just ask the planner for `planner.weight(a, b)` when adding up a path's cost? (Think about which planner is under test.)

______________________________________________________________

## Part 4: Results

| | Manhattan | BFS | Dijkstra |
|---|---|---|---|
| passed / 7 | ____ | ____ | ____ |
| which tests fail | ______________________ | ______________________ | ______________________ |

8. Each planner fails exactly the tests that describe what it cannot do. Say in one phrase what each cannot do:

Manhattan: ______________________  BFS: ______________________  Dijkstra: ______________________

## Part 5: The word

9. `run_all_tests()` works on three different classes and never names one. What is that property called, and what is the harness written against instead of a class?

______________________________________________________________

## Exit ticket

What would the harness need if `BFS` lacked `add_slow_edge()`?

______________________________________________________________
