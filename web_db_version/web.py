# -*- coding:UTF-8 -*-
from flask import render_template,Flask,request
from getGrades import get_grades
import os
import json
import random
import pymysql
from dao import DAO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    dao = DAO()
    credits = dao.getCredits()
    print(credits)
    return render_template('index.html',credits=credits)

@app.route('/getgrades', methods=['POST'])
def getGrades():
    if 'file' in request.files:
        file = request.files['file']
        fileName = str(random.randint(1000,9999))+file.filename
        file.save(fileName)
        grades = get_grades(fileName)
        os.remove(fileName)
        return json.dumps(grades,ensure_ascii=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)