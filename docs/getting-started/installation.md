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

## Python version support

This package is tested on Python 3.10, 3.11, 3.12 and 3.13. It should work on other versions of Python 3 as well.

## Python Package Installation

Download and install the latest release from pypi or clone the repository and install the package from source.

### From PyPI

```bash
pip install arabic-text-animator
```

Or to choose python 3 explicitly:
```bash
python3 -m pip install arabic-text-animator
```

After installation, you can use the `arabic-animate` command to create animations. For command reference, run `arabic-animate --help` or check the [quickstart guide](./quickstart.md).

### From Source
1. Clone the repository:
```bash
git clone https://github.com/saqib-ahmed/arabic-text-animator.git
cd arabic-text-animator
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install the package:
```bash
pip install -e .
```

## Font Installation
You can download any Arabic fonts from [here](https://fonts.google.com/specimen/Arabic) and install them on your system. We have two fonts available in the repository:

- DecoType Thuluth II
- KFGQPC Uthman Taha Naskh

You can download these fonts from [here](https://github.com/saqib-ahmed/arabic-text-animator/tree/main/fonts/Arabic) and install them on your system.

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