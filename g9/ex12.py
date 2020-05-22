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

def effect_gray(im):
    width, height = im.size
    new_im = Image.new("L", im.size)
    for x in range(width):
        for y in range(height):
            p = im.getpixel( (x,y) )
            l = int(p[0]*0.299 + p[1]*0.587 + p[2]*0.144)
            new_im.putpixel( (x,y), (l) )
    return new_im

def effect_intensity(im, f):
    new_im = im.convert("YCbCr")
    width, height = im.size
    new_img = Image.new("YCbCr", im.size)
    for x in range(width):
        for y in range(height):
            pixel = new_im.getpixel( (x,y) )
            py = min(255, int(pixel[0] * f)) # [0] is the Y channel
            new_img.putpixel( (x,y), (py, pixel[1], pixel[2]) )
    
    return new_img

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

        elif argv[i] == "gray":
            im = effect_gray(im)
            fname = fname + "-gray"

        elif argv[i] == "intensity":
            im = effect_intensity(im, float(argv[i+1]))
            fname = fname + "-f_"+argv[i+1]

        i += 1
    
    im.save(fname+"-new.jpg")

main(sys.argv)