* 一般指令模式 : 可以移动光标,可以删除字符和删除整列,可以复制粘贴
* 编辑模式 : 按下“i, I, o, O, a, A, r, R”任意一个字母时进入;按下ESC退出编辑模式
* 命令行命令模式 : 在一般模式下,输入“ : / ? ”中任意一个按钮,就可以输入命令;

### 一般指令模式指令
#### 移动光标
指令|作用
|-|-|
hjkl            |等同于←↓↑→
n[方向键]     |光标向指定方向移动数字个字符|不能用小键盘
[Ctrl] + [f]    |屏幕“向下”移动一页，相当于 [Page Down]按键
[Ctrl] + [b]    |屏幕“向上”移动一页，相当于 [Page Up] 按键
[Ctrl] + [d]    |屏幕“向下”移动半页
[Ctrl] + [u]    |屏幕“向上”移动半页
n[空格]         |光标向后移动指定字符
n[Enter]        |光标向下移动指定字符
0或[Home]       |移动到本列最前面
$或[End]        |移动到本列最后面
G               |移动到文件最后一列
nG              |n为数字 移动到第几行
gg              |移动到第一行 相当于1G

#### 搜寻与取代
指令|作用
|-|-|
/word   |向下寻找word字符串
$word   |向上寻找word字符串
n       |正向搜索
N       |反向搜索
:n1,n2s/word1/word2/g   |在n1和n2行之间搜索word1,替换为word2
:1,$s/word1/word2/g     |从第一列到最后一列寻找 word1 字串，并将该字串取代为 word2 
:1,$s/word1/word2/gc    |从第一列到最后一列寻找 word1 字串，并将该字串取代为 word2 ！且在取代前显示提示字符给使用者 确认 （confirm） 是否需要取代！

#### 删除,复制与粘贴
指令|作用
|-|-|
x,X         |x向后删除一个字符 , X向前删除一个字符
nx          |向后删除n个字符
dd          |删除当前列
ndd         |删除n列
yy          |复制当前列
nyy         |复制n列
p, P        |p 为将已复制的数据在光标下一列贴上，P 则为贴在光标上一列！ 
u           |撤回上一个动作
[Ctrl]+r或点    |重复上个动作

#### 切换到编辑模式
指令|作用
|-|-|
i   |从光标进入插入模式
a   |从光标下个字符进入插入模式
I   |从当前列最左侧非空字符前进入插入模式
A   |从当前列最后进入插入模式
o   |下一行插入新行
O   |上一行插入新行
r   |进入取代模式1个字符
R   |进入一直取代模式
[Esc]|退出编辑模式

#### 命令行命令
指令|作用
|-|-|
:w  |保存
:q  |退出
:q! |强制退出
:wq |保存并退出
:w [filename]   |另存为
:set nu |显示行号
:set nonu|取消行号

#### vim的暂存盘操作
当vim没有正常保存,你再次登录的时候会出现
```
E325: ATTENTION
Found a swap file by the name ".man_db.conf.swp"
          owned by: zero   dated: Tue Jan  8 15:31:46 2019
         file name: /tmp/vitest/man_db.conf
          modified: no
         user name: zero   host name: VM_16_8_centos
        process ID: 8151
While opening file "man_db.conf"
             dated: Tue Jan  8 15:24:35 2019

(1) Another program may be editing the same file.  If this is the case,
    be careful not to end up with two different instances of the same
    file when making changes.  Quit, or continue with caution.
(2) An edit session for this file crashed.
    If this is the case, use ":recover" or "vim -r man_db.conf"
    to recover the changes (see ":help recovery").
    If you did this already, delete the swap file ".man_db.conf.swp"
    to avoid this message.

Swap file ".man_db.conf.swp" already exists!
[O]pen Read-Only, (E)dit anyway, (R)ecover, (D)elete it, (Q)uit, (A)bort:
```

* [O]pen Read-Only：打开此文件成为只读文件， 可以用在你只是想要查阅该文件内容并不想要进行编辑行为时。一般来说，在 上课时，如果你是登陆到同学的计算机去看他的配置文件， 结果发现其实同学他自己也在编辑时，可以使用这个模式；
* （E）dit anyway：还是用正常的方式打开你要编辑的那个文件， 并不会载入暂存盘的内容。不过很容易出现两个使用者互相 改变对方的文件等问题！不好不好！
* （R）ecover：就是载入暂存盘的内容，用在你要救回之前未储存的工作。 不过当你救回来并且储存离开 vim 后，还是要手动 自行删除那个暂存盘喔！
* （D）elete it：你确定那个暂存盘是无用的！那么打开文件前会先将这个暂存盘删除！ 这个动作其实是比较常做的！因为你可 能不确定这个暂存盘是怎么来的，所以就删除掉他吧！哈哈！
* （Q）uit：按下 q 就离开 vim ，不会进行任何动作回到命令提示字符。
* （A）bort：忽略这个编辑行为，感觉上与 quit 非常类似！ 也会送你回到命令提示字符就是了;

#### 区块选择
以区块的模式选择字符
指令|作用
|-          |-|
v           |字符选择，会将光标经过的地方反白选择！
V           |列选择，会将光标经过的列反白选择！
[Ctrl]+v    |区块选择，可以用长方形的方式选择数据
y           |将反白的地方复制起来
d           |将反白的地方删除掉
p           |将刚刚复制的区块，在光标所在处贴上！


#### 多文件编辑

> vim [文件1] [文件2]

指令|作用
|-      |-|
:N      |编辑上一个文件
:n      |编辑下一个文件
:files  |列出目前这个 vim 的打开的所有文件

#### 分屏
指令|作用
|-      |-|
:sp [filename]          |打开一个新窗口，如果有加 filename， 表示在新窗口打开一个新文件，否则表示两个窗口为同一个文件内容（同 步显示）。
[ctrl]+w+ j [ctrl]+w+↓  |按键的按法是：先按下 [ctrl] 不放， 再按下 w 后放开所有的按键，然后再按下 j （或向下方向键），则光标可 移动到下方的窗口。
[ctrl]+w+ k [ctrl]+w+↑  |同上，不过光标移动到上面的窗口。
[ctrl]+w+ q             |其实就是 :q 结束离开啦！ 举例来说，如果我想要结束下方的窗口，那么利用 [ctrl]+w+↓ 移动到下方窗口后， 按下 :q 即可离开， 也可以按下 [ctrl]+w+q 啊



#### vim 环境参数设置

~/.vimrc 用来记录用户的vim配置
~/.viminfo 用来记录用户vim的使用情况

可以直接修改配置文件,让vim记住你的配置,从而不用每次进入vim都设置行号什么东东了
我这么设置

```
"这个文件中双引号就是注释"
set nu          "行号"
set ruler       "显示最后一排状态"
set backspace=2 "退格键可以删除任何内容"
set autoindent  "自动缩进"
```


#### 注意
另外,需要注意与window之间的换行符的不同;换行符转化和变编码回头再整理吧(我基本用不到哈哈)

## 打印版

![](https://img2018.cnblogs.com/blog/1528020/201901/1528020-20190109151413798-181163859.png)