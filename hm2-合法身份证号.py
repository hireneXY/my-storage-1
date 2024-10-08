# -*- coding: utf-8 -*-
import re

def validate_id_card(number):
    # 定义正则表达式
    pattern = r'^[1-9]\d{5}(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[1-2]\d|3[0-1])\d{3}(\d|X)$'
    
    # 匹配身份证号
    if re.match(pattern, number):
        return True
    else:
        return False

id_number = str(input("请输入身份证号："))

if validate_id_card(id_number):
    print("身份证号合法")
else: 
    print("身份证号不合法")
