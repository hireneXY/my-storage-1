#homework/data文件夹下的stuGrade.csv文件中包含5位同学的学号、语文成绩、数学成绩和英语成绩，请先用记事本打开该文件，查看文件内容，
#然后编写Python程序，读取该文件，并计算出各科的平均成绩（保留2位小数）。
#8.请在第7题的代码继续编写Python程序，将以下内容写入my.txt文件中，一并上传到github中。
# -*- coding: utf-8 -*-
import csv

# 打开 CSV 文件
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

    ave_chinese = round(total_chinese / num_students, 2)
    ave_math = round(total_math / num_students, 2)
    ave_english = round(total_english / num_students, 2)
    print(f'平均语文成绩：{ave_chinese}')
    print(f'平均数学成绩：{ave_math}')
    print(f'平均英语成绩：{ave_english}')


with open('成绩结果.txt', mode='w', encoding='utf-8') as output_file:
    output_file.write(f"平均语文成绩: {ave_chinese}\n")
    output_file.write(f"平均数学成绩: {ave_math}\n")
    output_file.write(f"平均英语成绩: {ave_english}\n")
    