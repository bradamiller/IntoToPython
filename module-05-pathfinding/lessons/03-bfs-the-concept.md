# Lesson 3: Breadth-First Search — The Concept

## Overview
Students discover, on paper, a method for finding the shortest path around blocked intersections that is precise enough for a computer to follow. In Lesson 1 they found such paths by looking at the whole grid and guessing; this lesson turns that intuition into an algorithm. The method is breadth-first search (BFS), taught as *ripples*: write 0 on the start, 1 on every intersection one step away, 2 on every new intersection one step from a 1, and so on. The first number written on the destination is the length of the shortest path, and if students also note *where they came from* each time they write a number, they can walk the numbers back down to the start and read off the path itself.

This is a paper-and-pencil lesson. No code is written, but students run one program at the end: the Lesson 3 trace program prints the same ring numbers on the same grid, so they can check their paper against the computer's. The hand traces from this lesson become the test cases for Lesson 5, where they implement the same method as `compute_bfs_path()`.

Students already understand graphs (Lesson 1) and can represent them as dictionaries (Lesson 2). The two things that are new here are the ripple order (always finish one ring before starting the next) and the `previous` record (write down where you came from). Those two ideas are the whole algorithm.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain why "look at the grid and guess" is not a method a computer can use
- Number every intersection of a small grid with its distance from the start, one ring at a time, around blocked intersections
- Explain why the first number written on the destination is the shortest path length
- Record, for each intersection, which intersection it was reached from
- Walk the `previous` record back from the destination to the start and write out the path (the intersections to drive *to*, not including the start)
- Recognize that more than one path can be shortest, and that any of them is correct
- Compare their paper rings with the program's `print_grid()` output

## Key Concepts
- **Breadth-first search (BFS)**: Explore outward from the start one step at a time -- every intersection one step away, then every new intersection two steps away, and so on -- until the destination is reached. Because every ring is exactly one step further than the last, the destination is reached by a shortest path the first time it is reached.
- **Ring number**: The number written on an intersection: how many steps it is from the start. The start is ring 0.
- **Reached**: An intersection has been *reached* once it has a ring number. It never gets a second one. (In code, "reached" means "is a key in `previous`".)
- **`previous`**: For every reached intersection, the intersection it was reached *from*. The start's previous is nothing. This is what turns a table of numbers into an actual path.
- **Walk-back**: Start at the destination, look up its previous, then that one's previous, and so on until you reach the start. Written in that order the list is backwards; flipped, it is the path. The start itself is not part of the path, because the robot is already there.
- **To-visit list**: The ring you are currently working on, oldest first. Taking the *oldest* intersection off the list each time is what makes the search go ring by ring. (Lesson 5 names this list `to_visit`.)

## Materials Required
- Printed worksheet (3x3 and 4x4 grids with blocked intersections; "came from" tables)
- Pencils, erasers; two colors help (one for ring numbers, one for the walk-back)
- Whiteboard or projector with a large grid drawn on it
- Computers with the Lesson 3 trace program (`code/starter/lesson-03-bfs-concept.py`) for the last 10 minutes -- no robot needed

## Lesson Flow

### Introduction (10 minutes)
**For 50-min classes:** 8 min
**For 3-hour sessions:** 12 min

1. **Hook: explain your method to a computer**
   - Put the Lesson 1 obstacle grid on the board (4x4, two or three blocked intersections). "You found the way around this in Lesson 1. How did you do it?"
   - Collect answers. They will be some version of "I looked at it." Press: "Write down your rule so that someone who can't see the whole grid at once -- a computer, which only ever sees one intersection and its neighbors -- could follow it and always get the shortest path."
   - Let students try for two minutes. Most rules will be Manhattan-with-patches ("go toward the goal, and if it's blocked go around"). Show one grid where that fails: a wall across the direct route that forces the robot to go *away* from the destination first (the worksheet's Part C grid).
   - "So we need a method that doesn't need to see the whole grid, never guesses, and still always finds a shortest path. There is one, and you can run it with a pencil."

2. **The idea: ripples**
   - On the board grid (3x3, nothing blocked yet), write **0** on the start. "Every intersection you can reach in one step gets a **1**." Write them. "Every intersection you can reach from a 1 that doesn't have a number yet gets a **2**." Write them. Keep going.
   - Ask: "What is the number on the destination?" "What does that number mean?" (Its distance from the start, in steps.) "Could there be a shorter path we missed?" Let students argue it out: every ring is one step further than the last, so nothing with a 3 on it can be reached in 2 steps.
   - Name it: **breadth-first search**. "Breadth" because it goes wide (the whole ring) before it goes deep.

### Guided Practice (15 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

1. **Rings around a wall**
   - Block the center of the 3x3 on the board: (1,1) gets an X. Start at (0,0), destination (2,2).
   - Trace together, saying the rule out loud each time: "Take the oldest numbered intersection we haven't looked around yet. Give each of its neighbors that has no number the next number."
   - Keep a running **to-visit** list on the side of the board: add an intersection when it gets its number, cross it off when you have looked around it. Students see that the list is a queue: things come off the front in the order they went on.
   - The result (see Materials below): 0 at (0,0); 1 at (0,1),(1,0); 2 at (0,2),(2,0); 3 at (1,2),(2,1); 4 at (2,2). Note that (1,1) is an X and never gets a number; nothing passes through it.

2. **Where did I come from?**
   - "The number tells us *how far*. It doesn't tell us *which way*. Let's fix that." Trace again, and this time, every time you write a number on an intersection, also write a tiny arrow back toward the intersection you came from (or fill in the "came from" table on the worksheet).
   - "Now start at the destination and follow the arrows backwards." (2,2) came from (2,1), which came from (2,0), which came from (1,0), which came from (0,0). Stop at the start.
   - Written forward: (1,0), (2,0), (2,1), (2,2). "Those are the intersections the robot drives *to*. The start isn't in the list because the robot is already standing on it." Students met this convention in Module 4 -- `compute_manhattan_path` also leaves the start out.

3. **More than one right answer**
   - Point at (2,2). It has two neighbors with a 3: (1,2) and (2,1). "Which one did we write down as 'came from'?" Whichever was looked around first -- which depends on the order neighbors were listed. "If a classmate got (0,1), (0,2), (1,2), (2,2), are they wrong?" No. Both have 4 steps; both are shortest. This matters in Lesson 6, where the tests check *properties* of a path rather than one expected list.

### Independent Practice (20 minutes)
**For 50-min classes:** 15 min
**For 3-hour sessions:** 25 min

Students work the worksheet in pairs. Then, for the last 10 minutes, they run the Lesson 3 trace program and compare.

**Exercise 1: 3x3, nothing blocked**, (0,0) to (2,2). Ring numbers and the came-from table. Expected: destination ring 4, several correct paths.

**Exercise 2: 3x3 with (1,1) blocked**, (0,0) to (2,2). The guided example, done solo. Expected: ring 4 again -- the wall in the middle doesn't lengthen the trip, which surprises some students.

**Exercise 3: 4x4 with a wall at (1,0) and (1,1)**, (0,0) to (3,0). The robot must go *away* from the destination first. Expected: destination ring 7; path (0,1), (0,2), (1,2), (2,2), (3,2), (3,1), (3,0) or the equivalent through (2,1)/(2,0)... students check with the program.

**Exercise 4: walled off.** 4x4 with (1,0), (1,1), (1,2), (1,3) all blocked, (0,0) to (3,0). Expected: the rings stop at row 0; the destination never gets a number. "What should the program return when that happens?" (An empty path -- Lesson 5.)

**Run the program.** `code/starter/lesson-03-bfs-concept.py` prints each step of the 3x3-with-(1,1)-blocked trace, then draws the grid with `print_grid()`. Students compare the printed rings with Exercise 2 and the printed path with their walk-back. If the path differs but the number of steps matches, that is Exercise 3's lesson again.

### Assessment

**Formative (during lesson)**:
- Can students say the rule in their own words? ("Oldest first; every unnumbered neighbor gets the next number.")
- Watch for students numbering a ring-2 intersection before all the ring-1 intersections are done -- the most common error, and the one that breaks the "first number is shortest" guarantee.
- Can students explain *why* the destination's number is the shortest path length?

**Summative (worksheet/exit ticket)**:
- Exercises 1-3 fully numbered with correct came-from tables and a correct walk-back
- Exit ticket: "An intersection already has a 2 on it. You reach it again from a 3. What do you write?" (Nothing. It keeps its 2. An intersection is numbered once.)

## Common Misconceptions
- **"I'll number the ones closest to the destination first."** That is a different (and wrong) algorithm. BFS pays no attention to where the destination is until it arrives there; that is exactly why it cannot be fooled by a wall that forces a detour.
- **"An intersection can get a smaller number later."** Not in BFS. Because rings are done in order, the first number written is always the smallest possible. (In Module 6, with slow segments, this stops being true -- which is the whole reason Dijkstra's algorithm exists.)
- **"The path includes the start."** The robot is already there. The path is the list of intersections to drive *to*. Students who include the start will get `len(path)` off by one in Lesson 5.
- **"There is one right path."** On an open grid there are usually many. The number of steps is what is unique.
- **"The blocked intersection gets a big number."** It gets no number at all. It is not in the graph (Lesson 2), so it is never anyone's neighbor.

## Differentiation
**For struggling students**: Trace with physical tokens on a large printed grid, one ring at a time, saying the number out loud. Do Exercises 1 and 2 only. Skip the came-from table at first and add it on the second pass.

**For advanced students**: Exercise 4 plus: "Write the rule as numbered steps precise enough to hand to a classmate who has never seen it." Then: "Where in your steps does the queue (oldest first) matter? What would go wrong with newest first?" (Depth-first search; it still finds *a* path but not necessarily a shortest one.) Students who get there have written Lesson 5's function in English.

## Materials & Code Examples

### Worked trace: 3x3, (1,1) blocked, (0,0) to (2,2)

Neighbors are listed in the order the code uses: up, down, left, right.

| Step | Looking around | Ring | New intersections reached (came from) | To-visit after |
|---|---|---|---|---|
| start | -- | -- | (0,0): 0 (nothing) | (0,0) |
| 1 | (0,0) | 0 | (1,0): 1 from (0,0); (0,1): 1 from (0,0) | (1,0), (0,1) |
| 2 | (1,0) | 1 | (2,0): 2 from (1,0) | (0,1), (2,0) |
| 3 | (0,1) | 1 | (0,2): 2 from (0,1) | (2,0), (0,2) |
| 4 | (2,0) | 2 | (2,1): 3 from (2,0) | (0,2), (2,1) |
| 5 | (0,2) | 2 | (1,2): 3 from (0,2) | (2,1), (1,2) |
| 6 | (2,1) | 3 | (2,2): 4 from (2,1) | (1,2), (2,2) |
| 7 | (1,2) | 3 | nothing new | (2,2) |
| 8 | (2,2) | 4 | destination reached -- stop | |

Grid of ring numbers (what `print_grid()` draws):

```
      0  1  2
    ----------
 0 |  0  1  2
 1 |  1  X  3
 2 |  2  3  4
```

Walk-back: (2,2) <- (2,1) <- (2,0) <- (1,0) <- (0,0). Path, forward, without the start: `[(1, 0), (2, 0), (2, 1), (2, 2)]`. Steps: 4.

### Answer key, Exercise 3 (4x4, wall at (1,0),(1,1), (0,0) to (3,0))

```
      0  1  2  3
    -------------
 0 |  0  1  2  3
 1 |  X  X  3  4
 2 |  6  5  4  5
 3 |  7  6  5  6
```

Destination ring 7. One shortest path: `[(0,1), (0,2), (1,2), (2,2), (3,2), (3,1), (3,0)]`; another: `[(0,1), (0,2), (1,2), (2,2), (2,1), (2,0), (3,0)]`. Both are correct.

### Answer key, Exercise 4 (row 1 all blocked)

```
      0  1  2  3
    -------------
 0 |  0  1  2  3
 1 |  X  X  X  X
 2 |  .  .  .  .
 3 |  .  .  .  .
```

The rings never cross row 1. The destination (3,0) is never reached. The program will return an empty path.

### Preview: what the code will look like (show, do not implement)

```python
previous = {start: None}        # reached intersections, and where from
to_visit = [start]              # the ring being worked on, oldest first

while len(to_visit) > 0:
    current = to_visit.pop(0)           # the OLDEST one
    if current == destination:
        break
    for neighbor in graph[current]:
        if neighbor not in previous:    # never reached before
            previous[neighbor] = current
            to_visit.append(neighbor)
```

"That is the whole search. Every line is something you did with your pencil today. Lesson 5 is where you type it."

## Teaching Notes
- The single most important habit is **finish the ring before starting the next one**. Model it by keeping the to-visit list visible on the board and always taking from the front. Students who skip ahead get wrong answers on Exercise 3 and usually can't see why; the list makes the error visible.
- Resist introducing `distances` or "infinity" here. BFS doesn't need them, and they are exactly the machinery Module 6 adds for a reason. If a student asks about slow roads, say "good question, Module 6" and move on.
- The came-from arrows are easier for most students than a table. Let them draw arrows on the grid; the table is for the worksheet's answer checking.
- The last ten minutes with the program matter: seeing the computer produce *their* numbers is what convinces students that the paper method is the real algorithm.

## Connections to Next Lessons
- **Lesson 4** packages the grid, the blocked list and the graph into a small toolkit of functions (`add_blocked`, `build_graph`), with `compute_bfs_path` as a placeholder.
- **Lesson 5** implements `compute_bfs_path()`: the preview code above, plus the walk-back. The worksheet traces from this lesson are its test cases.
- **Lesson 6** tests it by properties, and swaps it in for Manhattan.
- **Module 6 (optional)** changes exactly two lines of this method to handle segments that are slower than others.
