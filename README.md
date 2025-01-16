# Arabic Animations

A Python library for creating Arabic text writing animations, similar to Manim but specialized for Arabic calligraphy and text animations.

## Features

- Create smooth writing animations for Arabic text
- Support for RTL text rendering
- Live preview during development
- Export to MP4 video files
- Customizable text properties (font, size, color, stroke width)
- Multiple text elements with different timings
- Command-line interface with preview and render options

## Prerequisites

### macOS
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install system dependencies
brew install cairo
brew install pango
brew install pygobject3
brew install pkg-config
brew install fontconfig
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install -y \
    python3-gi \
    python3-gi-cairo \
    gir1.2-gtk-3.0 \
    libcairo2-dev \
    pkg-config \
    python3-dev \
    libgirepository1.0-dev
```

### Windows
Windows support is currently experimental. We recommend using WSL2 with Ubuntu for the best experience.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/arabic_animations.git
cd arabic_animations
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package:
```bash
pip install -e .
```

## Usage

### Basic Example

Create a new Python script (e.g., `my_animation.py`):

```python
from arabic_animations.core.scene import Scene
from arabic_animations.core.text import Text

# Create scene
scene = Scene(width=1920, height=1080)

# Create text objects
text1 = Text(
    "بسم الله الرحمن الرحيم",
    position=(960, 540),  # center position
    font_name="DecoType Thuluth II",
    font_size=128,
    write_duration=2.0
)

text2 = Text(
    "السلام عليكم",
    position=(960, 700),
    font_name="DecoType Thuluth II",
    font_size=72,
    write_duration=1.5
)

# Add texts to scene
scene.add(text1, text2)
```

### Command Line Interface

The library provides a command-line tool `arabic-animate` with the following commands:

```bash
# Live preview during development
arabic-animate render my_animation.py --preview

# Enable verbose output for debugging
arabic-animate render my_animation.py --preview -v

# Render to video file
arabic-animate render my_animation.py --output video.mp4
```

### Preview Controls

When using the preview window:
- Space: Play/Pause
- R: Reset to beginning
- Q: Quit preview

## API Reference

### Scene Class

```python
Scene(width=1920, height=1080, fps=60)
```
- `width`: Output width in pixels
- `height`: Output height in pixels
- `fps`: Frames per second for animation

Methods:
- `add(*objects)`: Add one or more objects to the scene

### Text Class

```python
Text(text, position=(0, 0), font_name="DecoType Thuluth",
     font_size=72, color=(0, 0, 0), stroke_width=2.0,
     write_duration=1.0)
```

Parameters:
- `text`: The text to animate (Arabic or any other script)
- `position`: (x, y) tuple for text position
- `font_name`: Name of the installed font to use
- `font_size`: Font size in points
- `color`: RGB tuple (0-1 range) for text color
- `stroke_width`: Width of the text stroke
- `write_duration`: Duration of the writing animation in seconds

Static Methods:
- `list_available_fonts()`: Print all available system fonts

## Font Installation

### Installing Arabic Fonts

1. Download the desired Arabic fonts (e.g., DecoType Thuluth)
2. Double-click the font file to open Font Book (macOS)
3. Click "Install Font"

Or manually:
- macOS: Copy fonts to `~/Library/Fonts/` or `/Library/Fonts/`
- Linux: Copy fonts to `~/.local/share/fonts/` or `/usr/local/share/fonts/`
- Windows: Copy fonts to `C:\Windows\Fonts\`

Verify font installation:
```python
from arabic_animations.core.text import Text
Text.list_available_fonts()
```

## Development

To contribute to the project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests (when available)
5. Submit a pull request

## Troubleshooting

### Common Issues

1. **Font not found**
   - Verify font installation using `Text.list_available_fonts()`
   - Check font name spelling
   - Try installing the font system-wide

2. **Preview window crashes**
   - Run with verbose flag: `--preview -v`
   - Check system resources
   - Update graphics drivers

3. **Text not rendering**
   - Verify text contains valid Unicode characters
   - Check font supports the required glyphs
   - Try a different font

## License

MIT License

## Acknowledgments

- Cairo Graphics Library
- Pango Text Layout Engine
- OpenCV for video output
