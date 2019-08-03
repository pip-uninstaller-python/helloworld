#10! = 10 * 9!
#9! = 9 * 7!  ……
#阶乘
def factorial (n):
 if n == 1:
  return 1
 else:
  return n*factorial(n-1)
print(factorial(5))
#幂函数
def power(n,i):
    if i == 0:
        return 1
    else:
        return n * power(n,i-1)
print(power(2,4))
#回文字符串
def P_string(n):
    if len(n) < 2:
        return True
    elif n[0] != n[-1]:
        return False
    else:
        return P_string(n[1:-1])
    #else:
        return n[0] == n[-1] and P_string(n[0:-1])
print(P_string('abcee'))