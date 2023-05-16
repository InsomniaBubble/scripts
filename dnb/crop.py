from PIL import Image
import os

# 图片文件夹路径
image_dir = 'cropped_frames'

# 遍历文件夹中的所有文件名
filenames = os.listdir(image_dir)
filenames = sorted(filenames, key=lambda x: int(x.split('.')[0]))

# 去除水平方向的黑边
for filename in filenames:
    print(filename)
    # 打开图片并获取其大小
    img = Image.open(os.path.join(image_dir, filename))
    width, height = img.size

    # 计算黑边的宽度
    left = 0
    right = width - 1
    while left < right and sum(1 for j in range(height) if img.getpixel((left, j))[0] < 50) > 0:
        left += 1
    while right > left and sum(1 for j in range(height) if img.getpixel((right, j))[0] < 50) > 0:
        right -= 1

    # 剪裁图片
    img = img.crop((left, 0, right + 1, height))
    img.save(os.path.join(image_dir, filename))