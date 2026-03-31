---
name: Use PNG robot image in slides
description: Use the XRP top-down PNG image instead of SVG rectangles for robot illustrations in slide decks
type: feedback
---

Use the PNG robot image (`tools/Robot Photos/XRPTopDownImageForSlides.png`) for robot illustrations in HTML slide decks instead of the hand-drawn SVG rectangle robots.

**Why:** Brad prefers the look of the real robot illustration over the simple SVG rect+text "XRP" placeholders. Tested in Module 3 deck 3 and approved.

**How to apply:**
- Copy the PNG to a local `images/` folder within the slides directory (avoids spaces in paths) as `xrp-top-down.png`
- The PNG robot faces **south (down)** by default
- Rotation guide: facing right (east) = `rotate(-90, cx, cy)`, facing left (west) = `rotate(90, cx, cy)`, facing up (north) = `rotate(180, cx, cy)`, facing down (south) = no rotation
- For ghost/transparent robots use `opacity="0.5"`
- Typical size: 40-48px width/height inside SVG viewBoxes
- Use `<image href="images/xrp-top-down.png" .../>` within SVG elements
