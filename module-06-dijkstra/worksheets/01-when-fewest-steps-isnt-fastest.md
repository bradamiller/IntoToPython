# Lesson 1 Worksheet: When Fewest Steps Isn't Fastest

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Measure the slow segment

| | Run 1 | Run 2 | Run 3 | Average |
|---|---|---|---|---|
| Normal block (s) | _____ | _____ | _____ | _____ |
| Slow segment (s) | _____ | _____ | _____ | _____ |

**weight = slow average / normal average = _____ / _____ = _____ -> rounded: _____**

1. Why is the weight a ratio and not the number of seconds?

______________________________________________________________

2. The slow segment joins intersections ( __ , __ ) and ( __ , __ ).

## Part 2: Two routes, by hand

4x4 grid, from (0, 0) to (0, 3). Use your measured weight for the slow segment between (0, 1) and (0, 2); every other block is 1.

**Route A (straight along row 0):** (0,0) -> (0,1) -> (0,2) -> (0,3)

cost = ____ + ____ + ____ = ______   steps: ____

**Route B (round through row 1):** (0,0) -> (1,0) -> (1,1) -> (1,2) -> (1,3) -> (0,3)

cost = ____ + ____ + ____ + ____ + ____ = ______   steps: ____

3. Which route has fewer steps? ______  Which is faster? ______

4. Which will `compute_bfs_path()` choose, and why?

______________________________________________________________

## Part 3: The tie

5. Redo Part 2 with the slow segment at weight **3**. Route A cost: ______  Route B cost: ______

6. Why does going round one segment on an open grid always cost exactly 3 blocks?

______________________________________________________________

7. So what is the smallest weight that makes the detour strictly better? ______

## Part 4: Another trip

From (0, 1) to (0, 2) -- the two ends of the slow segment themselves.

8. Direct: cost ______ (____ step).  Round through row 1: (0,1) -> (1,1) -> (1,2) -> (0,2): cost ______ (____ steps).

9. With your measured weight, which is faster? ______

10. From (3, 0) to (3, 3) -- a trip along row 3. Does the slow segment matter at all? Why?

______________________________________________________________

## Exit ticket

Weight 4, from (0, 0) to (0, 3): Route A costs ______, Route B costs ______, so the faster route is ______.
