# ---------------------------------------------------------------------
# 布尔（逻辑）运算

print(not True)
print(not False)

# and 运算适用「短路」原则，从左到右进行计算，只要有 False，直接返回 False
# 后面的计算都不再进行
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# or 运算适用「短路」原则，从左到右进行计算，只要有 True，直接返回 True
# 后面的计算都不再进行
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# 「异或」运算并不是 True xor False，而稍有不同
cond1 = True
cond2 = False
# 要么是这样
print(cond1 and not cond2 or cond2 and not cond1)
# 要么（在确保 cond1 和 cond2 为 bool 类型的情况下）这样
print(cond1 ^ cond1)
# 或者这样
print(bool(cond1) ^ bool(cond2))
# 再不然就这样
from operator import xor
print(xor(cond1, cond2))