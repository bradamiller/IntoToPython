# Module 3: Relative Driving on the Grid

## Overview

**Duration:** 1–2 weeks

**Theme:** Applying existing code to the grid and verifying it works

**Final Project:** Robot drives a square pattern on the grid (2 intersections per side)

## Learning Objectives

By the end of this module, students will be able to:
- Understand the relationship between grid intersections and the line-detection logic from Module 2
- Use the `LineTrack` class to navigate from one intersection to the next
- Sequence multiple drives and turns to create a closed path
- Test and debug a program on the physical grid
- Prepare for coordinate-based navigation (coming in Module 4)

## Key Concepts

- **Grid Navigation:** Reading line intersections as waypoints
- **Sequencing:** Combining drives and turns in order
- **Loops:** Using `for` loops to repeat patterns
- **Testing:** Running on hardware and verifying expected behavior
- **Code Reuse:** Applying the `LineTrack` class from Module 2 without modification

## Module Structure

### Single Phase: Relative Driving (Lessons 1–4)

This is a short, focused module. Students use Module 2 code as-is and practice navigating the grid.

- Lesson 1: Introduction to the Grid
- Lesson 2: Driving Multiple Intersections
- Lesson 3: Turning on the Grid
- Lesson 4: Module 3 Final Project

## Why This Module Exists

Module 2 was taught on a single circle. Module 3 shows that the same code works on a grid. This builds confidence before moving to coordinate-based thinking in Module 4.

## Python Concepts

**No new Python concepts in this module.** Students reinforce:
- Calling methods on class instances (`linetrack.track_until_cross()`)
- Using loops for repetition
- Sequential program flow
- Testing and debugging existing code

## Progression

1. **Week 10:** Understand the grid; drive to first intersection; drive multiple intersections
2. **Week 11:** Turn on the grid; complete square pattern project

**This module is brief and focuses on practical application, not new concepts.**

## Key Milestones

- ✓ **End of Week 10:** Robot drives to first intersection and stops; can drive 2 intersections forward
- ✓ **End of Week 11:** Final project complete — square pattern verified (robot returns to start)

## Assessment

Students demonstrate mastery by:
1. **Exercise code:** Drives to intersections reliably
2. **Final project demo:** Robot follows square path and returns to start

## Debugging Notes

**Common issues:**
- **Robot doesn't detect intersections properly:** Usually a carry-over from Module 2; recalibrate sensors
- **Robot skips intersections:** May be driving too fast; slow down with reduced speed settings
- **Robot isn't turning exactly 90°:** Use the `turn_right()` and `turn_left()` methods from Module 2; they handle alignment

## Resources

- Module 2 `LineTrack` class (use as-is)
- Grid setup and calibration (see teacher guide)
- Solution code showing full square pattern

## Next Module

Module 4 introduces **coordinates and pathfinding**. Instead of relative driving (turn right, drive forward), students will compute paths to absolute positions on the grid.

---

## Quick Start

1. **Load the grid** in your classroom (see teacher-guide/xrp-setup-guide.md)
2. **Review Lesson 1** to understand the grid-as-waypoints mental model
3. **Have students adapt their Module 2 code** to work on the grid
4. **Test and refine** intersection detection and alignment

---

**Note:** This is the shortest module, but it's important for bridging from relative to absolute navigation. Don't skip it; the confidence students gain transfers directly to Module 4.
