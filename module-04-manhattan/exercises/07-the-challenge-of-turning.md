# Exercise 7: The Challenge of Turning

**Starter code:** `code/starter/lesson-07-turning.py`

## Overview

The Manhattan class tells the robot **where** to go. Now you need to figure out **how** — specifically, which direction to face before each step. You will implement two functions: `get_needed_direction()` and `get_turn()`.

## What You Will Do

### Part 1: get_needed_direction()

Given the robot's current position and the next position (one step away), return the compass direction the robot needs to face: `"N"`, `"S"`, `"E"`, or `"W"`.

**Logic:**
- Compare rows: if the next row is greater, the robot moves south (`"S"`). If smaller, north (`"N"`).
- Compare columns: if the next column is greater, the robot moves east (`"E"`). If smaller, west (`"W"`).

Fill in the function body using `if`/`elif` statements.

### Part 2: get_turn()

Given the direction the robot is currently **facing** and the direction it **needs** to face, return the turn required: `"NONE"`, `"RIGHT"`, `"LEFT"`, or `"REVERSE"`.

**Logic:**
- Same direction → `"NONE"`
- Opposite direction (N↔S, E↔W) → `"REVERSE"`
- Clockwise one step (N→E, E→S, S→W, W→N) → `"RIGHT"`
- Otherwise → `"LEFT"`

Use a `right_turns` dictionary to check clockwise relationships.

### Part 3: Test Your Functions
Uncomment the test code and verify:
- `get_needed_direction((0,0), (1,0))` returns `"S"`
- `get_needed_direction((1,0), (0,0))` returns `"N"`
- `get_turn("N", "E")` returns `"RIGHT"`
- `get_turn("N", "S")` returns `"REVERSE"`
- All other test cases pass.

## Key Concepts

- **Direction from coordinates:** The difference between two adjacent positions tells you which compass direction to move.
- **Turn table:** A 4×4 lookup from (current heading, needed direction) to turn type.
- **Right turns go clockwise:** N → E → S → W → N.
- **Left turns go counterclockwise:** N → W → S → E → N.

## Expected Output

```
===== Testing get_needed_direction =====
(0,0) to (1,0): S
(1,0) to (0,0): N
(0,0) to (0,1): E
(0,1) to (0,0): W

===== Testing get_turn =====
Facing N, need N: NONE
Facing N, need S: REVERSE
Facing N, need E: RIGHT
Facing N, need W: LEFT
Facing E, need S: RIGHT
Facing W, need N: RIGHT
```

## When You Are Done

- Do all direction and turn tests pass?
- Can you trace through a full path by hand, tracking the heading at each step?
- These functions will become methods in the Navigator class in Lesson 8.
