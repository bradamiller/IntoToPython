#!/usr/bin/env python3
"""Generate the setpoint cross-section diagram for Module 2, Lesson 5."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os


def draw_setpoint_diagram(filename, figsize=(10, 5)):
    """
    Draw a cross-section of a taped line showing sensor readings
    across the white-edge-black transition.
    """
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    fig.patch.set_facecolor('white')

    # --- Top section: physical cross-section of the tape ---
    # White surface (left)
    white_rect = mpatches.FancyBboxPatch(
        (0, 2.8), 4.5, 1.2, boxstyle="round,pad=0.05",
        facecolor='#F5F5F5', edgecolor='#CCCCCC', linewidth=1.5)
    ax.add_patch(white_rect)
    ax.text(2.25, 3.4, 'White Surface', ha='center', va='center',
            fontsize=12, color='#666666', fontweight='bold')

    # Edge zone (middle)
    edge_rect = mpatches.FancyBboxPatch(
        (4.5, 2.8), 1.0, 1.2, boxstyle="round,pad=0.05",
        facecolor='#B0B0B0', edgecolor='#888888', linewidth=1.5)
    ax.add_patch(edge_rect)
    ax.text(5.0, 3.4, 'Edge', ha='center', va='center',
            fontsize=11, color='white', fontweight='bold')

    # Black tape (right)
    black_rect = mpatches.FancyBboxPatch(
        (5.5, 2.8), 4.5, 1.2, boxstyle="round,pad=0.05",
        facecolor='#2C2C2C', edgecolor='#111111', linewidth=1.5)
    ax.add_patch(black_rect)
    ax.text(7.75, 3.4, 'Black Tape', ha='center', va='center',
            fontsize=12, color='white', fontweight='bold')

    # --- Sensor reading curve ---
    x = np.linspace(0, 10, 200)
    # Sigmoid-like transition from ~0.1 (white) to ~0.9 (black)
    sensor = 0.1 + 0.8 / (1 + np.exp(-3 * (x - 5.0)))

    # Scale to plot coordinates
    plot_x = x
    plot_y = sensor * 2.2 + 0.2  # Scale 0-1 range to 0.2-2.4

    ax.plot(plot_x, plot_y, color='#2E75B6', linewidth=3, zorder=5)

    # --- Y-axis labels (sensor readings) ---
    for val, label in [(0.1, '0.1'), (0.3, '0.3'), (0.5, '0.5'), (0.7, '0.7'), (0.9, '0.9')]:
        y_pos = val * 2.2 + 0.2
        ax.text(-0.5, y_pos, label, ha='center', va='center',
                fontsize=10, color='#333333')
        ax.plot([-0.15, 0], [y_pos, y_pos], color='#CCCCCC', linewidth=0.8)

    ax.text(-0.5, 2.6, 'Sensor\nReading', ha='center', va='center',
            fontsize=10, color='#333333', fontweight='bold')

    # --- Setpoint line and annotation ---
    setpoint_y = 0.5 * 2.2 + 0.2  # y position for 0.5
    ax.plot([0, 10], [setpoint_y, setpoint_y], color='#E74C3C',
            linewidth=2, linestyle='--', zorder=4, alpha=0.7)
    ax.text(1.5, setpoint_y + 0.2, 'setpoint = 0.5', ha='center', va='bottom',
            fontsize=11, color='#E74C3C', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#E74C3C', alpha=0.9))

    # --- Arrow pointing to the edge ---
    ax.annotate('This is where\nwe want to be!',
                xy=(5.0, setpoint_y), xytext=(7.5, 0.8),
                fontsize=11, fontweight='bold', color='#27AE60',
                ha='center',
                arrowprops=dict(arrowstyle='->', color='#27AE60',
                                lw=2.5, connectionstyle='arc3,rad=-0.2'),
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#D5F5E3',
                          edgecolor='#27AE60'),
                zorder=10)

    # --- Region labels below the curve ---
    ax.text(1.5, 0.3, '~0.1 to 0.3', ha='center', va='center',
            fontsize=10, color='#666666', style='italic')
    ax.text(1.5, 0.0, '(low reading)', ha='center', va='center',
            fontsize=9, color='#999999')

    ax.text(8.5, 2.0, '~0.7 to 0.9', ha='center', va='center',
            fontsize=10, color='#666666', style='italic')
    ax.text(8.5, 1.7, '(high reading)', ha='center', va='center',
            fontsize=9, color='#999999')

    # --- Formatting ---
    ax.set_xlim(-1.2, 10.5)
    ax.set_ylim(-0.3, 4.3)
    ax.set_aspect('equal')
    ax.axis('off')

    ax.set_title('Sensor Reading Across the Tape Edge', fontsize=14,
                 fontweight='bold', pad=15, color='#1B3A5C')

    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Generated: {filename}")


if __name__ == '__main__':
    os.makedirs('module-02-line-tracking/slides/images', exist_ok=True)
    draw_setpoint_diagram('module-02-line-tracking/slides/images/setpoint-cross-section.png')
