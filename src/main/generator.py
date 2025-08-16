import random
from logging import getLogger
from typing import Any, Tuple

import cv2
import numpy as np

logger = getLogger('Log').getChild('generator')


class Generator:

    def __init__(self, config: Any) -> None:
        self.config = config

    def _get_blank_canvas(self) -> np.ndarray:
        blank_canvas = np.zeros(
            (self.config.IMAGE_SIZE, self.config.IMAGE_SIZE), dtype=np.uint8)

        return blank_canvas

    def generate_shape(self, shape_name: str) -> np.ndarray:
        if shape_name == 'line':
            mask = self._generate_line()
        elif shape_name == 'circle':
            mask = self._generate_circle()
        elif shape_name == 'ellipse':
            mask = self._generate_ellipse()
        elif shape_name == 'square':
            mask = self._generate_square()
        elif shape_name == 'triangle':
            mask = self._generate_triangle()
        else:
            logger.error(
                'Shapes Is_Generate is all "False", Set one of them to "True"')

        return mask

    def _generate_line(self) -> Tuple[np.ndarray, dict]:
        blank_canvas = self._get_blank_canvas()
        params_dict = {}
        xl = random.randint(
            self.config.LINE_MIN_LENGTH, self.config.LINE_MAX_LENGTH)
        yl = random.randint(
            self.config.LINE_MIN_LENGTH, self.config.LINE_MAX_LENGTH)
        x1 = random.randint(
            xl, self.config.IMAGE_SIZE - xl)
        y1 = random.randint(
            yl, self.config.IMAGE_SIZE - yl)
        x2 = random.randint(x1 - xl, x1 + xl)
        y2 = random.randint(y1 - yl, y1 + yl)
        pt1 = (x1, y1)
        pt2 = (x2, y2)
        color = random.choices(
            self.config.COLOR_VARIATIONS,
            weights=self.config.WEIGHT_COLOR_SELECTED)[0]
        line_thickness = random.choices(
            self.config.LINE_THICKNESS_VARIATIONS,
            weights=self.config.WEIGHT_LINE_THICKNESS_SELECTED,
        )[0]
        mask = cv2.line(
            blank_canvas,
            pt1=pt1,
            pt2=pt2,
            color=color,
            thickness=line_thickness,
        )
        params_dict['choiced_shapes'] = 'line'
        params_dict['params'] = {
            'pt1': pt1,
            'pt2': pt2,
            'color': color,
            'line_thickness': line_thickness,
        }

        return (mask, params_dict)

    def _generate_circle(self) -> Tuple[np.ndarray, dict]:
        blank_canvas = self._get_blank_canvas()
        params_dict = {}
        radius = random.randint(
            self.config.CIRCLE_MIN_RADIUS, self.config.CIRCLE_MAX_RADIUS)
        x = random.randint(
            radius, self.config.IMAGE_SIZE - radius)
        y = random.randint(
            radius, self.config.IMAGE_SIZE - radius)
        center = (x, y)
        color = random.choices(
            self.config.COLOR_VARIATIONS,
            weights=self.config.WEIGHT_COLOR_SELECTED)[0]
        line_thickness = random.choices(
            self.config.LINE_THICKNESS_VARIATIONS,
            weights=self.config.WEIGHT_LINE_THICKNESS_SELECTED,
        )[0]
        mask = cv2.circle(
            blank_canvas,
            center=center,
            radius=radius,
            color=color,
            thickness=line_thickness,
        )
        params_dict['choiced_shapes'] = 'circle'
        params_dict['params'] = {
            'center': center,
            'radius': radius,
            'color': color,
            'line_thickness': line_thickness,
        }
        return (mask, params_dict)

    def _generate_ellipse(self) -> Tuple[np.ndarray, dict]:
        blank_canvas = self._get_blank_canvas()
        params_dict = {}
        xr = random.randint(
            self.config.ELLIPSE_MIN_RADIUS, self.config.ELLIPSE_MAX_RADIUS)
        yr = random.randint(
            self.config.ELLIPSE_MIN_RADIUS, self.config.ELLIPSE_MAX_RADIUS)
        x = random.randint(
            xr, self.config.IMAGE_SIZE - xr)
        y = random.randint(
            yr, self.config.IMAGE_SIZE - yr)
        angle = random.randint(0, 360)
        box = ((x, y), (xr, yr), angle)
        color = random.choices(
            self.config.COLOR_VARIATIONS,
            weights=self.config.WEIGHT_COLOR_SELECTED)[0]
        line_thickness = random.choices(
            self.config.LINE_THICKNESS_VARIATIONS,
            weights=self.config.WEIGHT_LINE_THICKNESS_SELECTED,
        )[0]
        mask = cv2.ellipse(
            blank_canvas, box=box, color=color, thickness=line_thickness)
        params_dict['choiced_shapes'] = 'ellipse'
        params_dict['params'] = {
            'box': box,
            'color': color,
            'line_thickness': line_thickness,
        }

        return (mask, params_dict)

    def _generate_square(self) -> Tuple[np.ndarray, dict]:
        blank_canvas = self._get_blank_canvas()
        params_dict = {}
        w = random.randrange(
            self.config.SQUARE_MIN_SQUARE_SIZE, self.config.SQUARE_MAX_SQUARE_SIZE, 2)
        h = random.randrange(
            self.config.SQUARE_MIN_SQUARE_SIZE, self.config.SQUARE_MAX_SQUARE_SIZE, 2)
        x = random.randint(
            w / 2, self.config.IMAGE_SIZE - w / 2)
        y = random.randint(
            h / 2, self.config.IMAGE_SIZE - h / 2)
        pt1 = (int(x - w / 2), int(y + h / 2))
        pt2 = (int(x + w / 2), int(y - h / 2))
        color = random.choices(
            self.config.COLOR_VARIATIONS,
            weights=self.config.WEIGHT_COLOR_SELECTED)[0]
        line_thickness = random.choices(
            self.config.LINE_THICKNESS_VARIATIONS,
            weights=self.config.WEIGHT_LINE_THICKNESS_SELECTED,
        )[0]
        mask = cv2.rectangle(
            blank_canvas,
            pt1=pt1,
            pt2=pt2,
            color=color,
            thickness=line_thickness,
        )
        params_dict['choiced_shapes'] = 'square'
        params_dict['params'] = {
            'pt1': pt1,
            'pt2': pt2,
            'color': color,
            'line_thickness': line_thickness,
        }

        return (mask, params_dict)

    def _generate_triangle(self) -> Tuple[np.ndarray, dict]:
        blank_canvas = self._get_blank_canvas()
        params_dict = {}
        possible_polt_flag = False
        while possible_polt_flag is False:
            xl = random.randint(self.config.TRIANGLE_MIN_LENGTH,
                                self.config.TRIANGLE_MAX_LENGTH)
            yl = random.randint(self.config.TRIANGLE_MIN_LENGTH,
                                self.config.TRIANGLE_MAX_LENGTH)
            x1 = random.randint(
                xl, self.config.IMAGE_SIZE - xl)
            y1 = random.randint(
                yl, self.config.IMAGE_SIZE - yl)
            x2 = random.randint(x1 - xl, x1 + xl)
            y2 = random.randint(y1 - yl, y1 + yl)
            x3 = random.randint(x2 - xl, x2 + xl)
            y3 = random.randint(y2 - yl, y2 + yl)
            if (x3 <= self.config.IMAGE_SIZE & x3 >= 0) & \
                    (y3 <= self.config.IMAGE_SIZE & y3 >= 0):
                possible_polt_flag = True
        pts = [np.array(((x1, y1), (x2, y2), (x3, y3)))]
        color = random.choices(
            self.config.COLOR_VARIATIONS,
            weights=self.config.WEIGHT_COLOR_SELECTED)[0]
        line_thickness = random.choices(
            self.config.LINE_THICKNESS_VARIATIONS,
            weights=self.config.WEIGHT_LINE_THICKNESS_SELECTED,
        )[0]
        mask = cv2.polylines(
            blank_canvas,
            pts=pts,
            isClosed=self.config.TRIANGLE_IS_CLOSED,
            color=color,
            thickness=line_thickness,
        )
        params_dict['choiced_shapes'] = 'triangle'
        params_dict['params'] = {
            'pts': pts,
            'isClosed': self.config.TRIANGLE_IS_CLOSED,
            'color': color,
            'line_thickness': line_thickness,
        }

        return (mask, params_dict)
