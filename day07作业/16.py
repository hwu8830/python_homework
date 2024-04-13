# 过滤某个文件夹下的所有"xx.py"python文件

import os
import glob

def filter_python_files(folder_path):
    # 使用 glob 模块匹配文件夹下所有以 ".py" 结尾的文件
    python_files = glob.glob(os.path.join(folder_path, "*.py"))
    return python_files

# 测试
folder_path = "/path/to/your/folder"  # 替换为实际的文件夹路径
python_files = filter_python_files(folder_path)
print("文件夹下的所有 Python 文件：", python_files)
