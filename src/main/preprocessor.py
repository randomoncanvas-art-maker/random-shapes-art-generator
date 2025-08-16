import configparser
from typing import Any

import cv2
import numpy as np


class Preprocessor:

    def __init__(self, config: Any, file_path: str) -> None:
        self.config = config
        self.file_path = file_path
        self.canvas = self._create_canvas()
        self.target = self._create_target()

    def _create_canvas(self) -> np.ndarray:
        canvas = np.zeros(
            (self.config.IMAGE_SIZE, self.config.IMAGE_SIZE), dtype=np.uint8)

        return canvas

    def _create_target(self) -> np.ndarray:
        original = cv2.imread(self.file_path, cv2.IMREAD_GRAYSCALE)
        original = cv2.resize(
            original, (self.config.IMAGE_SIZE, self.config.IMAGE_SIZE))
        blurred = cv2.GaussianBlur(original, (3, 3), 0)
        target = 1.0 - blurred / 255.0  # 黒=1、白=0　ぼかして白黒反転

        return target
