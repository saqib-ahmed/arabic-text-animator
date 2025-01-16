# Animations

## Basic Animation Concepts

The library uses a time-based animation system where each text object has a `write_duration` that controls how long it takes to write the text.

### Single Text Animation

```python
text = Text(
    "بسم الله",
    position=Position.CENTER,
    write_duration=2.0  # Text will take 2 seconds to write
)
scene.add(text)
```

### Multiple Text Animations

#### Parallel Animation
Text objects animate simultaneously:

```python
text1 = Text("بسم الله", write_duration=2.0)
text2 = Text("الرحمن الرحيم", write_duration=1.5)

# Both texts will start animating at the same time
scene.add(text1, text2, serial=False)
```

#### Serial Animation
Text objects animate one after another:

```python
text1 = Text("بسم الله", write_duration=2.0)
text2 = Text("الرحمن الرحيم", write_duration=1.5)

# text2 will start after text1 finishes
scene.add(text1, text2, serial=True)
```

## Animation Timing

### Duration Control
```python
# Slow writing animation
text = Text(
    "بسم الله",
    write_duration=3.0  # 3 seconds
)

# Quick writing animation
text = Text(
    "بسم الله",
    write_duration=0.5  # Half second
)
```

## Preview and Rendering

### Live Preview
During development, use the preview window to see your animations:

```bash
arabic-animate render animation.py --preview
```

Preview controls:
- Space: Play/Pause
- R: Reset animation
- Q: Quit preview

### Final Rendering
Render the final animation to a video file:

```bash
arabic-animate render animation.py --output final.mp4
```