# Lesson 2 Slide Outline: Tuples

## Slide 1: Title & Learning Objectives
**Title:** Tuples — Storing Coordinates in Python

**Learning Objectives:**
- Create tuples to represent coordinate pairs
- Access tuple elements using indexing
- Understand why tuples are immutable
- Use tuples to store robot positions

**Agenda:**
- What is a tuple? (10 min)
- Creating and indexing tuples (10 min)
- Tuples for coordinates (10 min)
- Practice exercises (15 min)

---

## Slide 2: Hook — Packaging Two Numbers Together
**Problem:** We need to store a position as TWO numbers (row and col).

**Awkward approach:**
```python
row = 2
col = 3
# Now we have two separate variables for one position...
# What if we have 10 positions? That's 20 variables!
```

**Better approach:**
```python
position = (2, 3)
# One variable, one position — clean!
```

**Question:** "How can we store two related numbers as a single value?"

---

## Slide 3: What Is a Tuple?
**Tuple:** An ordered, immutable collection of values

**Creating a tuple:**
```python
position = (2, 3)
point = (0, 0)
destination = (3, 1)
```

**Key features:**
- Uses parentheses: `( )`
- Values separated by commas
- Can hold any number of values
- Values are ordered (first, second, third...)

**Pronunciation:** "tuh-pull" or "too-pull" — both are correct!

---

## Slide 4: Accessing Tuple Elements — Indexing
**Use square brackets with an index number:**

```python
position = (2, 3)

row = position[0]    # First element → 2
col = position[1]    # Second element → 3

print("Row:", row)   # Row: 2
print("Col:", col)   # Col: 3
```

**Index starts at 0:**

| Index | Value | Meaning |
|---|---|---|
| [0] | 2 | Row |
| [1] | 3 | Column |

**Critical Rule:** Indexing starts at 0, not 1!

---

## Slide 5: Why Tuples Are Immutable
**Immutable = cannot be changed after creation**

```python
position = (2, 3)
position[0] = 5      # ERROR! Can't modify a tuple
```

**Why is this good for coordinates?**
- A coordinate IS a fixed point — (2, 3) is always row 2, col 3
- If you need a new position, create a new tuple:

```python
old_position = (2, 3)
new_position = (2, 4)   # New tuple, one column to the right
```

**Analogy:** A street address doesn't change. "123 Main St" is always the same place. If you move, you get a NEW address.

---

## Slide 6: Tuples for Robot Coordinates
**Storing the robot's position:**
```python
start = (0, 0)
destination = (2, 3)

print("Start:", start)
print("Going to:", destination)
print("Start row:", start[0], "Start col:", start[1])
```

**Output:**
```
Start: (0, 0)
Going to: (2, 3)
Start row: 0 Start col: 1
```

**Comparing coordinates:**
```python
current = (1, 2)
target = (1, 2)
print(current == target)   # True — same position!

other = (2, 1)
print(current == other)    # False — different positions!
```

---

## Slide 7: Tuple Math — Calculating Distance
**How far apart are two coordinates?**

```python
start = (0, 0)
destination = (2, 3)

row_distance = destination[0] - start[0]   # 2 - 0 = 2
col_distance = destination[1] - start[1]   # 3 - 0 = 3

print("Rows to travel:", row_distance)
print("Cols to travel:", col_distance)
print("Total steps:", row_distance + col_distance)  # 5
```

**This is the Manhattan distance!**
- Row difference + column difference = total intersections to cross
- Named after Manhattan's grid street layout

---

## Slide 8: Common Tuple Mistakes
**Mistake 1: Forgetting parentheses**
```python
position = 2, 3       # Actually still creates a tuple! But not clear.
position = (2, 3)     # Better — explicit parentheses
```

**Mistake 2: Wrong index**
```python
position = (2, 3)
row = position[1]     # WRONG — this is the column (3), not the row!
row = position[0]     # CORRECT — row is at index 0
```

**Mistake 3: Trying to modify**
```python
position = (2, 3)
position[0] = 5       # TypeError! Tuples are immutable.
```

**Remember:** `[0]` = row, `[1]` = column

---

## Slide 9: Your Turn!
**Activity:**
1. Open Python and create these tuples:
   - `home = (0, 0)`
   - `school = (3, 2)`
   - `store = (1, 4)`
2. Print each position
3. Print the row and column of each separately
4. Calculate the Manhattan distance between home and school
5. Calculate the Manhattan distance between home and store

**Challenge:** Which destination is closer to home (fewer total steps)?

**Checkpoints:**
- Can you create a tuple?
- Can you access [0] and [1]?
- Can you calculate row and column distances?

---

## Slide 10: Connection to Next Lesson
**What you did today:**
- Created tuples to store coordinates
- Accessed elements with [0] and [1]
- Calculated distances between positions

**Next lesson (Lesson 3):**
- Learn about **lists** — ordered collections that CAN change
- Store multiple coordinates as a **path**
- Build a list of tuples: `[(0,0), (1,0), (2,0), (2,1)]`

**Key connection:** A tuple is ONE position. A list of tuples is a PATH.
