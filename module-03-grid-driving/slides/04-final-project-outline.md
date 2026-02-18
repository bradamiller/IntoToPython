# Lesson 4 Slide Outline: Module 3 Final Project

## Slide 1: Title & Learning Objectives
**Title:** Module 3 Final Project — Square Pattern

**Learning Objectives:**
- Integrate driving and turning into a complete square pattern
- Use a for loop to repeat the drive-and-turn sequence
- Debug and refine a program on physical hardware
- Verify the robot returns to its starting position

**Agenda:**
- Project overview and requirements (5 min)
- Planning phase (10 min)
- Implementation and testing (25 min)
- Demo and reflection (5 min)

---

## Slide 2: Hook — The Square Challenge
**Your mission:** Make the robot drive a perfect square on the grid.

**The plan:**
- Each side = 2 intersections
- 4 sides + 4 right turns
- Robot ends where it started!

**Think about it:** This is just the polygon from Module 1 — but on a grid using line following!

---

## Slide 3: Planning the Square
**Draw the path:**

```
Start/End → + → + ┐
                   ↓
            +      +
            ↑      ↓
            + ← + ←┘
```

**Each side is identical:**
1. Drive 2 intersections forward
2. Turn right

**Repeat 4 times → complete square**

---

## Slide 4: The Program Structure
**One loop does it all:**

```python
board.wait_for_button()
print("Starting square pattern!")

for leg in range(4):
    print("Side", leg + 1, "of 4")
    drive_intersections(tracker, 2)
    tracker.turn_right()

print("Square complete!")
```

**Each iteration:**
- Drives 2 intersections forward (one side)
- Turns right (one corner)
- Repeats for all 4 sides

---

## Slide 5: Project Requirements
**Your program must include:**

| Requirement | Points |
|---|---|
| Uses LineTrack class from Module 2 | 10 |
| Square uses a for loop (not copy-paste) | 10 |
| Robot completes all 4 sides | 10 |
| Robot returns to starting position | 10 |
| Print statements show progress | 5 |
| Code is readable and organized | 5 |
| **Total** | **50** |

---

## Slide 6: Testing Strategy
**Don't test the full square first!**

**Step 1: Test one side**
- Drive 2 intersections and stop
- Verify it stops at the right place

**Step 2: Test one side + turn**
- Drive 2, turn right
- Verify the turn lines up

**Step 3: Test two sides**
- Use range(2) — half the square
- Verify the L-shape

**Step 4: Full square**
- Use range(4)
- Does it come back to start?

---

## Slide 7: Debugging Tips
**Robot doesn't return to start?**
- Check: Are turns exactly 90°? Adjust turn_right() timing
- Check: Is it driving exactly 2 intersections? Add print statements

**Robot skips an intersection?**
- Slow down: Reduce base_effort
- Check clearing time — too long? Too short?

**Robot veers after turning?**
- The turn might not be finding the line cleanly
- Try adding a small delay after turn: `time.sleep(0.2)`

**General strategy:** Change ONE thing, test, observe.

---

## Slide 8: Extension Challenges
**If you finish early:**

**Challenge A: Bigger Square**
- Change from 2 to 3 intersections per side

**Challenge B: Rectangle**
```python
lengths = [2, 3, 2, 3]
for leg in range(4):
    drive_intersections(tracker, lengths[leg])
    tracker.turn_right()
```

**Challenge C: Left-Turn Square**
- Use turn_left() instead — square goes the other direction

**Challenge D: Figure Eight**
- Drive a square right, then a square left (touching at one corner)

---

## Slide 9: Your Turn!
**Activity:**
1. Copy your LineSensor and LineTrack classes
2. Write the drive_intersections helper function
3. Write the main program with the for loop
4. Test incrementally (1 side → 2 sides → full square)
5. Demo your working square!

**Checkpoints:**
- Does the robot complete all 4 sides?
- Does the robot end up near where it started?
- Does your code use a for loop?
- Do print statements track which side is running?

---

## Slide 10: Reflection and Looking Ahead
**Module 3 Summary:**
- Reused LineTrack class on a grid (code reuse!)
- Learned to clear intersections for multi-intersection driving
- Sequenced drives and turns for complex paths
- Used for loops for repeated patterns
- No new Python concepts — just applied what you already know!

**Looking ahead to Module 4:**
- Module 3: YOU decide the path (hardcoded 2 intersections, turn right)
- Module 4: The COMPUTER calculates the path (Manhattan algorithm)
- You'll give coordinates like (2, 3) and the robot figures out how to get there
- The LineTrack class continues to be used!

**Big picture:** Each module builds on the last. Nothing is wasted.
