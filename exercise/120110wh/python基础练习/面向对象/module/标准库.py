# Py标准库  开箱即用
# 为了实现开箱即用的思想，Python中为我们提供一个模块的标准库
# 再这个标准库中，有很多很强大的模块，我们可以直接使用
#   并且标准库会随python的安装一同安装
# sys模块，它里面提供了一些变量和函数，是我们可以获取到python解析器的信息
#   或者通过函数来操作python解析器
import sys
import pprint
print(sys.argv)
# pprint.pprint(sys.modules)
# pprint.pprint(sys.path)
print(sys.platform)
#sys.exit() 退出

# os 模块，让我们可以对操作系统进行访问
import os
print(os)
#os.environ
# 通过这个属性可以获取到系统的环境变量（path）
pprint.pprint(os.environ['path'])
# os.system()
# 可以用来执行操作系统的名字
os.system('dir')