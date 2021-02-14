import os
import sys
from tqdm import tqdm
import glob

def predict3(folder, model):
    mp4Files = glob.glob(folder + "*.mp4")
    for video in tqdm(mp4Files, desc ="Progress", ncols= 80):
        cmd = 'python predict3.py --video_name=<video>  --load_weights=<model>'
        cmd = cmd.replace('<video>', video)
        cmd = cmd.replace('<model>', model)
        os.system(cmd)

def add_start_end_point(csv_dir, video_dir):
    csv_files = glob.glob(csv_dir + "*.csv")
    for csv in tqdm(csv_files, desc ="Progress", ncols= 80):
        cmd = 'python add_start_end_point.py <csv_file> <video_file>'
        cmd = cmd.replace('<csv_file>', csv)
        filename = csv.split('\\')[-1]
        video = video_dir + filename.replace('.csv', '.mp4')
        cmd = cmd.replace('<video_file>', video)
        os.system(cmd)

def curve_fitting(csv_dir, output_dir):
    csvFiles = glob.glob(csv_dir + "*.csv")
    for csv in tqdm(csvFiles, desc ="Progress", ncols= 80):
        cmd = 'python curve_fitting.py <csv_file> <output_image_directory>'
        cmd = cmd.replace('<csv_file>', csv)
        cmd = cmd.replace('<output_image_directory>', output_dir)
        try:
            cmd = cmd.replace('\\', '/')
        except:
            pass
        os.system(cmd)

def main():
#     predict3('data/', 'model_30')
#     add_start_end_point('predict/', 'predict/')
    curve_fitting('predict/', 'predict/')
if __name__ == '__main__':
    main()