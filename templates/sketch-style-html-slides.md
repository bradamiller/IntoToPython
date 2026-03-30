# Sketch-Style HTML Slide Deck Instructions

Use these instructions when generating HTML slide decks in the hand-drawn/sketch style for the IntroToPython curriculum.

## Reference Implementation

See `module-03-grid-driving/slides/01-introduction-to-the-grid-sketch.html` for a complete working example.

---

## Design Philosophy

The slides should feel like a friendly whiteboard sketch — informal, visual, and approachable for students learning Python with physical robots. Prioritize illustrations and diagrams over bullet-heavy text. Every slide should have at least one visual element (SVG illustration, callout box, or diagram).

---

## Fonts (Google Fonts)

Include this in the `<head>`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@400;600;700&family=Patrick+Hand&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
```

| Purpose | Font | Usage |
|---------|------|-------|
| Slide titles, section headers, labels | `'Caveat', cursive` | Large, slightly rotated for hand-drawn feel |
| Body text, bullets, navigation | `'Patrick Hand', cursive` | Readable hand-written style |
| Code blocks, inline code | `'Fira Code', monospace` | Clean monospace for Python code |

---

## Color Palette

| Name | Hex | Usage |
|------|-----|-------|
| Teal Blue | `#5b8fa8` | Headers, accents, primary callout borders, sidebar highlights |
| Warm Orange | `#e8a87c` | Highlights, arrows, emphasis borders, question boxes, "current" markers |
| Soft Green | `#85c88a` | Success/answer callouts, checkpoints, third accent color |
| Dark Text | `#2d3436` | Primary body text, SVG strokes |
| Muted Gray | `#636e72` | Secondary text, labels |
| Border Gray | `#b8c5d0` | Borders, dividers, sidebar border, progression arrows |
| Paper Background | `#fdfcfa` | Slide background |
| Sidebar Background | `#faf8f5` | Navigation sidebar |
| Code Background | `#f0ede8` | Code block fills |

Use colors at low opacity for fills (e.g., `rgba(91, 143, 168, 0.12)`) to keep the light, airy feel.

---

## Layout Structure

### Page Layout
- **Left sidebar** (240px) with navigation links — light background with subtle ruled lines
- **Slides container** fills remaining viewport width
- Slides are full-height (`100vh`), one visible at a time

### Slide Layout
- **Title bar** at top: light background with teal bottom border (NOT a dark filled bar)
- **Content area** below with generous padding (30px 50px)
- **Navigation** fixed at bottom center with prev/next buttons and slide counter
- Subtle notebook-paper ruled lines in the background (`background-image: linear-gradient(...)`)

---

## Sketch-Style CSS Techniques

### Slight rotations for hand-drawn feel
Apply small `transform: rotate(-0.5deg)` to titles, code blocks, and illustration boxes. Keep rotation between -1deg and 1deg.

### Box shadows
Use offset solid shadows instead of blurs: `box-shadow: 3px 3px 0 rgba(91, 143, 168, 0.15)`

### Border radius
Use generous radius (`12px`-`14px`) on all boxes for rounded, friendly shapes.

### Double underlines on title bar
Use `::after` pseudo-element with a slightly rotated line below the border for a sketch effect.

### Bullet points
Style with colored circles using `::before` pseudo-elements instead of default list markers. Use teal for level-0 bullets, orange for level-1.

---

## Content Block Styles

### Code Blocks
```css
.code-block {
    background-color: #f0ede8;
    border: 2px solid #b8c5d0;
    border-radius: 12px;
    padding: 18px 22px;
    font-family: 'Fira Code', monospace;
    font-size: 16px;
    box-shadow: 3px 3px 0 rgba(91, 143, 168, 0.15);
    transform: rotate(-0.2deg);
}
```
Add a `::before` label showing `< / >` in a small bordered pill in the top-right corner. **Hide this badge** on compact/inline code blocks near SVGs (add `display: none` to the `::before` when the code block has inline styles for small sizing).

### Question Boxes (dashed orange border)
Use for posing questions to students. Add a `?` circle badge in the top-left using `::before`.

### Answer Boxes (dashed green border)
Use for revealing answers. Add a `!` circle badge in the top-left using `::before`.

### Insight Boxes (solid orange border)
Use for key takeaways. Centered text in Caveat font, slightly rotated, with offset shadow.

### Sketch Boxes (solid teal border)
General-purpose containers for grouping related content. Light teal background fill.

### Activity Steps
Numbered circles (teal background, white text) with step descriptions. Use for hands-on exercises.

### Checkpoints
Empty bordered squares (green) for students to mentally check off. Use for verification steps.

---

## SVG Illustrations

Every slide should include at least one inline SVG illustration. These are key to the sketch feel.

### Robot Icon (XRP Style — Top-Down View)
The robot is depicted as a top-down view of the SparkFun XRP robot:
- Square gray body (`fill="#b8c5d0"`, `stroke="#2d3436"`, `rx="3"`, typically 24x24)
- "XRP" label text centered on body (Caveat font, 8px, `fill="#2d3436"`)
- Dark gray sensor bar protruding from the front (`fill="#636e72"`, typically 8x16, `rx="2"`)
- Two red reflectance sensors (S1/S2) on the bar (`fill="#e85d5d"`, typically 4x4, `rx="1"`)
- **NO wheels** — the XRP robot does not show wheels in illustrations
- Sensors should straddle the line being followed (one on each side)
- Orient the sensor bar based on travel direction (right=bar on right, down=bar on bottom, etc.)

Example (robot traveling right):
```svg
<rect x="X" y="Y" width="24" height="24" rx="3" fill="#b8c5d0" stroke="#2d3436" stroke-width="2"/>
<text x="X+12" y="Y+16" font-family="Caveat, cursive" font-size="8" fill="#2d3436" text-anchor="middle" font-weight="600">XRP</text>
<rect x="X+22" y="Y+4" width="8" height="16" rx="2" fill="#636e72" stroke="#2d3436" stroke-width="1"/>
<rect x="X+28" y="Y+6" width="4" height="4" rx="1" fill="#e85d5d" stroke="#2d3436" stroke-width="1"/>
<rect x="X+28" y="Y+14" width="4" height="4" rx="1" fill="#e85d5d" stroke="#2d3436" stroke-width="1"/>
```

### Grid Diagrams
- Dark lines for the grid paths (`stroke="#2d3436"`, `stroke-width="2.5-3"`)
- **NO circles at intersections** — just plain crossing lines like the real grid
- Row/column labels in Caveat font, teal color
- Robot icons placed on the grid to show position

### Flow/Arrow Diagrams
- Curved paths using SVG `<path>` with cubic beziers for organic feel
- Dashed lines (`stroke-dasharray="6,4"`) for movement paths
- Orange filled triangular arrowheads (`<polygon>`)
- Caveat font labels along the paths

### Progression Diagrams
- Rounded rectangle steps connected by arrows
- Current/active step highlighted with orange border and background
- Step labels in Caveat font

### Comparison Diagrams
- Two rounded boxes side by side with an arrow between them
- Different accent colors for source vs. destination

### General SVG Guidelines
- Use `stroke="#2d3436"` and `stroke-width="2-2.5"` for consistent hand-drawn line weight
- Apply small rotations (`transform="rotate(-1 cx cy)"`) to shapes for organic feel
- Keep viewBox dimensions appropriate — typically 400-600px wide, 80-260px tall
- Use Caveat font for all text labels within SVGs
- Use the three accent colors (teal, orange, green) consistently for different semantic meanings

---

## Navigation

### Sidebar
- Shows module name and lesson number at top
- Lists all slide titles as clickable links
- Active slide highlighted with left border and teal background

### Bottom Navigation Bar
- Centered, rounded pill shape with border
- Previous/Next buttons with teal border, hand-style font
- Slide counter in Caveat font (e.g., "3 / 10")

### Keyboard Navigation
- Right arrow or spacebar: next slide
- Left arrow: previous slide

---

## Title Slide (Slide 1) — Special Layout

The title slide differs from content slides:
- No title bar — instead, full-page centered layout
- Robot SVG illustration at top
- Module label in small Patrick Hand font with letter-spacing
- Lesson title in large Caveat font (64px), slightly rotated, with orange underline via `::after`
- Two-column layout below for Learning Objectives (left) and Agenda (right)
- Section headers in Caveat with teal underline

---

## Two-Column Layouts

Use `display: flex; gap: 30px` for side-by-side content. Common patterns:
- Code on left, illustration on right (slides showing code + what happens)
- Today's recap on left, next lesson preview on right (wrap-up slides)

---

## File Naming Convention

```
NN-lesson-title-sketch.html
```

Example: `01-introduction-to-the-grid-sketch.html`

---

## Generating from Outline Markdown

When creating slides from an existing `*-outline.md` file:

1. Parse the outline for slide titles and content blocks (text, bullets, code, tables)
2. Map each slide to the appropriate layout:
   - Slide 1 → Title slide (special layout)
   - Slides with code + text → Two-column layout
   - Slides with tables → Table with sketch styling
   - Activity slides → Numbered step layout with checkpoints
   - Final slide → Two-column recap/preview
3. Add SVG illustrations relevant to each slide's content
4. Use callout boxes (question, answer, insight) to break up text and add visual interest
5. Ensure every slide has at least one visual element beyond plain text/bullets

---

## Robot Code Conventions

When showing XRP robot code examples in slides:

- **Never use time-based movement**: No `time.sleep()`, no `set_effort() + sleep`, no timed drives
- **Clearing intersections**: After every `track_until_cross()`, always call `tracker.drivetrain.straight(8, 0.5)` to drive forward 8 cm (the distance from front sensors to rear turning center). This aligns the robot's turning center over the intersection for correct turns.
- **`drivetrain.straight(distance, effort)`**: Takes exactly 2 parameters — distance in cm, effort from -1 to 1. There is no units parameter.
- **Always clear**: Never skip clearing with conditional logic. Every intersection arrival needs clearing.
- **Pattern**:
```python
tracker.track_until_cross()
tracker.drivetrain.straight(8, 0.5)  # clear intersection
```
