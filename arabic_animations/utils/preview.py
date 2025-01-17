import numpy as np
import logging
import traceback
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer, QFileSystemWatcher
from PyQt5.QtGui import QImage, QPixmap, QResizeEvent
from typing import Optional, List, Dict, Any
from arabic_animations.core.scene import Scene
import importlib.util
import sys
import os

logger = logging.getLogger('arabic_animations')

class PreviewWindow(QMainWindow):
    def __init__(self, script_path: str, verbose: bool = False) -> None:
        super().__init__()
        self.script_path = script_path
        self.verbose = verbose
        self.current_time: float = 0
        self.is_playing: bool = True

        # Load initial scene
        self.scene = self._load_scene()

        # Setup file watcher
        self.watcher = QFileSystemWatcher([script_path])
        self.watcher.fileChanged.connect(self.reload_scene)

        self._setup_ui()

    def _load_scene(self) -> Scene:
        """Load scene from script file"""
        try:
            # Create a new module name based on the file path
            module_name = os.path.splitext(os.path.basename(self.script_path))[0]

            # Load the module
            spec = importlib.util.spec_from_file_location(module_name, self.script_path)
            if spec is None or spec.loader is None:
                raise ImportError("Could not load module specification")

            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)

            # Get the scene object
            if not hasattr(module, 'scene'):
                raise AttributeError("Script must define a 'scene' object")

            return module.scene

        except Exception as e:
            logger.error(f"Error loading scene: {e}")
            if self.verbose:
                logger.debug(traceback.format_exc())
            return None

    def reload_scene(self) -> None:
        """Reload the scene when the script file changes"""
        logger.info("Detected file change, reloading scene...")
        try:
            new_scene = self._load_scene()
            if new_scene:
                self.scene = new_scene
                self.current_time = 0
                logger.info("Scene reloaded successfully")
        except Exception as e:
            logger.error(f"Error reloading scene: {e}")
            if self.verbose:
                logger.debug(traceback.format_exc())

    def _setup_ui(self) -> None:
        """Setup the UI components"""
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
        self.timer.start(1000 // self.scene.fps)

        # Set initial size
        self.resize(1280, 720)

    def update_frame(self) -> None:
        """Update the current frame"""
        if not self.scene:
            return

        if self.is_playing:
            if self.verbose:
                logger.debug(f"Rendering frame at t={self.current_time:.3f}")

            try:
                frame = self.scene.render_frame(self.current_time)
                if frame is not None:
                    height, width = frame.shape[:2]
                    bytes_per_line = 4 * width

                    # Convert frame to QImage with correct color space
                    q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGBA8888)
                    pixmap = QPixmap.fromImage(q_img)

                    # Scale pixmap to fit window while maintaining aspect ratio
                    scaled_pixmap = pixmap.scaled(
                        self.image_label.size(),
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation  # Use better quality scaling
                    )
                    self.image_label.setPixmap(scaled_pixmap)

                self.current_time += 1/self.scene.fps
                if self.current_time > self.scene.duration:
                    self.current_time = 0

            except Exception as e:
                logger.error(f"Error rendering frame: {e}")
                if self.verbose:
                    logger.debug(traceback.format_exc())

    def toggle_play(self) -> None:
        """Toggle play/pause state"""
        self.is_playing = not self.is_playing
        self.play_button.setText('Pause' if self.is_playing else 'Play')
        logger.info("Preview " + ("Playing" if self.is_playing else "Paused"))

    def reset(self) -> None:
        """Reset animation to beginning"""
        self.current_time = 0
        logger.info("Reset to beginning")

    def resizeEvent(self, event: QResizeEvent) -> None:
        """Handle window resize events"""
        super().resizeEvent(event)
        if self.image_label.pixmap():
            # Rescale image when window is resized
            scaled_pixmap = self.image_label.pixmap().scaled(
                self.image_label.size(), Qt.KeepAspectRatio)
            self.image_label.setPixmap(scaled_pixmap)

class LivePreview:
    def __init__(self, script_path: str, verbose: bool = False) -> None:
        self.script_path = script_path
        self.verbose = verbose

    def start(self) -> None:
        """Start live preview"""
        try:
            app = QApplication([])
            window = PreviewWindow(self.script_path, self.verbose)
            window.show()
            app.exec_()

        except Exception as e:
            logger.error(f"Preview error: {e}")
            if self.verbose:
                logger.debug(traceback.format_exc())