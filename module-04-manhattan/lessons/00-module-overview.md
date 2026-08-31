# Lesson 0: Module 4 Overview — The Big Picture

## Overview
This is a short (15-20 minute) teacher-led discussion that shows students the complete Module 4 vision before they learn any individual piece. Using top-down design, the teacher reveals the final multi-destination navigation program and then peels back the layers to show what each function does and what building blocks are needed. No coding, no worksheets. The goal is motivational framing: students see that the main program is surprisingly short because the functions encapsulate the complexity, and every subsequent lesson builds one specific piece of this puzzle. This overview gives students a mental map so that when they learn tuples, lists, or the driving functions, they already know *why* they need them.

Classes are never required to build any of this -- an optional callout at the end of this lesson mentions that courses covering OOP will see the same system rebuilt with classes in each lesson's Optional Extension, once the functions version is understood.

## Learning Objectives
By the end of this lesson, students will be able to:
- Describe the overall goal of Module 4: a robot that autonomously visits multiple destinations on a grid
- Identify the two main functions (`compute_manhattan_path` and `drive_path`) and explain each one's job in one sentence
- Read the high-level main program loop and explain what each line does in plain English
- Explain what "top-down design" means: start with the big picture, then break it into smaller pieces
- Point to which lesson in the module builds each piece of the system

## Key Concepts
- **Top-down design**: Starting with the desired outcome and breaking it into progressively smaller, manageable pieces until each piece is something you know how to build
- **Separation of concerns**: `compute_manhattan_path` handles "where to go" (planning); `drive_path` handles "how to get there" (execution). Each function has one job.
- **Abstraction**: The main program does not know how paths are computed or how the robot turns. It just calls functions and trusts them to do their jobs.
- **Code reuse**: `drive_path` calls the driving toolkit from Module 2/3 rather than reimplementing line following and turning from scratch

## Materials Required
- Projector or whiteboard for displaying code and diagrams
- No computers, robots, or worksheets needed
- Optional: printed reference card of the main program for students to keep in their notebooks

## Lesson Flow

### The Mission (5 minutes)

1. **Hook: "Here's What Your Robot Will Do"**:
   - Describe (or demonstrate on the grid) a robot that starts at one corner of the grid and visits three or four destinations in order, all by itself.
   - "No remote control. No manual steering. The robot figures out the path and drives it, intersection by intersection."
   - "That sounds hard. How would you even start building something like that?"

2. **Collect Student Ideas**:
   - Ask: "If you had to break this problem into smaller pieces, what would the pieces be?"
   - Students might say: know where you are, know where to go, figure out the route, make the robot move, turn corners, follow the line...
   - Validate all reasonable answers: "You are already thinking like a software designer. The strategy you are using has a name: **top-down design**. Start with the big problem, break it into smaller ones, then break those into even smaller ones, until you reach something you know how to do."

### Peeling Back the Layers (10 minutes)

1. **Level 1 — The Main Program**:
   - Show the main program on the projector:
     ```python
     position = (0, 0)
     heading = 0

     destinations = [(2, 0), (2, 3), (0, 3)]

     for dest in destinations:
         path = compute_manhattan_path(position, dest)
         position, heading = drive_path(path, position, heading)
     ```
   - Walk through each line in plain English:
     - "Start tracking the robot's position at (0, 0)."
     - "Start tracking its heading -- 0 means facing North."
     - "Here is our list of destinations to visit."
     - "For each destination: compute the path, then drive it -- and update where we are and which way we're facing from what driving the path actually did."
   - Key observation: "This is the ENTIRE main program. Seven lines. It is short because the functions do all the work."
   - "You do not need to understand how `compute_manhattan_path` or `drive_path` work yet. You just need to see that this is our goal."

2. **Level 2 — Two Functions, Two Jobs**:
   - Draw two boxes on the board:
     ```
     compute_manhattan_path()      drive_path()
     -----------------             -----------------
     Given: where I am             Given: a list of
       and where I want to go        intersections to visit
     Computes: a list of           Drives: the robot through
       intersections to follow       each intersection
     ```
   - `compute_manhattan_path` produces a path. `drive_path` consumes it. They connect through the path list -- and through the plain `position`/`heading` variables the main program carries from one call to the next.
   - "`compute_manhattan_path` never touches the robot. `drive_path` never does math about which route to take. Each function has one job. This is called **separation of concerns**."
   - Ask: "Why is this a good idea?" Accept answers. Bridge to: "If the path computation is wrong, you know the bug is in `compute_manhattan_path`. If the robot turns the wrong way, the bug is in `drive_path`. Keeping things separate makes debugging easier."

3. **Level 3 — What Does `drive_path` Need To Do?**:
   - Zoom into `drive_path`. At each intersection, the robot must:
     1. **Figure out which direction to face.** If the next intersection is one row down, the robot needs to face South. If one column to the right, it needs to face East. We represent directions as numbers: 0 = North, 1 = East, 2 = South, 3 = West.
     2. **Turn to face that direction.** Keep turning right until facing the right way. We will use a simple while loop for this.
     3. **Drive forward to the next intersection.** Follow the line until detecting a cross — this is exactly what the driving toolkit does. You already built this in Module 2!
   - "So `drive_path` does not start from scratch. It reuses the line-following and turning code you already wrote. That is the power of building a reusable toolkit."

### Your Roadmap (3-5 minutes)

1. **Map Each Piece to a Lesson**:
   - Present the roadmap:
     - **Lesson 1**: Coordinates on the grid — learn the (row, col) system
     - **Lesson 2**: Tuples — store positions as (row, col) pairs in Python
     - **Lesson 3**: Lists — store paths as lists of positions
     - **Lessons 4-5**: The Manhattan algorithm — compute paths (on paper, then in code)
     - **Lesson 6**: Testing without a robot — verify your code before running on hardware
     - **Lesson 7**: Turning logic — represent headings as numbers, count right turns on paper
     - **Lesson 8**: Driving the path — implement `turn_to()` and `drive_path()` using the Module 2/3 toolkit
     - **Lesson 9**: Final project — put it all together and run on the robot
   - "Every lesson builds one piece of the puzzle. Nothing is random. By Lesson 9, you will have built everything you need and connected them into a working system."

2. **Return to the Main Program**:
   - Show the main program code one more time.
   - "By Lesson 9, you will understand every line of this code — because you will have written every piece yourself."
   - "Let's get started."

### Assessment

**Formative (verbal, during discussion)**:
- Can students name the two functions and what each one does?
- Can students explain in their own words what the for loop does? ("Go through each destination, compute the path, drive it, and update position/heading from what driving returned.")
- Can students point to which lesson will teach a given piece? ("Which lesson teaches us how the robot decides which way to turn?" — Lesson 7.)

## Teaching Notes
- **This lesson is intentionally short.** Resist the urge to explain how anything works. The goal is the shape, not the details.
- **Students will not understand the code yet — that is expected and fine.** Tell them: "You are not supposed to understand every line right now. By Lesson 9, you will."
- **Deflect "how does it work?" questions to future lessons.** If students ask "how does compute_manhattan_path work?" say "Great question — that is exactly what Lessons 4 and 5 are about." This builds anticipation.
- **Refer back to this overview at the start of every subsequent lesson.** Open each lesson with: "Remember the big picture? Today we are building [this piece]." This connects each lesson to the whole.
- **Consider printing the main program on a reference card** that students keep in their notebooks and revisit at the start of each lesson. Highlighting the piece they are building that day makes the connection concrete.
- **The pedagogical strategy here is an "advance organizer"** — showing the destination before the journey helps students understand why each step matters and how the pieces fit together.
- **If your course also covers classes**, mention briefly that every lesson from here on has an Optional Extension showing the same system rebuilt with `Manhattan` and `Navigator` objects -- but don't preview it now. Let students build the functions version first; the class version makes a lot more sense once they've felt what it's replacing.

## Connections to Next Lessons
- **Lesson 1** will introduce the coordinate system (row, col) that appears in the code as positions like (0, 0) and (2, 3)
- Every subsequent lesson builds one component shown in this overview
- **Lesson 9** will return to this exact main program and students will have built every piece themselves
- Teachers should reference this overview at the start of each lesson to maintain the connection between the individual topic and the big picture
