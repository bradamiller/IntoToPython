# Lesson 2 Worksheet: Dictionaries

**Name:** ________________________
**Date:** ________________________

---

## Part 1: Creating Dictionaries

A **dictionary** stores **key-value pairs**. Each key maps to a value, like a real dictionary maps words to definitions.

Fill in the blanks to create dictionaries:

**1.** A dictionary that maps fruit names to their colors:

```python
fruit_colors = {
    "apple": __________,
    "banana": __________,
    "grape": __________
}
```

**2.** A dictionary that maps student names to their ages:

```python
students = {
    __________: 14,
    __________: 15,
    __________: 14
}
```

**3.** What symbol is used to start and end a dictionary? __________

**4.** What symbol separates a key from its value? __________

**5.** What symbol separates one key-value pair from the next? __________

---

## Part 2: Accessing Values

Given this dictionary:

```python
scores = {"Alice": 95, "Bob": 87, "Carol": 92}
```

What does each expression evaluate to?

| Expression | Result |
|---|---|
| `scores["Alice"]` | __________ |
| `scores["Bob"]` | __________ |
| `scores["Carol"]` | __________ |
| `len(scores)` | __________ |

**What happens if you try `scores["Dave"]`?**

____________________________________________________________________

---

## Part 3: Checking Membership

The `in` keyword checks if a **key** exists in a dictionary.

Given:

```python
inventory = {"apples": 5, "bananas": 3, "oranges": 0}
```

What does each expression evaluate to? Write **True** or **False**:

| Expression | Result |
|---|---|
| `"apples" in inventory` | __________ |
| `"grapes" in inventory` | __________ |
| `"oranges" in inventory` | __________ |
| `5 in inventory` | __________ |
| `"Apples" in inventory` | __________ |

**Does `in` check for keys or values?** __________

**Is dictionary lookup case-sensitive?** YES / NO

---

## Part 4: Modifying Dictionaries

Given:

```python
pets = {"cat": 2, "dog": 1}
```

Trace each line and write the dictionary contents after:

| Line of Code | Dictionary Contents After |
|---|---|
| `pets["fish"] = 3` | __________________________________________ |
| `pets["cat"] = 4` | __________________________________________ |
| `pets["dog"] = pets["dog"] + 1` | __________________________________________ |

**How do you add a new key-value pair to a dictionary?**

____________________________________________________________________

**How do you change the value for an existing key?**

____________________________________________________________________

---

## Part 5: Code Output Prediction

**Program A:**

```python
info = {"name": "XRP", "wheels": 2, "sensors": 3}

for key in info:
    print(key)
```

**Predicted output:**

```
__________
__________
__________
```

**Program B:**

```python
info = {"name": "XRP", "wheels": 2, "sensors": 3}

for key in info:
    print(key, "->", info[key])
```

**Predicted output:**

```
__________
__________
__________
```

**Program C:**

```python
counts = {}
words = ["the", "cat", "the", "hat", "the"]

for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1

print(counts)
```

**Predicted output:**

```
__________________________________________________________
```

---

## Part 6: Building a Graph Dictionary

In a graph, we can use a dictionary where each **key** is a node and each **value** is a **list of neighbors**.

Here is a simple 2x2 grid:

```
(0,0) --- (0,1)
  |         |
(1,0) --- (1,1)
```

Fill in the dictionary that represents this graph:

```python
graph = {
    (0, 0): [__________, __________],
    (0, 1): [__________, __________],
    (1, 0): [__________, __________],
    (1, 1): [__________, __________]
}
```

**How many keys does this dictionary have?** __________

**What type are the keys?** __________

**What type are the values?** __________

---

## Part 7: Graph Dictionary with Blocked Nodes

Now consider the same 2x2 grid, but **(0, 1)** is blocked:

```
(0,0)     [X X]
  |
(1,0) --- (1,1)
```

Fill in the graph dictionary (blocked nodes are not included):

```python
graph = {
    (0, 0): [__________],
    (1, 0): [__________, __________],
    (1, 1): [__________]
}
```

**Why is (0, 1) not a key in the dictionary?**

____________________________________________________________________

**Why is (0, 1) not in any neighbor list?**

____________________________________________________________________

---

## Part 8: Tracing Code with Dictionaries

Trace through this code step by step:

```python
graph = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (1, 1)],
    (1, 0): [(0, 0), (1, 1)],
    (1, 1): [(0, 1), (1, 0)]
}

start = (0, 0)
neighbors = graph[start]
print("Start:", start)
print("Neighbors:", neighbors)
print("First neighbor:", neighbors[0])
print("Number of neighbors:", len(neighbors))
```

**Predicted output:**

```
Start: __________
Neighbors: __________
First neighbor: __________
Number of neighbors: __________
```

---

## Part 9: Dictionary Methods

Given:

```python
robot = {"speed": 50, "direction": "north", "battery": 100}
```

Fill in what each expression returns:

| Expression | Result |
|---|---|
| `list(robot.keys())` | __________________________________________ |
| `list(robot.values())` | __________________________________________ |
| `robot.get("speed")` | __________ |
| `robot.get("color", "unknown")` | __________ |
| `robot.get("color")` | __________ |

**What is the difference between `robot["color"]` and `robot.get("color")`?**

____________________________________________________________________

____________________________________________________________________

---

## Reflection

**Why are dictionaries a good choice for representing a graph in Python?**

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

---

**Next Lesson:** We'll learn about **Dijkstra's Algorithm** — a famous method for finding shortest paths in a graph!
