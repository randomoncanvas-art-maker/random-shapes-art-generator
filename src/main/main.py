import random
import argparse

import numpy as np
from evaluator import Evaluator
from generator import Generator
from preprocessor import Preprocessor
from config_init import ConfigInit
from tqdm import tqdm
from visualizer import Visualizer


def main(args):
    # config
    config = ConfigInit(args)

    # Preprocessing
    prepro = Preprocessor(config=config, file_path=config.input_file_path)
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
        "line": {
            "is_Generate": config.line_is_generate,
            "weight_selected": config.line_weight_selected
        },
        "circle": {
            "is_Generate": config.circle_is_generate,
            "weight_selected": config.circle_weight_selected
        },
        "ellipse": {
            "is_Generate": config.ellipse_is_generate,
            "weight_selected": config.ellipse_weight_selected
        },
        "square": {
            "is_Generate": config.square_is_generate,
            "weight_selected": config.square_weight_selected
        },
        "triangle": {
            "is_Generate": config.triangle_is_generate,
            "weight_selected": config.triangle_weight_selected
        },
    }
    shapes_candidates_and_weight = {
        name: shapes_is_generate_list[name]["weight_selected"]
        for name in shapes_is_generate_list if shapes_is_generate_list[name]["is_Generate"] is True
    }
    shapes_candidates_list = list(shapes_candidates_and_weight.keys())
    shapes_weight_list = list(shapes_candidates_and_weight.values())

    # Main processing
    for _ in tqdm(range(config.num_iterations)):
        best_score = -np.inf
        best_params = None
        best_mask = None

        for _ in range(config.num_plot_per_iter):
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

        if (best_params is not None) & (best_score >= config.score_threshold):
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
