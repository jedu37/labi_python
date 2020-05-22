from PIL import Image
from PIL import ExifTags
import sys

def main(fname):
    im = Image.open(fname)
    print("Modo: "+ im.mode)

main(sys.argv[1])