# Pacing Guide

## 18-Week Semester Overview

| Weeks | Module | Duration | Notes |
|---|---|---|---|
| 1–4 | Module 1: Driving | 3–4 weeks | Blockly foundation (weeks 1–2), Python transition (weeks 3–4) |
| 5–9 | Module 2: Line Tracking | 4–5 weeks | Heaviest module—sensors, control, first classes |
| 10–11 | Module 3: Grid Driving | 1–2 weeks | Applies Module 2 code to the grid; short module |
| 12–15 | Module 4: Manhattan | 3–4 weeks | Data structures + pathfinding; algorithmic thinking |
| 16–18 | Module 5: Pathfinding (Capstone) | 3–4 weeks | BFS + obstacle detection + capstone demo |
| (19–20) | Module 6: Dijkstra (optional) | 1–2 weeks | Only if there is time, or a second semester. Weights; BFS → Dijkstra; the slow-segment grid. The course is complete without it. |

## Week-by-Week Breakdown

### Module 1: Learning How to Drive the Robot (Weeks 1–4)

**Goal:** Students comfortable with robot hardware; fluent with Python basics and polygon-drawing function.

| Week | Phase | Content | Key Activities |
|---|---|---|---|
| **W1** | Blockly (L1–2) | Robot intro, shapes | Hardware tour; draw square on whiteboard |
| **W2** | Blockly (L3–5) | Functions, parameters, polygons | Polygon function with variable sides |
| **W3** | Python Intro (L8–9) | Hello Python, loops | Rewrite square in Python; for loops |
| **W4** | Python (L10–11) | Functions & final project | Polygon function in Python; draw multiple shapes |

**Milestones:**
- ✓ By end of W1: Robot drives forward/backward reliably
- ✓ By end of W2: Polygon function works in Blockly
- ✓ By end of W3: for loop and range() understood
- ✓ By end of W4: Final project complete—Python polygon drawer

---

### Module 2: Line Tracking (Weeks 5–9)

**Goal:** Students understand sensors, control loops, and classes; LineSensor and LineTrack classes implemented and tested.

**⌚ This is the heaviest module—allow sufficient time.**

| Week | Phase | Lessons | Key Activities |
|---|---|---|---|
| **W5** | Sensors (L1–2) | Reflectance sensor; edge detection | Sensor calibration; drive to line and stop |
| **W6** | Sensors (L3–4) | Bounce driving; random turns | Continuous edge-following; avoiding repetitive paths |
| **W7** | Control (L5–6) | Proportional control; two-sensor tracking | Edge-following with one sensor, then two |
| **W8** | Control (L7) + Classes (L8) | Intersections; LineSensor class | Detect cross; build LineSensor class |
| **W9** | Classes (L9–10) | LineTrack class; final project | Object composition; full circle-crossing program |

**Milestones:**
- ✓ By end of W5: Sensor calibration complete; can detect line vs. off-line
- ✓ By end of W6: Robot bounces when hitting edge; tested in circle
- ✓ By end of W7: Proportional control works; smooth line following
- ✓ By end of W8: LineSensor and LineTrack classes built and tested separately
- ✓ By end of W9: Full program complete—4 reversals on circle crossing

---

### Module 3: Relative Driving on the Grid (Weeks 10–11)

**Goal:** Apply Module 2 code to the grid; demonstrate sequential driving and turning.

**📝 Short module—mostly applying existing code, no new major concepts.**

| Week | Lessons | Key Activities |
|---|---|---|
| **W10** | L1–2 | Intro to grid; drive to first intersection; drive 2 intersections forward |
| **W11** | L3–4 | Turning on grid; square pattern final project |

**Milestones:**
- ✓ By end of W10: Can drive to first intersection; drive 2 intersections in a line
- ✓ By end of W11: Final project complete—square pattern with 4 turns

---

### Module 4: Manhattan Navigation (Weeks 12–15)

**Goal:** Understand coordinate systems and pathfinding; Manhattan and Navigator classes implemented and tested without hardware.

| Week | Phase | Lessons | Key Activities |
|---|---|---|---|
| **W12** | Data Structures (L1–3) | Coordinates, tuples, lists | Coordinate mapping; tuple/list practice |
| **W13** | Manhattan (L4–6) | Algorithm, implementation, testing | Hand-trace algorithm; implement Manhattan class |
| **W14** | Navigator (L7–9) | Turning logic; integration | Direction/heading logic; Navigator class |
| **W15** | Integration & Testing | Final project | Full integration; test with robot on grid |

**Milestones:**
- ✓ By end of W12: Coordinate system understood; can map grid positions
- ✓ By end of W13: Manhattan algorithm implemented; tested without hardware
- ✓ By end of W14: Navigator class complete; tested with robot
- ✓ By end of W15: Final project complete—navigate to 4+ destinations

---

### Module 5: Pathfinding Around Obstacles (Weeks 16–18)

**Goal:** Implement breadth-first search, detect obstacles with the rangefinder, and demonstrate dynamic rerouting.

| Week | Phase | Lessons | Key Activities |
|---|---|---|---|
| **W16** | Graphs & BFS (L1–3) | Graph theory, dictionaries, the ripples hand trace | Hand-trace BFS with blocked nodes; compare with `print_grid` |
| **W17** | Implementation (L4–6) | Pathfinding toolkit, `compute_bfs_path`, property tests, swapping | Implement BFS; paper tests; swap for Manhattan |
| **W18** | Capstone (L7–9) | Rangefinder, experience loop, demo | Full capstone: navigate, detect obstacles, recompute, prove "learning" |

**Milestones:**
- ✓ By end of W16: BFS understood via hand-tracing
- ✓ By end of W17: `compute_bfs_path()` passes the harness; swappable with Manhattan
- ✓ By end of W18: Capstone complete—robot navigates with obstacle avoidance


### Module 6: Dijkstra's Algorithm (Optional — Weeks 19–20, or a second semester)

**Goal:** Upgrade BFS to Dijkstra's algorithm for a grid with a slow segment.

**Only if there is time.** The course is complete at the end of Module 5 and nothing depends on this module.

| Week | Lessons | Key Activities |
|---|---|---|
| **W19** | L1–3 | Time the slow segment; add weights and a cost check to the harness (BFS fails it); copy BFS, make the two changes, run three planners through one harness |
| **W20** | L4 (+L5) | Drive the slow-segment grid: BFS run, then Dijkstra run. Classes track: the `Dijkstra` class |

**Setup:** one grid segment made deliberately slow (e.g. a winding tape detour between two adjacent intersections) that students can time with a stopwatch. See `module-06-dijkstra/README.md`.

---

## Pacing Flexibility

**If students are ahead:**
- Add extensions from exercises (listed in each lesson template)
- Challenge: Implement additional features (e.g., multiple rangefinders, optimization)
- Have them create their own challenge course or competition

**If students are behind:**
- Don't skip Module 1 Blockly phase—it builds intuition
- Extend Module 2 by another week if needed (it's heavy)
- Use solution code more liberally in later modules
- Pair struggling students with peers or provide one-on-one debugging time
- Consider reducing final project scope (e.g., 2 destinations instead of 4)

**If hardware is unavailable (simulator only):**
- All lessons are compatible with XRP simulation
- Module 3 (grid driving) requires simulated grid; otherwise no major changes
- Module 5 capstone may need adjustment (simulate obstacle detection)

---

## Key Dates / Checkpoints

| Checkpoint | Content | Week | Key Deliverable |
|---|---|---|---|
| **Checkpoint 1** | Module 1 complete | W4 | Python polygon function + multiple shapes |
| **Checkpoint 2** | Sensors & basic loops | W6 | Circle-driving with bounce logic |
| **Checkpoint 3** | Classes implemented | W9 | Full line-tracking with 4 reversals |
| **Checkpoint 4** | Grid navigation working | W11 | Square pattern |
| **Checkpoint 5** | Manhattan navigation | W15 | Multi-destination navigation |
| **Capstone Demo** | BFS + obstacles | W18 | Full autonomous navigation with learning |

---

## Per-Lesson Time Allocation

**General rule:** Each lesson takes ~45–60 minutes of instructional time, broken down as:
- Introduction: 5–10 min
- Direct instruction: 10–15 min
- Guided practice: 15–20 min
- Independent practice/exercises: 20–30 min
- Wrap-up: 5–10 min

**Adjust based on your class period length and student pace.**

---

## Tips for Staying on Track

1. **Block out learning objectives clearly** at the start of each lesson
2. **Use starter code liberally** to save time on syntax, focus on concepts
3. **Don't try to finish every exercise**—assign based on time; solutions are available
4. **Test hardware ahead of time** to avoid losing class time to setup
5. **Use code reviews and pair programming** to accelerate learning and reduce debugging time
6. **Celebrate milestones**—students stay motivated when they see progress
