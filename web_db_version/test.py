# import pymysql

# db = pymysql.connect("localhost","root","123456","zongce")

# cursor = db.cursor()

# sql = "SELECT * FROM tb_credit where enable_status=1"

# for row in results:
#     subject = row[1]
#     credit = row[2]
#     term = row[3]
#     enableStatus=row[4]

# """获取科目和对应的学分"""
# def getCredits(results):
#     credits = [{},{}]
#     for row in results:
#         subject = row[1]
#         credit = row[2]
#         term = row[3]
#         credits[term-1][subject] = str(credit)
#     return credits

# print(getCredits(results))

# db.close()
import re

str="(21323)"
str = re.sub(r'[()]','',str)
print(str)