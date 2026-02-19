#!/usr/bin/env python3
"""Insert generated graphics into PPTX slide decks."""

import os
import sys

# Add parent directory so we can import
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.generate_grid_diagram import insert_image_into_pptx

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Each entry: (pptx_path, slide_number, image_path, left, top, width)
insertions = [
    # GRAPHIC 1: Module 4, Lesson 7, Slide 5 — Turn Lookup Table
    (
        'module-04-manhattan/slides/07-the-challenge-of-turning.pptx',
        5,
        'module-04-manhattan/slides/images/turn-lookup-table.png',
        1.5, 1.5, 5.0
    ),
    # GRAPHIC 2: Module 4, Lesson 7, Slide 7 — Path with Headings
    (
        'module-04-manhattan/slides/07-the-challenge-of-turning.pptx',
        7,
        'module-04-manhattan/slides/images/path-with-headings.png',
        1.5, 1.5, 5.0
    ),
    # GRAPHIC 3: Module 5, Lesson 1, Slide 3 — Manhattan Fails
    (
        'module-05-dijkstra/slides/01-the-grid-as-a-graph.pptx',
        3,
        'module-05-dijkstra/slides/images/manhattan-fails-with-obstacles.png',
        0.8, 1.8, 6.5
    ),
    # GRAPHIC 4: Module 5, Lesson 1, Slide 5 — 3x3 Graph
    (
        'module-05-dijkstra/slides/01-the-grid-as-a-graph.pptx',
        5,
        'module-05-dijkstra/slides/images/grid-as-graph-3x3.png',
        2.0, 1.5, 4.5
    ),
    # GRAPHIC 5a: Module 5, Lesson 3, Slide 5 — Dijkstra Setup
    (
        'module-05-dijkstra/slides/03-dijkstras-algorithm-the-concept.pptx',
        5,
        'module-05-dijkstra/slides/images/dijkstra-step0-setup.png',
        1.5, 1.5, 5.0
    ),
    # GRAPHIC 5b: Module 5, Lesson 3, Slide 6 — Dijkstra Steps 1-3
    (
        'module-05-dijkstra/slides/03-dijkstras-algorithm-the-concept.pptx',
        6,
        'module-05-dijkstra/slides/images/dijkstra-step1.png',
        1.5, 1.5, 5.0
    ),
    # GRAPHIC 5c: Module 5, Lesson 3, Slide 7 — Dijkstra Final
    (
        'module-05-dijkstra/slides/03-dijkstras-algorithm-the-concept.pptx',
        7,
        'module-05-dijkstra/slides/images/dijkstra-final.png',
        1.5, 1.5, 5.0
    ),
    # GRAPHIC 6: Module 5, Lesson 3, Slide 8 — Backpointer Path
    (
        'module-05-dijkstra/slides/03-dijkstras-algorithm-the-concept.pptx',
        8,
        'module-05-dijkstra/slides/images/backpointer-path.png',
        2.0, 1.5, 4.5
    ),
    # GRAPHIC 7: Module 4, Lesson 4, Slide 6 — Compass Rose
    (
        'module-04-manhattan/slides/04-the-manhattan-algorithm.pptx',
        6,
        'module-04-manhattan/slides/images/compass-rose-directions.png',
        2.5, 1.5, 4.0
    ),
    # GRAPHIC 8: Module 4, Lesson 1, Slide 4 — Labeled 4x4 Grid
    (
        'module-04-manhattan/slides/01-coordinates-on-the-grid.pptx',
        4,
        'module-04-manhattan/slides/images/labeled-grid-4x4.png',
        1.5, 1.5, 5.0
    ),
    # GRAPHIC 9: Module 5, Lesson 4, Slide 9 — 4x4 with Blocked
    (
        'module-05-dijkstra/slides/04-the-dijkstra-class.pptx',
        9,
        'module-05-dijkstra/slides/images/graph-4x4-blocked.png',
        1.5, 1.5, 5.0
    ),
    # GRAPHIC 10: Module 5, Lesson 9, Slide 6 — Run 1 vs Run 2
    (
        'module-05-dijkstra/slides/09-capstone-project.pptx',
        6,
        'module-05-dijkstra/slides/images/run1-vs-run2.png',
        0.8, 1.8, 6.5
    ),
]

if __name__ == '__main__':
    os.chdir(BASE)
    for pptx, slide, image, left, top, width in insertions:
        if not os.path.exists(pptx):
            print(f"WARNING: PPTX not found: {pptx}")
            continue
        if not os.path.exists(image):
            print(f"WARNING: Image not found: {image}")
            continue
        try:
            insert_image_into_pptx(pptx, slide, image,
                                   left_inches=left, top_inches=top,
                                   width_inches=width)
        except Exception as e:
            print(f"ERROR inserting {image} into {pptx} slide {slide}: {e}")
