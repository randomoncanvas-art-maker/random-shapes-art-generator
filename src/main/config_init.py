import configparser
import os
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
            self.IMAGE_SIZE = int(config_ini['COMMON_PARAMETER']['Image_Size'])
            self.NUM_ITERATIONS = int(
                config_ini['COMMON_PARAMETER']['Num_Iterations'])
            self.NUM_PLOT_PER_ITER = int(
                config_ini['COMMON_PARAMETER']['Num_Plot_Per_Iter'])
            self.WHITE_PENALTY = float(
                config_ini['COMMON_PARAMETER']['White_Penalty'])
            self.SCORE_THRESHOLD = int(
                config_ini['COMMON_PARAMETER']['Score_Threshold'])
            self.COLOR_VARIATIONS = [float(i) for i in eval(
                config_ini['COMMON_PARAMETER']['Color_Variations'])]
            self.WEIGHT_COLOR_SELECTED = [float(i) for i in eval(
                config_ini['COMMON_PARAMETER']['Weight_Color_Selected'])]
            self.LINE_THICKNESS_VARIATIONS = [int(i) for i in eval(
                config_ini['COMMON_PARAMETER']['Line_Thickness_Variations'])]
            self.WEIGHT_LINE_THICKNESS_SELECTED = [float(i) for i in eval(config_ini[
                'COMMON_PARAMETER']['Weight_Line_Thickness_Selected'])]
            self.INPUT_FILE_PATH = self.args.input_file_path
            self.SAVE_DIR_PATH = self.args.output_dir_path
            # line parameters
            self.LINE_IS_GENERATE = bool(
                config_ini['LINE_PARAMETER']['Is_Generate'])
            self.LINE_WEIGHT_SELECTED = float(
                config_ini['LINE_PARAMETER']['Weight_Selected'])
            self.LINE_MIN_LENGTH = int(
                config_ini['LINE_PARAMETER']['Min_Length'])
            self.LINE_MAX_LENGTH = int(
                config_ini['LINE_PARAMETER']['Max_Length'])
            # circle parameters
            self.CIRCLE_IS_GENERATE = bool(
                config_ini['CIRCLE_PARAMETER']['Is_Generate'])
            self.CIRCLE_WEIGHT_SELECTED = float(
                config_ini['CIRCLE_PARAMETER']['Weight_Selected'])
            self.CIRCLE_MIN_RADIUS = int(
                config_ini['CIRCLE_PARAMETER']['Min_Radius'])
            self.CIRCLE_MAX_RADIUS = int(
                config_ini['CIRCLE_PARAMETER']['Max_Radius'])
            # ellipse parameters
            self.ELLIPSE_IS_GENERATE = bool(
                config_ini['ELLIPSE_PARAMETER']['Is_Generate'])
            self.ELLIPSE_WEIGHT_SELECTED = float(
                config_ini['ELLIPSE_PARAMETER']['Weight_Selected'])
            self.ELLIPSE_MIN_RADIUS = int(
                config_ini['ELLIPSE_PARAMETER']['Min_Radius'])
            self.ELLIPSE_MAX_RADIUS = int(
                config_ini['ELLIPSE_PARAMETER']['Max_Radius'])
            # square parameters
            self.SQUARE_IS_GENERATE = bool(
                config_ini['SQUARE_PARAMETER']['Is_Generate'])
            self.SQUARE_WEIGHT_SELECTED = float(
                config_ini['SQUARE_PARAMETER']['Weight_Selected'])
            self.SQUARE_MIN_SQUARE_SIZE = int(
                config_ini['SQUARE_PARAMETER']['Min_Square_Size'])
            self.SQUARE_MAX_SQUARE_SIZE = int(
                config_ini['SQUARE_PARAMETER']['Max_Square_Size'])
            # triangle parameters
            self.TRIANGLE_IS_GENERATE = bool(
                config_ini['TRIANGLE_PARAMETER']['Is_Generate'])
            self.TRIANGLE_WEIGHT_SELECTED = float(
                config_ini['TRIANGLE_PARAMETER']['Weight_Selected'])
            self.TRIANGLE_MIN_LENGTH = int(
                config_ini['TRIANGLE_PARAMETER']['Min_Length'])
            self.TRIANGLE_MAX_LENGTH = int(
                config_ini['TRIANGLE_PARAMETER']['Max_Length'])
            self.TRIANGLE_IS_CLOSED = bool(
                config_ini['TRIANGLE_PARAMETER']['Is_Closed'])

        except Exception as e:
            print('config error{0}'.format(e))
        #   logger.critical('config error {0}'.format(e))
