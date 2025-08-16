import argparse
import logging
import random

import numpy as np
from config_init import ConfigInit
from evaluator import Evaluator
from generator import Generator
from preprocessor import Preprocessor
from rich.logging import RichHandler
from tqdm import tqdm
from visualizer import Visualizer


def main(args):
    # setiing logger
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(markup=True, rich_tracebacks=True)]
    )
    # config
    config = ConfigInit(args)

    # Preprocessing
    prepro = Preprocessor(config=config, file_path=config.INPUT_FILE_PATH)
    canvas = prepro.canvas
    target = prepro.target

    # Evaluator
    eval = Evaluator(config=config, target=target)

    # generator
    gen = Generator(config=config)

    # Lists for recording shapes
    records_params = []
    records_scores = []
    records_masks = []
    records_canvas = []

    # Selecting shapes to generate
    shapes_is_generate_list = {
        'line': {
            'is_Generate': config.LINE_IS_GENERATE,
            'weight_selected': config.LINE_WEIGHT_SELECTED
        },
        'circle': {
            'is_Generate': config.CIRCLE_IS_GENERATE,
            'weight_selected': config.CIRCLE_WEIGHT_SELECTED
        },
        'ellipse': {
            'is_Generate': config.ELLIPSE_IS_GENERATE,
            'weight_selected': config.ELLIPSE_WEIGHT_SELECTED
        },
        'square': {
            'is_Generate': config.SQUARE_IS_GENERATE,
            'weight_selected': config.SQUARE_WEIGHT_SELECTED
        },
        'triangle': {
            'is_Generate': config.TRIANGLE_IS_GENERATE,
            'weight_selected': config.TRIANGLE_WEIGHT_SELECTED
        },
    }
    shapes_candidates_and_weight = {
        name: shapes_is_generate_list[name]['weight_selected']
        for name in shapes_is_generate_list if shapes_is_generate_list[name]['is_Generate'] is True
    }
    shapes_candidates_list = list(shapes_candidates_and_weight.keys())
    shapes_weight_list = list(shapes_candidates_and_weight.values())

    # Main processing
    for _ in tqdm(range(config.NUM_ITERATIONS)):
        best_score = -np.inf
        best_params = None
        best_mask = None

        for _ in range(config.NUM_PLOT_PER_ITER):
            # choise shapes
            choiced_shape = random.choices(
                shapes_candidates_list, weights=shapes_weight_list)[0]
            mask, params_dict = gen.generate_shape(shape_name=choiced_shape)
            score = eval.evaluate_function(mask=mask, canvas=canvas)
            if score > best_score:
                best_score = score
                best_params = params_dict
                best_mask = mask
            else:
                pass

        if (best_params is not None) & (best_score >= config.SCORE_THRESHOLD):
            canvas += best_mask
            canvas = np.clip(canvas, 0, 1)
            records_params.append(best_params)
            records_scores.append(best_score)
            records_masks.append(best_mask)
            records_canvas.append(canvas)
        else:
            pass

    # Visualizer
    visual = Visualizer(config=config)
    visual.save_generated_images(
        canvas=canvas)
    visual.save_generated_images_with_target(
        canvas=canvas, target=target)
    visual.save_generated_animation(
        records_canvas=records_canvas)
    visual.save_score_graph(
        records_scores=records_scores)
    visual.save_parameters(
        records_params=records_params,
        records_scores=records_scores,
        records_masks=records_masks,
        records_canvas=records_canvas)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='argparseTest.py',
        usage='Demonstration of argparser',
        description='description',
        epilog='end',
        add_help=True,  # -h/–help オプションの追加
    )
    parser.add_argument('-i', '--input_file_path',
                        help='Input image file path')
    parser.add_argument('-o', '--output_dir_path',
                        help='Output directory path')
    args = parser.parse_args()
    main(args)
