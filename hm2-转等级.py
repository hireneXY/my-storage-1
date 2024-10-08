# -*- coding: utf-8 -*-
def to_grade(score):
    if score >= 90:
        return '优秀'
    elif score >= 75 and score < 90:
        return '良好'
    elif score >= 60 and score < 75:
        return '合格'
    else:
        return '不合格'
    
your_score = int(input('请输入你的成绩：'))
print('成绩等级是：%s' % to_grade(your_score))