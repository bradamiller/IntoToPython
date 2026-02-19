#!/usr/bin/env python3
"""Generate grid diagrams for course slides.

This script creates grid path visualizations as PNG images
and can insert them into existing PPTX files.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import numpy as np


def draw_grid_path(filename, rows, cols, path, blocked=None,
                   start_label="START", end_label="END",
                   title=None, figsize=(8, 6)):
    """
    Draw a grid with a highlighted path.

    Parameters:
        filename: output PNG path
        rows, cols: grid dimensions
        path: list of (row, col) tuples
        blocked: list of (row, col) tuples for blocked nodes (optional)
        start_label, end_label: labels for first/last path nodes
        title: optional title text
        figsize: figure size in inches
    """
    if blocked is None:
        blocked = []

    fig, ax = plt.subplots(1, 1, figsize=figsize)

    # Colors
    GRID_COLOR = '#CCCCCC'
    PATH_COLOR = '#2E75B6'
    PATH_FILL = '#D6E8F7'
    BLOCKED_COLOR = '#FF6B6B'
    BLOCKED_FILL = '#FFD4D4'
    NODE_COLOR = '#333333'
    START_COLOR = '#27AE60'
    END_COLOR = '#E74C3C'
    BG_COLOR = '#FAFAFA'

    ax.set_facecolor(BG_COLOR)
    fig.patch.set_facecolor('white')

    # Draw grid lines
    for r in range(rows):
        for c in range(cols):
            # Horizontal edges
            if c < cols - 1:
                ax.plot([c, c + 1], [rows - 1 - r, rows - 1 - r],
                        color=GRID_COLOR, linewidth=1.5, zorder=1)
            # Vertical edges
            if r < rows - 1:
                ax.plot([c, c], [rows - 1 - r, rows - 2 - r],
                        color=GRID_COLOR, linewidth=1.5, zorder=1)

    # Draw blocked nodes
    for (br, bc) in blocked:
        y = rows - 1 - br
        circle = plt.Circle((bc, y), 0.25, facecolor=BLOCKED_FILL,
                             edgecolor=BLOCKED_COLOR, linewidth=2, zorder=3)
        ax.add_patch(circle)
        ax.text(bc, y, 'X', ha='center', va='center',
                fontsize=14, fontweight='bold', color=BLOCKED_COLOR, zorder=4)

    # Draw path edges (thick colored lines with arrows)
    for i in range(len(path) - 1):
        r1, c1 = path[i]
        r2, c2 = path[i + 1]
        y1 = rows - 1 - r1
        y2 = rows - 1 - r2
        # Draw thick path line
        ax.annotate('', xy=(c2, y2), xytext=(c1, y1),
                    arrowprops=dict(arrowstyle='->', color=PATH_COLOR,
                                    lw=3, mutation_scale=20),
                    zorder=5)

    # Draw all grid nodes
    for r in range(rows):
        for c in range(cols):
            y = rows - 1 - r
            if (r, c) in blocked:
                continue

            is_on_path = (r, c) in path
            is_start = path and (r, c) == path[0]
            is_end = path and (r, c) == path[-1]

            if is_start:
                color = START_COLOR
                size = 0.28
            elif is_end:
                color = END_COLOR
                size = 0.28
            elif is_on_path:
                color = PATH_COLOR
                size = 0.22
            else:
                color = NODE_COLOR
                size = 0.12

            if is_on_path:
                circle = plt.Circle((c, y), size, facecolor='white',
                                     edgecolor=color, linewidth=2.5, zorder=6)
                ax.add_patch(circle)
                circle2 = plt.Circle((c, y), size * 0.5, facecolor=color,
                                      edgecolor=color, linewidth=0, zorder=7)
                ax.add_patch(circle2)
            else:
                circle = plt.Circle((c, y), size, facecolor=NODE_COLOR,
                                     edgecolor=NODE_COLOR, linewidth=0, zorder=6)
                ax.add_patch(circle)

    # Add coordinate labels
    for c in range(cols):
        ax.text(c, rows - 0.3, f'Col {c}', ha='center', va='center',
                fontsize=10, color='#666666', fontweight='bold')
    for r in range(rows):
        y = rows - 1 - r
        ax.text(-0.7, y, f'Row {r}', ha='center', va='center',
                fontsize=10, color='#666666', fontweight='bold')

    # Add start/end labels
    if path:
        sr, sc = path[0]
        sy = rows - 1 - sr
        # Place start label to the right if at col 0, otherwise above
        if sc == 0:
            ax.text(sc + 0.5, sy + 0.35, start_label, ha='left', va='bottom',
                    fontsize=11, fontweight='bold', color=START_COLOR, zorder=8)
        else:
            ax.text(sc, sy + 0.5, start_label, ha='center', va='bottom',
                    fontsize=11, fontweight='bold', color=START_COLOR, zorder=8)

        er, ec = path[-1]
        ey = rows - 1 - er
        ax.text(ec, ey - 0.5, end_label, ha='center', va='top',
                fontsize=11, fontweight='bold', color=END_COLOR, zorder=8)

    # Add title
    if title:
        ax.set_title(title, fontsize=14, fontweight='bold', pad=20, color='#1B3A5C')

    # Formatting
    ax.set_xlim(-1, cols)
    ax.set_ylim(-1, rows)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Generated: {filename}")


def insert_image_into_pptx(pptx_path, slide_number, image_path,
                            left_inches=1.5, top_inches=1.5,
                            width_inches=5, output_path=None):
    """
    Insert an image into an existing PPTX file on a specific slide.

    Parameters:
        pptx_path: path to existing PPTX file
        slide_number: 1-indexed slide number
        image_path: path to PNG image
        left_inches, top_inches: position from top-left
        width_inches: image width (height auto-scaled)
        output_path: where to save (defaults to overwriting pptx_path)
    """
    from pptx import Presentation
    from pptx.util import Inches

    prs = Presentation(pptx_path)
    slide = prs.slides[slide_number - 1]  # Convert to 0-indexed

    slide.shapes.add_picture(
        image_path,
        Inches(left_inches),
        Inches(top_inches),
        Inches(width_inches)
    )

    save_path = output_path or pptx_path
    prs.save(save_path)
    print(f"Inserted {image_path} into slide {slide_number} of {save_path}")


if __name__ == '__main__':
    # === Proof of concept: Manhattan path (0,0) to (2,3) ===
    draw_grid_path(
        'module-04-manhattan/slides/images/path-0_0-to-2_3.png',
        rows=3, cols=4,
        path=[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)],
        title='Manhattan Path: (0, 0) → (2, 3)',
        figsize=(8, 5)
    )

    # === With obstacles: Dijkstra example ===
    draw_grid_path(
        'module-05-dijkstra/slides/images/dijkstra-with-obstacles.png',
        rows=4, cols=4,
        path=[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (3, 0)],
        blocked=[(1, 0), (1, 1)],
        title='Dijkstra Path Around Obstacles',
        figsize=(7, 7)
    )
