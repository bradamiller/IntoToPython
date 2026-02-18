# Lesson 3 Slide Outline: Lists

## Slide 1: Title & Learning Objectives
**Title:** Lists — Storing Paths as Collections

**Learning Objectives:**
- Create and manipulate lists in Python
- Use append() to add items to a list
- Iterate through a list with a for loop
- Represent a path as a list of coordinate tuples

**Agenda:**
- What is a list? (8 min)
- Creating lists and append() (10 min)
- Iterating with for loops (10 min)
- Paths as lists of tuples (17 min)

---

## Slide 2: Hook — One Position Is Not Enough
**Problem:** We can store ONE position with a tuple.

```python
position = (2, 3)
```

**But a path has MANY positions:**
- (0, 0) → (1, 0) → (2, 0) → (2, 1) → (2, 2) → (2, 3)

**Question:** "How do we store a whole sequence of positions?"

**Answer:** A list!

---

## Slide 3: What Is a List?
**List:** An ordered, mutable collection of values

**Creating a list:**
```python
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
empty = []
```

**Key features:**
- Uses square brackets: `[ ]`
- Values separated by commas
- Can hold any type of value
- Can grow and shrink (mutable!)

**Tuple vs. List:**

| Feature | Tuple | List |
|---|---|---|
| Brackets | ( ) | [ ] |
| Can change? | No (immutable) | Yes (mutable) |
| Best for | Fixed data (coordinates) | Collections (paths) |

---

## Slide 4: List Operations
**Creating and accessing:**
```python
colors = ["red", "green", "blue"]
print(colors[0])      # "red"
print(colors[1])      # "green"
print(len(colors))    # 3
```

**Adding items with append():**
```python
colors = ["red", "green"]
colors.append("blue")
print(colors)         # ["red", "green", "blue"]
colors.append("yellow")
print(colors)         # ["red", "green", "blue", "yellow"]
```

**Key:** append() adds to the END of the list

---

## Slide 5: Iterating Through a List
**Use a for loop to visit each item:**

```python
colors = ["red", "green", "blue"]

for color in colors:
    print(color)
```

**Output:**
```
red
green
blue
```

**With index numbers:**
```python
for i in range(len(colors)):
    print("Item", i, "is", colors[i])
```

**Output:**
```
Item 0 is red
Item 1 is green
Item 2 is blue
```

---

## Slide 6: Building a List Step by Step
**Start empty, add items in a loop:**

```python
squares = []

for i in range(5):
    squares.append(i * i)

print(squares)
```

**Output:**
```
[0, 1, 4, 9, 16]
```

**Step by step:**

| Iteration | i | i * i | List after append |
|---|---|---|---|
| 1 | 0 | 0 | [0] |
| 2 | 1 | 1 | [0, 1] |
| 3 | 2 | 4 | [0, 1, 4] |
| 4 | 3 | 9 | [0, 1, 4, 9] |
| 5 | 4 | 16 | [0, 1, 4, 9, 16] |

**This pattern is KEY for building paths!**

---

## Slide 7: A Path Is a List of Tuples
**Combining lists and tuples:**

```python
path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]

print("Path has", len(path), "steps")
print("Start:", path[0])
print("End:", path[-1])
```

**Iterating through a path:**
```python
for step in path:
    print("Visit:", step)
    print("  Row:", step[0], "Col:", step[1])
```

**Output:**
```
Visit: (0, 0)
  Row: 0 Col: 0
Visit: (1, 0)
  Row: 1 Col: 0
...
```

---

## Slide 8: Building a Path with append()
**Build a path programmatically:**

```python
path = []

# Add the starting position
path.append((0, 0))

# Move down 2 rows
path.append((1, 0))
path.append((2, 0))

# Move right 3 columns
path.append((2, 1))
path.append((2, 2))
path.append((2, 3))

print("Path:", path)
```

**Output:**
```
Path: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]
```

**Next lesson:** We'll write code that CALCULATES the path automatically!

---

## Slide 9: Common List Mistakes
**Mistake 1: append() inside vs. outside loop**
```python
path = []
for i in range(3):
    position = (i, 0)
path.append(position)    # WRONG — only adds the last one!
```

```python
path = []
for i in range(3):
    position = (i, 0)
    path.append(position)  # CORRECT — adds each one
```

**Mistake 2: Confusing [ ] and ( )**
```python
path = [(0, 0), (1, 0)]   # List of tuples ✓
path = ((0, 0), (1, 0))   # Tuple of tuples — not what we want
```

**Mistake 3: Forgetting the list is empty**
```python
path = []
print(path[0])    # IndexError! Empty list has no items.
```

---

## Slide 10: Your Turn!
**Activity:**
1. Create an empty list called `path`
2. Use append() to add these coordinates in order:
   - (0, 0), (0, 1), (0, 2), (1, 2), (2, 2)
3. Print the full path
4. Print how many steps the path has
5. Use a for loop to print each step with its row and column

**Challenge:** Write a loop that builds a path from (0, 0) down to (4, 0):
```python
path = []
for row in range(5):
    path.append((row, 0))
print(path)
```

**Checkpoints:**
- Can you create and append to a list?
- Can you iterate through a list of tuples?
- Can you access the row and column from each tuple in the list?

---

## Slide 11: Connection to Next Lesson
**What you did today:**
- Created lists and used append()
- Iterated through lists with for loops
- Built paths as lists of coordinate tuples

**Next lesson (Lesson 4):**
- Learn the **Manhattan algorithm** — how to calculate a path automatically
- Given a start and destination, compute every step
- No more adding coordinates by hand!

**Key insight:** You now have the data structures. Next, you'll learn the algorithm.
