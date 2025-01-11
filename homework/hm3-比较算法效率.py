# -*- coding: utf-8 -*-
import random
import time

def generate_random_array(size, lower=1, upper=1000000):
    return [random.randint(lower, upper) for _ in range(size)]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

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
    
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

    
sizes = [100, 1000, 10000]
arrays = []
for size in sizes:
    arrays.append(generate_random_array(size))
time_1 = []
time_2 = []
time_3 = []
time_4 = []
for i, arr in enumerate(arrays):
    begin = time.time()
    sorted_1 = insertion_sort(arr)
    end = time.time()
    time_1.append(end - begin)
    begin = 0
    end = 0
    begin = time.time()
    sorted_2 = selection_sort(arr)
    end = time.time()
    time_2.append(end - begin)
    begin = 0
    end = 0
    begin = time.time()
    sorted_3 = quick_sort(arr)
    end = time.time()
    time_3.append(end - begin)
    begin = 0
    end = 0
    begin = time.time()
    sorted_4 = merge_sort(arr)
    end = time.time()
    time_4.append(end - begin)
    begin = 0
    end = 0

print("时间/s:(100,1000,10000)")
print("插入排序：", time_1)
print("选择排序：", time_2)
print("快速排序：", time_3)
print("归并排序：", time_4)
