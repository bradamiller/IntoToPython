# Lesson 0: Module 4 Overview — The Big Picture

## Overview
This is a short (15-20 minute) teacher-led discussion that shows students the complete Module 4 vision before they learn any individual piece. Using top-down design, the teacher reveals the final multi-destination navigation program and then peels back the layers to show what each class does and what building blocks are needed. No coding, no worksheets. The goal is motivational framing: students see that the main program is surprisingly short because classes encapsulate the complexity, and every subsequent lesson builds one specific piece of this puzzle. This overview gives students a mental map so that when they learn tuples, lists, or classes, they already know *why* they need them.

## Learning Objectives
By the end of this lesson, students will be able to:
- Describe the overall goal of Module 4: a robot that autonomously visits multiple destinations on a grid
- Identify the two main classes (Manhattan and Navigator) and explain each one's job in one sentence
- Read the high-level main program loop and explain what each line does in plain English
- Explain what "top-down design" means: start with the big picture, then break it into smaller pieces
- Point to which lesson in the module builds each piece of the system

## Key Concepts
- **Top-down design**: Starting with the desired outcome and breaking it into progressively smaller, manageable pieces until each piece is something you know how to build
- **Separation of concerns**: Manhattan handles "where to go" (planning); Navigator handles "how to get there" (execution). Each class has one job.
- **Abstraction**: The main program does not know how paths are computed or how the robot turns. It just calls methods and trusts the classes to do their jobs.
- **Code reuse**: Navigator delegates physical movement to LineTrack from Module 2 rather than reimplementing line following and turning from scratch

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
     manhattan = Manhattan((0, 0))
     navigator = Navigator((0, 0), 0)
     destinations = [(2, 0), (2, 3), (0, 3)]

     for dest in destinations:
         path = manhattan.compute_path(dest)
         navigator.drive_path(path)
         manhattan.position = navigator.position
     ```
   - Walk through each line in plain English:
     - "Create a Manhattan object that knows how to plan paths, starting at position (0, 0)."
     - "Create a Navigator object that knows how to drive the robot, also starting at (0, 0), facing North."
     - "Here is our list of destinations to visit."
     - "For each destination: compute the path, drive the path, then update where we are."
   - Key observation: "This is the ENTIRE main program. Seven lines. It is short because the classes do all the work."
   - "You do not need to understand how `compute_path` or `drive_path` work yet. You just need to see that this is our goal."

2. **Level 2 — Two Classes, Two Jobs**:
   - Draw two boxes on the board:
     ```
     Manhattan class               Navigator class
     -----------------             -----------------
     Given: where I am             Given: a list of
       and where I want to go        intersections to visit
     Computes: a list of           Drives: the robot through
       intersections to follow       each intersection
     ```
   - Manhattan produces a path. Navigator consumes it. They connect through the path list.
   - "Manhattan never touches the robot. Navigator never does math about which route to take. Each class has one job. This is called **separation of concerns**."
   - Ask: "Why is this a good idea?" Accept answers. Bridge to: "If the path computation is wrong, you know the bug is in Manhattan. If the robot turns the wrong way, the bug is in Navigator. Keeping things separate makes debugging easier."

3. **Level 3 — What Does Navigator Need To Do?**:
   - Zoom into the Navigator. At each intersection, the robot must:
     1. **Figure out which direction to face.** If the next intersection is one row down, the robot needs to face South. If one column to the right, it needs to face East. We represent directions as numbers: 0 = North, 1 = East, 2 = South, 3 = West.
     2. **Turn to face that direction.** Keep turning right until facing the right way. We will use a simple while loop for this.
     3. **Drive forward to the next intersection.** Follow the line until detecting a cross — this is exactly what LineTrack does. You already built this in Module 2!
   - "So Navigator does not start from scratch. It reuses the line-following and turning code you already wrote. That is the power of building reusable classes."

### Your Roadmap (3-5 minutes)

1. **Map Each Piece to a Lesson**:
   - Present the roadmap:
     - **Lesson 1**: Coordinates on the grid — learn the (row, col) system
     - **Lesson 2**: Tuples — store positions as (row, col) pairs in Python
     - **Lesson 3**: Lists — store paths as lists of positions
     - **Lessons 4-5**: The Manhattan algorithm — compute paths (on paper, then in code)
     - **Lesson 6**: Testing without a robot — verify your code before running on hardware
     - **Lesson 7**: Turning logic — represent headings as numbers, count right turns on paper
     - **Lesson 8**: The Navigator class — implement turn_to() and drive_path() using LineTrack
     - **Lesson 9**: Final project — put it all together and run on the robot
   - "Every lesson builds one piece of the puzzle. Nothing is random. By Lesson 9, you will have built everything you need and connected them into a working system."

2. **Return to the Main Program**:
   - Show the main program code one more time.
   - "By Lesson 9, you will understand every line of this code — because you will have written every piece yourself."
   - "Let's get started."

### Assessment

**Formative (verbal, during discussion)**:
- Can students name the two classes and what each one does?
- Can students explain in their own words what the for loop does? ("Go through each destination, compute the path, drive it, update position.")
- Can students point to which lesson will teach a given piece? ("Which lesson teaches us how the robot decides which way to turn?" — Lesson 7.)

## Teaching Notes
- **This lesson is intentionally short.** Resist the urge to explain how anything works. The goal is the shape, not the details.
- **Students will not understand the code yet — that is expected and fine.** Tell them: "You are not supposed to understand every line right now. By Lesson 9, you will."
- **Deflect "how does it work?" questions to future lessons.** If students ask "how does compute_path work?" say "Great question — that is exactly what Lessons 4 and 5 are about." This builds anticipation.
- **Refer back to this overview at the start of every subsequent lesson.** Open each lesson with: "Remember the big picture? Today we are building [this piece]." This connects each lesson to the whole.
- **Consider printing the main program on a reference card** that students keep in their notebooks and revisit at the start of each lesson. Highlighting the piece they are building that day makes the connection concrete.
- **The pedagogical strategy here is an "advance organizer"** — showing the destination before the journey helps students understand why each step matters and how the pieces fit together.

## Connections to Next Lessons
- **Lesson 1** will introduce the coordinate system (row, col) that appears in the code as positions like (0, 0) and (2, 3)
- Every subsequent lesson builds one component shown in this overview
- **Lesson 9** will return to this exact main program and students will have built every piece themselves
- Teachers should reference this overview at the start of each lesson to maintain the connection between the individual topic and the big picture
