from PIL import Image
from PIL import ExifTags
import sys

def midPoint(x1,y1,x2,y2):
    x = (x1/2) - (x2/2)
    y = (y1/2) - (y2/2)

    return x,y

def main(f1name,f2name,f):
    im = Image.open(f1name)
    i_width,i_height = im.size
    watermark = Image.open(f2name)
    w_width,w_height = watermark.size
    x_start,y_start = midPoint(i_width,i_height, w_width,w_height)
    for x in range(w_width):
        for y in range(w_height):
            x1 = int(x+x_start)
            y1 = int(y+y_start)  
            p1 = im.getpixel( (x1,y1) )
            p2 = watermark.getpixel( (x,y) )
            if(p2[3] == 0):
                continue
            r = int(p1[0]*(1-f)+p2[0]*f)
            g = int(p1[1]*(1-f)+p2[1]*f)
            b = int(p1[2]*(1-f)+p2[2]*f)
            im.putpixel((x1,y1), (r, g, b) )
    
    im.save(f1name+"-wm.jpg")

main(sys.argv[1],sys.argv[2],float(sys.argv[3]))