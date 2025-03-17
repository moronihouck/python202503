def replace_sensitive_words(text, shield_file):
    """
    将输入文字中的屏蔽词替换为等长的 * 号
    :param text: 输入的待处理文字
    :param shield_file: 屏蔽词文件路径
    :return: 处理后的文字
    """
    # 读取屏蔽词列表
    try:
        with open(shield_file, 'r', encoding='utf-8') as f:
            shield_words = [line.strip() for line in f.readlines() if line.strip()]
            # 上面的一行命令和下面的几行代码效果是一样的
            # shield_words = []
            # for line in f.readlines():
            #     stripped = line.strip()
            #     if stripped:  # 非空
            #         shield_words.append(stripped)
    except FileNotFoundError:
        print(f"错误：文件 {shield_file} 不存在")
        return text  # 文件不存在，返回原文本

    # 从最长的屏蔽词开始替换，避免短词干扰长词
    shield_words.sort(key=len, reverse=True)

    # 逐个替换屏蔽词
    result = text
    for word in shield_words:
        if word in result:
            # 用等长的 * 替换
            replacement = '*' * len(word)
            result = result.replace(word, replacement)

    return result


# 主程序：控制台验证
if __name__ == "__main__":
    # 假设屏蔽词文件名为 'shield_words.txt'
    shield_file = 'censors.txt'

    # 从控制台输入待检测文字
    input_text = input("请输入待检测文字：")

    # 调用方法处理
    processed_text = replace_sensitive_words(input_text, shield_file)

    # 输出处理结果
    print("处理后的文字：", processed_text)