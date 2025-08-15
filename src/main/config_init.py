import os
import configparser
from typing import Any

CONFIG_FILE_PATH = '../../config/config.ini'


class ConfigInit:
    def __init__(self, args: Any) -> None:
        # Read config
        config_ini = configparser.ConfigParser()
        if not os.path.exists(CONFIG_FILE_PATH):
            #   logger.error('設定ファイルがありません')
            exit(-1)
        config_ini.read(CONFIG_FILE_PATH, encoding='utf-8')
        self.args = args
        # logging.info('----設定開始----')
        try:
            # common parameters
            self.image_size = int(config_ini["COMMON_PARAMETER"]["Image_Size"])
            self.num_iterations = int(
                config_ini["COMMON_PARAMETER"]["Num_Iterations"])
            self.num_plot_per_iter = int(
                config_ini["COMMON_PARAMETER"]["Num_Plot_Per_Iter"])
            self.white_penalty = float(
                config_ini["COMMON_PARAMETER"]["White_Penalty"])
            self.score_threshold = int(
                config_ini["COMMON_PARAMETER"]["Score_Threshold"])
            self.color_variations = [float(i) for i in eval(
                config_ini["COMMON_PARAMETER"]["Color_Variations"])]
            self.weight_color_selected = [float(i) for i in eval(
                config_ini["COMMON_PARAMETER"]["Weight_Color_Selected"])]
            self.line_thickness_variations = [int(i) for i in eval(
                config_ini["COMMON_PARAMETER"]["Line_Thickness_Variations"])]
            self.weight_line_thickness_selected = [float(i) for i in eval(config_ini[
                "COMMON_PARAMETER"]["Weight_Line_Thickness_Selected"])]
            self.input_file_path = self.args.input_file_path
            self.save_dir_path = self.args.output_dir_path
            # line parameters
            self.line_is_generate = bool(
                config_ini["LINE_PARAMETER"]["Is_Generate"])
            self.line_weight_selected = float(
                config_ini["LINE_PARAMETER"]["Weight_Selected"])
            self.line_min_length = int(
                config_ini["LINE_PARAMETER"]["Min_Length"])
            self.line_max_length = int(
                config_ini["LINE_PARAMETER"]["Max_Length"])
            # circle parameters
            self.circle_is_generate = bool(
                config_ini["CIRCLE_PARAMETER"]["Is_Generate"])
            self.circle_weight_selected = float(
                config_ini["CIRCLE_PARAMETER"]["Weight_Selected"])
            self.circle_min_radius = int(
                config_ini["CIRCLE_PARAMETER"]["Min_Radius"])
            self.circle_max_radius = int(
                config_ini["CIRCLE_PARAMETER"]["Max_Radius"])
            # ellipse parameters
            self.ellipse_is_generate = bool(
                config_ini["ELLIPSE_PARAMETER"]["Is_Generate"])
            self.ellipse_weight_selected = float(
                config_ini["ELLIPSE_PARAMETER"]["Weight_Selected"])
            self.ellipse_min_radius = int(
                config_ini["ELLIPSE_PARAMETER"]["Min_Radius"])
            self.ellipse_max_radius = int(
                config_ini["ELLIPSE_PARAMETER"]["Max_Radius"])
            # square parameters
            self.square_is_generate = bool(
                config_ini["SQUARE_PARAMETER"]["Is_Generate"])
            self.square_weight_selected = float(
                config_ini["SQUARE_PARAMETER"]["Weight_Selected"])
            self.square_min_square_size = int(
                config_ini["SQUARE_PARAMETER"]["Min_Square_Size"])
            self.square_max_square_size = int(
                config_ini["SQUARE_PARAMETER"]["Max_Square_Size"])
            # triangle parameters
            self.triangle_is_generate = bool(
                config_ini["TRIANGLE_PARAMETER"]["Is_Generate"])
            self.triangle_weight_selected = float(
                config_ini["TRIANGLE_PARAMETER"]["Weight_Selected"])
            self.triangle_min_length = int(
                config_ini["TRIANGLE_PARAMETER"]["Min_Length"])
            self.triangle_max_length = int(
                config_ini["TRIANGLE_PARAMETER"]["Max_Length"])
            self.triangle_is_closed = bool(
                config_ini["TRIANGLE_PARAMETER"]["Is_Closed"])

        except Exception as e:
            print("config error{0}".format(e))
        #   logger.critical("config error {0}".format(e))
