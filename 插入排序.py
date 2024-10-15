# -*- coding: utf-8 -*-
def insertion_sort(arr):
    # 遍历整个数组
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # 将当前元素插入到已排序的部分
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

input_nums = input("请输入一个数组,用逗号分隔:")
str_nums = input_nums.split(",")
float_nums = [float(num) for num in str_nums]

print(f"数组 {float_nums} 经插入排序后为:{insertion_sort(float_nums)}")