import json
# 引入json解析库,用于把json数据转换为字典，json数组转换为列表，json字符串转换为python字符串

jsonstring = '{"user-man":[{"name":"peter"},{"name":"xiaoming"}],' \
             '"user-woman":[{"name":"Anni"},{"name":"zhangsan"}]}'
json_data = json.loads(jsonstring)

# 第二种方式
print(json_data["user-man"])
print(json_data["user-woman"])
print(json_data["user-man"][0]["name"])
print(json_data["user-woman"][1]["name"])

print('\n')

# 第一种方式
print(json_data.get("user-man"))
print(json_data.get("user-woman"))
print(json_data.get("user-man")[0].get("name"))
print(json_data.get("user-woman")[1].get("name"))

