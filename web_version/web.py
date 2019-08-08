# -*- coding:UTF-8 -*-
from flask import render_template,Flask,request
from getGrades import get_grades
import os
import json
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # 根路由返回static下的index.html目录
    return app.send_static_file('index.html')

# 通过getgrades方法实现图片的上传和结果的返回
@app.route('/getgrades', methods=['POST'])
def getGrades():
    if 'file' in request.files:
        # 获取图片
        file = request.files['file']
        # 设置图片名
        fileName = str(random.randint(1000,9999))+file.filename
        # 保存图片
        file.save(fileName)
        # 识别成绩和科目
        grades = get_grades(fileName)
        # 删除图片
        os.remove(fileName)
        # 返回json数据
        return json.dumps(grades,ensure_ascii=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)