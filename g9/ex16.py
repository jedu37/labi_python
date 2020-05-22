from PIL import Image
from PIL import ExifTags
import sys
import math

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

def gamma_correction(im,g):
    new_im = im.convert("YCbCr")
    width, height = im.size
    new_img = Image.new("YCbCr", im.size)
    f = 255/(math.pow(255,g))
    for x in range(width):
        for y in range(height):
            pixel = new_im.getpixel( (x,y) )
            py = min(255, int(math.pow(pixel[0],g) * f)) # [0] is the Y channel
            new_img.putpixel( (x,y), (py, pixel[1], pixel[2]) )
    
    return new_img

def saturation_correction(im,f):
    new_im = im.convert("YCbCr")
    width, height = im.size
    new_img = Image.new("YCbCr", im.size)
    for x in range(width):
        for y in range(height):
            p = new_im.getpixel( (x,y) )
            py = p[0]
            pb = min(255,int((p[1] - 128) * f) + 128)
            pr = min(255,int((p[2] - 128) * f) + 128)
            new_img.putpixel( (x,y), (py, pb, pr) )
    
    return new_img

def sepia(im):
    new_im = Image.new(im.mode, im.size)
    width, height = im.size
    for x in range(width):
        for y in range(height):  
            p = im.getpixel( (x,y) )
            r = int(0.189*p[0] + 0.769*p[1] + 0.393*p[2])
            g = int(0.168*p[0] + 0.686*p[1] + 0.349*p[2])
            b = int(0.131*p[0] + 0.534*p[1] + 0.272*p[2])
            new_im.putpixel((x,y), (r, g, b) )

    return new_im

def lomo(im):
    new_im = Image.new(im.mode, im.size)
    width, height = im.size
    for x in range(width):
        for y in range(height):  
            p = im.getpixel( (x,y) )
            b = int(0.189*p[0] + 0.769*p[1] + 0.393*p[2])
            g = int(0.168*p[0] + 0.686*p[1] + 0.349*p[2])
            r = int(0.131*p[0] + 0.534*p[1] + 0.272*p[2])
            new_im.putpixel((x,y), (r, g, b) )

    return new_im

def is_edge(im, x,y, diff, bw):
    #Obter o pixel
    p = im.getpixel( (x , y) )
    width, height = im.size
    if x < width-1 and y < height-1 and x > 0 and y > 0:
        #Vizinhos acima e abaixo
        for vx in range(-1,1):
            for vy in [-1, 1]:
                px = im.getpixel( (x + vx, y + vy) )
                if abs(p[0]- px[0]) > diff:
                    return (0,0,0)
        #Vizinhos da esquerda e direita
        for vx in [-1, 1]:
            px = im.getpixel( (x + vx, y) )
            if abs(p[0]- px[0]) > diff:
                return (0,128,128)
    
    if bw :
        return (255,255,255)
    else:
        return p

def find_edges(im, bw ,diff):
    new_im = Image.new(im.mode, im.size)
    width, height = im.size
    for x in range(width):
        for y in range(height):  
            p = is_edge(im,x,y,diff,bw)
            new_im.putpixel((x,y),p)

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

        elif argv[i] == "gray":
            im = effect_gray(im)
            fname = fname + "-gray"

        elif argv[i] == "intensity":
            im = effect_intensity(im, float(argv[i+1]))
            fname = fname + "-f_"+argv[i+1]
        
        elif argv[i] == "gamma":
            im = gamma_correction(im, float(argv[i+1]))
            fname = fname + "-gamma_"+argv[i+1]

        elif argv[i] == "saturation":
            im = saturation_correction(im, float(argv[i+1]))
            fname = fname + "-saturated_"+argv[i+1]
        
        elif argv[i] == "sepia":
            im = sepia(im)
            fname = fname + "-sepia"

        elif argv[i] == "lomo":
            im = lomo(im)
            fname = fname + "-lomo"
        
        elif argv[i] == "edge":
            im = find_edges(im , bool(argv[i+1]), float(argv[i+2]))
            fname = fname + "-edges"

        i += 1
    
    im.save(fname+"-new.jpg")

main(sys.argv)