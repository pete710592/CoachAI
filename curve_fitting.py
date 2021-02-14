import os
import sys
import cv2
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from utils.functions import checkDirExist

'''
Usage: python curve_fitting.py <csv file> <output image directory>
Input: csv file, output directory
Output: csv file(!!OVERWRITE!!), image
'''

def main():
    # Variables
    filepath = sys.argv[1]
    output_dir = sys.argv[2]
    filename = filepath.split('/')[-1]
    checkDirExist(output_dir)
    
    # Read the csv file and save as dataframe
    df = pd.read_csv(filepath)

    # Remove nulls
    xdata = np.array(df[df['X']!=0]['X'])
    ydata = np.array(df[df['Y']!=0]['Y'])

    # Curve fitting
    def func(x, a, b, c, d, e):
        return a*x**4 + b*x**3 + c*x**2 + d*x + e
    popt, pcov = curve_fit(func, xdata, ydata)

    # Interpolation method
    df['X'] = df['X'].replace(0, np.nan)
    df = df.interpolate()
    df['X'] = round(df['X'])
    df.loc[df['Y']==0, 'Y'] = round(func(df[df['Y']==0]['X'], *popt))

    # Adjust data type
    df = df.astype({'X':'int32', 'Y':'int32'})

    # Overwrite csv files
    df.to_csv(filepath, index=False)

    # Plot
    img = np.ones((1080, 1920, 3), np.uint8)*255
    # img = cv2.imread('image.png')
    point_color = [0, 0, 0]

    # log
    error = False

    for index in range(len(df['X'])):
        y, x = df.loc[index, 'X'], df.loc[index, 'Y']
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    img[x+i, y+j] = point_color
                except IndexError as e:
                    error = True
                    pass
    
    # log
    if error == True:
        f = open('error.txt', 'a')
        f.write('\n'+str(filename))
        f.close()

    # Save as image
    output = filename.replace('.csv', '.jpg')
    output = os.path.join(output_dir, output)
    cv2.imwrite(output, img)

if __name__ == "__main__":
    main()