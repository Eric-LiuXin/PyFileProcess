import os
testPath = 'D:\Eric'
# 获取当前路径下所有子文件夹
sub_dir = [file for file in os.listdir(testPath) if os.path.isdir('\\'.join([testPath,file]))]

# 获取当前路径下的非目录子文件
sub_file = [file for file in os.listdir(testPath) if os.path.isfile(os.path.join(testPath,file))]

# 获取当前路径下的所有非目录子文件
all_file = [[os.path.join(root, file) for file in files] for root, dirs, files in os.walk(testPath)]

# 获取当前路径下的所有指定文件类型的非目录子文件
all_txt = list()
for root, dirs, files in os.walk(testPath):
    for file in files:
        file_path = os.path.join(root, file)
        if os.path.splitext(file_path)[1] == '.txt' : all_txt.append(file_path)

# 获取当前路径下的所有指定文件类型的非目录子文件 2
all_txt = list()
for root, dirs, files in os.walk(testPath):
    all_txt.extend([os.path.join(root, file) for file in files if os.path.splitext(os.path.join(root, file))[1] == '.txt'])
