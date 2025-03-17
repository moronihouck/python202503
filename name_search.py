import os

def search_files_and_content(directory, keyword):
    """
    搜索指定目录中文件名和内容中含有关键字的文件和目录
    :param directory: 指定文件夹路径
    :param keyword: 要搜索的关键字
    """
    # 用于存储结果
    name_matches = []  # 文件名或目录名中含有关键字
    content_matches = []  # 文件内容中含有关键字

    # 确保目录存在
    if not os.path.exists(directory):
        print(f"错误：目录 {directory} 不存在")
        return

    # 递归遍历目录
    for root, dirs, files in os.walk(directory):
        # 检查目录名
        for dir_name in dirs:
            if keyword.lower() in dir_name.lower():
                full_path = os.path.join(root, dir_name)
                name_matches.append(f"目录: {full_path}")

        # 检查文件名和内容
        for file_name in files:
            full_path = os.path.join(root, file_name)
            # 检查文件名是否含有关键字
            if keyword.lower() in file_name.lower():
                name_matches.append(f"文件: {full_path}")

            # 检查文件内容（仅限文本文件）
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if keyword.lower() in content.lower():
                        content_matches.append(full_path)
            except (IOError, UnicodeDecodeError):
                # 跳过无法读取的文件（如二进制文件）
                continue

    # 输出结果
    print(f"\n文件名或目录名中含有 '{keyword}' 的结果：")
    if name_matches:
        for match in name_matches:
            print(match)
    else:
        print("无匹配项")

    print(f"\n文件内容中含有 '{keyword}' 的结果：")
    if content_matches:
        for match in content_matches:
            print(match)
    else:
        print("无匹配项")

# 主程序
if __name__ == "__main__":
    # 获取用户输入
    search_dir = input("请输入要搜索的文件夹路径：")
    search_keyword = input("请输入要搜索的关键字：")

    # 执行搜索
    search_files_and_content(search_dir, search_keyword)