# Lesson 3 Worksheet: Lists

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Creating Lists

Write the Python code for each:

| Description | Code |
|---|---|
| An empty list | `path = _______________` |
| A list with three numbers: 1, 2, 3 | `numbers = _______________` |
| A list with two strings: "hello", "world" | `words = _______________` |
| A list with one tuple: (0, 0) | `path = _______________` |

**What characters surround a list's values?** __________

**Tuple uses ( ) and list uses [ ]. Why does the difference matter?**

____________________________________________________________________

---

## Part 2: List vs. Tuple

Fill in the comparison table:

| Feature | Tuple | List |
|---|---|---|
| Bracket type | ( ) | __________ |
| Can you change it after creation? | No (immutable) | __________ |
| Best used for | Fixed data like a coordinate | __________ |
| Example | `(2, 3)` | __________ |

---

## Part 3: Append Exercises

Trace what happens to the list after each `append()` call:

```python
path = []
path.append((0, 0))
path.append((1, 0))
path.append((2, 0))
```

| After line | Contents of `path` |
|---|---|
| `path = []` | `[]` |
| `path.append((0, 0))` | __________________________________ |
| `path.append((1, 0))` | __________________________________ |
| `path.append((2, 0))` | __________________________________ |

**How many items are in the list at the end?** __________

**What does `path[0]` return?** __________

**What does `path[2]` return?** __________

**What does `len(path)` return?** __________

---

## Part 4: Iteration Tracing

Trace the output of this code:

```python
colors = ["red", "green", "blue"]

for color in colors:
    print(color)
```

**Output:**

1. ____________________________
2. ____________________________
3. ____________________________

Now trace this code with a list of tuples:

```python
path = [(0, 0), (1, 0), (2, 0)]

for step in path:
    print("Visit:", step)
```

**Output:**

1. ____________________________
2. ____________________________
3. ____________________________

---

## Part 5: Accessing Tuples Inside a List

Given this list of tuples:

```python
path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
```

Fill in the values:

| Expression | Value |
|---|---|
| `path[0]` | __________ |
| `path[3]` | __________ |
| `path[0][0]` | __________ |
| `path[0][1]` | __________ |
| `path[3][0]` | __________ |
| `path[3][1]` | __________ |
| `len(path)` | __________ |
| `path[-1]` | __________ |

**Explain what `path[3][1]` means in words:**

____________________________________________________________________

---

## Part 6: Building a Path Step by Step

The robot needs to go from (0, 0) to (2, 3) by moving down 2 rows, then right 3 columns. Write the append statements to build this path:

```python
path = []
path.append(____________)    # Starting position
path.append(____________)    # One row down
path.append(____________)    # Two rows down
path.append(____________)    # One column right
path.append(____________)    # Two columns right
path.append(____________)    # Three columns right (destination)
```

**Write out the final path list:**

`path = ` ________________________________________________________

---

## Part 7: Loop-Based Path Building

Trace this code that builds a path using a loop:

```python
path = []
for row in range(4):
    path.append((row, 0))
print(path)
```

| Iteration | `row` | Appended | List after append |
|---|---|---|---|
| 1 | 0 | (0, 0) | [(0, 0)] |
| 2 | _____ | __________ | __________________________________ |
| 3 | _____ | __________ | __________________________________ |
| 4 | _____ | __________ | __________________________________ |

**Final output:** ________________________________________________________

Now trace this code:

```python
path = []
for col in range(3):
    path.append((2, col))
print(path)
```

| Iteration | `col` | Appended | List after append |
|---|---|---|---|
| 1 | _____ | __________ | __________________________________ |
| 2 | _____ | __________ | __________________________________ |
| 3 | _____ | __________ | __________________________________ |

**Final output:** ________________________________________________________

---

## Part 8: Iterating Through a Path

Trace the complete output of this program:

```python
path = [(0, 0), (1, 0), (1, 1), (1, 2)]

print("Path has", len(path), "positions")

for step in path:
    row = step[0]
    col = step[1]
    print("Row:", row, "Col:", col)
```

**Output:**

1. ________________________________________________
2. ________________________________________________
3. ________________________________________________
4. ________________________________________________
5. ________________________________________________

---

## Part 9: Spot the Error

Each code snippet has a mistake. Identify and fix it.

**Error 1:**
```python
path = []
for i in range(3):
    position = (i, 0)
path.append(position)    # Something is wrong with the indentation
```

Problem: ________________________________________________________________

Fix: ____________________________________________________________________

**Error 2:**
```python
path = []
print(path[0])
```

Problem: ________________________________________________________________

Fix: ____________________________________________________________________

**Error 3:**
```python
path = ((0, 0), (1, 0), (2, 0))   # Storing a path
path.append((3, 0))
```

Problem: ________________________________________________________________

Fix: ____________________________________________________________________

---

## Part 10: Code Writing

Write a program that:
1. Creates an empty list called `path`
2. Uses a `for` loop with `range(5)` to add coordinates (0, 0), (1, 0), (2, 0), (3, 0), (4, 0)
3. Prints each step in the path using a `for` loop

```python
path = _______________

for row in range(___):
    path.append(________________)

for step in path:
    print(________________)
```

---

## Reflection

**A tuple is ONE position. A list of tuples is a PATH. Explain in your own words why we need both data structures.**

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

---

**Next Lesson:** We'll learn the **Manhattan algorithm** — how to automatically calculate a path from any start to any destination!
