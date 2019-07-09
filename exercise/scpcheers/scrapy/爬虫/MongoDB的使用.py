import pymongo

'''
 mongodb是一种非关系型数据库（NoSQL）
 传统的关系型数据库在应付Web2.0网站，
 特别是大规模和高并发的SNS类型的Web2.0纯动态网站已经显得力不从心，暴露很多难以克服的问题
 NoSQL由其本身的特点得到了非常迅速的发展
 NoSQL的产生主要是为了解决大规模数据集合多重数据种类带来的挑战，尤其是大数据应用难题
 分为四大类：键值存储数据库（eg.Redis）
            列存储数据库（eg.Hbase）
            文档型数据库（eg.MongoDB）
            图形数据库（eg.Graph）
'''

client = pymongo.MongoClient('localhost', 27017)  # 连接数据库
mydb = client['mydb']  # 新建mysb数据库
test = mydb['test']  # 新建test数据集合/表
# mongoDB数据库只有插入数据才会建库建表
test.insert_one({'name': 'Jan', 'sex': '男', 'grade': '98'})  # 插入数据
# mongoexport -d mydb -c test --csv -f name,sex,grade -o test.csv
# 上面语句用于导出数据为csv格式
'''
-d : 数据库
-c : 表数据
-f : 要导出的字段
生成的csv文件在bin目录下
'''

