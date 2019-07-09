import pymysql

'''
    关系数据库时间里在关系模型基础上的数据库
    借助于集合代数等数学概念和方法来处理数据
    实体与实体之间的各种联系军用关系模型表示
    数据属性与其他数据是有关联的（外键...）
'''

# 连接数据库 先定义连接对象 password = 123456
conn = pymysql.connect(host='localhost', user='root', passwd='123456',
                       db='mydb', port=3306, charset='utf8')
cursor = conn.cursor()  # 光标对象
cursor.execute("insert into students (name,sex,grade) values(%s,%s,%s)",
               ('张三', '女', 87))  # 插入数据
conn.commit()

