# ---------------------------------------------------------------------
# 列表 list

li = [2, 4]
print('Repeating {} {} times: {}'.format(li, 3, li * 3))  # 重复三次

li.append(1)  # 添加元素
li.append(3)
li.extend([10, 20])  # 扩展列表
print('The list: {}'.format(li))
print('List {} contains {} elements'.format(li, len(li)))
print()

# 列表的索引 indexing
print('The first element is indexed by 0: {}'.format(li[0]))
print('The second element is indexed by 1: {}'.format(li[1]))
print('The last element is indexed by -1: {}'.format(li[-1]))
print('The second to last element is indexed by -2: {}'.format(li[-2]))
print()

del li[-1]  # 删除最后一个元素


# 查找 find the index
m = 3
if m in li:
    print('The index of {} is {}'.format(m, li.index(m)))
else:
    print('{} is not in {}.'.format(m, li.index(m)))
print()


# 切片 slicing
print('The first half: {}'.format(li[:len(li) // 2]))
print('The second half: {}'.format(li[len(li) // 2:]))
print('All even indices: {}'.format(li[::2]))
print('All odd indices: {}'.format(li[1::2]))
print('Reverse order: {}'.format(li[::-1]))
print()


# 排序 sort
print('A sorted copy of list {} is {}'.format(li, sorted(li)))
print()


# ---------------------------------------------------------------------
# 复制 copy
li1 = li
li2 = li.copy()
li3 = li[::]
li[0] = -100
li2[1] = -100
print('The original list: {}'.format(li))
print('The one assigned by reference: {}'.format(li1))
print('The one assigned by calling `copy` member: {}'.format(li2))
print('The one assigned by indexing all: {}'.format(li3))
print()


# ---------------------------------------------------------------------
# 列表推导 list comprehension
r = range(20)  # r 是一个 range 对象
print([x + 1 for x in r])  # 遍历 r，各个元素 +1，生成一个新列表
print([x ** 2 for x in r if x % 2 == 1])  # r 中所有奇数的平方
