import os
import time
from moviepy.editor import VideoFileClip
from PIL import Image

# 视频文件路径
video_path = 'tar.mp4'

# 保存图像的文件夹路径
output_dir = 'raw_frames'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 截取间隔（单位：秒）
interval = 5

# 读取视频文件
clip = VideoFileClip(video_path)

# 循环截取帧并保存
for t in range(0, int(clip.duration), interval):
    # 获取时间为 t 的帧
    frame = clip.get_frame(t * 1.001)

    # 生成文件名
    filename = os.path.join(output_dir, f'{t // 5}.jpg')

    # 保存图像
    Image.fromarray(frame).save(filename)

    # 显示进度
    print(f'Saved frame {t // 5}.')

    # 等待一段时间
    # time.sleep(1)

print('Done.')
