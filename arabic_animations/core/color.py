from enum import Enum
from dataclasses import dataclass, field
from typing import Union, Tuple, Optional
import colorsys

class ColorFormat(Enum):
    RGB = "rgb"
    HEX = "hex"
    HSL = "hsl"
    HSV = "hsv"

@dataclass
class Color:
    """
    Color class supporting multiple formats and alpha channel
    Values are stored internally as RGB (0-1 range)
    """
    r: float = 0.0
    g: float = 0.0
    b: float = 0.0
    a: float = 1.0

    @classmethod
    def from_rgb(cls, r: float, g: float, b: float, a: float = 1.0) -> 'Color':
        """Create from RGB values (0-1 range)"""
        return cls(r, g, b, a)

    @classmethod
    def from_rgb255(cls, r: int, g: int, b: int, a: float = 1.0) -> 'Color':
        """Create from RGB values (0-255 range)"""
        return cls(r/255, g/255, b/255, a)

    @classmethod
    def from_hex(cls, hex_color: str) -> 'Color':
        """Create from hex string (#RRGGBB or #RRGGBBAA)"""
        hex_color = hex_color.lstrip('#')
        if len(hex_color) == 6:
            r, g, b = tuple(int(hex_color[i:i+2], 16)/255 for i in (0, 2, 4))
            return cls(r, g, b)
        elif len(hex_color) == 8:
            r, g, b, a = tuple(int(hex_color[i:i+2], 16)/255 for i in (0, 2, 4, 6))
            return cls(r, g, b, a)
        raise ValueError("Invalid hex color format")

    @classmethod
    def from_hsl(cls, h: float, s: float, l: float, a: float = 1.0) -> 'Color':
        """Create from HSL values (H: 0-360, S: 0-1, L: 0-1)"""
        r, g, b = colorsys.hls_to_rgb(h/360, l, s)
        return cls(r, g, b, a)

    @classmethod
    def from_hsv(cls, h: float, s: float, v: float, a: float = 1.0) -> 'Color':
        """Create from HSV values (H: 0-360, S: 0-1, V: 0-1)"""
        r, g, b = colorsys.hsv_to_rgb(h/360, s, v)
        return cls(r, g, b, a)

    def to_rgb(self) -> Tuple[float, float, float, float]:
        """Get RGB values (0-1 range)"""
        return (self.r, self.g, self.b, self.a)

    def to_rgb255(self) -> Tuple[int, int, int, float]:
        """Get RGB values (0-255 range)"""
        return (int(self.r * 255), int(self.g * 255), int(self.b * 255), self.a)

    def to_hex(self) -> str:
        """Get hex string"""
        if self.a == 1:
            return f"#{int(self.r*255):02x}{int(self.g*255):02x}{int(self.b*255):02x}"
        return f"#{int(self.r*255):02x}{int(self.g*255):02x}{int(self.b*255):02x}{int(self.a*255):02x}"

    def to_hsl(self) -> Tuple[float, float, float, float]:
        """Get HSL values"""
        h, l, s = colorsys.rgb_to_hls(self.r, self.g, self.b)
        return (h*360, s, l, self.a)

    def to_hsv(self) -> Tuple[float, float, float, float]:
        """Get HSV values"""
        h, s, v = colorsys.rgb_to_hsv(self.r, self.g, self.b)
        return (h*360, s, v, self.a)

    def with_alpha(self, alpha: float) -> 'Color':
        """Return new color with modified alpha"""
        return Color(self.r, self.g, self.b, alpha)

    def lighten(self, amount: float) -> 'Color':
        """Return lightened color"""
        h, s, l, a = self.to_hsl()
        return Color.from_hsl(h, s, min(1, l + amount), a)

    def darken(self, amount: float) -> 'Color':
        """Return darkened color"""
        h, s, l, a = self.to_hsl()
        return Color.from_hsl(h, s, max(0, l - amount), a)

# Predefined colors
class Colors:
    # Basic colors
    WHITE = Color(1, 1, 1)
    BLACK = Color(0, 0, 0)
    RED = Color(1, 0, 0)
    GREEN = Color(0, 1, 0)
    BLUE = Color(0, 0, 1)

    # Extended colors
    TRANSPARENT = Color(0, 0, 0, 0)
    GRAY = Color(0.5, 0.5, 0.5)
    YELLOW = Color(1, 1, 0)
    CYAN = Color(0, 1, 1)
    MAGENTA = Color(1, 0, 1)

    # UI colors
    PRIMARY = Color.from_hex("#007AFF")
    SECONDARY = Color.from_hex("#5856D6")
    SUCCESS = Color.from_hex("#34C759")
    WARNING = Color.from_hex("#FF9500")
    DANGER = Color.from_hex("#FF3B30")

    # Paper colors
    PAPER_WHITE = Color.from_hex("#FFFFFF")
    PAPER_CREAM = Color.from_hex("#FFF8DC")
    PAPER_SEPIA = Color.from_hex("#F4ECD8")

@dataclass
class Style:
    """Text styling options"""
    stroke_color: Color = field(default_factory=lambda: Colors.BLACK)
    fill_color: Optional[Color] = None
    stroke_width: float = 2.0
    background_color: Color = field(default_factory=lambda: Colors.PAPER_WHITE)
    shadow_color: Optional[Color] = None
    shadow_offset: Tuple[float, float] = (0, 0)
    shadow_blur: float = 0.0
    glow_color: Optional[Color] = None
    glow_radius: float = 0.0
    gradient: Optional[Tuple[Color, Color]] = None
    gradient_direction: Optional[Tuple[float, float]] = None  # (x, y) vector