import cv2
import numpy as np
import time
import logging
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap

logger = logging.getLogger('arabic_animations')

class PreviewWindow(QMainWindow):
    def __init__(self, scene, verbose=False):
        super().__init__()
        self.scene = scene
        self.verbose = verbose
        self.current_time = 0
        self.is_playing = True

        # Setup UI
        self.setWindowTitle('Animation Preview')
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)

        # Image display
        self.image_label = QLabel()
        layout.addWidget(self.image_label)

        # Controls
        controls_layout = QVBoxLayout()
        self.play_button = QPushButton('Pause')
        self.play_button.clicked.connect(self.toggle_play)
        self.reset_button = QPushButton('Reset')
        self.reset_button.clicked.connect(self.reset)

        controls_layout.addWidget(self.play_button)
        controls_layout.addWidget(self.reset_button)
        layout.addLayout(controls_layout)

        # Timer for animation
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000 // scene.fps)

        # Set initial size
        self.resize(1280, 720)

    def update_frame(self):
        if self.is_playing:
            if self.verbose:
                logger.debug(f"Rendering frame at t={self.current_time:.3f}")

            frame = self.scene.render_frame(self.current_time)
            if frame is not None:
                height, width = frame.shape[:2]
                bytes_per_line = 4 * width

                # Convert frame to QImage
                q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGBA8888)
                pixmap = QPixmap.fromImage(q_img)

                # Scale pixmap to fit window while maintaining aspect ratio
                scaled_pixmap = pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio)
                self.image_label.setPixmap(scaled_pixmap)

            self.current_time += 1/self.scene.fps
            if self.current_time > self.scene.duration:
                self.current_time = 0

    def toggle_play(self):
        self.is_playing = not self.is_playing
        self.play_button.setText('Pause' if self.is_playing else 'Play')
        logger.info("Preview " + ("Playing" if self.is_playing else "Paused"))

    def reset(self):
        self.current_time = 0
        logger.info("Reset to beginning")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.image_label.pixmap():
            # Rescale image when window is resized
            scaled_pixmap = self.image_label.pixmap().scaled(
                self.image_label.size(), Qt.KeepAspectRatio)
            self.image_label.setPixmap(scaled_pixmap)

class LivePreview:
    def __init__(self, scene, verbose=False):
        self.scene = scene
        self.verbose = verbose

    def start(self):
        """Start live preview"""
        try:
            app = QApplication([])
            window = PreviewWindow(self.scene, self.verbose)
            window.show()
            app.exec_()

        except Exception as e:
            logger.error(f"Preview error: {e}")
            if self.verbose:
                logger.debug(traceback.format_exc())