import csv

# csv文件的读取，把csv文件这种的每行数据转化为一个列表
fp = open('F:/douban.csv', encoding='utf-8')
reader = csv.reader(fp)
for row in reader:
    print(row)
fp.close()

# 转化为字典
fp2 = open('F:/douban.csv', encoding='utf-8')
reader2 = csv.DictReader(fp2)
for row in reader2:
    print(row)
fp2.close()

