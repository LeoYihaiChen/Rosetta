from PIL import Image
import numpy

WIDTH = 1024
HEIGHT = 1024

RADIUS = 100
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

pixel_lines = []

for pixel_y in range(HEIGHT): 
    pixel_line = []
    for pixel_x in range(WIDTH):
        dist_x = pixel_x - CENTER_X
        dist_y = pixel_y - CENTER_Y
        
        if dist_x * dist_x + dist_y * dist_y <= RADIUS * RADIUS:
            color = (255, 0, 0)
        else:
            color = (0, 0, 0)        
        
        pixel_line.append(color)

    pixel_lines.append(pixel_line)

pixel_array = numpy.array(pixel_lines, dtype=numpy.uint8)
img = Image.fromarray(pixel_array, mode="RGB")   
img.save('/Users/yihaichen/Desktop/mycomputer/code/code/python/windowpy/images/circle.bmp')
