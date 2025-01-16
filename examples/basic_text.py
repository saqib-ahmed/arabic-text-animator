from arabic_animations.core.scene import Scene
from arabic_animations.core.text import Text
from arabic_animations.core.position import Position, Padding

# List available fonts
# Text.list_available_fonts()

# Create scene
scene = Scene(width=1920, height=1080)

# Create text objects
text1 = Text(
    "بسم الله الرحمن الرحيم",
    position=Position.TOP,  # Place at top center
    padding=Padding(top=50),  # 50 pixels from top
    font_name="DecoType Thuluth II",
    font_size=128,
    write_duration=2.0
)

text2 = Text(
    "السلام عليكم",
    position=Position.CENTER,  # Center of screen
    font_name="DecoType Thuluth II",
    font_size=72,
    write_duration=1.5
)

# Add texts to scene serially
scene.add(text1, text2, serial=True)
