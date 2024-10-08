# -*- coding: utf-8 -*-
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibon = [0, 1]  # 初始化前两个数
    for _ in range(2, n):
        new = fibon[-1] + fibon[-2]
        fibon.append(new)
    
    return fibon


num = int(input("请输入要生成的斐波那契数列的长度："))
sequence = fibonacci(num)
print(f"斐波那契数列的前 {num} 个数为：{sequence}")