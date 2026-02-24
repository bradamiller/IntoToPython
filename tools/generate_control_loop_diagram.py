#!/usr/bin/env python3
"""Generate the proportional control loop diagram for Module 2, Lesson 5, Slide 8."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os


def draw_control_loop_diagram(filename, figsize=(9, 7)):
    """
    Draw a circular flow diagram showing the proportional control loop:
    Read Sensor --> Calculate Error --> Calculate Correction --> Set Motors --> (back to) Read Sensor
    """
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    fig.patch.set_facecolor('white')

    # Center of the circular layout
    cx, cy = 5.0, 4.5
    radius = 2.8

    # Four steps arranged in a circle (top, right, bottom, left)
    # Angles: 90° (top), 0° (right), 270° (bottom), 180° (left)
    steps = [
        {"label": "Read\nSensor", "angle": 90, "color": "#2E75B6", "icon": "1"},
        {"label": "Calculate\nError", "angle": 0, "color": "#E67E22", "icon": "2"},
        {"label": "Calculate\nCorrection", "angle": 270, "color": "#27AE60", "icon": "3"},
        {"label": "Set\nMotors", "angle": 180, "color": "#8E44AD", "icon": "4"},
    ]

    box_width = 2.2
    box_height = 1.2
    positions = []

    for step in steps:
        angle_rad = np.radians(step["angle"])
        x = cx + radius * np.cos(angle_rad)
        y = cy + radius * np.sin(angle_rad)
        positions.append((x, y))

        # Draw rounded rectangle box
        rect = mpatches.FancyBboxPatch(
            (x - box_width / 2, y - box_height / 2),
            box_width, box_height,
            boxstyle="round,pad=0.15",
            facecolor=step["color"],
            edgecolor='white',
            linewidth=2,
            alpha=0.9,
            zorder=5
        )
        ax.add_patch(rect)

        # Step number circle
        num_circle = plt.Circle(
            (x - box_width / 2 + 0.3, y + box_height / 2 - 0.25),
            0.2, facecolor='white', edgecolor=step["color"],
            linewidth=1.5, zorder=6
        )
        ax.add_patch(num_circle)
        ax.text(x - box_width / 2 + 0.3, y + box_height / 2 - 0.25,
                step["icon"], ha='center', va='center',
                fontsize=9, fontweight='bold', color=step["color"], zorder=7)

        # Label text
        ax.text(x + 0.05, y - 0.05, step["label"], ha='center', va='center',
                fontsize=13, fontweight='bold', color='white', zorder=6)

    # Draw curved arrows between steps
    arrow_color = '#555555'
    arrow_style = mpatches.FancyArrowPatch

    # Helper to draw an arrow from one box edge to the next
    def draw_curved_arrow(start_pos, end_pos, start_angle, end_angle, bend='arc3,rad=-0.3'):
        """Draw arrow from edge of start box to edge of end box."""
        sx, sy = start_pos
        ex, ey = end_pos

        # Calculate departure point on the edge of start box
        sa_rad = np.radians(start_angle)
        # Calculate arrival point on the edge of end box
        ea_rad = np.radians(end_angle)

        # Offset from center of box to edge
        dx_s = (box_width / 2 + 0.05) * np.cos(sa_rad)
        dy_s = (box_height / 2 + 0.05) * np.sin(sa_rad)
        dx_e = (box_width / 2 + 0.05) * np.cos(ea_rad)
        dy_e = (box_height / 2 + 0.05) * np.sin(ea_rad)

        arrow = mpatches.FancyArrowPatch(
            (sx + dx_s, sy + dy_s),
            (ex + dx_e, ey + dy_e),
            arrowstyle='->', mutation_scale=20,
            connectionstyle=bend,
            color=arrow_color, linewidth=2.5, zorder=3
        )
        ax.add_patch(arrow)

    # Arrows: top->right, right->bottom, bottom->left, left->top
    # Top (Read Sensor) -> Right (Calculate Error): depart right side, arrive top
    draw_curved_arrow(positions[0], positions[1], -30, 120, 'arc3,rad=-0.3')
    # Right (Calculate Error) -> Bottom (Calculate Correction): depart bottom, arrive right
    draw_curved_arrow(positions[1], positions[2], 210, 30, 'arc3,rad=-0.3')
    # Bottom (Calculate Correction) -> Left (Set Motors): depart left, arrive bottom
    draw_curved_arrow(positions[2], positions[3], 150, -30, 'arc3,rad=-0.3')
    # Left (Set Motors) -> Top (Read Sensor): depart top, arrive left
    draw_curved_arrow(positions[3], positions[0], 30, 210, 'arc3,rad=-0.3')

    # Center label
    ax.text(cx, cy, "Control\nLoop", ha='center', va='center',
            fontsize=16, fontweight='bold', color='#1B3A5C',
            style='italic', zorder=4,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#F0F4F8',
                      edgecolor='#1B3A5C', alpha=0.8))

    # Bottom annotation
    ax.text(cx, 0.6, "This loop runs hundreds of times per second",
            ha='center', va='center', fontsize=12, color='#666666',
            style='italic',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFF9E6',
                      edgecolor='#F0C040', alpha=0.9))

    # Title
    ax.set_title('The Proportional Control Loop', fontsize=15,
                 fontweight='bold', pad=15, color='#1B3A5C')

    ax.set_xlim(0.5, 9.5)
    ax.set_ylim(0.0, 8.5)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Generated: {filename}")


if __name__ == '__main__':
    os.makedirs('module-02-line-tracking/slides/images', exist_ok=True)
    draw_control_loop_diagram('module-02-line-tracking/slides/images/control-loop-diagram.png')
