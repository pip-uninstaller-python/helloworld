import numpy as np
import matplotlib.pyplot as plt


def main():
    # line
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    c, s = np.cos(x), np.sin(x)
    plt.figure(1)
    plt.plot(x, c, color="blue", linewidth=1.0, linestyle="-", label="COS", alpha=0.5)  # 自变量， 因变量
    plt.plot(x, s, "r.", label="SIN")  # 正弦  "-"/"r-"/"r."
    plt.title("COS & SIN")
    ax = plt.gca()
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data", 0))  # 横轴位置
    ax.spines["bottom"].set_position(("data", 0))  # 纵轴位置
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    plt.xticks([-np.pi, -np.pi / 2.0, np.pi / 2, np.pi],
               [r'$-\pi/2$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$-\pi$'])
    plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor="white", edgecolor="None", alpha=0.2))
    plt.legend(loc="upper left")  # 左上角的显示图标
    plt.grid()  # 网格线
    # plt.axis([-1, 1, -0.5, 1])  # 显示范围
    plt.fill_between(x, np.abs(x) < 0.5, c, c < 0.5, color="green", alpha=0.25)
    t = 1
    plt.plot([t, t], [0, np.cos(t)], "y", linewidth=3, linestyle="--")
    # 注释
    plt.annotate("cos(1)", xy=(t, np.cos(1)), xycoords="data", xytext=(+10, +30),
                 textcoords="offset points", arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))
    plt.show()


# Scatter --> 散点图
def scatter():
    fig = plt.figure()  # 建立一个表格
    fig.add_subplot(3, 3, 1)
    n = 128
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(Y, X)  # 上色
    plt.axes([0.025, 0.025, 0.95, 0.95])  # 显示范围
    plt.scatter(X, Y, s=75, c=T, alpha=.5)  # s点的大小， c颜色， alpha透明度
    plt.xlim(-1.5, 1.5), plt.xticks([])  # x范围
    plt.ylim(-1.5, 1.5), plt.yticks([])  # x范围
    plt.axis()
    plt.title("scatter")
    plt.xlabel("x")
    plt.ylabel("y")
    # plt.show()

    # other
    fig = plt.figure()  # 建立一个表格
    ax = fig.add_subplot(3, 3, 1)
    n = 128
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(Y, X)  # 上色
    # plt.axes([0.025, 0.025, 0.95, 0.95])  # 显示范围
    ax.scatter(X, Y, s=75, c=T, alpha=.5)  # s点的大小， c颜色， alpha透明度
    plt.xlim(-1.5, 1.5), plt.xticks([])  # x范围
    plt.ylim(-1.5, 1.5), plt.yticks([])  # x范围
    plt.axis()
    plt.title("scatter")
    plt.xlabel("x")
    plt.ylabel("y")
    # plt.show()

    # 散点图
    # fig = plt.figure()  # 建立一个表格
    fig.add_subplot(332)  # n>10不可用这个数值
    n = 10  # 10个点
    X = np.arange(n)  # 构建一个数列 0-9
    # 营造出来一种有变化的效果
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)  # *随机数， 随机数范围在0.5-1.0之间
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    # 然后画出来
    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
    for x, y in zip(X, Y1):  # 添加注释 位置， 格式， ha水平位置， va垂直位置
        plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
    for x, y in zip(X, Y1):
        plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')
    plt.show()


# 柱状图
def bar():
    fig = plt.figure()  # 建立一个表格
    fig.add_subplot(332)  # n>10不可用这个数值
    n = 10  # 10个点
    X = np.arange(n)  # 构建一个数列 0-9
    # 营造出来一种有变化的效果
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)  # *随机数， 随机数范围在0.5-1.0之间
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    # 然后画出来
    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
    for x, y in zip(X, Y1):  # 添加注释 位置， 格式， ha水平位置， va垂直位置
        plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
    for x, y in zip(X, Y1):
        plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')
    plt.show()


if __name__ == '__main__':
    # main()
    scatter()
    # bar()
