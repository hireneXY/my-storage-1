# -*- coding: utf-8 -*-
def find_second_largest(s):

    new_s = list(set(s))#去重
    
    new_s.sort()
    
    if len(new_s) < 2:
        return -1
    else:
        return new_s[-2]


input_nums = input("请输入一个整数数组,用逗号分隔:")
str_nums = input_nums.split(",")
int_nums = [int(num) for num in str_nums]

print(f"数组 {int_nums} 的第二大数为：{find_second_largest(int_nums)}")