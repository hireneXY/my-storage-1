# -*- coding: utf-8 -*-
def decimal_to_binary(num, precision):

    # 分离整数和小数部分
    inte_part = int(num)
    frac_part = num - inte_part

    # 转换整数部分为二进制
    binary_inte = bin(inte_part)[2:]  # 去前缀 '0b'

    # 转换小数部分为二进制
    binary_frac = ''

    for _ in range(precision):
        frac_part *= 2
        if frac_part >= 1:
            binary_frac += '1'
            frac_part -= 1
        else:
            binary_frac += '0'
        
        if frac_part == 0:
            break

    # 组合整数部分和小数部分
    binary_num = f"{binary_inte}.{binary_frac}"
    return binary_num

# 测试函数
decimal_num = float(input("请输入一个十进制数："))
precision = 10
binary_num = decimal_to_binary(decimal_num, precision)
print(f"十进制数 {decimal_num} 转换为二进制数为：{binary_num}")