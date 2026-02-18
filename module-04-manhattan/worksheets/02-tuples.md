# Lesson 2 Worksheet: Tuples

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Creating Tuples

Write the Python code to create a tuple for each coordinate:

| Description | Code |
|---|---|
| The origin (row 0, column 0) | `position = _______________` |
| Row 2, column 3 | `position = _______________` |
| Row 3, column 1 | `position = _______________` |
| Row 0, column 4 | `position = _______________` |

**What characters surround a tuple's values?** __________

**What separates the values inside a tuple?** __________

---

## Part 2: Indexing Tuples

Given this tuple:

```python
position = (2, 3)
```

Fill in the blanks:

| Expression | Value |
|---|---|
| `position[0]` | __________ |
| `position[1]` | __________ |

1. **Which index gives you the row?** __________

2. **Which index gives you the column?** __________

3. **Does indexing start at 0 or 1?** __________

---

## Part 3: Predict the Output

For each code snippet, predict what will be printed:

**Snippet A:**
```python
start = (0, 0)
print(start)
```
**Output:** ____________________________

**Snippet B:**
```python
dest = (3, 2)
print("Row:", dest[0])
print("Col:", dest[1])
```
**Output line 1:** ____________________________

**Output line 2:** ____________________________

**Snippet C:**
```python
a = (1, 2)
b = (1, 2)
print(a == b)
```
**Output:** ____________________________

**Snippet D:**
```python
a = (1, 2)
b = (2, 1)
print(a == b)
```
**Output:** ____________________________

**Why are Snippets C and D different?**

____________________________________________________________________

**Snippet E:**
```python
point = (3, 1)
row = point[0]
col = point[1]
print("Position is row", row, "column", col)
```
**Output:** ____________________________

---

## Part 4: Immutability

**Immutable means:** ____________________________________________________

1. **What happens when you run this code?**

```python
position = (2, 3)
position[0] = 5
```

Answer: ____________________________________________________________________

2. **If you want to represent a new position, what do you do instead of modifying the tuple?**

Answer: ____________________________________________________________________

Write the code to create a new tuple for row 5, column 3:

```python
new_position = _______________
```

3. **Why is immutability a GOOD thing for coordinates?**

____________________________________________________________________

---

## Part 5: Tuple Math — Manhattan Distance

The Manhattan distance between two positions is the number of row steps plus the number of column steps.

**Formula:**
```
row_distance = |destination[0] - start[0]|
col_distance = |destination[1] - start[1]|
total_distance = row_distance + col_distance
```

Calculate the Manhattan distance for each pair:

| Start | Destination | Row Distance | Col Distance | Manhattan Distance |
|---|---|---|---|---|
| (0, 0) | (2, 3) | \|2 - 0\| = _____ | \|3 - 0\| = _____ | __________ |
| (0, 0) | (3, 0) | \|3 - 0\| = _____ | \|0 - 0\| = _____ | __________ |
| (1, 1) | (3, 3) | __________ | __________ | __________ |
| (2, 3) | (0, 1) | __________ | __________ | __________ |
| (1, 2) | (1, 2) | __________ | __________ | __________ |

**Which pair of positions is closest together?** ____________________________

**Which pair is farthest apart?** ____________________________

---

## Part 6: Code Tracing

Trace through this code and write the value of each variable:

```python
home = (0, 0)
school = (3, 2)

row_diff = school[0] - home[0]
col_diff = school[1] - home[1]
total = row_diff + col_diff

print("Rows:", row_diff)
print("Cols:", col_diff)
print("Total:", total)
```

| Variable | Value |
|---|---|
| `home[0]` | __________ |
| `home[1]` | __________ |
| `school[0]` | __________ |
| `school[1]` | __________ |
| `row_diff` | __________ |
| `col_diff` | __________ |
| `total` | __________ |

**Output line 1:** ____________________________

**Output line 2:** ____________________________

**Output line 3:** ____________________________

---

## Part 7: Spot the Error

Each code snippet has a mistake. Identify and fix it.

**Error 1:**
```python
position = (2, 3)
row = position[1]    # Getting the row
```
Problem: ________________________________________________________________

Fix: ____________________________________________________________________

**Error 2:**
```python
position = [2, 3]    # Storing a coordinate
```
Problem: ________________________________________________________________

Fix: ____________________________________________________________________

**Error 3:**
```python
position = (2, 3)
position[0] = 4      # Move to row 4
```
Problem: ________________________________________________________________

Fix: ____________________________________________________________________

---

## Part 8: Tuple vs. Two Variables

**Version A — Two separate variables:**
```python
row = 2
col = 3
```

**Version B — One tuple:**
```python
position = (2, 3)
```

1. **If you have 5 different positions, how many variables does Version A need?** __________

2. **How many variables does Version B need for 5 positions?** __________

3. **Which version is easier to pass to a function? Why?**

   ____________________________________________________________________

---

## Reflection

**Explain in your own words: What is a tuple and why is it useful for storing coordinates?**

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

---

**Next Lesson:** We'll learn about **lists** — collections that CAN change — and use them to store a whole path of coordinates!
