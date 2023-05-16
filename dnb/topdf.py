from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PIL import Image
import os

# 图片文件夹路径和输出文件名
image_dir = 'cropped_frames'
output_filename = 'raw.pdf'

# 创建 PDF 文件
c = canvas.Canvas(output_filename, pagesize=A4)
c.setTitle("电脑报 1992年合订本")

# 遍历文件夹中的所有文件名
filenames = os.listdir(image_dir)
filenames = sorted(filenames, key=lambda x: int(x.split('.')[0]))

# 将每张图片插入到 PDF 中
for filename in filenames:
    print(filename)
    # 打开图片并获取其大小
    img = Image.open(os.path.join(image_dir, filename))
    width, height = img.size

    # 计算缩放比例，使图片适合 PDF 页面
    if width > height:
        ratio = A4[0] / width
    else:
        ratio = A4[1] / height

    # 将图片插入到 PDF 中
    c.drawImage(os.path.join(image_dir, filename), 0, 0, width * ratio, height * ratio)

    # 添加新页面
    c.showPage()

# 保存 PDF 文件
c.save()
