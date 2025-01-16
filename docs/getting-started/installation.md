# Installation

## System Dependencies

### macOS
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install system dependencies
brew install cairo pango pygobject3 pkg-config fontconfig
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

## Python Package Installation

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