from PIL import Image
from PIL import ExifTags
import sys

def main(fname):
    im = Image.open(fname)
    width, height = im.size
    for s in [0.2, 8]:
        dimension = ( int(width*s), int(height*s) )
        new_im = im.resize( dimension, Image.NEAREST)
        new_im.save(fname+"_NEAREST_"+"-%.2f.jpg" % s)
    for s in [0.2, 8]:
            dimension = ( int(width*s), int(height*s) )
            new_im = im.resize( dimension, Image.BILINEAR)
            new_im.save(fname+"_BILINEAR_"+"-%.2f.jpg" % s)
    for s in [0.2, 8]:
        dimension = ( int(width*s), int(height*s) )
        new_im = im.resize( dimension, Image.BICUBIC)
        new_im.save(fname+"_BICUBIC_"+"-%.2f.jpg" % s)
    for s in [0.2, 8]:
            dimension = ( int(width*s), int(height*s) )
            new_im = im.resize( dimension, Image.ANTIALIAS)
            new_im.save(fname+"_ANTIALIAS_"+"-%.2f.jpg" % s)


main(sys.argv[1])