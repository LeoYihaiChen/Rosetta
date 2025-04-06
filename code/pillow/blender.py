from PIL import Image
import numpy


DIRECTORY_PATH = "/Users/yihaichen/Desktop/mycomputer/code/project1/python/windowpy/images/"


def blendImages(path1 : str, path2 : str) -> None:

    img1 = None
    img2 = None
    
    try:
        img1 = Image.open(path1)
        img2 = Image.open(path2)
    except:
        print("Error: File open exception")
        return
    
    new1 = resize(img1, 1024, 512)    
    new2 = resize(img2, 1024, 512)
    
    output = Image.blend(new1, new2, 0.5)
    output.save(DIRECTORY_PATH + "blended.bmp")
    
def resize(image : Image, new_width : int, new_height : int) -> Image:
    old_width = image.width
    old_height = image.height

    if new_width == old_width and new_height == old_height:
        return image
    
    scale_x = old_width / new_width
    scale_y = old_height / new_height

    new_pixels = []

    for y in range(new_height):
        new_line = []
        old_y = int(y * scale_y)
        for x in range(new_width):
            old_x = int(x * scale_x)
            pixel = image.getpixel((old_x, old_y))
            new_line.append(pixel)
            
        new_pixels.append(new_line)
        
    pixel_array = numpy.array(new_pixels, dtype=numpy.uint8)
    output_image = Image.fromarray(pixel_array, mode="RGB")
    return output_image

blendImages('/Users/yihaichen/Desktop/mycomputer/png/军事/歼击机/test1.jpg',
            '/Users/yihaichen/Desktop/mycomputer/png/军事/歼击机/test2.jpg')      