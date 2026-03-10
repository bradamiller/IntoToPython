---
name: slide-deck-generator
description: Generate PowerPoint and HTML slide decks from markdown outlines for the IntroToPython curriculum. Use when: creating presentations, updating slide decks, generating PPTX from markdown, making HTML slides with navigation, ensuring readable code fonts, preventing slide overflow.
---

# Slide Deck Generator

This skill generates professional slide decks for the IntroToPython curriculum from markdown outline files. It supports both PowerPoint (.pptx) and HTML output formats with optimized layouts for readability and presentation quality.

## Features

- **Markdown-driven**: Create slides from structured markdown files
- **Multiple layouts**: Automatic layout selection based on content (text-only, code blocks, tables, side-by-side)
- **Readable code**: Ensures program code fonts remain readable (minimum 14pt) and don't get too small
- **HTML output**: Generates HTML slides with left-side navigation index
- **Overflow prevention**: Automatically adjusts content to prevent elements running off slide edges or bottom
- **Consistent styling**: Professional color scheme and typography throughout

## Usage

Use this skill when you need to:
- Generate new slide presentations from markdown outlines
- Update existing presentations with improved formatting
- Create HTML versions with navigation
- Ensure code readability in presentations
- Prevent layout issues in slide decks

## Bundled Assets

- `generate_slides.py`: Main generation script with improved code font handling and HTML output
- `html_template.html`: Template for HTML slide generation with navigation
- `styles.css`: CSS styles for HTML output

## Improvements Over Previous Version

1. **Code Font Readability**: Minimum font size of 14pt for code blocks, with automatic scaling
2. **HTML Generation**: New HTML output with slide index navigation on the left
3. **Overflow Protection**: Content positioning that prevents elements from running off the page
4. **Better Layout Logic**: Improved algorithms for placing text, code, and tables

## File Structure

Place markdown outline files in `module-XX/slides/` directories following the naming pattern `XX-lesson-name-outline.md`.

The skill will automatically detect the module from the file path and generate appropriately named output files.