from arabic_animations.core.scene import Scene
from arabic_animations.core.text import Text

# List available fonts
Text.list_available_fonts()

# Create scene
scene = Scene(width=1920, height=1080)

# Try with a different font first to test
text1 = Text("بسم الله الرحمن الرحيم",
             position=(960, 540),
             font_name="DecoType Thuluth II",
             font_size=128,
             write_duration=2.0)

text2 = Text("السلام عليكم",
             position=(960, 700),
             font_name="DecoType Thuluth II",
             font_size=72,
             write_duration=1.5)

scene.add(text1, text2)