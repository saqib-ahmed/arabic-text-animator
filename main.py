from arabic_text_animator import ArabicTextAnimator

animator = ArabicTextAnimator(1920, 1080, 60)

# Create animation
frames = animator.create_animation(
    text="""
            بسم الله الرحمن الرحيم
                الحمد لله رب العالمين
    اللهم صل على محمد وعلى آل محمد
                            أما بعد
    """,
    font_name="DecoType Thuluth II",
    font_size=64,
    duration=5,
    color=(0, 0, 0),  # black
    stroke_width=1.5
)

# Save as video
animator.save_video(frames, "arabic_animation.mp4")
