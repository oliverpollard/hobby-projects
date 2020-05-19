from PIL import Image,ExifTags
from argparse import ArgumentParser
import os.path

def file_exists(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg

parser = ArgumentParser(description="produces square images with white borders")
parser.add_argument("-i", "--input", dest="input", required=True, help="input image", metavar="FILE", type=lambda x: file_exists(parser, x))
parser.add_argument("-o", "--output", dest="output", required=True, help="output image", metavar="FILE")

args = parser.parse_args()

image = Image.open(args.input)
x_size, y_size = image.size

for orientation in ExifTags.TAGS.keys():
    if ExifTags.TAGS[orientation]=='Orientation':
        break
exif=dict(image._getexif().items())


print(x_size, y_size)

if x_size > y_size:
	new_length = int(1.22549 * x_size)
elif x_size < y_size:
	new_length = int(1.22549 * y_size)
else:
	new_length = int(1.22549 * x_size)

if (new_length % 2) != 0:
   new_length = new_length + 1

new_size = (new_length, new_length)
print(new_size)
new_im = Image.new("RGB", new_size,color=(255,255,255))   ## luckily, this is already black!
print((new_length-x_size)/2, (new_length-y_size)/2)
new_im.paste(image, (int((new_length-x_size)/2), int((new_length-y_size)/2)))

"""

if exif[orientation] == 3:
    new_im=new_im.rotate(180, expand=True)
elif exif[orientation] == 6:
    new_im=new_im.rotate(270, expand=True)
elif exif[orientation] == 8:
    new_im=new_im.rotate(90, expand=True)
"""
new_im.save(args.output)