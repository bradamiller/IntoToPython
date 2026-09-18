# Lesson 2: Driving Multiple Intersections

## Overview
Students learn to drive past an intersection and continue to the next one. The key challenge is that after `track_until_cross()` stops at a cross, the robot is still ON the cross — it must clear the intersection before calling `track_until_cross()` again. Students already have a `clear_intersection()` function from Module 2 Lesson 9 (it drives a fixed 8 cm forward); this lesson reuses it directly in the main program, and combines it with a `for` loop to drive a specified number of intersections.

*If your course covers the Module 2 Optional Extension (classes), everything below works identically through `tracker.track_until_cross()` and `tracker.clear_intersection()` instead of bare function calls.*

## Learning Objectives
By the end of this lesson, students will be able to:
- Explain why the robot must "clear" an intersection before continuing
- Reuse the `clear_intersection()` function from Module 2 in a new context
- Write code that drives past an intersection and continues to the next
- Use a `for` loop to drive a specified number of intersections
- Count intersections accurately while the robot drives

## Key Concepts
- **Clearing the intersection**: Driving a fixed 8 cm forward after detecting a cross so the sensors move past it — same `clear_intersection()` function from Lesson 9, used here without a turn
- **Drive-and-continue pattern**: `track_until_cross()` → `clear_intersection()` → `track_until_cross()` again
- **Counting intersections**: Using a `for` loop to repeat the pattern a specific number of times
- **Skip the last clear**: Clearing only makes sense *between* intersections — the last one is where we want to stop

## Materials Required
- XRP Robot with reflectance sensors
- White surface with taped grid (at least 4×4 intersections)
- Working sensor and driving toolkit from Module 2, including `clear_intersection()`
- VS Code with XRPLib installed

## Lesson Flow

### Introduction (10 minutes)

1. **Hook: The Problem**:
   - Demo: Run `track_until_cross()` — robot stops at first intersection
   - Ask: "What if we want to go to the SECOND intersection?"
   - Run `track_until_cross()` again — robot doesn't move! Why?
   - "It's still ON the cross. Both sensors are still high. It thinks it already arrived!"

2. **The Solution: We Already Built This**:
   - Recall from Module 2 Lesson 9: `clear_intersection()` drives a fixed 8 cm forward, exactly the distance needed to move the sensors past an intersection
   - It was written for the turn functions, but nothing about it is turn-specific — it just moves the robot past whatever cross it's currently sitting on
   - Pattern: detect → clear → detect → clear → ...

3. **Reusing `clear_intersection()`**:
   ```python
   track_until_cross()
   clear_intersection()
   track_until_cross()
   ```
   - This drives to the first intersection, clears it, then drives to the second
   - No new function needed — just call an existing one in a new place

### Guided Practice: Drive Two Intersections (15 minutes)

1. **Two intersections manually**:
   ```python
   board = Board.get_default_board()

   board.wait_for_button()

   # Drive to first intersection
   print("Driving to intersection 1...")
   track_until_cross()
   print("Intersection 1 reached!")

   # Clear the intersection
   clear_intersection()

   # Drive to second intersection
   print("Driving to intersection 2...")
   track_until_cross()
   print("Intersection 2 reached!")
   ```

2. **Discussion**: This works but it's repetitive. What if we want 5 intersections?

3. **Using a for loop**:
   ```python
   board.wait_for_button()

   intersections = 3

   for i in range(intersections):
       print("Driving to intersection", i + 1)
       track_until_cross()
       print("Intersection", i + 1, "reached!")

       # Clear the intersection (except after the last one)
       if i < intersections - 1:
           clear_intersection()

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
     def drive_intersections(count):
         for i in range(count):
             track_until_cross()
             if i < count - 1:
                 clear_intersection()
     ```
   - Call it: `drive_intersections(2)`

### Wrap-Up (5 minutes)

1. **Key Takeaways**:
   - Must clear the intersection before looking for the next one
   - `clear_intersection()` isn't just for turning — it's a general-purpose function
   - A `for` loop makes it easy to drive any number of intersections
   - Don't clear after the last intersection — stop there!

2. **Preview**: Next lesson we'll add turns at intersections

## Common Issues
- **Robot doesn't clear the intersection**: Check that `clear_intersection()` is being called between drives, not skipped
- **Robot overshoots past the next intersection**: This shouldn't happen with distance-based clearing — if it does, check the 8 cm measurement against your robot
- **Robot counts wrong number of intersections**: Add print statements to trace the count
- **Robot veers off line after clearing**: Check the grid tape is consistent with the circle from Module 2

## Assessment
- Can the student explain why clearing is necessary?
- Can the student explain why `clear_intersection()` from Lesson 9 works here too, with no turn involved?
- Can the student drive exactly N intersections using a for loop?
- Can the student identify what happens if clearing is skipped?
