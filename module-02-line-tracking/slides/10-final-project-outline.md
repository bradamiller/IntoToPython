# Lesson 10 Slide Outline: Module 2 Final Project

## Slide 1: Title & Learning Objectives
**Title:** Module 2 Final Project

**Learning Objectives:**
- Integrate the sensor and driving toolkits into a complete program
- Write a main program that follows the circle and reverses at the cross
- Test, debug, and refine a working robot program
- Present and reflect on your work

**Agenda:**
- Project overview & requirements (10 min)
- Planning (15 min)
- Implementation & testing (30 min)
- Demo & reflection (15 min)

---

## Slide 2: Module 2 Journey
**Your progress:**
1. Lesson 1: Read sensors ✓
2. Lesson 2: while loops — drive to edge ✓
3. Lesson 3: if/else — bounce driving ✓
4. Lesson 4: import random — random turns ✓
5. Lesson 5: Proportional control ✓
6. Lesson 6: Two-sensor line following ✓
7. Lesson 7: Intersection detection ✓
8. Lesson 8: Sensor functions toolkit ✓
9. Lesson 9: Driving functions toolkit ✓
10. **Today: Put it ALL together!**

---

## Slide 3: Project Requirements
**The robot must:**
1. Follow the taped circle
2. Detect the cross intersection
3. Turn around (reverse direction)
4. Continue following
5. Repeat for **4 total reversals**
6. Stop and print a completion message

**Code must:**
- Use the sensor and driving toolkit functions
- Include print statements showing progress
- Be organized and commented

---

## Slide 4: Project Options
**Option A: Standard (Recommended)**
- Follow → detect → reverse → repeat 4 times → stop
- Use existing toolkit functions without modification

**Option B: Enhanced**
- Option A plus: add `turn_around()` function, timing prints, LED feedback

**Option C: Advanced**
- Option A plus: off-line recovery, variable speed, creative additions

---

## Slide 5: The Main Program
```python
board = Board.get_default_board()

board.wait_for_button()
print("Starting!")

for i in range(4):
    print("Leg", i + 1, "- Following...")
    track_until_cross()
    print("Cross! Reversing...")
    turn_right()
    turn_right()

print("Done! 4 reversals complete.")
```

**The power of organized toolkits:** The main program is just 10 lines!

---

## Slide 6: Testing Strategy
**Test incrementally:**

| Test | What to Check |
|---|---|
| Test 1 | Does `track_until_cross()` follow to the cross? |
| Test 2 | Does the turn-around work? |
| Test 3 | Does 1 full reversal work? |
| Test 4 | Do all 4 reversals complete? |

**If something fails:** Add print statements, check `THRESHOLD`, adjust parameters.

---

## Slide 7: Common Issues & Fixes

| Problem | Fix |
|---|---|
| Robot doesn't detect cross | Adjust `THRESHOLD`, widen tape cross |
| Robot loses line after turn | Check `clear_intersection()`'s 8 cm against your robot |
| Robot goes wrong way after turn | Try `turn_left()` instead of `turn_right()` |
| Robot oscillates on the line | Reduce `KP` value |
| Robot is too slow/fast | Adjust `BASE_EFFORT` |

---

## Slide 8: Rubric (50 points)
| Category | Points |
|---|---|
| Code organization (toolkits correct) | 10 |
| Line following works | 5 |
| Cross detection works | 5 |
| Reversal works | 5 |
| Completes 4 reversals | 5 |
| Testing evidence (prints) | 6 |
| Debugging process | 4 |
| Demo works | 4 |
| Code explanation | 3 |
| Reflection | 3 |
| **Total** | **50** |

---

## Slide 9: Build Time!
**Steps:**
1. Verify the sensor and driving toolkits work
2. Write main program
3. Test incrementally (1 reversal → 4 reversals)
4. Debug and tune
5. Prepare for demo

**Ask for help if stuck — debugging is part of the process!**

---

## Slide 10: Looking Ahead — Module 3
**What you've built:**
- Reusable sensor and driving function toolkits
- Skills: loops, conditionals, global variables, function composition

**Module 3: Grid Driving**
- Use the driving toolkit on a taped GRID
- `track_until_cross()` drives between intersections
- `turn_right()` and `turn_left()` navigate the grid
- **Your Module 2 toolkits are the foundation for everything that follows!**

---

## Slide 11: Optional Extension -- The Final Project with Classes

*For courses that also cover classes/objects. Skip if not covering classes.*

```python
tracker = LineTrack()

board.wait_for_button()
for i in range(4):
    tracker.track_until_cross()
    tracker.turn_right()
    tracker.turn_right()
```

**Every call has a direct counterpart:** `tracker.track_until_cross()` ↔ `track_until_cross()`, `tracker.turn_right()` ↔ `turn_right()`. Robot behavior is identical either way -- only the packaging differs.
