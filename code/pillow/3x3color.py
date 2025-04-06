from PIL import Image as IM
import numpy as nu
from colors import colorslist

HEIGHT = 300
WIDTH = 300

# empty list
pixels = []

for j in range(HEIGHT):
    pixel_line = [colorslist[0]] * WIDTH

    for i in range(WIDTH):
        color = None
        
        if i < WIDTH / 3:
            if j < HEIGHT / 3:
                color = 3-1
            elif j < HEIGHT / 3 * 2:
                color = 4-1
            else:
                color = 5-1
        elif i < WIDTH / 3 * 2:
            if j < HEIGHT / 3:
                color = 6-1
            elif j < HEIGHT / 3 * 2:
                color = 7-1
            else:
                color = 8-1
        else:
            if j < HEIGHT / 3:
                color = 9-1
            elif j < HEIGHT / 3 * 2:
                color = 10-1
            else:
                color = 11-1
                
        pixel_line[i] = colorslist[color]
        
    pixels.append(pixel_line)

pixel_array = nu.array(pixels, dtype=nu.uint8)
img = IM.fromarray(pixel_array, mode="RGB")   
img.save('/Users/yihaichen/Desktop/mycomputer/code/project1/python/windowpy/images/3x3_image.bmp')
