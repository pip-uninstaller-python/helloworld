import xlwt  # 将数据写入Excel的库文件中

book = xlwt.Workbook(encoding='utf-8')  # 创建工作簿
sheet = book.add_sheet('sheet1')  # 创建工作表
sheet.write(0, 0, 'python')  # 在相应单元格写入数据
sheet.write(1, 1, 'love')
book.save('test.xls')  # 保存到文件中

