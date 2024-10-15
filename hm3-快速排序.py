# -*- coding: utf-8 -*-
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        arr = quick_sort(left) + middle + quick_sort(right)
        return arr

input_nums = input("请输入一个数组,用逗号分隔:")
str_nums = input_nums.split(",")
float_nums = [float(num) for num in str_nums]

print(f"数组 {float_nums} 经快速排序后为:{quick_sort(float_nums)}")
