# -*- coding:UTF-8 -*-
from flask import render_template
from flask import Flask
from flask import request
from getGrades import get_grades
import os
import json
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return app.send_static_file('index.html')

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