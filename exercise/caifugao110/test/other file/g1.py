# from gao import Student
# student = Student()
# student.print_file()

import re
s = 'dianjimaodianjibingdianjijietou'

# def dianji(value):
#     matched = value.group()
#     if 'd'in matched:
#         return '~'
#     else:
#         return '!'
#
# r = re.sub('\w', dianji, s)
# print(r)

# import json
# json_str = '{"name":"gaojian","age":24}'
# student = json.loads(json_str)
# print(type(student))
# print(student)
# print(student['name'])
# print(student['age'])
#
# # 2019.07.02 P11.58


origin = 0


def go(step):
    global origin
    origin = step + origin
    return origin


print(go(2))
print(go(3))
print(go(8))

# 2019.07.03 P12.10
