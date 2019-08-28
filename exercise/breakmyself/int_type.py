# -*- coding: utf-8 -*-
# 开发团队   ：pip uninstall python
# 开发人员   ：breakmyself
# 开发时间   ：2019/8/14  11:22 
# 文件名称   ：int_type.PY
# 开发工具   ：PyCharm
#github主页：https://github.com/breakmyself
"""
python整数类型有四种
十进制：正常的计数方式
二进制：0b或者0B开头的
八进制：0o或者0O开头
十六进制：0x或者0X开头

"""
#十六进制的类型
hex_value1 = 0x13
hex_value2 = 0XaF
print("hexValue1的值为:"'',hex_value1)
print("hexValue2的值为: "'',hex_value2)
#二进制类型的整数
bin_val = 0b111
bin_va2 = 0B101
print("binVa1的值为: "'',bin_val)
print("binVa2的值为: "'',bin_va2)
#八进制的整数类型


otc_va1 = 0o54
print("otcVa1的值为: " '',otc_va1)
otc_va2 = 0O17
print("otcVa2的值为: "'',otc_va2)
#浮点型
one_million = 1_000_000
print(one_million)
price = 234_234_234
android = 1234_1234
print(price,android)