import sys, os
import imageio

def convert_exr_to_jpg(exr_file, jpg_file):
    if not os.path.isfile(exr_file):
        return False

    filename, extension = os.path.splitext(exr_file)
    if not extension.lower().endswith('.exr'):
        return False

    # imageio.plugins.freeimage.download() #DOWNLOAD IT
    image = imageio.imread(exr_file)
    print(image.dtype)

    # remove alpha channel for jpg conversion
    image = image[:,:,:3]


    data = 65535 * image
    data[data>65535]=65535
    rgb_image = data.astype('uint16')
    print(rgb_image.dtype)
    #rgb_image = imageio.core.image_as_uint(rgb_image, bitdepth=16)

    imageio.imwrite(jpg_file, rgb_image, format='jpeg')
    return True


if __name__ == '__main__':
    exr = "torus.exr"
    jpg = "torus3.jpeg"
    convert_exr_to_jpg(exr, jpg)
