# Lesson 2 Slide Outline: Dictionaries

## Slide 1: Title & Learning Objectives
**Title:** Dictionaries — Key-Value Storage in Python

**Learning Objectives:**
- Create dictionaries with key-value pairs
- Access, add, and check for keys in a dictionary
- Use tuples as dictionary keys
- Represent a grid graph as a dictionary of neighbors

**Agenda:**
- What is a dictionary? (10 min)
- Creating and accessing dictionaries (10 min)
- Representing graphs with dictionaries (10 min)
- Building a grid graph in code (5 min)
- Practice exercise (10 min)

---

## Slide 2: Hook — Looking Up a Word
**Question:** "When you look up a word in a real dictionary, what do you need?"

**Answer:** You need the **word** (the key) to find its **definition** (the value).

- You don't read the whole dictionary from beginning to end
- You go straight to the word and get its definition
- Fast, direct lookup!

**Python dictionaries work the same way:**
- Give it a **key**, get back a **value**
- Instead of words and definitions, we'll use **coordinates and neighbors**

---

## Slide 3: What Is a Dictionary?
**Dictionary:** A collection of **key-value pairs**

```python
# A real-world example: student ages
ages = {"Alice": 15, "Bob": 16, "Carol": 15}

print(ages["Alice"])    # 15
print(ages["Bob"])      # 16
```

**Key features:**
- Curly braces: `{ }`
- Each entry: `key: value`
- Entries separated by commas
- Keys must be unique — no two entries with the same key
- Values can repeat — multiple students can be 15

**How it differs from a list:**
| | List | Dictionary |
|---|---|---|
| Access by | Index (position number) | Key (any immutable value) |
| Syntax | `my_list[0]` | `my_dict["Alice"]` |
| Ordered by | Position | Key lookup |

---

## Slide 4: Creating and Accessing Dictionaries
**Creating:**
```python
# Empty dictionary
empty = {}

# Dictionary with initial data
scores = {"math": 95, "science": 87, "english": 91}
```

**Accessing values:**
```python
print(scores["math"])       # 95
print(scores["science"])    # 87
```

**Adding new entries:**
```python
scores["history"] = 88
print(scores)
# {"math": 95, "science": 87, "english": 91, "history": 88}
```

**What happens with a bad key?**
```python
print(scores["art"])    # KeyError! "art" is not in the dictionary
```

---

## Slide 5: Checking for Keys
**Use `in` to check if a key exists before accessing:**

```python
scores = {"math": 95, "science": 87}

if "math" in scores:
    print("Math score:", scores["math"])

if "art" in scores:
    print("Art score:", scores["art"])
else:
    print("No art score found")
```

**Output:**
```
Math score: 95
No art score found
```

**Why this matters for graphs:**
- Before looking up a node's neighbors, check if it exists
- Blocked nodes won't be in our dictionary
- `if (1, 1) in graph:` tells us whether that intersection is accessible

---

## Slide 6: Tuples as Dictionary Keys
**Remember tuples from Module 4?** Tuples are immutable, so they can be dictionary keys!

```python
# Dictionary with tuple keys
positions = {
    (0, 0): "home",
    (2, 3): "school",
    (1, 4): "store"
}

print(positions[(0, 0)])    # "home"
print(positions[(2, 3)])    # "school"
```

**Check if a coordinate exists:**
```python
target = (2, 3)
if target in positions:
    print("Found:", positions[target])
```

**This is the key idea:** We'll use coordinate tuples as keys, and lists of neighbor coordinates as values.

---

## Slide 7: Representing a Graph as a Dictionary
**Keys = node coordinates, Values = lists of neighbor coordinates**

**A simple 2x2 grid:**
```
(0,0) --- (0,1)
  |         |
(1,0) --- (1,1)
```

**As a dictionary:**
```python
graph = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (1, 1)],
    (1, 0): [(0, 0), (1, 1)],
    (1, 1): [(0, 1), (1, 0)]
}
```

**Reading the dictionary:**
- `graph[(0, 0)]` returns `[(0, 1), (1, 0)]` — the neighbors of (0,0)
- `graph[(1, 1)]` returns `[(0, 1), (1, 0)]` — the neighbors of (1,1)

**To find where you can go from (0, 0):**
```python
neighbors = graph[(0, 0)]
print("From (0,0) I can go to:", neighbors)
# From (0,0) I can go to: [(0, 1), (1, 0)]
```

---

## Slide 8: Building a 3x3 Grid Graph
**A 3x3 grid with (1, 1) blocked:**
```
(0,0) --- (0,1) --- (0,2)
  |                   |
(1,0)               (1,2)
  |                   |
(2,0) --- (2,1) --- (2,2)
```

**As a dictionary (blocked node is simply not included):**
```python
graph = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (0, 2)],
    (0, 2): [(0, 1), (1, 2)],
    (1, 0): [(0, 0), (2, 0)],
    (1, 2): [(0, 2), (2, 2)],
    (2, 0): [(1, 0), (2, 1)],
    (2, 1): [(2, 0), (2, 2)],
    (2, 2): [(2, 1), (1, 2)]
}
```

**Notice:**
- (1, 1) is NOT a key — it's blocked
- (0, 0) no longer lists (1, 0)... wait, it does! But (1, 1) is not in anyone's neighbor list
- Blocked nodes disappear from keys AND from all neighbor lists

---

## Slide 9: Looping Through a Dictionary
**Print all nodes and their neighbors:**
```python
for node in graph:
    print(node, "-->", graph[node])
```

**Output:**
```
(0, 0) --> [(0, 1), (1, 0)]
(0, 1) --> [(0, 0), (0, 2)]
(0, 2) --> [(0, 1), (1, 2)]
...
```

**Count how many neighbors each node has:**
```python
for node in graph:
    num_neighbors = len(graph[node])
    print(node, "has", num_neighbors, "neighbors")
```

**This is useful for understanding the graph structure:**
- Corner nodes: 2 neighbors
- Edge nodes: 3 neighbors
- Interior nodes: 4 neighbors (unless neighbors are blocked)

---

## Slide 10: Your Turn!
**Activity: Build a Graph Dictionary in Python**

1. Open Python and create a dictionary for this 3x3 grid with **(1, 2) blocked:**
```
(0,0) --- (0,1) --- (0,2)
  |         |
(1,0) --- (1,1)
  |         |
(2,0) --- (2,1) --- (2,2)
```

2. Print the neighbors of (0, 0)
3. Print the neighbors of (1, 1)
4. Check: is (1, 2) in the graph? Print the result
5. Loop through the dictionary and print each node with its neighbor count

**Checkpoints:**
- Can you create a dictionary with tuple keys?
- Can you access neighbors with `graph[(r, c)]`?
- Can you check membership with `in`?
- Does your blocked node correctly disappear from all neighbor lists?

---

## Slide 11: Connection to Next Lesson
**What you did today:**
- Learned dictionaries: key-value pairs with `{key: value}` syntax
- Used tuples as dictionary keys
- Represented a grid graph as a dictionary of neighbor lists

**Next lesson (Lesson 3):**
- Learn **Dijkstra's algorithm** — a famous algorithm for finding shortest paths
- Uses dictionaries for distances, previous nodes, and the graph itself
- Finds the shortest path around obstacles automatically

**Key connection:** The graph dictionary you built today is the INPUT to Dijkstra's algorithm. The algorithm reads neighbors from the dictionary to explore paths.
