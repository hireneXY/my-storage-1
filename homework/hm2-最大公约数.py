# -*- coding: utf-8 -*-
def max_commom_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))
print("最大公约数是：", max_commom_divisor(num1, num2))
