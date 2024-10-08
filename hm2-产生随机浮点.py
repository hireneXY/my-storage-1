# -*- coding: utf-8 -*-
import random

num_samples = 5
random_floats = [random.uniform(10, 20) for _ in range(num_samples)]

# 输出结果
for i, num in enumerate(random_floats):
    print(f"第 {i + 1} 个随机浮点数为：{num}")