# -*- coding: utf-8 -*-
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

input_nums = input("请输入一个数组,用逗号分隔:")
str_nums = input_nums.split(",")
float_nums = [float(num) for num in str_nums]

print(f"数组 {float_nums} 经选择排序后为:{selection_sort(float_nums)}")
