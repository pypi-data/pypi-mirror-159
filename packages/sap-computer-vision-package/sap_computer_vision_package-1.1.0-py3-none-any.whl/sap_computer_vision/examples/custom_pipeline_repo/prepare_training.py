import pathlib
import json
from metaflow import FlowSpec, step, argo, Parameter, JSONType
import subprocess
import os
import glob
import random


DATA_OUTPUT_DIR = str(pathlib.Path('/tmp/dataout'))
DATA_INPUT_DIR = pathlib.Path('/tmp/datain')


def read_files(folder_path):
    files = glob.glob(folder_path + '/*')
    return files


def synthesize_images(src_folder, dst_folder, bg_folder, sample_num=1):
    org_files = read_files(src_folder)
    bg_files = read_files(bg_folder)

    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    bash_cmd = "/sap_cv/synthesize_image/synthesize_background.sh {} {} {} {} {}"
    transparency = list(range(0, 15, 5))  # [0]
    angles = list(range(-30, 31, 10))

    for i in org_files:
        for j in range(sample_num):  # generate sample_num synthetic query per catalog
            bg = random.choice(bg_files)
            rand_t = random.choice(transparency)
            rand_a = random.choice(angles)
            bash_tmp = bash_cmd.format(bg, i, rand_t, rand_a, dst_folder)
            process = subprocess.Popen(
                bash_tmp.split(), stdout=subprocess.PIPE)
            _ = process.communicate()


class PrepareTraining(FlowSpec):
    data_input_img = Parameter("catalog_images")
    data_input_backgrounds = Parameter("background_images")
    image_target_size = Parameter("imagesize",
                                  help=f"Image size of the prepared data.",
                                  type=JSONType,
                                  default=json.dumps([500, 500]))
    seed = Parameter("seed",
                     help="Random seed.",
                     default=1337)
    @argo(output_artifacts=[{'name': 'prepareddata',
                             'globalName': 'prepareddata',
                             'path': str(DATA_OUTPUT_DIR),
                             'archive': {'none': {}}}],
          input_artifacts=[{'name': 'datain',
                            'path': str(DATA_INPUT_DIR)}])
    @step
    def start(self):
        synthesize_images(src_folder=self.data_input_img,
                          dst_folder=str(DATA_OUTPUT_DIR),
                          bg_folder=self.data_input_backgrounds,
                          sample_num=5)
        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == '__main__':
    PrepareTraining()
