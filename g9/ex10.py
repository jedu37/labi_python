from PIL import Image
from PIL import ExifTags
import sys

def color_switch(im):
    new_im = Image.new(im.mode, im.size)
    width, height = im.size
    for x in range(width):
        for y in range(height):
            p = im.getpixel( (x,y) )
            r = p[1]
            g = p[0]
            b = p[2]
            new_im.putpixel((x,y), (r, g, b) )

    return new_im

def color_invert(im):
    new_im = Image.new(im.mode, im.size)
    width, height = im.size
    for x in range(width):
        for y in range(height):
            p = im.getpixel( (x,y) )
            r = 255-p[0]
            g = 255-p[1]
            b = 255-p[2]
            new_im.putpixel((x,y), (r, g, b) )

    return new_im

def main(argv):
    fname = argv[1]
    im = Image.open(fname)
    i = 0

    while i < len(argv):
        if argv[i] == "switch":
            im = color_switch(im)
            fname = fname + "-switched"

        elif argv[i] == "invert":
            im = color_invert(im)
            fname = fname + "-invertesd"
        i += 1
    
    im.save(fname+"-new.jpg")

main(sys.argv)