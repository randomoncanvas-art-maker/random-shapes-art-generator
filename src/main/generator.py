import configparser
import random
from typing import Tuple

import cv2
import numpy as np


class Generator:

    def __init__(self, config: configparser.ConfigParser) -> None:
        self.config = config

    def _get_blank_canvas(self) -> np.ndarray:
        blank_canvas = np.zeros(
            (self.config.image_size, self.config.image_size), dtype=np.uint8)

        return blank_canvas

    def generate_shape(self, shape_name: str) -> np.ndarray:
        if shape_name == "line":
            mask = self._generate_line()
        elif shape_name == "circle":
            mask = self._generate_line()
        elif shape_name == "ellipse":
            mask = self._generate_line()
        elif shape_name == "square":
            mask = self._generate_line()
        elif shape_name == "triangle":
            mask = self._generate_line()
        else:
            pass

        return mask

    def _generate_line(self) -> Tuple[np.ndarray, dict]:
        blank_canvas = self._get_blank_canvas()
        params_dict = {}
        xl = random.randint(
            self.config.line_min_length, self.config.line_max_length)
        yl = random.randint(
            self.config.line_min_length, self.config.line_max_length)
        x1 = random.randint(
            xl, self.config.image_size - xl)
        y1 = random.randint(
            yl, self.config.image_size - yl)
        x2 = random.randint(x1 - xl, x1 + xl)
        y2 = random.randint(y1 - yl, y1 + yl)
        pt1 = (x1, y1)
        pt2 = (x2, y2)
        color = random.choices(
            self.config.color_variations,
            weights=self.config.weight_color_selected)[0]
        line_thickness = random.choices(
            self.config.line_thickness_variations,
            weights=self.config.weight_line_thickness_selected,
        )[0]
        mask = cv2.line(
            blank_canvas,
            pt1=pt1,
            pt2=pt2,
            color=color,
            thickness=line_thickness,
        )
        params_dict["choiced_shapes"] = "line"
        params_dict["params"] = {
            "pt1": pt1,
            "pt2": pt2,
            "color": color,
            "line_thickness": line_thickness,
        }

        return (mask, params_dict)

    def _generate_circle(self) -> Tuple[np.ndarray, dict]:
        blank_canvas = self._get_blank_canvas()
        params_dict = {}
        radius = random.randint(
            self.config.circle_min_radius, self.config.circle_max_radius)
        x = random.randint(
            radius, self.config.image_size - radius)
        y = random.randint(
            radius, self.config.image_size - radius)
        center = (x, y)
        color = random.choices(
            self.config.color_variations,
            weights=self.config.weight_color_selected)[0]
        line_thickness = random.choices(
            self.config.line_thickness_variations,
            weights=self.config.weight_line_thickness_selected,
        )[0]
        mask = cv2.circle(
            blank_canvas,
            center=center,
            radius=radius,
            color=color,
            thickness=line_thickness,
        )
        params_dict["choiced_shapes"] = "circle"
        params_dict["params"] = {
            "center": center,
            "radius": radius,
            "color": color,
            "line_thickness": line_thickness,
        }
        return (mask, params_dict)

    def _generate_ellipse(self) -> Tuple[np.ndarray, dict]:
        blank_canvas = self._get_blank_canvas()
        params_dict = {}
        xr = random.randint(
            self.config.ellipse_min_radius, self.config.ellipse_max_radius)
        yr = random.randint(
            self.config.ellipse_min_radius, self.config.ellipse_max_radius)
        x = random.randint(
            xr, self.config.image_size - xr)
        y = random.randint(
            yr, self.config.image_size - yr)
        angle = random.randint(0, 360)
        box = ((x, y), (xr, yr), angle)
        color = random.choices(
            self.config.color_variations,
            weights=self.config.weight_color_selected)[0]
        line_thickness = random.choices(
            self.config.line_thickness_variations,
            weights=self.config.weight_line_thickness_selected,
        )[0]
        mask = cv2.ellipse(
            blank_canvas, box=box, color=color, thickness=line_thickness)
        params_dict["choiced_shapes"] = "ellipse"
        params_dict["params"] = {
            "box": box,
            "color": color,
            "line_thickness": line_thickness,
        }

        return (mask, params_dict)

    def _generate_square(self) -> Tuple[np.ndarray, dict]:
        blank_canvas = self._get_blank_canvas()
        params_dict = {}
        w = random.randrange(
            self.config.square_min_square_size, self.config.square_max_square_size, 2)
        h = random.randrange(
            self.config.square_min_square_size, self.config.square_max_square_size, 2)
        x = random.randint(
            w / 2, self.config.image_size - w / 2)
        y = random.randint(
            h / 2, self.config.image_size - h / 2)
        pt1 = (int(x - w / 2), int(y + h / 2))
        pt2 = (int(x + w / 2), int(y - h / 2))
        color = random.choices(
            self.config.color_variations,
            weights=self.config.weight_color_selected)[0]
        line_thickness = random.choices(
            self.config.line_thickness_variations,
            weights=self.config.weight_line_thickness_selected,
        )[0]
        mask = cv2.rectangle(
            blank_canvas,
            pt1=pt1,
            pt2=pt2,
            color=color,
            thickness=line_thickness,
        )
        params_dict["choiced_shapes"] = "square"
        params_dict["params"] = {
            "pt1": pt1,
            "pt2": pt2,
            "color": color,
            "line_thickness": line_thickness,
        }

        return (mask, params_dict)

    def _generate_triangle(self) -> Tuple[np.ndarray, dict]:
        blank_canvas = self._get_blank_canvas()
        params_dict = {}
        possible_polt_flag = False
        while possible_polt_flag is False:
            xl = random.randint(self.config. triangle_min_length,
                                self.config. triangle_max_length)
            yl = random.randint(self.config. triangle_min_length,
                                self.config. triangle_max_length)
            x1 = random.randint(
                xl, self.config.image_size - xl)
            y1 = random.randint(
                yl, self.config.image_size - yl)
            x2 = random.randint(x1 - xl, x1 + xl)
            y2 = random.randint(y1 - yl, y1 + yl)
            x3 = random.randint(x2 - xl, x2 + xl)
            y3 = random.randint(y2 - yl, y2 + yl)
            if (x3 <= self.config.image_size & x3 >= 0) & \
                    (y3 <= self.config.image_size & y3 >= 0):
                possible_polt_flag = True
        pts = [np.array(((x1, y1), (x2, y2), (x3, y3)))]
        color = random.choices(
            self.config.color_variations,
            weights=self.config.weight_color_selected)[0]
        line_thickness = random.choices(
            self.config.line_thickness_variations,
            weights=self.config.weight_line_thickness_selected,
        )[0]
        mask = cv2.polylines(
            blank_canvas,
            pts=pts,
            isClosed=self.config. triangle_is_closed,
            color=color,
            thickness=line_thickness,
        )
        params_dict["choiced_shapes"] = "triangle"
        params_dict["params"] = {
            "pts": pts,
            "isClosed": self.config. triangle_is_closed,
            "color": color,
            "line_thickness": line_thickness,
        }

        return (mask, params_dict)
