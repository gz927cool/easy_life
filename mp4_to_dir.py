import os
import shutil
"""
Why? :使用Radarr软件进行电影的管理和搜刮，但该软件加本地已经有的影片时要求每个电影必须在根目录中有自己的文件夹。
How? :检测当前目录中的mp4格式文件，为每个mp4文件生成一个同名文件夹，然后将该mp4文件移动到该文件夹中。
"""
# 获取当前目录下的所有文件
files = os.listdir('.')

# 遍历文件，找到mp4格式的文件
for file in files:
    if file.endswith('.mp4'):
        # 为该mp4文件生成一个同名文件夹
        folder_name = file.rsplit('.', 1)[0]
        os.makedirs(folder_name, exist_ok=True)
        
        # 将mp4文件移动到该文件夹中
        shutil.move(file, os.path.join(folder_name, file))
