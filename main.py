# 在这个文件中编写代码实现题目要求的功能
import keyword  # 建议使用这个库处理关键字
reserved_words = set(keyword.kwlist)

# 以下内容自行完成
# 在这个文件中编写代码实现题目要求的功能
import keyword  # 建议使用这个库处理关键字
reserved_words = set(keyword.kwlist)

# 读取 random_int.py 文件内容
with open('random_int.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

converted_lines = []
for line in lines:
    words = []
    # 按单词分割（简单处理，实际可根据需要优化）
    for word in line.split():
        if word in reserved_words:
            words.append(word)
        else:
            words.append(word.upper())
    # 重新拼接行
    converted_line = ' '.join(words) + '\n'
    converted_lines.append(converted_line)

# 将转换后的内容保存到新文件
with open('converted_random_int.py', 'w', encoding='utf-8') as f:
    f.writelines(converted_lines)
