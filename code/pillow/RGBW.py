from PIL import Image
import numpy as np

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pixels = [[RED, GREEN], [BLUE, YELLOW]]
pixel_array = np.array(pixels, dtype=np.uint8)

img = Image.fromarray(pixel_array, mode="RGB")

# 保存图像
img.save('colored_image.bmp')