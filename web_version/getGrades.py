# -*- coding:UTF-8 -*-
# 用于表格的OCR识别

# 这个库需要导入
# pip install baidu-aip
from aip import AipOcr
import re
import os
import json
import sys

APP_ID = '16051361'
API_KEY = 'IK2PyA6XiMlBHmRuOrzRb71j'
SECRET_KEY = '9s9pEuhOpKH8m9ZNA9uTGMsXa3WFjU8E'

credit = {'数字图像处理':2,
        '移动终端开发技术':3,
        '无线射频识别技术与应用':4,
        '嵌入式系统实训':2,
        '嵌入式系统及应用':4,
        'Web应用开发':3,
        '毛泽东思想和中国特色社会主义理论体系概论':3,
        '软件工程':3,
        '专业英语':2,
        '信息安全技术':3,
        'Web应用开发实训':2,
        '无线传感器网络技术':4,
        'ZigBee通信协议与应用':4}
# 用于补偿科目信息的不全
true_subjects = ['毛泽东思想和中国特色社会主义理论体系概论']

# 创建客户端连接
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

""" 获取成绩信息 """
def get_grade_info(wordsResult):
    grades = {}
    for i in range(len(wordsResult)):
        # 获取wordsResult里面的"综合成绩:100"的结果
        words = wordsResult[i]['words']
        # 匹配成绩
        matchObj = re.match(r'(.*)综合成绩:(.*)',words)
        # 如果words里面存在"综合成绩:100"的情况
        if(matchObj):
            grade = matchObj.group(2)
            # 这里可能存在一种情况是综合成绩前面有科目的情况
            if(matchObj.group(1)!=''):
                false_subject = matchObj.group(1)
                subject = complete_subject(false_subject)
            else:
                subject = wordsResult[i-1]['words']
            if(credit.__contains__(subject)):
                    grades[subject] = grade            
    return grades

""" 获取基础分 """
def get_basic_point(grades):
    grade_credit_sum = 0
    credit_sum = 0
    for subject in grades:
        if(credit.__contains__(subject)):
            grade_credit_sum += int(grades[subject])*credit[subject]
            credit_sum += credit[subject]
    base_point = grade_credit_sum / credit_sum * 0.8
    return base_point

""" 补偿科目 """
def complete_subject(subject):
    for true_subject in true_subjects:
        if(re.match(subject,true_subject)):
            return true_subject
    return subject

def get_grades(image):
    # 获取图片
    image = get_file_content(image)
    # 通用文字识别
    wordsResult = client.basicGeneral(image)['words_result']
    # 获取成绩字典
    grades = get_grade_info(wordsResult)
    return grades
    # 获取基础分
    # base_point = get_basic_point(grades)
