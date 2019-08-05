#给定一个字符串，从头部或尾部截取指定数量的字符串，然后将其翻转拼接。
def rotate(input,d):
    Lfirst = input[0 : d]
    Lsecond = input[d :]
    Rfirst = input[0 : len(input)-d]
    Rsecond = input[len(input)-d : ]
    print('头部切片翻转：',(Lsecond + Lfirst))
    print('尾部切片翻转：',(Rsecond + Rfirst))
if __name__=='__main__':
    input = 'zrzqt'
    d = 2#截取2个字符
    rotate(input,d)
'''
利用索引进行切片操作时，可包含三个参数:
如对列表来说即：list[start_index: stop_index: step]。
 起始位置 : start_index (空时默认为 0)。
 终点位置: stop_index (空时默认为列表长度) 需要注意起点与终点索引的位置关系。
 步长: step (空时默认为 1，不能为 0)。
例如用于整个字符翻转：
def rotate(input):
    print("字符翻转前: " + input)
    input = input[:: -1]
    print("字符翻转后: " + input)
if __name__ == "__main__":
    input = 'zrzqt'
    rotate(input)
'''
