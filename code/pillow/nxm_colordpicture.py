from PIL import Image
import numpy
from colors import colorslist
import random

BLOCKW = int(input("Block Width: "))
BLOCKH = int(input("Block Height: "))
PATTERNW = int(input("PATTERN Width: "))
PATTERNH = int(input("PATTERN Height: "))

WIDTH = BLOCKW * PATTERNW
HEIGHT = BLOCKH * PATTERNH

picture_colors = []
for y in range(PATTERNH):
    WIDTH_colors = []
    for x in range(PATTERNW):
        # color = random.randint(0, len(colorslist)-1)
        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        WIDTH_colors.append(color)
    picture_colors.append(WIDTH_colors)
    
print(f"picture_colors = {picture_colors}")

pixel_lines = []

for pixel_y in range(HEIGHT):
    block_y = pixel_y // BLOCKH
    
    pixel_line = []
    for pixel_x in range(WIDTH):
        block_x = pixel_x // BLOCKW
        pixel_line.append(picture_colors[block_y][block_x])
        
    pixel_lines.append(pixel_line)

pixel_array = numpy.array(pixel_lines, dtype=numpy.uint8)
img = Image.fromarray(pixel_array, mode="RGB")   
img.save('/Users/yihaichen/Desktop/mycomputer/code/code/python/windowpy/images/nxmcolored_image.bmp')
