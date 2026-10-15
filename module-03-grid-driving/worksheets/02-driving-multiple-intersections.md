# Lesson 2 Worksheet: Driving Multiple Intersections

**Name:** ________________________
**Date:** ________________________

---

## Part 1: The thought experiment

**Why doesn't this reach the second intersection?**
```python
track_to_intersection()   # drives to intersection 1
track_to_intersection()   # should drive to intersection 2...
```

1. When the first call stops, where are the sensors? ______________________

2. What does `is_at_cross()` return at the moment the second call starts? ______

3. So what does the second call's `while not is_at_cross():` loop do? ______________________________________________

4. What one call goes between them, and what does it do to the sensors? ______________________________________________

---

## Part 2: Trace the pattern

```python
track_to_intersection()
drive_past_intersection()
track_to_intersection()
drive_past_intersection()
```

| After line | Sensors are... | Wheels are... |
|---|---|---|
| 1 | on intersection 1 | short of intersection 1 |
| 2 | ________________ | ________________ |
| 3 | ________________ | ________________ |
| 4 | ________________ | ________________ |

**Where is the robot parked at the end?** ______________________

---

## Part 3: Loop tracing

```python
intersections = 3

for i in range(intersections):
    print("Driving to intersection", i + 1)
    track_to_intersection()
    drive_past_intersection()

print("Done! Parked on intersection", intersections)
```

| Pass | `i` | Prints | Robot ends parked on... |
|---|---|---|---|
| 1 | 0 | ________________ | ________________ |
| 2 | ___ | ________________ | ________________ |
| 3 | ___ | ________________ | ________________ |

**A classmate says the last `drive_past_intersection()` will carry the robot off intersection 3. Are they right? Why or why not?**

______________________________________________________________

______________________________________________________________

---

## Part 4: Fix the bug

**Program A:**
```python
def drive_intersections(count):
    for i in range(count):
        track_to_intersection()
```
With `drive_intersections(3)`, how many intersections does the robot actually reach? ______ Why? ______________________________________________

**Program B:**
```python
def drive_intersections(count):
    for i in range(count):
        track_to_intersection()
        if i < count - 1:
            drive_past_intersection()
```
Where does the robot end after `drive_intersections(3)` -- wheels on intersection 3, or short of it? ______________________ What happens if you call `turn_clockwise()` next? ______________________________________________

**Write the correct helper:**
```python
def drive_intersections(count):
    for i in range(count):
        ________________________________
        ________________________________
```

---

## Part 5: Design your own

Write a program that drives 2 intersections, prints "Halfway!", then drives 2 more, using the helper:

```python
________________________________
________________________________
________________________________
```

**How many times did `drive_past_intersection()` run in total?** ______

**Where is the robot parked?** ______________________
