# ---------------------------------------------------------------------
# 字符串

# 字符串可使用单引号 ‘ 或者双引号 "
print("Cat's tail.")
print('I said, "why?"')
print('Dog\'s head.')

# 字符串的衔接，可使用加号 + 或者任意空格、空行
print('Hello, ' + 'world.')
print("Hello, " 'world.')

# 字符串的重复
print('-' * 80)

# 字符串索引
print('Python'[1])

# 数长度
s = "The quick brown fox jumps over a lazy dog."
print(len(s))

# 查找字符
print(s.index('s'))
print(s.find('S'))  # 大写 S 找不到，返回 -1

# 替换字符
print(len(s.replace(' ', '').replace('.', '')))
s1 = s.lower().replace(' ', '').replace('.', '')
print({c: s1.count(c) for c in 'abcdefghijklmnopqrstuvwxyz' if s1.count(c) > 1})

# 字符串插值
print('Hello, Mr {}.'.format("Anderson"))

# Unicode
print(len('你好吗？我很好……'))
print(len('お元気ですか。私は元気です。'))
