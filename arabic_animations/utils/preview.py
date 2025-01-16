import cv2
import numpy as np
import threading
import time
import traceback
import sys
import logging

logger = logging.getLogger('arabic_animations')

class LivePreview:
    def __init__(self, scene, verbose=False):
        self.scene = scene
        self.is_playing = False
        self.current_time = 0
        self.verbose = verbose
        self.running = True

    def start(self):
        """Start live preview"""
        try:
            self.is_playing = True
            logger.debug("Creating preview window...")
            cv2.namedWindow('Preview', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Preview', 1280, 720)  # Reasonable default size

            # Start playback thread
            logger.debug("Starting playback thread...")
            self.preview_thread = threading.Thread(target=self._playback_loop, daemon=True)
            self.preview_thread.start()

            # Main event loop
            while self.running:
                key = cv2.waitKey(1) & 0xFF  # Add & 0xFF for compatibility
                if key == ord('q'):
                    self.running = False
                elif key == ord(' '):
                    self.is_playing = not self.is_playing
                    status = "Playing" if self.is_playing else "Paused"
                    logger.info(f"Preview {status}")
                elif key == ord('r'):
                    self.current_time = 0
                    logger.info("Reset to beginning")

            self.preview_thread.join(timeout=1.0)
            cv2.destroyAllWindows()

        except Exception as e:
            logger.error(f"Preview error: {e}")
            if self.verbose:
                logger.debug(traceback.format_exc())
            cv2.destroyAllWindows()
            sys.exit(1)

    def _playback_loop(self):
        last_frame_time = time.time()
        frame_delay = 1.0 / self.scene.fps

        while self.running:
            try:
                current_time = time.time()
                if self.is_playing and (current_time - last_frame_time) >= frame_delay:
                    if self.verbose:
                        logger.debug(f"Rendering frame at t={self.current_time:.3f}")

                    frame = self.scene.render_frame(self.current_time)
                    if frame is not None:
                        cv2.imshow('Preview', cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR))

                    self.current_time += frame_delay
                    if self.current_time > self.scene.duration:
                        self.current_time = 0

                    last_frame_time = current_time

                # Small sleep to prevent CPU hogging
                time.sleep(0.001)

            except Exception as e:
                logger.error(f"Playback error: {e}")
                if self.verbose:
                    logger.debug(traceback.format_exc())
                self.running = False
                break