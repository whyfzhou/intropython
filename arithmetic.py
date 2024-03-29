# ---------------------------------------------------------------------
# 基本算术运算

print('1 + 1 = {}'.format(1 + 1))
print('5 - 4 = {}'.format(5 - 4))
print('3 * 9 = {}'.format(3 * 9))
print('25 / 4 = {}'.format(25 / 4))  # 真除法
print('25 // 4 = {}'.format(25 // 4))  # 整数除法
print('25 % 4 = {}'.format(25 % 4))  # 求模
print('2**10 = {}'.format(2**10))  # 幂运算
print('(1+4) / 2**3 = {}'.format((1+4) / 2**3))  # 5 / 8 = 0.625


# ---------------------------------------------------------------------
# 与多数编程语言（如 C/C++ 不同），Python 3 的
# 整数类型不限大小（当然啦，还是受内存限制），
# 比如我们可以计算 100 的阶乘

def factor(n):
    if n < 0:
        return 0
    m = 1
    for i in range(1, n + 1):
        m *= i
    return m

print('100! = {}'.format(factor(100)))

# ---------------------------------------------------------------------
# 浮点数按照 IEEE-754 的双精度进行
# You tried to solve your problem using IEEE-754,
# now you have NaN problems.
