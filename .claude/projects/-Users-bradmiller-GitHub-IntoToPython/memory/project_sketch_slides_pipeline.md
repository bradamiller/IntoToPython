---
name: Sketch-style slide pipeline (in progress)
description: Built a rough.js + Playwright + python-pptx pipeline to generate hand-drawn style PPTX slides; awaiting user feedback on the test output
type: project
---

Built a proof-of-concept pipeline for generating sketch-style PPTX slides for Module 3 Lesson 1.

**Pipeline:**
1. `_roughjs-illustrations.html` — HTML page with rough.js that draws all illustrations on canvas elements
2. Playwright screenshots each illustration as transparent PNG → `_illustrations/` folder
3. `build_sketch_pptx.py` — python-pptx script that assembles the PPTX with sketch fonts/colors and embeds the PNGs

**Files created (all in `module-03-grid-driving/slides/`):**
- `01-introduction-to-the-grid-sketch-test.pptx` — test PPTX output (user needs to review)
- `01-introduction-to-the-grid-sketch.html` — standalone HTML version (created first, user liked the style)
- `_roughjs-illustrations.html` — rough.js illustration source
- `_illustrations/` — 10 transparent PNGs of hand-drawn illustrations
- `build_sketch_pptx.py` — PPTX builder script

**Also created:** `templates/sketch-style-html-slides.md` — detailed style guide for reproducing the sketch look

**Why:** User saw hand-drawn/sketch-style slides in a YouTube video and wanted that aesthetic for the curriculum.

**How to apply:** When user returns, ask for feedback on the test PPTX. Key things to check: do the fonts render correctly (Caveat/Patrick Hand need to be installed), do illustrations look good at projection size, and any layout/color tweaks. If the approach works, generalize the pipeline for other lessons. A local HTTP server is needed for Playwright to access the rough.js HTML (used `python3 -m http.server 8765`).
