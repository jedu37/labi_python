from PIL import Image
from PIL import ExifTags
from PIL import ImageDraw
from PIL import ImageFont
import sys

def main(fname):
    im = Image.open(fname)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("g9/Radens.ttf", 40)
    draw.text( (20, 20) ,"LabI", (255,255,255), font=font)
    im.save(fname+"-word.jpg")

main(sys.argv[1])