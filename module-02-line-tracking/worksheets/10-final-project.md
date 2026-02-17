# Lesson 10 Worksheet: Module 2 Final Project

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Project Planning

### Requirements Checklist
Check off each requirement as you complete it:

- [ ] Robot follows the taped circle
- [ ] Robot detects the cross intersection
- [ ] Robot turns around (reverses direction)
- [ ] Robot continues following after reversing
- [ ] Robot completes 4 total reversals
- [ ] Robot stops and prints a completion message
- [ ] Code uses LineSensor and LineTrack classes
- [ ] Code includes print statements showing progress
- [ ] Code is organized and commented

### My Project Option: (circle one)
**A: Standard** / **B: Enhanced** / **C: Advanced**

### Pseudocode
Write your main program plan in plain English:

```
1. ____________________________________________
2. ____________________________________________
3. ____________________________________________
4. ____________________________________________
5. ____________________________________________
6. ____________________________________________
```

---

## Part 2: Class Inventory

List the methods available in each class:

**LineSensor:**
| Method | What It Returns | When to Use |
|---|---|---|
| `get_error()` | ________________ | ________________ |
| `is_at_cross()` | ________________ | ________________ |
| `is_off_line()` | ________________ | ________________ |

**LineTrack:**
| Method | What It Does | When to Use |
|---|---|---|
| `track_until_cross()` | ________________ | ________________ |
| `turn_right()` | ________________ | ________________ |
| `turn_left()` | ________________ | ________________ |

---

## Part 3: Testing Log

Record the result of each test:

| Test # | What I Tested | Result (Pass/Fail) | Notes |
|---|---|---|---|
| 1 | `track_until_cross()` works | __________ | ________________________ |
| 2 | Turn-around works | __________ | ________________________ |
| 3 | 1 full reversal | __________ | ________________________ |
| 4 | 4 reversals complete | __________ | ________________________ |

### Debugging Notes
If something didn't work, what did you change?

| Problem | What I Changed | Did It Fix It? |
|---|---|---|
| ________________________ | ________________________ | __________ |
| ________________________ | ________________________ | __________ |
| ________________________ | ________________________ | __________ |

---

## Part 4: Parameter Tuning

Record the parameters that work best for your robot:

| Parameter | Starting Value | Final Value | Why I Changed It |
|---|---|---|---|
| `threshold` | 0.5 | __________ | ________________________ |
| `base_effort` | 0.4 | __________ | ________________________ |
| `Kp` | 0.5 | __________ | ________________________ |
| `time.sleep()` in turns | 0.3 | __________ | ________________________ |

---

## Part 5: Module 2 Concept Review

Match each concept to when it was introduced:

| Concept | Lesson |
|---|---|
| Reflectance sensors | Lesson ___ |
| `while` loops | Lesson ___ |
| `if/else` | Lesson ___ |
| `import` and `random` | Lesson ___ |
| Proportional control | Lesson ___ |
| Two-sensor following | Lesson ___ |
| Intersection detection | Lesson ___ |
| Classes (`class`, `__init__`, `self`) | Lesson ___ |
| Object composition | Lesson ___ |

---

## Part 6: Reflection

1. **What was the hardest part of Module 2?**

   ____________________________________________________________________

2. **How did using classes (LineSensor, LineTrack) make the final project easier compared to writing everything in one big program?**

   ____________________________________________________________________

   ____________________________________________________________________

3. **What would you improve about your code if you had more time?**

   ____________________________________________________________________

4. **What programming concept do you feel most confident about now?**

   ____________________________________________________________________

5. **Rate your confidence with each concept (1 = not confident, 5 = very confident):**

   | Concept | Confidence (1-5) |
   |---|---|
   | while loops | ___ |
   | if/else | ___ |
   | import / modules | ___ |
   | Proportional control | ___ |
   | Classes and methods | ___ |
   | Object composition | ___ |

---

**Congratulations on completing Module 2!** Your LineSensor and LineTrack classes will be used again in Module 3 when you drive on the grid.
