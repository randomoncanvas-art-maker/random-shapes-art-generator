import configparser
import json
import os
from typing import List

import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import ArtistAnimation


class Visualizer:
    def __init__(self, config: configparser.ConfigParser) -> None:
        self.config = config
        self.save_dir_path = self.config.save_dir_path
        if not os.path.isdir(self.save_dir_path):
            os.mkdir(self.save_dir_path)

    def save_generated_images(self, canvas: np.ndarray) -> None:
        output_img = (1.0 - canvas) * 255
        output_img = output_img.astype(np.uint8)
        plt.figure(figsize=(6, 6))
        plt.imshow(output_img, cmap='gray')
        plt.axis('off')
        # plt.show()
        # save
        cv2.imwrite(os.path.join(self.save_dir_path,
                    'output_images.png'), output_img)

    def save_generated_images_with_target(self, target: np.ndarray, canvas: np.ndarray) -> None:
        target_img = (1.0 - target) * 255
        target_img = target_img.astype(np.uint8)
        output_img = (1.0 - canvas) * 255
        output_img = output_img.astype(np.uint8)
        fig = plt.figure()
        a = fig.add_subplot(1, 2, 1)
        plt.imshow(target_img, cmap='gray')
        a.axis('off')
        a = fig.add_subplot(1, 2, 2)
        plt.imshow(output_img, cmap='gray')
        a.axis('off')
        # save
        plt.savefig(os.path.join(self.save_dir_path,
                    'output_compare_images.png'))

    def save_generated_animation(self, records_canvas: List[np.ndarray]) -> None:
        imgs = []
        fig = plt.figure(figsize=(6, 6))
        for shapes_id in range(0, len(records_canvas)):
            output_img = (1.0 - records_canvas[shapes_id]) * 255
            output_img = output_img.astype(np.uint8)
            plt.axis('off')
            img = plt.imshow(output_img, cmap='gray')
            imgs.append([img])
        ani = ArtistAnimation(
            fig, imgs, interval=100, blit=True, repeat_delay=3000
        )
        # save
        ani.save(
            os.path.join(
                self.save_dir_path,
                'output_animation.gif'), writer='pillow'
        )

    def save_score_graph(self, records_scores: List[float]) -> None:
        plt.figure(figsize=(10, 4))
        plt.plot(
            range(1, len(records_scores) + 1),
            records_scores,
            marker='o',
            markersize=2,
            linewidth=1,
        )
        plt.xlabel('Shapes ID')
        plt.ylabel('Score')
        plt.title('Score Progression')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        # save
        plt.savefig(os.path.join(self.save_dir_path, 'output_score_graph.png'))

    def save_parameters(self,
                        records_params: List[dict],
                        records_scores: List[float],
                        records_masks: List[np.ndarray],
                        records_canvas: List[np.ndarray]) -> None:
        resules_dict = {}
        shapes_id = 1
        for params, score, mask, convas in zip(records_params, records_scores, records_masks, records_canvas):
            resules_dict['Shapes_id'] = shapes_id
            resules_dict['Params'] = params
            resules_dict['Score'] = score
            resules_dict['Mask'] = mask.tolist()
            resules_dict['Convas'] = convas.tolist()
            shapes_id += 1
        with open(os.path.join(self.save_dir_path, 'records.json'), mode='w') as f:
            d = json.dumps(resules_dict, indent=4)
            f.write(d)
