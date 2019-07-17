import numpy as np


# numpy基本操作
def main():
    lst = [[1, 3, 5], [2, 4, 6]]
    print(type(lst))
    np_lst = np.array(lst)
    print(type(np_lst))
    # 可指定dtype --> datatype
    np_lst = np.array(lst, dtype=np.float)
    # numpy中的数据类型  ↓
    # bool,int,int8/16/32/64/128, uint8/16/32/128, float, float16/32/64, complex64/128
    print(np_lst.shape)  # 形状 --> (2,3)
    print(np_lst.ndim)  # 维度
    print(np_lst.dtype)  # 数据类
    print(np_lst.itemsize)  # 64位占8个字节， 所以itemsize就是8
    print(np_lst.size)  # 大小， 6个元素就返回6


# 生成各种随机array
def array_test():
    # some Arrays
    print(np.zeros([2, 4]))
    print(np.ones([3, 5]))
    print("Rand: ")
    print(np.random.rand(2, 4))
    print(np.random.rand())
    print("RandInt: ")
    print(np.random.randint(1, 10, 3))
    print("Randn:")
    print(np.random.randn(2, 4))
    print("Choice:")
    print(np.random.choice([10, 20, 30, 2, 8]))
    print("Distribute:")
    print(np.random.beta(1, 10, 100))


# 操作
def array_oper():
    lst = np.arange(1, 11).reshape([2, -1])
    print(np.exp(lst))  # 似然指数
    print(np.exp2(lst))  # 似然指数的平方
    print(np.sqrt(lst))  # 开方
    print(np.sin(lst))  # 三角函数
    print(np.log(lst))  # 倍数

    lst = np.array([[[1, 2, 3, 4],
                     [4, 5, 6, 7]],
                    [[7, 8, 9, 10],
                     [10, 11, 12, 13]],
                    [[14, 15, 16, 17],
                     [18, 19, 20, 21]]
                    ])
    print(lst.sum(axis=2))  # 最大取值与数组维数有关，数组一共有几维，那么最大值就是最大维数-1
    # 计算规则: axis=0， 1+7+14=22, 2+8+15=25 ...  分成了最外围三个大块
    #          axis=1, 1+4=5, 2+5=7 ... 7+10=17...  分成了中间维度的6个中块
    #          axis=2, 1+2+3+4=10, 4+5+6+7=22 7+8+9+10=34 ... 分成了最小维度的单个数字
    print("Max:")
    print(lst.max(axis=1))
    print("Min:")
    print(lst.min(axis=0))

    lst1 = np.array([10, 20, 30, 40])
    lst2 = np.array([4, 3, 2, 1])
    print("Add:")
    print(lst1 + lst2)
    print("Sub:")
    print(lst1 - lst2)
    print("Mul:")
    print(lst1 * lst2)
    print("Div:")
    print(lst1 / lst2)
    print("Square:")  # 乘方
    print(lst1 ** 2)
    print("Dot:")  # 点乘
    print(np.dot(lst1.reshape([2, 2]), lst2.reshape([2, 2])))
    print("Cancatenate:")  # 拼接
    print(np.concatenate((lst1, lst2), axis=0))
    print(np.vstack((lst1, lst2)))  # 另一种写法
    print(np.hstack((lst1, lst2)))  # 另一种写法
    print(np.split(lst1, 4))  # 分隔成4份 or 2份 ...
    print(np.copy(lst1))  # 拷贝


from numpy.linalg import *  # 引入线性方程组操作所需包


# 线性方程组
def liner():
    print(np.eye(3))  # 单位矩阵
    lst = np.array([[1., 2.],
                    [3., 4.]])
    print("Inv:")  # 矩阵的幂
    print(inv(lst))
    print("T:")  # 转置矩阵
    print(lst.transpose())
    print("Det:")  # 行列式
    print(det(lst))
    print("Eig:")  # 特征值和特征向量
    print(eig(lst))  # 返回一个元组, 第一个是特征值, 第二个是特征向量
    y = np.array([[5.], [7.]])
    print("Solve:")
    print(solve(lst, y))


# numpy在其它方面的应用
def oters_oper():
    print("FFT:")  # 信号处理领域  --> 快速傅里叶变换，属于数字信号处理(DPS)里面的内容
    print(np.fft.fft(np.array([1, 1, 1, 1, 1, 1, 1, 1])))
    print("Coef:")  # 相关系数的运算  皮尔逊相关系数
    print(np.corrcoef([1, 0, 1], [0, 2, 1]))
    print("Poly:")  # 生成一元多次函数
    print(np.poly1d([2, 1, 3]))


if __name__ == '__main__':
    # main()
    # array_test()
    # array_oper()
    # liner()
    oters_oper()
