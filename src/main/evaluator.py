from typing import Any

import numpy as np


class Evaluator:

    def __init__(self, config: Any, target: np.ndarray) -> None:
        self.config = config
        self.target = target
        self.penalty_mask = 1 - self.config.WHITE_PENALTY * (1 - self.target)

    def evaluate_function(self, mask: np.ndarray, canvas: np.ndarray) -> np.ndarray:
        overlap = self.target * mask - canvas * mask
        score = np.sum(overlap * self.penalty_mask)
        return score
