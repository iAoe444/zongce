import pymysql


class DAO:
    # 初始化
    def __init__(self):
        # 创建连接
        self.conn = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            db='zongce',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor  # 以字典的形式返回数据
        )
        # 获取游标
        self.cursor = self.conn.cursor()

    """获取科目和对应的学分"""

    def getCredits(self):
        credits = []
        sql = "SELECT subject,credit,term FROM tb_credit where enable_status=1"
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            credits.append(row)
        return credits

    """补偿科目信息"""

    def completeSubject(self, need_completed_subject):
        sql = "SELECT subject FROM tb_credit where subject like '%" + \
            need_completed_subject + "%'"
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    # 关闭连接
    def close(self):
        self.cursor.close()
        self.conn.close()
