#!/usr/bin/env python3
"""Generate sketch-style illustrations for Module 3 Lesson 1 slides using Gemini API."""

import os
import sys
import time
from google import genai
from google.genai import types

API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyDHK2n61ZdQGpbFZuNFGgLSoclP8vfXC30")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "_illustrations-gemini")
os.makedirs(OUTPUT_DIR, exist_ok=True)

client = genai.Client(api_key=API_KEY)

STYLE_PREFIX = (
    "Hand-drawn sketch-style illustration on a white background, "
    "using a muted color palette of steel blue (#5b8fa8), peach/salmon (#e8a87c), "
    "soft green (#85c88a), and dark charcoal (#2d3436) outlines. "
    "The style should look like it was drawn with markers on notebook paper, "
    "slightly imperfect lines, friendly and educational feel. "
    "No text shadows or 3D effects. Clean white background. "
)

# Each image: (filename, prompt)
IMAGES = [
    (
        "illust-robot.png",
        STYLE_PREFIX +
        "A cute friendly robot character, boxy body in steel blue with rounded corners, "
        "two big round white eyes with dark pupils, a small peach/salmon mouth bar, "
        "an antenna on top with a peach circle, small blue arms sticking out to the sides, "
        "and two gray circular wheels at the bottom. The robot should be small and centered, "
        "about 80x80 pixels worth of detail. Simple, minimal, like a doodle in a notebook."
    ),
    (
        "illust-circle-to-grid.png",
        STYLE_PREFIX +
        "Two diagrams side by side with an arrow between them. "
        "LEFT side labeled 'Module 2: Circle' in blue handwriting: a black circle/oval track "
        "with a small peach dot marking a cross point, and a tiny blue robot on the track. "
        "CENTER: a large peach/salmon arrow pointing right with handwritten text 'same code!' above it. "
        "RIGHT side labeled 'Module 3: Grid' in blue handwriting: a 3x3 grid of black lines "
        "with peach/salmon dots at each intersection, and a tiny blue robot on one of the grid lines. "
        "Wide landscape format, approximately 520x160 pixels of content."
    ),
    (
        "illust-grid-layout.png",
        STYLE_PREFIX +
        "A 4x4 grid diagram with labeled rows and columns. "
        "Blue handwritten labels 'Col 0', 'Col 1', 'Col 2', 'Col 3' across the top. "
        "Blue handwritten labels 'Row 0', 'Row 1', 'Row 2', 'Row 3' down the left side. "
        "Black lines forming the grid, with peach/salmon filled circles at every intersection (16 total). "
        "A small blue robot sitting on the grid near Row 1, Col 0 area. "
        "The grid lines should look slightly hand-drawn, not perfectly straight. "
        "Landscape format, approximately 460x260 pixels of content."
    ),
    (
        "illust-progression.png",
        STYLE_PREFIX +
        "Three rounded rectangle boxes in a horizontal row connected by arrows. "
        "LEFT box with blue border: 'Module 2' header, text 'Follow a circle, detect one cross'. "
        "CENTER box with peach/salmon border (highlighted as current): 'Module 3 (now!)' header, "
        "text 'Navigate a GRID of crosses'. "
        "RIGHT box with soft green border: 'Module 4' header, text 'Use COORDINATES for pathfinding'. "
        "Dark arrows between the boxes. Landscape format, approximately 500x100 pixels."
    ),
    (
        "illust-puzzle-pieces.png",
        STYLE_PREFIX +
        "Three rounded rectangle puzzle-piece-style boxes in a row with '+' signs between them. "
        "LEFT box with blue fill/border: 'Line Following'. "
        "CENTER box with peach/salmon fill/border: 'Cross Detection'. "
        "RIGHT box with green fill/border: 'Turns'. "
        "Plus signs in peach between the boxes. Simple, clean, landscape format about 380x100 pixels."
    ),
    (
        "illust-method-cards.png",
        STYLE_PREFIX +
        "Three card-shaped rounded rectangles side by side, slightly tilted like index cards. "
        "LEFT card with blue tint: monospace text 'track_until_cross()' and italic note '→ drives forward'. "
        "CENTER card with peach tint: monospace text 'turn_right()' and italic note '↻ turns 90°'. "
        "RIGHT card with green tint: monospace text 'turn_left()' and italic note '↺ turns 90°'. "
        "Landscape format, approximately 500x90 pixels."
    ),
    (
        "illust-drive-to-intersection.png",
        STYLE_PREFIX +
        "A diagram showing a robot driving along a horizontal black line toward an intersection. "
        "LEFT: a small blue robot on the line labeled 'start' in blue. "
        "A dashed peach arrow shows the path from the robot toward the intersection. "
        "CENTER: a black cross/plus shape (horizontal and vertical lines crossing) with a peach circle "
        "at the intersection point. Labels: 'follows line...' along the path, "
        "'sensors detect the cross!' near the intersection, and 'STOP!' below in peach. "
        "Landscape format, approximately 250x180 pixels."
    ),
    (
        "illust-drive-and-turn.png",
        STYLE_PREFIX +
        "A diagram showing three steps of robot movement at a grid intersection. "
        "A black cross shape (two perpendicular lines) with a peach circle at the center. "
        "Step 1 (blue): a faded robot on the left with a dashed blue arrow driving toward the intersection, "
        "labeled '1. drive' in blue. "
        "Step 2 (peach): a curved arrow at the intersection showing a right turn, labeled '2. turn right' in peach. "
        "Step 3 (green): a dashed green arrow going downward from the intersection, "
        "labeled '3. drive again!' in green, with a dashed circle below labeled 'next intersection'. "
        "Portrait-ish format, approximately 260x220 pixels."
    ),
    (
        "illust-code-reuse-arrow.png",
        STYLE_PREFIX +
        "Two rounded rectangle boxes connected by a large arrow. "
        "LEFT box with blue border: 'Module 2' in blue, subtitle 'Circle + LineTrack' in gray. "
        "A large peach/salmon arrow pointing right with handwritten text 'zero changes!' above it. "
        "RIGHT box with peach border: 'Module 3' in peach, subtitle 'Grid Navigation' in gray. "
        "Wide landscape format, approximately 600x80 pixels."
    ),
    (
        "illust-three-intersections.png",
        STYLE_PREFIX +
        "A horizontal black line with three intersections (vertical lines crossing it). "
        "Each intersection has a peach circle and is numbered '1', '2', '3' above. "
        "A small blue robot on the far left of the horizontal line. "
        "A large dashed peach arc/arrow curves from the robot over all three intersections, "
        "with handwritten text 'for loop!' in peach along the arc. "
        "Wide landscape format, approximately 440x80 pixels."
    ),
]


def generate_image(prompt: str, filename: str) -> bool:
    """Generate a single image using Gemini and save it."""
    output_path = os.path.join(OUTPUT_DIR, filename)
    print(f"  Generating {filename}...", end=" ", flush=True)

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"],
            ),
        )

        # Extract image from response
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                with open(output_path, "wb") as f:
                    f.write(part.inline_data.data)
                print(f"OK -> {output_path}")
                return True

        print("FAILED (no image in response)")
        # Print text parts for debugging
        for part in response.candidates[0].content.parts:
            if part.text:
                print(f"    Response text: {part.text[:200]}")
        return False

    except Exception as e:
        print(f"ERROR: {e}")
        return False


def main():
    print(f"Generating {len(IMAGES)} illustrations via Gemini API...")
    print(f"Output directory: {OUTPUT_DIR}\n")

    results = []
    for filename, prompt in IMAGES:
        ok = generate_image(prompt, filename)
        results.append((filename, ok))
        # Small delay to avoid rate limiting
        time.sleep(1)

    print(f"\n--- Results ---")
    success = sum(1 for _, ok in results if ok)
    print(f"Generated: {success}/{len(IMAGES)}")
    for filename, ok in results:
        status = "OK" if ok else "FAILED"
        print(f"  [{status}] {filename}")

    if success < len(IMAGES):
        sys.exit(1)


if __name__ == "__main__":
    main()
