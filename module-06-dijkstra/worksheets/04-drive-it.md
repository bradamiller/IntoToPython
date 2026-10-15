# Lesson 4 Worksheet: Drive It

**Team:** ________________________
**Date:** ________________________

---

## Part 1: Before the button

Slow segment typed in: `add_slow_edge(( __ , __ ), ( __ , __ ), ____ )`
Trip: from ( __ , __ ) to ( __ , __ ).  Normal block time (Lesson 1): ______ s

The program printed:

| Planner | steps | cost | path |
|---|---|---|---|
| BFS | ____ | ____ | ______________________________ |
| Dijkstra | ____ | ____ | ______________________________ |

1. Predicted time = cost x normal block time:  BFS ______ s   Dijkstra ______ s

2. Which lines of the program are new since Module 5? ______________________________________________

## Part 2: Two runs

| Planner | predicted s | stopwatch s | program's `elapsed` | turns in the path |
|---|---|---|---|---|
| BFS | ______ | ______ | ______ | ____ |
| Dijkstra | ______ | ______ | ______ | ____ |

3. Which planner's robot arrived first? ______  By how many seconds? ______

4. Was the measured gap bigger or smaller than the predicted gap? ______ What does the "turns" column suggest about why?

______________________________________________________________

## Part 3: Why the driving didn't change

5. `drive_path()` is handed a list. Does it know, or care, which planner made the list? Why not?

______________________________________________________________

6. A team's two plans come out identical. Name two setup mistakes that would cause that.

______________________________________________________________

## Part 4: A second trip

7. Choose a different start and destination where the slow segment is on the fewest-steps route: from ( __ , __ ) to ( __ , __ ). Predict both costs: BFS ______ Dijkstra ______. Run both. Measured: BFS ______ s  Dijkstra ______ s.

## Exit ticket

In one sentence: why did the route with more steps win?

______________________________________________________________
