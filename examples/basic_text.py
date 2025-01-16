from arabic_animations.core.scene import Scene
from arabic_animations.core.text import Text

# List available fonts
# Text.list_available_fonts()

# Create scene
scene = Scene(width=1920, height=1080)

# Create text objects
text1 = Text(
    "بسم الله الرحمن الرحيم",
    position=(0, 0),
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

# Add texts to scene serially (one after another)
scene.add(text1, text2, serial=True)

# Or for parallel animation:
# scene.add(text1, text2, serial=False)