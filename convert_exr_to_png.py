import os
import numpy as np
import cv2

os.environ["OPENCV_IO_ENABLE_OPENEXR"] = "1"

fpath = '/home/raychorn/images/'

fpath2 = '/home/raychorn/images-png/'
if not os.path.exists(fpath2):
    os.makedirs(fpath2)

exr = os.path.join(fpath, 'V1-0001_CappySmack_Noodles00108000.exr')
png = "{}.png".format(os.path.splitext(exr)[0])

def convert_exr_to_png( exr_file, png_file):
    im = cv2.imread( exr_file,-1)
    im = im*65535
    im[im>65535] = 65535
    im = np.uint16( im)
    cv2.imwrite( png_file, im)
    print("{} --> {}".format(exr_file, png_file))


if (__name__ == '__main__'):
    # for all files in fpath convert all files ending in .exr to .png
    for f in os.listdir(fpath):
        if f.endswith('.exr'):
            exr = os.path.join(fpath, f)
            png = "{}.png".format(os.path.splitext(exr)[0].replace(fpath, fpath2))
            convert_exr_to_png(exr, png)
            