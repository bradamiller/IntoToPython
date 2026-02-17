#!/usr/bin/env python3
"""Generate a PowerPoint presentation from a Module 2 Lesson 1 slide outline."""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import os

# ── Colors ──
DARK_BLUE = RGBColor(0x1B, 0x3A, 0x5C)
BLACK = RGBColor(0x00, 0x00, 0x00)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
DARK_GRAY = RGBColor(0x33, 0x33, 0x33)
LIGHT_GRAY = RGBColor(0xF0, 0xF0, 0xF0)
MEDIUM_GRAY = RGBColor(0x99, 0x99, 0x99)
ACCENT_BLUE = RGBColor(0x2E, 0x75, 0xB6)
TABLE_HEADER_BG = RGBColor(0x2E, 0x75, 0xB6)
TABLE_ALT_BG = RGBColor(0xE8, 0xF0, 0xF8)

# ── Fonts ──
TITLE_FONT = "Calibri"
BODY_FONT = "Calibri"
CODE_FONT = "Courier New"

# ── Sizes ──
SLIDE_WIDTH = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)


def add_title_bar(slide, title_text):
    """Add a colored title bar at the top of the slide."""
    # Title background shape
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(0), Inches(0),
        SLIDE_WIDTH, Inches(1.2)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = DARK_BLUE
    shape.line.fill.background()

    # Title text
    txBox = slide.shapes.add_textbox(
        Inches(0.6), Inches(0.15),
        Inches(12), Inches(0.9)
    )
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title_text
    p.font.size = Pt(32)
    p.font.color.rgb = WHITE
    p.font.bold = True
    p.font.name = TITLE_FONT


def add_bullet_text(text_frame, text, level=0, font_size=Pt(18), bold=False, color=BLACK):
    """Add a bullet point to a text frame."""
    p = text_frame.add_paragraph()
    p.text = text
    p.level = level
    p.font.size = font_size
    p.font.color.rgb = color
    p.font.name = BODY_FONT
    p.font.bold = bold
    p.space_after = Pt(6)
    return p


def add_code_block(slide, code_text, left, top, width, height):
    """Add a code block with gray background."""
    # Background rectangle
    bg = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        left, top, width, height
    )
    bg.fill.solid()
    bg.fill.fore_color.rgb = LIGHT_GRAY
    bg.line.color.rgb = MEDIUM_GRAY
    bg.line.width = Pt(1)

    # Code text box (slightly inset)
    txBox = slide.shapes.add_textbox(
        left + Inches(0.2), top + Inches(0.15),
        width - Inches(0.4), height - Inches(0.3)
    )
    tf = txBox.text_frame
    tf.word_wrap = True

    lines = code_text.strip().split('\n')
    for i, line in enumerate(lines):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = line
        p.font.size = Pt(14)
        p.font.name = CODE_FONT
        p.font.color.rgb = DARK_GRAY
        p.space_after = Pt(2)


def add_table(slide, headers, rows, left, top, width, row_height=Inches(0.45)):
    """Add a formatted table to the slide."""
    num_rows = len(rows) + 1  # +1 for header
    num_cols = len(headers)
    table_shape = slide.shapes.add_table(
        num_rows, num_cols, left, top, width, row_height * num_rows
    )
    table = table_shape.table

    # Set column widths
    col_width = int(width / num_cols)
    for i in range(num_cols):
        table.columns[i].width = col_width

    # Header row
    for i, header in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = header
        cell.fill.solid()
        cell.fill.fore_color.rgb = TABLE_HEADER_BG
        for p in cell.text_frame.paragraphs:
            p.font.size = Pt(16)
            p.font.bold = True
            p.font.color.rgb = WHITE
            p.font.name = BODY_FONT
            p.alignment = PP_ALIGN.CENTER

    # Data rows
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            cell = table.cell(r + 1, c)
            cell.text = val
            if r % 2 == 1:
                cell.fill.solid()
                cell.fill.fore_color.rgb = TABLE_ALT_BG
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(14)
                p.font.name = BODY_FONT
                p.alignment = PP_ALIGN.CENTER


def create_content_area(slide):
    """Create a text box for main content below the title bar."""
    txBox = slide.shapes.add_textbox(
        Inches(0.6), Inches(1.5),
        Inches(12), Inches(5.5)
    )
    tf = txBox.text_frame
    tf.word_wrap = True
    return tf


def build_presentation():
    prs = Presentation()
    prs.slide_width = SLIDE_WIDTH
    prs.slide_height = SLIDE_HEIGHT
    blank_layout = prs.slide_layouts[6]  # Blank layout

    # ════════════════════════════════════════
    # SLIDE 1: Title & Learning Objectives
    # ════════════════════════════════════════
    slide = prs.slides.add_slide(blank_layout)

    # Large title area
    bg = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(0), Inches(0),
        SLIDE_WIDTH, Inches(3.0)
    )
    bg.fill.solid()
    bg.fill.fore_color.rgb = DARK_BLUE
    bg.line.fill.background()

    # Module subtitle
    txBox = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11), Inches(0.6))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = "Module 2: Line Tracking"
    p.font.size = Pt(20)
    p.font.color.rgb = RGBColor(0xA0, 0xC4, 0xE8)
    p.font.name = TITLE_FONT

    # Main title
    txBox = slide.shapes.add_textbox(Inches(0.8), Inches(1.0), Inches(11), Inches(1.2))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = "Lesson 1: The Reflectance Sensor"
    p.font.size = Pt(44)
    p.font.color.rgb = WHITE
    p.font.bold = True
    p.font.name = TITLE_FONT

    # Learning objectives section
    txBox = slide.shapes.add_textbox(Inches(0.8), Inches(3.4), Inches(6), Inches(3.5))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = "Learning Objectives"
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    p.font.name = TITLE_FONT

    objectives = [
        "Explain how reflectance sensors detect light vs. dark surfaces",
        "Read sensor values using the Reflectance class",
        "Record calibration data for your specific robot and surface",
        "Choose a threshold value for line detection",
    ]
    for obj in objectives:
        add_bullet_text(tf, obj, level=0, font_size=Pt(18), color=DARK_GRAY)

    # Agenda section
    txBox = slide.shapes.add_textbox(Inches(7.5), Inches(3.4), Inches(5), Inches(3.5))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = "Agenda"
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    p.font.name = TITLE_FONT

    agenda = [
        ("How sensors work", "10 min"),
        ("Reading sensor values", "15 min"),
        ("Calibration exercise", "20 min"),
    ]
    for item, duration in agenda:
        add_bullet_text(tf, f"{item}  ({duration})", level=0, font_size=Pt(18), color=DARK_GRAY)

    # ════════════════════════════════════════
    # SLIDE 2: Hook — How Does a Robot "See"?
    # ════════════════════════════════════════
    slide = prs.slides.add_slide(blank_layout)
    add_title_bar(slide, 'How Does a Robot "See"?')

    tf = create_content_area(slide)
    p = tf.paragraphs[0]
    p.text = ""

    add_bullet_text(tf, 'Discussion Question:', level=0, font_size=Pt(22), bold=True, color=DARK_BLUE)
    add_bullet_text(tf, '"You can see the black line. How could a robot tell the difference?"', level=0, font_size=Pt(20), color=DARK_GRAY)
    add_bullet_text(tf, '', level=0)
    add_bullet_text(tf, 'Key Insight:', level=0, font_size=Pt(22), bold=True, color=DARK_BLUE)
    add_bullet_text(tf, "Robots don't have eyes \u2014 they use sensors that measure physical properties.", level=0, font_size=Pt(20), color=DARK_GRAY)
    add_bullet_text(tf, '', level=0)
    add_bullet_text(tf, 'Today:', level=0, font_size=Pt(22), bold=True, color=DARK_BLUE)
    add_bullet_text(tf, 'We\'ll learn to read the XRP\'s reflectance sensors \u2014 the robot\'s way of "seeing" the line.', level=0, font_size=Pt(20), color=DARK_GRAY)

    # ════════════════════════════════════════
    # SLIDE 3: How Reflectance Sensors Work
    # ════════════════════════════════════════
    slide = prs.slides.add_slide(blank_layout)
    add_title_bar(slide, "How Reflectance Sensors Work")

    tf = create_content_area(slide)
    p = tf.paragraphs[0]
    p.text = ""

    add_bullet_text(tf, "The sensor has two parts:", level=0, font_size=Pt(22), bold=True, color=DARK_BLUE)
    add_bullet_text(tf, "Infrared LED \u2014 shines light downward", level=1, font_size=Pt(18), bold=True)
    add_bullet_text(tf, "Light detector \u2014 measures how much bounces back", level=1, font_size=Pt(18), bold=True)
    add_bullet_text(tf, '', level=0)
    add_bullet_text(tf, 'White surface: Reflects most light \u2192 low value (close to 0.0)', level=0, font_size=Pt(18))
    add_bullet_text(tf, 'Black surface: Absorbs most light \u2192 high value (close to 1.0)', level=0, font_size=Pt(18))
    add_bullet_text(tf, '', level=0)
    add_bullet_text(tf, 'Analogy: Flashlight on a mirror vs. a black t-shirt', level=0, font_size=Pt(18), color=ACCENT_BLUE, bold=True)
    add_bullet_text(tf, '', level=0)
    add_bullet_text(tf, 'Show: Photo of XRP underside with sensors highlighted', level=0, font_size=Pt(16), color=MEDIUM_GRAY)

    # ════════════════════════════════════════
    # SLIDE 4: Sensor Value Range (with table)
    # ════════════════════════════════════════
    slide = prs.slides.add_slide(blank_layout)
    add_title_bar(slide, "Sensor Value Range")

    # Intro text
    txBox = slide.shapes.add_textbox(Inches(0.6), Inches(1.5), Inches(12), Inches(0.8))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Values range from 0.0 to 1.0:"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    p.font.name = BODY_FONT

    # Table
    headers = ["Position", "Left Sensor", "Right Sensor"]
    rows = [
        ["On white surface", "~0.1 \u2013 0.3", "~0.1 \u2013 0.3"],
        ["On line edge", "~0.4 \u2013 0.6", "~0.4 \u2013 0.6"],
        ["On black line", "~0.7 \u2013 0.9", "~0.7 \u2013 0.9"],
    ]
    add_table(slide, headers, rows, Inches(1.5), Inches(2.5), Inches(10))

    # Key ideas below table
    txBox = slide.shapes.add_textbox(Inches(0.6), Inches(4.8), Inches(12), Inches(2))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = ""
    add_bullet_text(tf, "Key idea: The transition from white to black is GRADUAL, not sudden.", level=0, font_size=Pt(20), bold=True, color=DARK_BLUE)
    add_bullet_text(tf, "The XRP has TWO sensors \u2014 left and right \u2014 each reads independently.", level=0, font_size=Pt(18))

    # ════════════════════════════════════════
    # SLIDE 5: Reading Sensors in Python
    # ════════════════════════════════════════
    slide = prs.slides.add_slide(blank_layout)
    add_title_bar(slide, "Reading Sensors in Python")

    # Import and setup label
    txBox = slide.shapes.add_textbox(Inches(0.6), Inches(1.5), Inches(5.5), Inches(0.5))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = "Import and setup:"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    p.font.name = BODY_FONT

    add_code_block(slide,
        'from XRPLib.reflectance import Reflectance\n'
        'from XRPLib.board import Board\n'
        '\n'
        'reflectance = Reflectance.get_default_reflectance()\n'
        'board = Board.get_default_board()',
        Inches(0.6), Inches(2.1), Inches(5.5), Inches(2.0)
    )

    # Read values label
    txBox = slide.shapes.add_textbox(Inches(7.0), Inches(1.5), Inches(5.5), Inches(0.5))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = "Read values:"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    p.font.name = BODY_FONT

    add_code_block(slide,
        'board.wait_for_button()\n'
        'left = reflectance.get_left()\n'
        'right = reflectance.get_right()\n'
        'print("Left:", left, "Right:", right)',
        Inches(7.0), Inches(2.1), Inches(5.5), Inches(1.7)
    )

    # Key point
    txBox = slide.shapes.add_textbox(Inches(0.6), Inches(5.0), Inches(12), Inches(1.0))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Key point: get_left() and get_right() return a number between 0.0 and 1.0."
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.font.name = BODY_FONT

    # ════════════════════════════════════════
    # SLIDE 6: Continuous Reading
    # ════════════════════════════════════════
    slide = prs.slides.add_slide(blank_layout)
    add_title_bar(slide, "Continuous Reading")

    txBox = slide.shapes.add_textbox(Inches(0.6), Inches(1.5), Inches(6), Inches(0.5))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = "Read many times in a loop:"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    p.font.name = BODY_FONT

    add_code_block(slide,
        'import time\n'
        '\n'
        'board.wait_for_button()\n'
        '\n'
        'for i in range(50):\n'
        '    left = reflectance.get_left()\n'
        '    right = reflectance.get_right()\n'
        '    print("Left:", left, "  Right:", right)\n'
        '    time.sleep(0.1)',
        Inches(0.6), Inches(2.1), Inches(6), Inches(3.0)
    )

    # Side notes
    txBox = slide.shapes.add_textbox(Inches(7.5), Inches(2.1), Inches(5), Inches(3.0))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = ""
    add_bullet_text(tf, "Why?", level=0, font_size=Pt(20), bold=True, color=DARK_BLUE)
    add_bullet_text(tf, "See how values change as you move the robot across the line.", level=0, font_size=Pt(18))
    add_bullet_text(tf, "", level=0)
    add_bullet_text(tf, "time.sleep(0.1)", level=0, font_size=Pt(18), bold=True, color=ACCENT_BLUE)
    add_bullet_text(tf, "Pause 0.1 seconds so readings aren't too fast to read.", level=0, font_size=Pt(18))

    # ════════════════════════════════════════
    # SLIDE 7: What Is a Threshold?
    # ════════════════════════════════════════
    slide = prs.slides.add_slide(blank_layout)
    add_title_bar(slide, "What Is a Threshold?")

    tf = create_content_area(slide)
    p = tf.paragraphs[0]
    p.text = ""

    add_bullet_text(tf, 'Threshold: A cutoff value to decide "on line" vs. "off line"', level=0, font_size=Pt(22), bold=True, color=DARK_BLUE)
    add_bullet_text(tf, '', level=0)
    add_bullet_text(tf, 'Example:', level=0, font_size=Pt(20), bold=True, color=DARK_BLUE)
    add_bullet_text(tf, 'Off line readings: 0.1, 0.2, 0.15, 0.25', level=1, font_size=Pt(18))
    add_bullet_text(tf, 'On line readings: 0.75, 0.8, 0.85, 0.9', level=1, font_size=Pt(18))
    add_bullet_text(tf, 'Threshold = 0.5 (halfway between)', level=1, font_size=Pt(18), bold=True, color=ACCENT_BLUE)
    add_bullet_text(tf, '', level=0)
    add_bullet_text(tf, 'Rule: If sensor > threshold \u2192 on the line', level=0, font_size=Pt(20), bold=True)
    add_bullet_text(tf, 'Rule: If sensor < threshold \u2192 off the line', level=0, font_size=Pt(20), bold=True)
    add_bullet_text(tf, '', level=0)
    add_bullet_text(tf, 'Important: The threshold depends on YOUR surface and tape. Calibrate!', level=0, font_size=Pt(20), color=ACCENT_BLUE, bold=True)

    # ════════════════════════════════════════
    # SLIDE 8: Calibration Exercise
    # ════════════════════════════════════════
    slide = prs.slides.add_slide(blank_layout)
    add_title_bar(slide, "Calibration Exercise")

    tf = create_content_area(slide)
    p = tf.paragraphs[0]
    p.text = ""

    add_bullet_text(tf, 'Your task:', level=0, font_size=Pt(22), bold=True, color=DARK_BLUE)
    add_bullet_text(tf, '1. Place robot on WHITE surface \u2192 record sensor values', level=0, font_size=Pt(18))
    add_bullet_text(tf, '2. Place robot on BLACK line \u2192 record sensor values', level=0, font_size=Pt(18))
    add_bullet_text(tf, '3. Place robot on EDGE of line \u2192 record sensor values', level=0, font_size=Pt(18))
    add_bullet_text(tf, '4. Calculate your threshold (halfway between off-line and on-line averages)', level=0, font_size=Pt(18))
    add_bullet_text(tf, '', level=0)
    add_bullet_text(tf, 'Why calibrate?', level=0, font_size=Pt(22), bold=True, color=DARK_BLUE)
    add_bullet_text(tf, 'Different surfaces, tape colors, and lighting conditions give different values.', level=0, font_size=Pt(18))
    add_bullet_text(tf, '', level=0)
    add_bullet_text(tf, "Save your threshold! You'll use it for the rest of Module 2.", level=0, font_size=Pt(20), bold=True, color=ACCENT_BLUE)

    # ════════════════════════════════════════
    # SLIDE 9: Your Turn!
    # ════════════════════════════════════════
    slide = prs.slides.add_slide(blank_layout)
    add_title_bar(slide, "Your Turn!")

    # Activity column
    txBox = slide.shapes.add_textbox(Inches(0.6), Inches(1.5), Inches(6), Inches(5))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = ""
    add_bullet_text(tf, 'Activity:', level=0, font_size=Pt(22), bold=True, color=DARK_BLUE)
    add_bullet_text(tf, '1. Create sensor_test.py', level=0, font_size=Pt(18))
    add_bullet_text(tf, '2. Write the continuous reading program', level=0, font_size=Pt(18))
    add_bullet_text(tf, '3. Collect calibration data for 3 positions', level=0, font_size=Pt(18))
    add_bullet_text(tf, '4. Record in your worksheet', level=0, font_size=Pt(18))
    add_bullet_text(tf, '5. Determine your threshold value', level=0, font_size=Pt(18))

    # Checkpoints column
    txBox = slide.shapes.add_textbox(Inches(7.5), Inches(1.5), Inches(5), Inches(5))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = ""
    add_bullet_text(tf, 'Checkpoints:', level=0, font_size=Pt(22), bold=True, color=DARK_BLUE)
    add_bullet_text(tf, 'Can you read sensor values?', level=0, font_size=Pt(18))
    add_bullet_text(tf, 'Do white and black give different numbers?', level=0, font_size=Pt(18))
    add_bullet_text(tf, 'Did you find a good threshold?', level=0, font_size=Pt(18))

    # ════════════════════════════════════════
    # SLIDE 10: Connection to Next Lesson
    # ════════════════════════════════════════
    slide = prs.slides.add_slide(blank_layout)
    add_title_bar(slide, "Connection to Next Lesson")

    tf = create_content_area(slide)
    p = tf.paragraphs[0]
    p.text = ""

    add_bullet_text(tf, 'What you did today:', level=0, font_size=Pt(22), bold=True, color=DARK_BLUE)
    add_bullet_text(tf, 'Learned how reflectance sensors work', level=0, font_size=Pt(18))
    add_bullet_text(tf, 'Read sensor values in Python', level=0, font_size=Pt(18))
    add_bullet_text(tf, 'Calibrated your sensors and chose a threshold', level=0, font_size=Pt(18))
    add_bullet_text(tf, '', level=0)
    add_bullet_text(tf, 'Next lesson (Lesson 2):', level=0, font_size=Pt(22), bold=True, color=DARK_BLUE)
    add_bullet_text(tf, 'Use a while loop to keep the robot driving', level=0, font_size=Pt(18))
    add_bullet_text(tf, 'Stop when the sensor detects the line', level=0, font_size=Pt(18))
    add_bullet_text(tf, 'First time the robot uses sensors to control its behavior!', level=0, font_size=Pt(18))
    add_bullet_text(tf, '', level=0)
    add_bullet_text(tf, "Save your calibration data \u2014 you'll need it!", level=0, font_size=Pt(20), bold=True, color=ACCENT_BLUE)

    # ── Save ──
    output_path = os.path.join(
        os.path.dirname(__file__),
        "module-02-line-tracking", "slides", "01-the-reflectance-sensor.pptx"
    )
    prs.save(output_path)
    print(f"Presentation saved to: {output_path}")
    print(f"Total slides: {len(prs.slides)}")


if __name__ == "__main__":
    build_presentation()
