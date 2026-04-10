# Lesson 5 Slide Outline: Implementing the Manhattan Class

## Slide 1: Title & Learning Objectives
**Title:** Implementing the Manhattan Class

**Learning Objectives:**
- Understand why we wrap functions in a class
- Convert the compute_path function from Lesson 4 into a method
- Use `self.position` to store state instead of passing a parameter
- Test the class with print statements

**Agenda:**
- Why use a class? (5 min)
- From function to method (10 min)
- Building compute_path step by step (15 min)
- Testing your class (15 min)

---

## Slide 2: Hook — You Already Have the Algorithm
**In Lesson 4** you wrote a `compute_path` function with 4 while loops.

**Today's question:** "What if the robot needs to remember where it is?"

**With a function:**
```python
path = compute_path((0, 0), (2, 3))
# Every call needs the start position
path = compute_path((2, 3), (1, 0))
```

**With a class:**
```python
nav = Manhattan((0, 0))
path = nav.compute_path((2, 3))
# The object remembers where it started
```

**A class bundles data and behavior together.**

---

## Slide 3: Why Use a Class?
**A function knows nothing between calls.**
- You pass in start and destination every time
- Nothing remembers where the robot is

**A class stores state.**
- `self.position` remembers the robot's position
- Methods can use that stored data without extra parameters

**Real-world parallel:** A GPS app remembers your location. You only type the destination.

**Our goal:** Wrap the Lesson 4 function in a `Manhattan` class so the robot's position is stored.

---

## Slide 4: The Class Skeleton
**Two pieces: `__init__` stores data, `compute_path` does the work.**

```python
class Manhattan:
    def __init__(self, start):
        self.position = start

    def compute_path(self, destination):
        # Build and return the path
        pass
```

**What changed from the function?**
- `start` is no longer a parameter of `compute_path` — it lives in `self.position`
- `self` connects the method to the object's data

---

## Slide 5: Converting the Function to a Method
**Lesson 4 function (review):**
```python
def compute_path(start, destination):
    path = []
    current_row, current_col = start
    dest_row, dest_col = destination
    # ... 4 while loops ...
    return path
```

**Lesson 5 method — what changes?**
```python
def compute_path(self, destination):
    path = []
    current_row, current_col = self.position
    dest_row, dest_col = destination
    # ... same 4 while loops ...
    return path
```

**Only two changes:**
1. Replace `start` parameter with `self`
2. Replace `start` usage with `self.position`

**The 4 while loops stay exactly the same!**

---

## Slide 6: The 4 While Loops — No If/Else Needed
**Each direction gets its own while loop:**

```python
while current_row < dest_row:        # Move south
    current_row = current_row + 1
    path.append((current_row, current_col))

while current_row > dest_row:        # Move north
    current_row = current_row - 1
    path.append((current_row, current_col))

while current_col < dest_col:        # Move east
    current_col = current_col + 1
    path.append((current_row, current_col))

while current_col > dest_col:        # Move west
    current_col = current_col - 1
    path.append((current_row, current_col))
```

**Why does this work?** If the robot is already in the right row, the first two loops just skip. Same for columns.

**No if/else needed** — the `<` and `>` conditions handle direction automatically.

---

## Slide 7: Tracing Through an Example
**`Manhattan((0, 0)).compute_path((2, 3))`**

**Path starts empty: `[]`**

**Loop 1 — south (row < dest_row):**

| current_row | Appended |
|---|---|
| 0 -> 1 | (1, 0) |
| 1 -> 2 | (2, 0) |
| 2 == 2 | stop |

**Loop 2 — north:** 2 > 2? No, skip.

**Loop 3 — east (col < dest_col):**

| current_col | Appended |
|---|---|
| 0 -> 1 | (2, 1) |
| 1 -> 2 | (2, 2) |
| 2 -> 3 | (2, 3) |
| 3 == 3 | stop |

**Loop 4 — west:** 3 > 3? No, skip.

**Result: `[(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]` — 5 steps**

---

## Slide 8: Edge Cases
**Same row — (0, 0) to (0, 3):**
- South loop: 0 < 0? No, skip.
- North loop: 0 > 0? No, skip.
- East loop runs 3 times: `[(0, 1), (0, 2), (0, 3)]`
- 3 steps

**Going backward — (3, 3) to (1, 0):**
- South loop: 3 < 1? No, skip.
- North loop runs 2 times: `[(2, 3), (1, 3)]`
- East loop: 3 < 0? No, skip.
- West loop runs 3 times: `[(1, 2), (1, 1), (1, 0)]`
- Full path: `[(2, 3), (1, 3), (1, 2), (1, 1), (1, 0)]` — 5 steps

**Same position — (2, 2) to (2, 2):**
- All four loops skip. Path is `[]` — 0 steps.

---

## Slide 9: Your Turn!
**Activity:**
1. Open the starter file: `lesson-05-manhattan-class.py`
2. Copy your 4 while loops from Lesson 4 into the `compute_path` method
3. Uncomment the test code at the bottom
4. Run and verify these cases:

| Start | Destination | Expected Steps |
|---|---|---|
| (0, 0) | (2, 3) | 5 |
| (3, 3) | (1, 0) | 5 |
| (0, 0) | (0, 3) | 3 |
| (2, 2) | (2, 2) | 0 |

**Checkpoints:**
- Does the path NOT include the start position?
- Does `len(path)` match the expected steps?
- Does the same-position case return `[]`?

---

## Slide 10: Connection to Next Lesson
**What you did today:**
- Wrapped the Lesson 4 function in a Manhattan class
- Used `self.position` to store the robot's location
- Tested compute_path with print statements

**Next lesson (Lesson 6):**
- Write **systematic tests** for the Manhattan class
- Learn how to verify code **without a robot**
- Build confidence before putting the algorithm on hardware

**Key insight:** The algorithm is pure math — no motors, no sensors. We can test it on any computer!
