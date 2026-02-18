# Lesson 2 Slide Outline: Driving Multiple Intersections

## Slide 1: Title & Learning Objectives
**Title:** Driving Multiple Intersections

**Learning Objectives:**
- Explain why the robot must clear an intersection before continuing
- Write code that drives past an intersection to the next one
- Use a for loop to drive a specified number of intersections
- Count intersections accurately

**Agenda:**
- The clearing problem (10 min)
- Driving past an intersection (10 min)
- For loops for counting (10 min)
- Practice (15 min)

---

## Slide 2: Hook — The Stuck Robot
**Demo:** Robot drives to first intersection, stops.

**Run track_until_cross() again...**
- Nothing happens! The robot doesn't move!

**Why?** The robot is still ON the cross. Both sensors are high. It thinks it's already at an intersection!

**Question:** "How do we tell the robot to keep going to the NEXT intersection?"

---

## Slide 3: The Clearing Problem
**After track_until_cross(), the robot is AT the cross:**

```
  Line ──────+────── Line
             |
         [ROBOT]  ← Sensors right on the cross!
             |
             Line
```

**If we call track_until_cross() again:**
- Both sensors are already above threshold
- `is_at_cross()` returns True immediately
- The robot "detects" the intersection it's already on!

**Solution:** Drive forward briefly to move PAST the cross.

---

## Slide 4: Clearing the Intersection
**The fix: Drive forward a short distance after detecting:**

```python
# Detect the intersection
tracker.track_until_cross()

# Clear the intersection (drive past it)
tracker.drivetrain.set_effort(0.3, 0.3)
time.sleep(0.3)

# Now we can detect the NEXT intersection
tracker.track_until_cross()
```

**The clearing drive:**
- Low speed (0.3 effort) — don't go too fast
- Short time (0.3 seconds) — just enough to move past
- Adjust these values for your robot and grid spacing

---

## Slide 5: Driving Two Intersections
**Complete program:**

```python
board.wait_for_button()

# Intersection 1
print("Driving to intersection 1...")
tracker.track_until_cross()
print("Reached intersection 1!")

# Clear
tracker.drivetrain.set_effort(0.3, 0.3)
time.sleep(0.3)

# Intersection 2
print("Driving to intersection 2...")
tracker.track_until_cross()
print("Reached intersection 2!")
```

**This works! But what about 5 intersections? 10?**

---

## Slide 6: Using a For Loop
**A for loop makes it easy to drive any number of intersections:**

```python
intersections = 3

for i in range(intersections):
    print("Driving to intersection", i + 1)
    tracker.track_until_cross()
    print("Reached intersection", i + 1)

    # Clear (except after the last one!)
    if i < intersections - 1:
        tracker.drivetrain.set_effort(0.3, 0.3)
        time.sleep(0.3)
```

**Why skip clearing on the last intersection?**
- We want to STOP at the final intersection
- That's where we'll turn or end the program

---

## Slide 7: Tracing the Loop
**For intersections = 3:**

| i | Action | Clear? |
|---|---|---|
| 0 | Drive to intersection 1 | Yes (0 < 2) |
| 1 | Drive to intersection 2 | Yes (1 < 2) |
| 2 | Drive to intersection 3 | No (2 < 2 is False) |

**Result:** Robot drives through 3 intersections, stops at the 3rd.

**Change to any number:** Just change `intersections = N`

---

## Slide 8: Making It a Function
**Wrap it in a reusable function:**

```python
def drive_intersections(tracker, count):
    for i in range(count):
        tracker.track_until_cross()
        if i < count - 1:
            tracker.drivetrain.set_effort(0.3, 0.3)
            time.sleep(0.3)
```

**Usage:**
```python
drive_intersections(tracker, 2)   # Drive 2 intersections
drive_intersections(tracker, 4)   # Drive 4 intersections
```

**This function will be very useful in the final project!**

---

## Slide 9: Your Turn!
**Activity:**
1. Write a program that drives exactly 2 intersections and stops
2. Modify it to drive 3 intersections
3. Create the `drive_intersections(tracker, count)` function
4. Test with different counts (1, 2, 3, 4)

**Debugging:** If the robot counts wrong:
- Add print statements inside the loop
- Check that clearing time is appropriate
- Make sure you're not clearing after the last intersection

**Checkpoints:**
- Does the robot stop at exactly the right intersection?
- Does changing the count change the behavior?
- Does your function work for any count?

---

## Slide 10: Connection to Next Lesson
**What you did today:**
- Learned why clearing is necessary
- Drove multiple intersections with a for loop
- Created a reusable drive_intersections function

**Next lesson (Lesson 3):**
- Add TURNS at intersections
- Navigate L-shaped and more complex paths
- Combine driving and turning in sequences

**Preview:** drive 2 intersections → turn right → drive 2 more = L-shape!
