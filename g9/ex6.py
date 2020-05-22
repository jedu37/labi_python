from PIL import Image
import sys

def main(fname):
    im = Image.open(fname)
    for i in [".tiff",".png",".bmp"]:
        im.save(fname+i)

main(sys.argv[1])