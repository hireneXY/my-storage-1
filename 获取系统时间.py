#使用python代码获取当前系统时间
# -*- coding: utf-8 -*-
import time

current_time = time.time()
print(f"当前时间的时间戳: {current_time}")

local_time = time.localtime(current_time)
print(f"当前时间的本地时间: {time.strftime('%Y-%m-%d %H:%M:%S', local_time)}")

# 获取当前时间的 UTC 时间
utc_time = time.gmtime(current_time)
print(f"当前时间的国际时间: {time.strftime('%Y-%m-%d %H:%M:%S', utc_time)}")