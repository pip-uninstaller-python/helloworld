#EMS(Employee Manger System 员工管理系统)练习.py
print("{0:=^30}".format('欢迎使用员工管理系统'))
#员工信息'字符串形式统一保存'
employee = ['\t\t孙某某\t21\t\t男\t\tC市','\t\t朱某某\t22\t\t男\t\tA市']
while(1):
    print('请选择要做的操作：')
    print('        1、查询员工')
    print('        2、添加员工')
    print('        3、删除员工')
    print('        4、退出系统')
    option = input('请选择(1-4):')
    print('='*38)
    #查询员工
    if option == '1':
        #打印表头
        print('序号\t姓名\t年龄\t性别\t住址\t')
        #显示员工信息
        n = 1
        for i in employee:
            print('{}{}'.format(n,i))
            n += 1
            continue
    #添加员工
    elif option == '2':
        #获取要添加员工的信息：
        emp_name = input("请输入姓名：")
        emp_year = input("请输入年龄：")
        emp_gender= input("请输入性别：")
        emp_address = input("请输入住址：")
        print("姓名：{}\t年龄：{}\t性别：{}\t住址：{}".format(emp_name,emp_year,emp_gender,emp_address))
        print('=' * 38)
        emp_ensure = input('请确认员工信息是否正确(Y/N):')
        if emp_ensure == 'Y':
            print('=' * 38)
            print("数据已被添加至数据库中！")
            employee.append('\t\t{}\t{}\t\t{}\t\t{}'.format(emp_name, emp_year, emp_gender, emp_address))
        else:
            print('=' * 38)
            print('已取消，请重新录入')
            continue
    #删除员工
    elif option == '3':
        print("请确认您要删除的员工信息")
        print('=' * 38)
        del_name = int(input("请输入您要删除的员工序号(1-999): "))
        employee.pop(del_name-1)
    #退出系统
    elif option == '4':
        input('感谢您的使用，按任意键退出程序！')
        break
    #输入错误
    else:
        print('您的输入有误，请重新选择！')
        continue
    print('='*38)
