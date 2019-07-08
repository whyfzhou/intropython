# ---------------------------------------------------------------------
# 字典

di = {'a': 'alpha', 'b': 'beta', 'c': 'gamma', 'd': 4}

# 字典的索引用 key 值
print(di['a'])

if 'd' in di:
    print('d is in the dictionary.')

# 我们想知道 di 的 'e' 是什么，但不确定 di 中有 'e' 这个 key
if 'e' in di:
    print('e is in the dictionary, its data is {}'.format(di['e']))
    a = di['e']
else:
    print('e is not in the dictionary, use the default value 0.')
    a = 0
print('a is: {}'.format(a))
# 以上也可以简单写成
a = di.get('e', 0)

# 字典推导
print({d: k for k, d in di.items()})
# 等效于
print({di[k]: k for k in di})

# key 值必须是不可变的（hashable 的）数据类型（结构），如数字，字符串，元组
# 比如我们给 di 添加一组 key: data
di[(1, 2, 'c')] = 'whatever'
# 但是下面这行试图使用 list 做 key，会抛出 TypeError 异常
di[[1, 2, 'c']] = '...'  # 注释掉以后可以继续运行


# ---------------------------------------------------------------------
# 集合

s1 = {'a', 'fate', 1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 'california', 'a'}

print(s1 & s2)  # 交集 s1 ∩ s2
print(s1 | s2)  # 并集 s1 ∪ s2
print(s1 ^ s2)  # 差集（并集中除去交集以外的部分）
print('elf' in s1)  # 元素从属关系测试 'elf' ∈ s1
print('a' not in s1)  # 'a' ∉ s1
print((s1 & s2) <= s1)  # 集合包含关系测试 (s1 ∩ s2) ⊆ s1
print((s1 | s2) > s2)  # 方向随意，没等号表示真包含 (s1 ∪ s2) ⊃ s2

