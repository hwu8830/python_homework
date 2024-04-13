# 根据完整的路径从路径中分离文件路径、文件名及扩展名 
def separate_path(s):
    # 分离文件路径和文件名
    last_slash_index = s.rfind("/")
    file_path = s[:last_slash_index+1]
    file_name = s[last_slash_index+1:]
    
    # 分离文件名和扩展名
    dot_index = file_name.rfind(".")
    if dot_index == -1:  # 如果文件名中不包含扩展名
        file_extension = ""
        file_name_without_extension = file_name
    else:
        file_extension = file_name[dot_index+1:]
        file_name_without_extension = file_name[:dot_index]

    return file_path, file_name_without_extension, file_extension

s = input("请输入完整的文件路径：")
file_path, file_name, file_extension = separate_path(s)
print("文件路径:", file_path)
print("文件名:", file_name)
print("扩展名:", file_extension)
