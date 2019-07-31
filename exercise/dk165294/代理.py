from urllib import request

handler = request.ProxyHandler({"http":"182.92.113.148:8118"})

opener = request.build_opener(handler)

req= request.Request('http://httpbin.org/ip')

resp = opener.open(req)

print(resp.read())

#成功但免费代理极其不稳定