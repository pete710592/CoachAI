import os
import cv2
import sys
import random
import shutil
import pandas as pd

'''
Usage: python add_start_end_point.py <csv file> <video file>
Input: csv file, video file
Output: csv file(!!OVERWRITE!!)
'''

def main():
    # Variables
    csv_path = sys.argv[1]
    video_path = sys.argv[2]
    csv = csv_path.split('/')[-1]
    video = csv.replace('.csv', '.mp4')
    pixel_x, pixel_y = [], []

    def mouse(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            pixel_x.append(x)
            pixel_y.append(y)
            
    def frameGenerator(video_path):
        cmd = "python Frame_Generator.py <video> tmp"
        cmd = cmd.replace("<video>", video_path)
        os.system(cmd)

    def getCoordinate(index):
        frame = "tmp/" + str(index) + ".png"
        img = cv2.imread(frame)
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("image", img)
        cv2.setMouseCallback("image", mouse)

    def releaseTmp():
        try:
            shutil.rmtree("tmp")
        except OSError as e:
            print(e)

    # Read csv file
    df = pd.read_csv(csv_path)

    # Add start point
    if df.loc[0, 'X'] == 0:
        df.loc[0, 'X'] = 974
        df.loc[0, 'Y'] = 538

    # Handle nulls
    null_index = list(df[df['X']==0].index)
    sample = random.sample(null_index[:-1], round(len(null_index)*0.25))
    sample.sort()

    # Handle nulls (ONLY END POINT)
    sample = []
    if(df.loc[len(df)-1, 'X'] == 0):
        sample.append(len(df)-1)

    # if sample/end point isn't empty
    if sample:
        print('\n' + csv_path)

        # Generate frames
        frameGenerator(video_path)

        for index in sample:
            getCoordinate(index)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # Fill in dataframe
        for i in range(len(sample)):
            df.loc[sample[i], 'X'] = pixel_x[i]
            df.loc[sample[i], 'Y'] = pixel_y[i]

        # Delete frames
        releaseTmp()

    # Overwrite csv file
    df.to_csv(csv_path, index=False)

if __name__ == "__main__":
    main()