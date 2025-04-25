from PIL import Image
 
# 设置图片的大小和颜色
width = 100
height = 100
color = (0, 0, 255)  # 蓝色，RGB值分别为0, 0, 255
 
# 创建一个新的图像，并填充蓝色
image = Image.new('RGB', (width, height), color)
image.save('blue_image.bmp')