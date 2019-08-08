# -*- coding:UTF-8 -*-
# 用于表格的OCR识别

# 这个库需要导入
# pip install baidu-aip
from aip import AipOcr
import re
import os
import json
import sys
from dao import DAO

APP_ID = '16051361'
API_KEY = 'IK2PyA6XiMlBHmRuOrzRb71j'
SECRET_KEY = '9s9pEuhOpKH8m9ZNA9uTGMsXa3WFjU8E'

# 创建客户端连接
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

""" 获取成绩信息 """
def get_grade_info(wordsResult):
    dao = DAO()
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
                need_completed_subject = matchObj.group(1)
            else:
                need_completed_subject = wordsResult[i-1]['words']
            need_completed_subject = re.sub(r'[()]','',need_completed_subject)
            result = dao.completeSubject(need_completed_subject)
            if(result):
                subject = result['subject']
                grades[subject] = grade
    return grades

def get_grades(image):
    # 获取图片
    image = get_file_content(image)
    # 通用文字识别
    wordsResult = client.basicGeneral(image)['words_result']
    # 获取成绩字典
    grades = get_grade_info(wordsResult)
    return grades