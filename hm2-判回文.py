# -*- coding: utf-8 -*-
def if_palindrome(s):
    if s < 0 or (s % 10 == 0 and s != 0): 
        return False
    origin_s = s
    new = 0
    while s != 0 :
        new = new * 10 + s % 10 
        s //= 10 
    if origin_s == new: 
        return True
    else: 
        return False
    
num = int(input("请输入一个整数: "))
if if_palindrome(num): 
    print(num, "是回文数") 
else: 
    print(num, "不是回文数")
    