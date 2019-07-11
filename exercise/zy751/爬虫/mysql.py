import pymysql
strcr="""CREATE TABLE EMPLOYEE (#建表语句
         FIRST_NAME  CHAR(20) ,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
strin='insert into  employee(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) values("zheng","yong",22,"N",0)'#插入语句
strde='delete from employee where first_name="zheng"'#删除语句
con=pymysql.Connect(host='localhost',port=3306,user='root',password='root',db='db')
cursor=con.cursor()
cursor.execute('select version()')#查看mysql版本
data=cursor.fetchone()#获取数据
print(data)
try:
    cursor.execute(strcr)#执行建表语句
except:
    print("已存在")
try:
    cursor.execute(strin)
    con.commit()#操作提交
except:
    con.rollback()
try:
    cursor.execute(strde)
    con.commit()
except:
    con.rollback()
con.close()#关闭数据库连接