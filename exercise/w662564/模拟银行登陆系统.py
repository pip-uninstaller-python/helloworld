#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 13:28
# @Author  : 錵滊嫣缘
# @File    : 模拟银行登陆系统.py
# @Software: PyCharm

#这个系统没有做添加账号的功能
# 定义一个列表用于存储账户
ATM = [
    {'id': '123', 'password': 'a123', 'money': 123.00},
    {'id': '456', 'password': 'a456', 'money': 456.00},
    {'id': '789', 'password': 'a789', 'money': 789.00}
]
m = 0 #定义一个全局变量 用于存储金额
n = False #定义一个全局变量用于验证账号登陆与否
def ATM_log(id, password):
    '''
    登录系统
    :return:
    '''
    #申明全局变量n m
    global  n,m
    #遍历整个字典进行账号密码匹配
    for i in ATM:
        if id == i['id']and password ==i['password']:
            #当账号密码匹配成功，把N赋值为True  m赋值当前账号的金额
            n = True
            m = i['money']
            break

def ATM_inquire():
    '''
    查询余额
    :return:
    '''
    #这个函数其实可以完全不要  这样整个系统会更简便
    global  m
    print('当前账号余额：￥{:0.2f}元'.format(m))

def ATM_draw(draw):
    '''
    取钱
    :return:
    '''
    #申明m是全局变量
    global m
    # 判断账号余额是否打印要取的金额，大于就减去要取的，否则提示用户账号余额不足
    if m>=draw:
        m -=draw
        print('你本次取钱:￥{:0.2f}元'.format(draw))
        print('当前账号余额:￥{:0.2f}元'.format(m))
    else:
        print('账户余额不足请存钱')
def ATM_save(save):
    '''
    存钱
    :return:
    '''

    global m
    # 直接用原本的金额加上要存储的金额
    m +=save
    print('你本次存钱:￥{:0.2f}元'.format(save))
    print('当前账号余额:￥{:0.2f}元'.format(m))
if __name__ == '__main__':
    # 设定一个无限循环 用于账号登陆
    while True:
        id = input('请输入账号：') #输入账号
        password = input('请输入密码:') #输入密码
        ATM_log(id, password) #将账号密码传入登陆函数中经行验证
        if  n== False: # 判断账号是否验证成功，不成功就从新输入
            print('你输入的帐号密码不匹配请从新输入')
        else:
            #登陆成功之后的界面显示
            print('{:^45}'.format('登陆成功欢迎使用'))
            print('='*10,'请按照以下数字输入您要进行的操做','='*10)
            print('{:3}{:<18}{:<15}'.format(' ', '1.查询余额','2取款'))
            print('{:3}{:<20}{:<17}'.format(' ', '3.存款', '4退出系统'))
            print('=' * 51)
            while True:
                #用一个死循环去验证客户需要的操作
                sum = input('请输入数字：')
                if sum == '1': #当客户输入1的时候查询账户余额
                    ATM_inquire()
                    input('按回车继续')
                    print('=' * 51)
                elif sum == '2': #当客户输入2的时候取钱
                    draw= eval(input('请输入您要取的金额：(不能包含字母)'))
                    ATM_draw(draw)
                    input('按回车继续')
                    print('=' * 51)
                elif sum == '3': #当客户输入3的时候存钱
                    save = eval(input('请输入您要存的金额：(不能包含字母)'))
                    ATM_save(save)
                    input('按回车继续')
                    print('=' * 51)
                elif sum == '4': #当客户输入4的时候退出系统
                    print('='*5,' 再见 ', '='*5)
                    break
                else:
                    print('你输入的数字不正确请从新输入')
                    continue
            break