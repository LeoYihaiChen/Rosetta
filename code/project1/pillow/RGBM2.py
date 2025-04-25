from PIL import Image as IM
import numpy as nu
from colors import colorslist

HEIGHT = 256
WIDTH = 256

# empty list
pixels = []

for j in range(HEIGHT):
    pixel_line = [colorslist["black"]] * WIDTH

    for i in range(WIDTH):
        color = None
        
        if i < WIDTH / 2:
            if j < HEIGHT / 2:
                color = "red"
            else:
                color = "green"
        else:
            if j < HEIGHT / 2:
                color = "blue"
            else:
                color = "yellow"
                
        pixel_line[i] = colorslist[color]
        
    pixels.append(pixel_line)

pixel_array = nu.array(pixels, dtype=nu.uint8)
img = IM.fromarray(pixel_array, mode="RGB")   
img.save('/Users/yihaichen/Desktop/mycomputer/code/code/python/windowpy/images/bigcolored_image.bmp')
