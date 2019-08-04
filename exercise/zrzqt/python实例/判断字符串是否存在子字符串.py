#给定一个字符串，然后判断指定的字符串是否存在于该字符串中。
def check(string,sub_str):
    if (string.find(sub_str) == -1):
        print('不存在！')
    else:
        print('存在！')
string = 'abczrzqtabc'
sub_str = 'zrzqt'
check(string,sub_str)
