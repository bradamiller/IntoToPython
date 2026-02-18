# Lesson 2 Worksheet: Driving Multiple Intersections

**Name:** ________________________
**Date:** ________________________

---

## Part 1: The Clearing Problem

**Why doesn't this work?**
```python
tracker.track_until_cross()   # Drives to intersection 1
tracker.track_until_cross()   # Should drive to intersection 2...
```

Explain in your own words why the second `track_until_cross()` doesn't work:

______________________________________________________________

______________________________________________________________

**What must the robot do between the two calls?**

______________________________________________________________

---

## Part 2: Code Tracing

Trace through this code and fill in what happens at each step:

```python
tracker.track_until_cross()
tracker.drivetrain.set_effort(0.3, 0.3)
time.sleep(0.3)
tracker.track_until_cross()
```

| Step | Code | What the robot does |
|---|---|---|
| 1 | `track_until_cross()` | __________ |
| 2 | `set_effort(0.3, 0.3)` | __________ |
| 3 | `time.sleep(0.3)` | __________ |
| 4 | `track_until_cross()` | __________ |

**How many intersections did the robot pass through?** __________

**Where did the robot end up?** __________

---

## Part 3: Loop Tracing

Trace through this loop with `intersections = 3`:

```python
intersections = 3
for i in range(intersections):
    tracker.track_until_cross()
    if i < intersections - 1:
        tracker.drivetrain.set_effort(0.3, 0.3)
        time.sleep(0.3)
```

| i | track_until_cross() | Is i < 2? | Clears? | Intersection # reached |
|---|---|---|---|---|
| 0 | Drives to... | __________ | __________ | __________ |
| 1 | Drives to... | __________ | __________ | __________ |
| 2 | Drives to... | __________ | __________ | __________ |

**Why don't we clear after the last intersection?**

______________________________________________________________

---

## Part 4: Fix the Bug

Each program has a bug. Find and describe the fix:

**Bug 1:**
```python
for i in range(3):
    tracker.track_until_cross()
    tracker.drivetrain.set_effort(0.3, 0.3)
    time.sleep(0.3)
```
**What's wrong?** ______________________________________________________________

**Fix:** ______________________________________________________________

**Bug 2:**
```python
for i in range(3):
    tracker.drivetrain.set_effort(0.3, 0.3)
    time.sleep(0.3)
    tracker.track_until_cross()
```
**What's wrong?** ______________________________________________________________

**Fix:** ______________________________________________________________

---

## Part 5: Design Your Own

Write the code to drive exactly 4 intersections forward using a for loop:

```python
intersections = ____

for i in range(________):
    ___________________________________
    if _______________:
        ___________________________________
        ___________________________________
```

**Test your code on the robot. Does it stop at the 4th intersection?** __________

**What did you adjust (if anything)?** ______________________________________________________________
