import traceback
import logging

# 反向跟踪信息写入一个日志文件
try:
    raise Exception('This is the error message')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The trace info was written to errorInfo.txt')
'''
# 断言针对的是程序员的错误，而不是用户的错误。
assertInfo = 'open'
assert assertInfo == 'open', 'fail'
assertInfo = 'close'
assert assertInfo == 'open', 'fail'
'''

# 日志 显示该级别和更高的级别
# logging.disable(logging.DEBUG) 禁止该级别和更低级别的所有日志消息
logging.basicConfig(filename='loggintInfo.txt', level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s=- %(message)s')
logging.debug('Start of program')


def factorial(n):
    logging.info('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.warning('i is ' + str(i) + ', total is ' + str(total))
    logging.error('End of factorial(%s)' % (n))
    return total


print(factorial(5))
logging.critical('End of program')
