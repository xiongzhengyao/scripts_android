import os

# 判断是文件还是文件夹
def is_dir(path):
    return os.path.isdir(path)

def is_file(path):
    return os.path.isfile(path)

