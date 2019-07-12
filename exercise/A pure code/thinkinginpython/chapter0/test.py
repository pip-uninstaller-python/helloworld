import math
import dbm
import pickle


# 费马大定理   a n + b n = c n
def check_fermat():
    a = int(input('input a:'))
    b = int(input('input b:'))
    c = int(input('input c:'))
    n = int(input('input n:'))
    if n > 2 and math.pow(a, n) + math.pow(b, n) == math.pow(c, n):
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No,that doesn’t work.')


# check_fermat()

def is_triangle():
    a = int(input('trangle a:'))
    b = int(input('trangle b:'))
    c = int(input('trangle c:'))
    if a + b >= c or a + c >= b or b + c >= a:
        print('YES')
    else:
        print('NO')


# is_triangle()

# 圆面积计算
def distance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    d = dx ** 2 + dy ** 2
    return math.sqrt(d)


def area(r):
    return 2 * math.pi * r


def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))


# print(circle_area(0, 0, 1, 1))

def is_between(x, y, z):
    return x <= y <= z


# print(is_between(3, 2, 3))

# n!
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# print(factorial(3))

def Ackermann(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return Ackermann(m - 1, 1)
    if m > 0 and n > 0:
        return Ackermann(m - 1, Ackermann(m, n - 1))


# print(Ackermann(3, 4))

# 回文词
def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(c):
    if len(middle(c)) == 1:
        if first(c) == last(c):
            return True
        else:
            return False
    else:
        if first(c) == last(c):
            return is_palindrome(middle(c))
        else:
            return False


# print(is_palindrome('aca'))
'''
while True:
    line = input('>')
    if line == 'done':
        break
    print(line)
print('Done!')
'''


# 求a平方根
def mysqrt(x, a):
    epsilon = 0.001
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return y


# print(mysqrt(3, 2))


def test_squre_root():
    for a in range(9):
        print(a, mysqrt(3, a), math.sqrt(a), mysqrt(3, a) - math.sqrt(a))


# test_squre_root()

def eval_loop():
    i_data = []
    while True:
        i_user = input('>>')
        if i_user == 'done':
            print(i_data[-1])
            break
        else:
            i_data.append(eval(i_user))


# eval_loop()

# 1/π
def estimate_pi():
    total = 0
    k = 0
    factor = 2 * mysqrt(3, 2) / 9801
    while True:
        t = (factorial(4 * k) * (1103 + 26390 * k)) / (factorial(k) ** 4 * 396 ** (4 * k))
        k += 1
        total += t
        if abs(t) < 1e-15:
            break
    return 1 / (factor * total)


# print(estimate_pi())

# str.count()
# print('banana'.count('a'))

# 凯撒密码 (Caesar cypher)
def rotate_word(s, n):
    n_s = ''
    for c in s:
        n_s = n_s + chr(ord(c) + n)
    print(s, n_s)


# rotate_word('abcdef', -6)

# 返回元组
def min_max(t):
    return min(t), max(t)


m, n = min_max((1, 2, 3))


# print(m, n)


def try_it(*args, **kw):
    print('args:', args)
    print('kw:', kw)


'''
t = (1, 2, 3, 4)
d = {"a": "1", "b": "2", "c": "3"}
print(type(d))
try_it(t, d)
try_it('a', 1, None, a=1, b='2', c=3)
'''

# 文件  写入 读取
# 1 open
f_write = open("txt.txt", 'w')
f_write.write('hello world')
# print("every one",f_write,file=f_write)
f_write.close()

f_read = open("txt.txt", 'r')
print(f_read.readline())
f_read.close()

# 2 pickle
t = [1, 2, 3]
s = pickle.dumps(t)
print(pickle.loads(s))

# 3 dbm
db = dbm.open('num_1', 'c')
db['num_1'] = 'hello world'
print(db['num_1'])


if __name__=='__main__':
    print('test')