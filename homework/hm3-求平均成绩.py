# -*- coding: utf-8 -*-
import csv
import datetime
import time

with open('stuGrade.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    total_chinese = 0
    total_math = 0
    total_english = 0
    num_students = 0
    for row in csv_reader:
        chinese = int(row['chinese'])
        total_chinese += chinese
        math = int(row['math'])
        total_math += math
        english = int(row['english'])
        total_english += english
        num_students += 1
    
    ave_chinese = float(total_chinese / num_students)
    ave_math = float(total_math / num_students)
    ave_english = float(total_english / num_students)
    print(f'平均语文成绩：{ave_chinese:.2f}')
    print(f'平均数学成绩：{ave_math:.2f}')
    print(f'平均英语成绩：{ave_english:.2f}')



with open('成绩结果.txt', mode='w', encoding='utf-8') as output_file:
    output_file.write("学号:10235501409,姓名:孔祥玉\n")
    output_file.write(f"平均语文成绩: {ave_chinese:.2f},平均数学成绩: {ave_math:.2f},平均英语成绩: {ave_english:.2f}\n")
    # 输出当前时间
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    # 暂停两秒
    time.sleep(2)
    
    # 获取两秒后的当前时间
    two_seconds_later = datetime.datetime.now()
    formatted_two_seconds_later = two_seconds_later.strftime("%Y-%m-%d %H:%M:%S")

    output_file.write(f"Current time: {formatted_time}\n")
    output_file.write(f"Two seconds later: {formatted_two_seconds_later}")
    
