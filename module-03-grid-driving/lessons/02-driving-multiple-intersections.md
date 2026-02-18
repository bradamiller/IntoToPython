# Lesson 2: Driving Multiple Intersections

## Overview
Students learn to drive past an intersection and continue to the next one. The key challenge is that after `track_until_cross()` stops at a cross, the robot is still ON the cross — it must drive forward briefly to clear the intersection before calling `track_until_cross()` again. Students use `for` loops to drive a specified number of intersections.

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain why the robot must "clear" an intersection before continuing
- Write code that drives past an intersection and continues to the next
- Use a `for` loop to drive a specified number of intersections
- Count intersections accurately while the robot drives

## Key Concepts
- **Clearing the intersection**: Driving forward briefly after detecting a cross so the sensors move past it
- **Drive-and-continue pattern**: `track_until_cross()` → drive forward briefly → `track_until_cross()` again
- **Counting intersections**: Using a `for` loop to repeat the pattern a specific number of times
- **Timing**: The brief forward drive must be long enough to clear the cross but short enough to stay on the line

## Materials Required
- XRP Robot with reflectance sensors
- White surface with taped grid (at least 4×4 intersections)
- Working `LineSensor` and `LineTrack` classes from Module 2
- VS Code with XRPLib installed

## Lesson Flow

### Introduction (10 minutes)

1. **Hook: The Problem**:
   - Demo: Run `track_until_cross()` — robot stops at first intersection
   - Ask: "What if we want to go to the SECOND intersection?"
   - Run `track_until_cross()` again — robot doesn't move! Why?
   - "It's still ON the cross. Both sensors are still high. It thinks it already arrived!"

2. **The Solution: Clear the Cross**:
   - After stopping at a cross, drive forward a short distance
   - This moves the sensors past the intersection
   - THEN call `track_until_cross()` to drive to the next intersection
   - Pattern: detect → clear → detect → clear → ...

3. **How to Clear**:
   ```python
   # Drive forward briefly to clear the intersection
   tracker.drivetrain.set_effort(0.3, 0.3)
   time.sleep(0.3)
   ```
   - This drives forward at low speed for 0.3 seconds
   - Just enough to move past the cross
   - Adjust the time if the robot doesn't clear or overshoots

### Guided Practice: Drive Two Intersections (15 minutes)

1. **Two intersections manually**:
   ```python
   board = Board.get_default_board()
   tracker = LineTrack()

   board.wait_for_button()

   # Drive to first intersection
   print("Driving to intersection 1...")
   tracker.track_until_cross()
   print("Intersection 1 reached!")

   # Clear the intersection
   tracker.drivetrain.set_effort(0.3, 0.3)
   time.sleep(0.3)

   # Drive to second intersection
   print("Driving to intersection 2...")
   tracker.track_until_cross()
   print("Intersection 2 reached!")
   ```

2. **Discussion**: This works but it's repetitive. What if we want 5 intersections?

3. **Using a for loop**:
   ```python
   board.wait_for_button()

   intersections = 3

   for i in range(intersections):
       print("Driving to intersection", i + 1)
       tracker.track_until_cross()
       print("Intersection", i + 1, "reached!")

       # Clear the intersection (except after the last one)
       if i < intersections - 1:
           tracker.drivetrain.set_effort(0.3, 0.3)
           time.sleep(0.3)

   print("Done! Passed", intersections, "intersections.")
   ```

4. **Key Detail**: We DON'T clear after the LAST intersection — we want to stop there!
   - The `if i < intersections - 1` check handles this
   - On the last iteration, the robot stays at the intersection (ready to turn)

### Independent Practice (15 minutes)

1. **Exercise 1: Drive exactly 2 intersections**:
   - Use a for loop with `range(2)`
   - Verify the robot stops at the second intersection

2. **Exercise 2: Drive 3 intersections**:
   - Change the range to 3
   - Count along with the robot — does it stop at the right one?

3. **Exercise 3: Make it a function**:
   - Create a `drive_intersections(count)` function:
     ```python
     def drive_intersections(tracker, count):
         for i in range(count):
             tracker.track_until_cross()
             if i < count - 1:
                 tracker.drivetrain.set_effort(0.3, 0.3)
                 time.sleep(0.3)
     ```
   - Call it: `drive_intersections(tracker, 2)`

### Wrap-Up (5 minutes)

1. **Key Takeaways**:
   - Must clear the intersection before looking for the next one
   - A `for` loop makes it easy to drive any number of intersections
   - Don't clear after the last intersection — stop there!

2. **Preview**: Next lesson we'll add turns at intersections

## Common Issues
- **Robot doesn't clear the intersection**: Increase the sleep time (try 0.4 or 0.5)
- **Robot overshoots past the next intersection**: Decrease the sleep time or effort
- **Robot counts wrong number of intersections**: Add print statements to trace the count
- **Robot veers off line after clearing**: The clearing effort may be too high — try lower values

## Assessment
- Can the student explain why clearing is necessary?
- Can the student drive exactly N intersections using a for loop?
- Can the student identify what happens if clearing is skipped?
