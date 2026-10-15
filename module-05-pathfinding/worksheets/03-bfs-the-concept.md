# Lesson 3 Worksheet: Breadth-First Search — The Concept

**Name:** ________________________
**Date:** ________________________

No computer for Parts A–D. You are the computer.

---

## Part A: The rule

In Lesson 1 you found a path around blocked intersections by looking at the whole grid. A computer can't do that: it only ever sees one intersection and its neighbors.

**1.** Here is the method, with blanks. Fill them in.

> Write **0** on the start. Every intersection one step away gets a **___**. Every intersection one step from a 1 that has **no number yet** gets a **___**. Keep going, always finishing one ring before starting the ___________.

**2.** Why is the first number written on the destination the length of the *shortest* path? (One or two sentences.)

_______________________________________________________________

_______________________________________________________________

**3.** An intersection already has a **2** on it. Later you look around an intersection with a **3** on it, and it is a neighbor. What do you write on the 2? ______________

**4.** Blocked intersections get what number? ______________ Why?

_______________________________________________________________

---

## Part B: 3×3, nothing blocked

Start **(0,0)**, destination **(2,2)**. Write a ring number on every intersection. Draw a small arrow on each intersection pointing back to the one you came from.

```
        col 0   col 1   col 2
row 0  [     ] [     ] [     ]

row 1  [     ] [     ] [     ]

row 2  [     ] [     ] [     ]
```

**Came-from table** (fill in as you go; the start's is "none"):

| Intersection | Ring | Came from |
|---|---|---|
| (0,0) | 0 | none |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

**Walk-back.** Start at the destination and follow "came from" until you reach the start:

(2,2) ← ________ ← ________ ← ________ ← (0,0)

**Path**, written forward, *without* the start (the intersections the robot drives *to*):

`[ ________ , ________ , ________ , ________ ]`

**Number of steps:** ______

**5.** A classmate's path is different from yours but also has 4 steps. Are they wrong? ______ Why or why not?

_______________________________________________________________

---

## Part C: 3×3 with (1,1) blocked

Same start and destination. Put an **X** on (1,1) first. It never gets a number and is never anyone's neighbor.

```
        col 0   col 1   col 2
row 0  [     ] [     ] [     ]

row 1  [     ] [  X  ] [     ]

row 2  [     ] [     ] [     ]
```

**To-visit list.** Keep it as you go: add an intersection when it gets its number; cross it off when you have looked around it. Always take the one at the **front**.

_______________________________________________________________

_______________________________________________________________

| Intersection | Ring | Came from |
|---|---|---|
| (0,0) | 0 | none |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

**Walk-back:** (2,2) ← ________ ← ________ ← ________ ← (0,0)

**Path:** `[ ________ , ________ , ________ , ________ ]`   **Steps:** ______

**6.** Compare with Part B. Did the wall in the middle make the trip longer? ______ Why?

_______________________________________________________________

---

## Part D: 4×4 with a wall — the robot has to go the wrong way first

Blocked: **(1,0)** and **(1,1)**. Start **(0,0)**, destination **(3,0)**. The destination is straight down column 0, but the wall is in the way.

```
        col 0   col 1   col 2   col 3
row 0  [     ] [     ] [     ] [     ]

row 1  [  X  ] [  X  ] [     ] [     ]

row 2  [     ] [     ] [     ] [     ]

row 3  [     ] [     ] [     ] [     ]
```

Number every intersection. (You don't have to stop when you reach the destination -- numbering the whole grid is fine, and it makes the picture clearer.)

**Ring number on the destination (3,0):** ______

**One shortest path** (forward, without the start):

`[ ______ , ______ , ______ , ______ , ______ , ______ , ______ ]`

**7.** The first step of your path goes *away* from the destination. Why does BFS get this right when "head toward the goal" would not?

_______________________________________________________________

_______________________________________________________________

---

## Part E: Walled off

Blocked: **(1,0), (1,1), (1,2), (1,3)** -- the whole of row 1. Start **(0,0)**, destination **(3,0)**.

```
        col 0   col 1   col 2   col 3
row 0  [     ] [     ] [     ] [     ]

row 1  [  X  ] [  X  ] [  X  ] [  X  ]

row 2  [     ] [     ] [     ] [     ]

row 3  [     ] [     ] [     ] [     ]
```

**8.** Number what you can. Which intersections never get a number? ________________________________

**9.** The destination was never reached. What should `compute_bfs_path()` return in this case? ______________ (Lesson 5 will make it do that.)

---

## Part F: Check your work with the computer

Run `lesson-03-bfs-concept.py`. It traces Part C step by step and then draws the grid of ring numbers with `print_grid()`.

**10.** Do the printed ring numbers match your Part C grid? ______ If not, which intersection is different, and who is right?

_______________________________________________________________

**11.** Does the printed path match your Part C path exactly? ______ Does it have the same number of steps? ______

**12.** In the printed trace, find the line where the program "ignores" an intersection because it was already reached. Which intersection, and what ring number did it already have?

_______________________________________________________________

---

## Exit ticket

In your own words, in two sentences: what does the number on an intersection mean, and what does "came from" let you do that the number alone does not?

_______________________________________________________________

_______________________________________________________________
