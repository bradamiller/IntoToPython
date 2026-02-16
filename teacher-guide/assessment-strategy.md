# Assessment Strategy

## Overview

Assessment in this course focuses on **demonstrating competency through working code** rather than traditional tests. Students show understanding by:
1. Writing code that solves concrete problems
2. Debugging and improving their own solutions
3. Explaining their code and design decisions
4. Building progressively more complex programs

## Types of Assessment

### 1. Formative Assessment (Ongoing, Low-Stakes)

#### Exercise Completion
- Each lesson has 2–4 exercises
- **Criteria:** Code runs, produces expected output, meets requirements
- **Grading:** Completion-based (All Done, In Progress, Not Done) or simple rubric

#### Debugging Logs
- Students maintain a log of errors encountered and how they fixed them
- **Purpose:** Reflect on problem-solving process, identify patterns
- **Frequency:** Weekly review

#### Code Reviews (Peer & Self)
- Students exchange code with a peer and provide feedback
- Checklist: Does it work? Is it readable? Are there improvements?
- **Frequency:** After every major exercise

#### Participation & Collaboration
- Observation during labs
- **Criteria:** Engagement, questions asked, helping others, persistence

---

### 2. Module Checkpoints (Summative, Building Toward Capstone)

Each module ends with a **final project** that demonstrates mastery of that module's concepts.

#### Module 1: Polygon Function
- **Deliverable:** Python program with `draw_polygon(sides, size)` function drawing 4+ shapes
- **Rubric:**
  - [ ] Function takes parameters correctly (sides, size)
  - [ ] Loop logic is correct (calculates & turns proper angles)
  - [ ] Code is readable & well-commented
  - [ ] Program runs without errors
  - [ ] Output is visually correct (robot draws recognizable shapes)
- **Pass/Fail or Points:** Up to you; completion usually sufficient at this stage

#### Module 2: Line Tracking with 4 Reversals
- **Deliverable:** Robot follows circle, detects cross, reverses 4 times before stopping
- **Rubric:**
  - [ ] LineSensor class written with required methods
  - [ ] LineTrack class uses LineSensor (composition demonstrated)
  - [ ] Robot tracks line smoothly
  - [ ] Robot detects and responds to cross correctly
  - [ ] 4 reversals completed successfully
  - [ ] Code is organized and well-commented
- **Grading:** Rubric (5 points each criterion) or checklist pass/fail

#### Module 3: Square Pattern on Grid
- **Deliverable:** Robot drives 2 intersections per side, 4 sides, returns to start
- **Rubric:**
  - [ ] Uses LineTrack class from Module 2
  - [ ] Correctly counts/drives to intersections
  - [ ] Turns properly (90° onto new line)
  - [ ] Pattern closes (returns to start)
  - [ ] Documented and tested
- **Grading:** Pass/fail or points

#### Module 4: Manhattan Navigation to 4+ Destinations
- **Deliverable:** Program navigates to list of destinations, computes & follows paths
- **Rubric:**
  - [ ] Coordinates understood (tuples used correctly)
  - [ ] Manhattan class implements algorithm correctly
  - [ ] Navigator class handles turning/heading
  - [ ] Paths computed correctly (tested without hardware first)
  - [ ] Robot follows paths on grid to all destinations
  - [ ] Code is modular and tested
  - [ ] Documentation explains algorithm
- **Grading:** Rubric (5–10 points per criterion)

#### Module 5: Dijkstra Capstone
- **Deliverable:** Robot navigates with obstacle avoidance; demonstrates "learning" over multiple runs
- **Rubric:**
  - [ ] Dijkstra class implements algorithm correctly
  - [ ] Tested with various blocked node sets
  - [ ] Rangefinder detects obstacles at intersections
  - [ ] Blocked nodes added to list dynamically
  - [ ] Robot reroutes successfully on 2nd+ attempts
  - [ ] Demonstrates improvement (fewer collisions on subsequent runs)
  - [ ] Code is well-documented and tested
  - [ ] Student explains algorithm design choices verbally or in writing
- **Grading:** Rubric (10 points per criterion) or point-based (50–100 points total)

---

### 3. Final Capstone Demonstration (High-Stakes)

**Format:** Live demo + explanation

**Setup:** Teacher places physical obstacles on grid; student navigates to pre-set destinations.

**Success Criteria:**
1. Robot successfully reaches all destinations on first run with no obstacles
2. When obstacles are present, robot detects them and recalculates path
3. On subsequent runs (with known blocked intersections), robot finds more efficient routes
4. Code is demonstrated and student can explain key design decisions
5. Student reflects on challenges and solutions

**Grading:**
- **Excellent (A):** All criteria met; smooth execution; clear understanding
- **Good (B):** All criteria met; minor hiccups; solid understanding
- **Satisfactory (C):** Most criteria met; some debugging needed; basic understanding
- **Needs Work (D/F):** Several criteria not met; significant issues; incomplete understanding

---

## Rubric Examples

### Code Quality Rubric (Applies to All Modules)

| Criterion | Excellent | Good | Satisfactory | Needs Work |
|---|---|---|---|---|
| **Functionality** | Code runs perfectly; all requirements met | Code runs; minor bugs or missing features | Code mostly works; some bugs or missing features | Code doesn't run or is incomplete |
| **Code Style** | Well-organized, readable, good naming | Generally well-organized; mostly clear | Somewhat disorganized; unclear in places | Disorganized; difficult to read |
| **Comments** | Clear, helpful comments throughout | Comments explain key logic | Some comments; not always clear | Few or no comments |
| **Testing** | Thoroughly tested; works in multiple scenarios | Tested; works in main scenarios | Minimal testing | Not tested |
| **Debugging** | Identified and fixed own issues | Fixed issues with minimal help | Needed help debugging | Unable to debug effectively |

### Algorithm Understanding Rubric (Modules 4–5)

| Criterion | Excellent | Good | Satisfactory | Needs Work |
|---|---|---|---|---|
| **Algorithm Logic** | Correctly implements algorithm; handles edge cases | Correctly implements; minor edge case misses | Basic implementation; some errors | Significant algorithm misunderstandings |
| **Testing Without Hardware** | Thoroughly tested with multiple inputs | Tested; works for standard cases | Minimal testing | Not tested before hardware |
| **Explanation** | Can clearly explain algorithm and design choices | Can explain algorithm & choices | Can explain basic algorithm | Cannot explain algorithm |
| **Separation of Concerns** | Algorithm isolated from robot control | Mostly separated; minor coupling | Some separation; partially coupled | Tightly coupled; hard to test |

---

## Assessment Timeline

| When | What | Purpose |
|---|---|---|
| **Lesson start** | Learning objectives review | Set expectations |
| **During lesson** | Observation, questions, quick checks | Identify misconceptions early |
| **After lesson** | Exercise completion, debugging log | Formative feedback |
| **Weekly** | Code review or reflection | Metacognition, peer learning |
| **Module end** | Final project checkpoint | Summative—demonstrate mastery |
| **W18** | Capstone demo + reflection | Demonstrate competency, celebrate growth |

---

## Feedback Practices

### For Exercises (Formative)
- **Quick feedback:** "Does it run? Does it produce the expected output?" (Check mark or revision needed)
- **Detailed feedback:** Code review comments highlighting strengths and one improvement
- **Turnaround:** Same day or next day when possible

### For Module Checkpoints (Summative)
- **Rubric-based feedback:** Score + comment on each criterion
- **Conferences:** Brief conversation about strengths and next steps
- **Turnaround:** Within 1 week (before next module starts)

### For Capstone Demo
- **Live feedback:** Celebrate successes during demo
- **Written reflection:** "What went well? What was challenging? What did you learn?"
- **Grade provided:** Within 1 week

---

## Accommodations & Differentiation

### For Students Struggling With Coding
- Pair with more advanced peer (driver/navigator roles)
- Provide more detailed starter code
- Use solution code as a reference (ask: "What does this line do?")
- Extend deadlines slightly; focus on understanding over speed

### For Highly Capable Students
- Challenge: Implement additional features (e.g., A* algorithm instead of Manhattan, multiple robots, time-based challenges)
- Lead code reviews and help peers
- Create documentation or tutorials for younger students
- Extend the capstone (e.g., optimize paths, handle dynamic obstacles)

### For Students With Different Learning Styles
- **Visual:** Provide flowcharts, diagrams, trace examples on whiteboard
- **Kinesthetic:** Hands-on robot activity; let them physically walk through the algorithm
- **Verbal:** Encourage explanation & discussion; pair programming with talking aloud

---

## Grading Philosophy

**Mastery-based:** Grade reflects what students can do, not average of all attempts.

- **Early attempts:** Formative, feedback-focused, low/no stakes
- **Final projects:** Summative, graded against rubric
- **Resubmissions:** Allowed if student incorporates feedback
- **Growth:** Emphasis on progress (did you improve? do you understand better?)

**Suggested Grade Weights (Adjust for your context):**

| Component | Weight |
|---|---|
| Formative (exercises, labs, code reviews) | 40% |
| Module Checkpoints (5 final projects) | 40% |
| Capstone Demo + Reflection | 20% |

**Minimum Competency:** To pass the course, student must:
- Complete all 5 module projects (at least partial credit on each)
- Participate in capstone demo
- Show effort and growth throughout the semester

---

## Questions for Reflection

As you grade and assess, consider:
1. Can the student explain what their code does?
2. Did the student debug effectively, or did they give up?
3. Is the code readable and well-organized?
4. Does the student understand the underlying concept, not just the syntax?
5. How has the student's problem-solving improved over time?

---

## Resources for Teachers

- [Rubric Builder](https://www.ispringsolutions.com/blog/edtech/assignment-rubric) or use the templates provided
- Checklist for quick assessments
- Peer review forms (see templates folder)
- Student self-assessment reflection templates

