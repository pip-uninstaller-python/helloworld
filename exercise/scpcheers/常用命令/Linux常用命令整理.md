# Linux常用命令整理

## 快捷键
#### [Tab]
* [Tab] 接在一串指令的第一个字的后面，则为“命令补全”； 
* [Tab] 接在一串指令的第二个字以后时，则为“文件补齐”！ 
* 若安装 bash-completion 软件，则在某些指令后面使用 [tab] 按键时，可以进行“选项/参数的补齐”功能！

#### [Ctrl]-c
退出当前程序

#### [Ctrl]-d
键盘输入结束

#### [shift]+{[PageUP]|[Page Down]}按键
在纯文本中翻页



## 日常命令
#### uname检查内核版本
* -a 全部信息
* -r 核心版本
* -m 操作系统位版本比如 (x86_64)

#### date 获取当前日期时间

```
[root@VM_16_8_centos ~]# date
	Thu Jan  3 13:52:40 CST 2019
```
可以指定显示格式

```
[root@VM_16_8_centos ~]# date +%Y/%m/%d%H:%M 
2019/01/0313:52
```
#### cal日历
`cal [month] [year]`可以显示整年的日历

#### bc 计算器
进入计算器模式 进行简单的数学运算
`quit`结束

#### who 查看正在连接的用户
```
[root@VM_16_8_centos ~]# who
root     pts/0        2019-01-03 11:35 (1.119.152.66)
```

#### netstat -a 查看网络的连接状态
```
[root@VM_16_8_centos ~]# netstat -a
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN     
tcp        0     52 VM_16_8_centos:ssh      1.119.152.66:50947      ESTABLISHED
tcp        0      0 VM_16_8_centos:38550    169.254.0.55:lsi-bobcat ESTABLISHED
udp        0      0 0.0.0.0:bootpc          0.0.0.0:*                          
udp        0      0 VM_16_8_centos:ntp      0.0.0.0:*                          
udp        0      0 VM_16_8_centos:ntp      0.0.0.0:*                          
udp        0      0 0.0.0.0:ntp             0.0.0.0:*                          
udp6       0      0 [::]:ntp                [::]:*                             
Active UNIX domain sockets (servers and established)
Proto RefCnt Flags       Type       State         I-Node   Path
unix  2      [ ACC ]     STREAM     LISTENING     12294    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     3509988  /usr/local/yd.socket.client
unix  2      [ ACC ]     STREAM     LISTENING     12832    /var/run/acpid.socket
unix  2      [ ACC ]     SEQPACKET  LISTENING     10027    /run/udev/control
unix  2      [ ]         DGRAM                    10304    /run/systemd/shutdownd
unix  2      [ ACC ]     STREAM     LISTENING     10056    /run/lvm/lvmetad.socket
unix  2      [ ACC ]     STREAM     LISTENING     10076    /run/lvm/lvmpolld.socket
等等
```
#### ps 查看线程
* -aux 查看后台正在执行的程序


#### sync 将数据同步写入硬盘中

#### su 切换用户
* $su -root

#### shutdown 关机

#### reboot 重启

#### --help 查询相关信息

#### man 查看操作说明 info 分模块跳转的操作说明
后面跟关键字 查看该命令的说明文档
最上方`DATE(1) `会有一个数字,说明这个命令的代表内容
重要的有三个
代号|代表内容
-|-
1|使用者在shell环境中可以操作的指令或可可执行文件 
5|配置文件或者是某些文件的格式
8|系统管理员可用的管理指令



## 文件相关的命令

#### cd 跳转
* . 此层目录
* .. 代表上一层目录
* - 上一个目录
* ~ 当前用户主文件夹
* ~username 指定用户主文件夹


#### ls
* -l 详细数据
* -a 所有文件
* -d 只显示当前目录本身
* -i 显示文件占用的inode编号
* [--full-time] 显示完整的时间
* [--time=ctime或atime]
    * modification time（mtime）：当该文件的“内容数据”变更时，就会更新这个时间！内容数据指的是文件的内容，而不是文件的属性或权限！默认就是这个时间
    * status time （ctime）： 当该文件的“状态 （status）”改变时，就会更新这个时间，举例来说，像是权限与属性被更改了，都会更新这个时间啊。 
    * access time （atime）： 当“该文件的内容被取用”时，就会更新这个读取时间 （access）。举例来说，我们使用 cat 去读取 /etc/man_db.conf ， 就会更 新该文件的 atime 了
    从kernel2.6.29开始,文件系统默认继承了relatime属性,如果一直被访问,每天只会更新一次atime,或者mtime比atime新,那么下次更新,会更新atime;


权限    链接    拥有者    群组    文件大小    修改日期    文件名
```
[root@VM_16_8_centos ~]# ls -al
total 64
dr-xr-x---.  6 root root 4096 Jan  3 14:38 .
dr-xr-xr-x. 19 root root 4096 Jan  3 15:15 ..
-rw-------   1 root root 2245 Jan  3 15:15 .bash_history
-rw-r--r--.  1 root root   18 Dec 29  2013 .bash_logout
-rw-r--r--.  1 root root  176 Dec 29  2013 .bash_profile
-rw-r--r--.  1 root root  176 Dec 29  2013 .bashrc
drwxr-xr-x   3 root root 4096 Aug 13 17:08 .cache
drwxr-xr-x   3 root root 4096 Aug 13 17:08 .config
-rw-r--r--.  1 root root  100 Dec 29  2013 .cshrc
-rw-------   1 root root   39 Jan  3 14:28 .lesshst
drwxr-xr-x   2 root root 4096 Nov 30 22:54 .pip
-rw-r--r--   1 root root   73 Nov 30 22:54 .pydistutils.cfg
drwx------   2 root root 4096 Aug 13 17:07 .ssh
-rw-r--r--.  1 root root  129 Dec 29  2013 .tcshrc
-rw-r--r--   1 root root   11 Jan  3 14:38 test
-rw-------   1 root root  691 Jan  3 14:29 .viminfo
```

文件种类
* 正规文件(-)
    * 纯文本文件
    * 二进制档
    * 数据格式文件
* 目录(d)
* 连接文件(l) 快捷方式
* 设备与设备文件
    *  区块设备文件,硬盘软盘(b)
    *  字符设备文件,鼠标键盘(c)
*  数据接口文件(s) 网络数据
*  数据输送档(p) 文件传输

权限一共有10位
- 第一个字符代表文件(-),目录(d),链接(l)
- 其余三个为一组(rwx) 读写执行  文件夹的访问需要x
    - 第一组 文件所有者权限
    - 第二组 与文件所有者同一组的用户的权限
    - 第三组 不同组的其他用户权限
    - 另外 r=4 w=2 x=1 可以把每组用和来表示 例如 能读能写就为6

元件 | 内容 | 叠代物件 |r| w| x
-|-|-|-|-|-
文件| 详细数据data |文件数据夹 |读到文件内容| 修改文件内容(不能删除) |执行文件内容 
目录| 文件名| 可分类抽屉| 读目录下文件名 |对目录下文件与目录增,删,改名,移动 |进入该目录的权限（key）


#### pwd [-P] 当前目录路径
* -P 真实路径

#### mkdir 创建文件夹
* -p 创建多重目录
* -m [权限三数字] 创建指定权限的文件夹

#### rmdir 删除空目录
* -p 删除多重空目录

#### cp 复制
* ==-a==  ：相当于 -dr --preserve=all 的意思，至于 dr 请参考下列说明；（常用） 
* -d  ：若来源文件为链接文件的属性（link file），则复制链接文件属性而非文件本身； 
* -f  ：为强制（force）的意思，若目标文件已经存在且无法打开，则移除后再尝试一次； 
* ==-i==  ：若目标文件（destination）已经存在时，在覆盖时会先询问动作的进行（常用） 
* -l  ：进行硬式链接（hard link）的链接文件创建，而非复制文件本身； 
* ==-p==  ：连同文件的属性（权限、用户、时间）一起复制过去，而非使用默认属性（备份常用）； 
* -r  ：递回持续复制，用于目录的复制行为；（常用） 
* -s  ：复制成为符号链接文件 （symbolic link），亦即“捷径”文件； ll下 会显示指向的文件
* -u  ：destination 比 source 旧才更新 destination，或 destination 不存在的情况下才复制。 常用于备份工作
* --preserve=all ：除了 -p 的权限相关参数外，还加入 SELinux 的属性, links, xattr 等也复制了

#### mv 移动或改名
* -f 强制;无视一切直接覆盖
* -i 询问是否覆盖
* -u 若目标文件已经存在，且 source 比较新，才会更新 （update)

#### rm 删除
* -f 强制;忽略不存在的文件;无视警告
* -i 互动模式,删除前询问 root操作时默认加入
* -r 递归删除,危险!

#### basename 获取文件名

```
[root@VM_16_8_centos tmp]# basename /tmp/testing/test1 
test1
```

#### dirname 获取目录名

```
[root@VM_16_8_centos tmp]# dirname /tmp/testing/test1     
/tmp/testing
```



#### touch [文件名] 将文件三个时间属性置为此刻;如文件不存在,创建空文件
* -a  ：仅修订 access time； 
* -c  ：仅修改文件的时间，若该文件不存在则不创建新文件； 
* -d  ：后面可以接欲修订的日期而不用目前的日期，也可以使用 --date="日期或时间" 
* -m  ：仅修改 mtime ； 
* -t  ：后面可以接欲修订的时间而不用目前的时间，格式为[YYYYMMDDhhmm]

#### stat 获取文件状态
```
[zero@VM_16_8_centos tmp]$ stat test
  File: ‘test’
  Size: 0               Blocks: 0          IO Block: 4096   regular empty file
Device: fd01h/64769d    Inode: 1819        Links: 1
Access: (4711/-rws--x--x)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2019-01-07 11:50:15.887255356 +0800
Modify: 2019-01-07 11:50:15.887255356 +0800
Change: 2019-01-07 11:50:42.912253038 +0800
 Birth: -
```

#### file 判断文件的格式
```
[zero@VM_16_8_centos tmp]$ file test2
test2: UTF-8 Unicode text
```


#### umask 文件默认权限 后面三个数字是权限三数字,指减掉的权限
```
[root@VM_16_8_centos ~]# umask
0022
[root@VM_16_8_centos ~]# umask -S
u=rwx,g=rx,o=rx
```
后面直接跟全部4个数字后者后三位数字就能对他进行重新配置了
```
[zero@VM_16_8_centos ~]$ umask 002 =>拿掉非同组的写权限
```

> 一般情况下root的umask默认是022,普通用户的umask默认是002

## 文件属性与权限

#### chgrp 改变文件所属群组
> chgrp [-R]群组名 文件名
* -R 递归 把下面子目录所有文件也改变

#### chown 改变文件拥有者
> chown [-R] 帐号名称 文件或目录

或者一起修改群组名 用冒号或点连接

> chown [-R] 帐号名称:群组名称 群组名称 文件或目录
* -R 递归 把下面子目录所有文件也改变

#### chmod 改变文件的权限
> chomd [-R] 权限数字

## 文件的隐藏权限
#### chattr 设置文件隐藏属性
chattr指令只能在Ext2/Ext3/Ext4的 Linux 传统文件系统上面完整生效
> [root@study ~]# chattr [+-=][ASacdistu] 文件或目录名称
* + ：增加某一个特殊参数，其他原本存在参数则不动。 
* - ：移除某一个特殊参数，其他原本存在参数则不动。 
* = ：设置一定，且仅有后面接的参数
* A ：当设置了 A 这个属性时，若你有存取此文件（或目录）时，他的存取时间 atime 将不会被修改，     可避免 I/O 较慢的机器过度的存取磁盘。（目前建议使用文件系统挂载参数处理这个项目） 
* S  ：一般文件是非同步写入磁盘的（原理请参考前一章sync的说明），如果加上 S 这个属性时，     当你进行任何文件的修改，该更动会“同步”写入磁盘中。 
* ==a==  ：当设置 a 之后，这个文件将只能增加数据，而不能删除也不能修改数据，只有root 才能设置这属性 
* c  ：这个属性设置之后，将会自动的将此文件“压缩”，在读取的时候将会自动解压缩，     但是在储存的时候，将会先进行压缩后再储存（看来对于大文件似乎蛮有用的！） 
* d  ：当 dump 程序被执行的时候，设置 d 属性将可使该文件（或目录）不会被 dump 备份 
* ==i==  ：这个 i 可就很厉害了！他可以让一个文件“不能被删除、改名、设置链接也无法写入或新增数据！”     对于系统安全性有相当大的助益！只有 root 能设置此属性 
* s  ：当文件设置了 s 属性时，如果这个文件被删除，他将会被完全的移除出这个硬盘空间，     所以如果误删了，完全无法救回来了喔！ 
* u  ：与 s 相反的，当使用 u 来设置文件时，如果该文件被删除了，则数据内容其实还存在磁盘中，     可以使用来救援该文件喔！ 
* 注意1：属性设置常见的是 a 与 i 的设置值，而且很多设置值必须要身为 root 才能设置 
* 注意2：xfs 文件系统仅支持 AadiS 而已

#### lsattr 显示文件隐藏属性
* -a ：将隐藏文件的属性也秀出来； 
* -d ：如果接的是目录，仅列出目录本身的属性而非目录内的文件名； 
* -R ：连同子目录的数据也一并列出来!

> 可以记忆为ls + attr attr就是隐藏属性 这个指令可以直接使用,显示当前文件夹下文件的隐藏属性,也可以显示目标文件或文件夹

## 文件特殊权限 SUID/SGID/SBIT
```
[zero@VM_16_8_centos ~]$ ls -ld /tmp;ll /usr/bin/passwd
drwxrwxrwt. 7 root root 4096 Jan  7 10:48 /tmp
-rwsr-xr-x. 1 root root 27832 Jun 10  2014 /usr/bin/passwd
```
我们发现/tmp 和 /usr/bin/passwd 的属性中有 t 和 s 类似这种非rwx权限,称为特殊权限
#### SUID 当s在文件拥有者x权限的位置上时为SUID特殊权限(Set UID)
1. SUID 权限仅对二进制程序（binary program）有效； 
2. 执行者对于该程序需要具有 x 的可执行权限； 
3. 本权限仅在执行该程序的过程中有效 （run-time）； 
4. 执行者将具有该程序拥有者 （owner） 的权限。
* 简单的说,就是你执行具有s权限的程序的时候,会在执行过程中获取改程序拥有者的权限;

#### SGID 当s在文件群组x权限的位置上时为SGID特殊权限(set GID)
作用于文件上时
1. SGID 对二进制程序有用； 
2. 程序执行者对于该程序来说，需具备 x 的权限； 
3. 执行者在执行的过程中将会获得该程序群组的支持！

作用于目录上时
1. 使用者若对于此目录具有 r 与 x 的权限时，该使用者能够进入此目录； 
2. 使用者在此目录下的有效群组（effective group）将会变成该目录的群组； 
3. 用途：若使用者在此目录下具有 w 的权限（可以新建文件），则使用者所创建的新文件，该新文件的群组与此目录的群组相 同。

> 总而言之,s权限就是让你在执行文件或进入目录的时候,获得相应的身份;去什么场合穿什么衣服

##### SBIT 当t在x权限的位置上时为SBIT特殊权限(Sticky Bit)粘性数据
只作用于目录
1. 当使用者对于此目录具有 w, x 权限，亦即具有写入的权限时； 
2. 当使用者在该目录下创建文件或目录时，仅有自己与 root 才有权力删除该文件

举个栗子，我们的 /tmp 本身的权限是“drwxrwxrwt”， 在这样的权限内容下，任何人都可以在 /tmp 内新增、修改文件，但 仅有该文件/目录创建者与 root 能够删除自己的目录或文件。

#### 设置的方法
* 4为SUID
* 2为SGID
* 1为SBIT
仍然使用 chmod ,设置权限时,在三个数字前加上特殊权限的数字即可,如果添加的权限显示为大写,代表该权限无效,它的前置条件没有满足

## 文件搜寻
#### which 寻找可执行文件
> which [-a] 指令 
* -a 将所有符合条件的知名均列出,而不至第一个被找到的指令(包括指令的别名)

注意which只找PATH内所规范的目录;比如bash相关指令就找不到

#### whereis 在一些特定的目录中寻找文件文件名
> whereis [-bmsu] 文件或目录名
* -l    :可以列出 whereis 会去查询的几个主要目录而已 
* -b    :只找 binary 格式的文件 
* -m    :只找在说明文档 manual 路径下的文件 
* -s    :只找 source 来源文件 
* -u    :搜寻不在上述三个项目当中的其他特殊文件

#### locate  根据索引查找
依据 /var/lib/mlocate 内的数据库记载，找出使用者输入的关键字文件名,索引默认每天更新一次
*  -i  ：忽略大小写的差异； 
*  -c  ：不输出文件名，仅计算找到的文件数量 
*  -l  ：仅输出几行的意思，例如输出五行则是 -l 5 
*  -S  ：输出 locate 所使用的数据库文件的相关信息，包括该数据库纪录的文件/目录数量等 
*  -r  ：后面可接正则表达式的显示方式 

#### updatedb 更新索引
根据 /etc/updatedb.conf 的设置去搜寻系统硬盘内的文件名，并更新 /var/lib/mlocate 内的数据库文件；

#### find 全局查找
>  find [PATH] [option] [action] 
1. 与时间有关的选项：共有 -atime, -ctime 与 -mtime ，以 -mtime 说明   
    * -mtime  n ：n 为数字，意义为在 n 天之前的“一天之内”被更动过内容的文件；   
    * -mtime +n ：列出在 n 天之前（不含 n 天本身）被更动过内容的文件文件名；   
    * -mtime -n ：列出在 n 天之内（含 n 天本身）被更动过内容的文件文件名。   
    * -newer file ：file 为一个存在的文件，列出比 file 还要新的文件文件名 
2. 与使用者或群组名称有关的参数：   
    * -uid n ：n 为数字，这个数字是使用者的帐号 ID，亦即 UID ，这个 UID 是记录在            
    /etc/passwd 里面与帐号名称对应的数字。这方面我们会在第四篇介绍。   
    * -gid n ：n 为数字，这个数字是群组名称的 ID，亦即 GID，这个 GID 记录在            /etc/group，相关的介绍我们会第四篇说明～   
    * -user name ：name 为使用者帐号名称喔！例如 dmtsai    
    * -group name：name 为群组名称喔，例如 users ；   
    * -nouser    ：寻找文件的拥有者不存在 /etc/passwd 的人！   
    * -nogroup   ：寻找文件的拥有群组不存在于 /etc/group 的文件！                当你自行安装软件时，很可能该软件的属性当中并没有文件拥有者，                这是可能的！在这个时候，就可以使用 -nouser 与 -nogroup 搜寻。 
3. 与文件权限及名称有关的参数：   
    * -name filename：搜寻文件名称为 filename 的文件；   
    * -size [+-]SIZE：搜寻比 SIZE 还要大（+）或小（-）的文件。这个 SIZE 的规格有：                   c: 代表 Byte， k: 代表 1024Bytes。所以，要找比 50KB                   还要大的文件，就是“ -size +50k ”   -type TYPE    ：搜寻文件的类型为 TYPE 的，类型主要有：一般正规文件 （f）, 设备文件 （b, c）,                   目录 （d）, 链接文件 （l）, socket （s）, 及 FIFO （p） 等属性。   
    * -perm mode  ：搜寻文件权限“刚好等于” mode 的文件，这个 mode 为类似 chmod                 的属性值，举例来说， -rwsr-xr-x 的属性为 4755 ！   
    * -perm -mode ：搜寻文件权限“必须要全部囊括 mode 的权限”的文件，举例来说，                 我们要搜寻 -rwxr--r-- ，亦即 0744 的文件，使用 -perm -0744，                 当一个文件的权限为 -rwsr-xr-x ，亦即 4755 时，也会被列出来，                 因为 -rwsr-xr-x 的属性已经囊括了 -rwxr--r-- 的属性了。   
    * -perm /mode ：搜寻文件权限“包含任一 mode 的权限”的文件，举例来说，我们搜寻                 -rwxr-xr-x ，亦即 -perm /755 时，但一个文件属性为 -rw------                 也会被列出来，因为他有 -rw.... 的属性存在！ 
4. find可以进行额外的动作
```
[zero@VM_16_8_centos tmp]$ find / -perm /7000 -exec ls -l {} \;  =>将find的结果放入大括号内
```
5. 逻辑操作:
    * -o 是或者的意思  
    * -a 是而且的意思  
    * -not 是相反的意思  


## 查阅文件指令
#### cat (Concatenate 连续)从第一行开始显示
* -A  ：相当于 -vET 的整合选项，可列出一些特殊字符而不是空白而已； 
* -b  ：列出行号，仅针对非空白行做行号显示，空白行不标行号！ 
* -E  ：将结尾的断行字符 $ 显示出来； 
* -n  ：打印出行号，连同空白行也会有行号，与 -b 的选项不同； 
* -T  ：将 [tab] 按键以 ^I 显示出来； 
* -v  ：列出一些看不出来的特殊字符

#### tac 从最后一行开始显示
和cat相同

#### nl 显示的时候,顺便输出行号
* -b  ：指定行号指定的方式，主要有两种：      
    * -b a ：表示不论是否为空行，也同样列出行号（类似 cat -n）；      
    * -b t ：如果有空行，空的那一行不要列出行号（默认值）； 
* -n  ：列出行号表示的方法，主要有三种：
    * -n ln ：行号在屏幕的最左方显示；      
    * -n rn ：行号在自己字段的最右方显示，且不加 0 ；      
    * -n rz ：行号在自己字段的最右方显示，且加 0 ； 
* -w [数字]：行号字段的占用的字符数。


#### more 一页一页显示文件内容
* 空白键 （space）：代表向下翻一页； 
* Enter         ：代表向下翻“一行”； 
* /字串         ：代表在这个显示的内容当中，向下搜寻“字串”这个关键字； 
    * n         : 跳转到下一个匹配的字串 
* :f            ：立刻显示出文件名以及目前显示的行数； 
* q             ：代表立刻离开 more ，不再显示该文件内容。 
* b 或 [ctrl]-b ：代表往回翻页，不过这动作只对文件有用，对管线无用

#### less 可以前后翻页
* 空白键    ：向下翻动一页； 
* [pagedown]：向下翻动一页；
* [pageup]  ：向上翻动一页； 
* /字串     ：向下搜寻“字串”的功能； 
* ?字串     ：向上搜寻“字串”的功能； 
* n         ：重复前一个搜寻 （与 / 或 ? 有关！） 
* N         ：反向的重复前一个搜寻 （与 / 或 ? 有关！） 
* g         ：前进到这个数据的第一行去； 
* G         ：前进到这个数据的最后一行去 （注意大小写）； 
* q         ：离开 less 这个程序；
* F         : 持续刷新,显示最新数据


#### head 只看头几行
* -n [数字]：后面接数字，代表显示几行的意思 默认10行,如果数字是负数,代表不显示后面多少行
* -f 持续刷新


#### tail 只看最后几行
* -n [数字]: 同上
* -f 持续刷新

#### od [-t TYPE]以二进制输出
* -t  ：后面可以接各种“类型 （TYPE）”的输出，例如：      
    * a       ：利用默认的字符来输出；      
    * c       ：使用 ASCII 字符来输出      
    * d[size] ：利用十进制（decimal）来输出数据，每个整数占用 size Bytes ；      
    * f[size] ：利用浮点数值（floating）来输出数据，每个数占用 size Bytes ；      
    * o[size] ：利用八进位（octal）来输出数据，每个整数占用 size Bytes ；      
    * x[size] ：利用十六进制（hexadecimal）来输出数据，每个整数占用 size Bytes 


## 文件压缩
常见的压缩文件的后缀名
* *.Z         compress 程序压缩的文件； 
* *.zip       zip 程序压缩的文件； 
* *.gz        gzip 程序压缩的文件； 
* *.bz2       bzip2 程序压缩的文件； 
* *.xz        xz 程序压缩的文件； 
* *.tar       tar 程序打包的数据，并没有压缩过； 
* *.tar.gz    tar 程序打包的文件，其中并且经过 gzip 的压缩 
* *.tar.bz2   tar 程序打包的文件，其中并且经过 bzip2 的压缩 
* *.tar.xz    tar 程序打包的文件，其中并且经过 xz 的压缩

#### gzip [-cdtv#] 文件名 
* -c  ：将压缩的数据输出到屏幕上，可通过数据流重导向来处理； 
* -d  ：解压缩； 
* -t  ：可以用来检验一个压缩文件的一致性～看看文件有无错误； 
* -v  ：可以显示出原文件/压缩文件的压缩比等信息； 
* -#  ：# 为数字的意思，代表压缩等级，-1 最快，但是压缩比最差、-9 最慢，但是压缩比最好！默认是 -6

压缩不保留源文件 , 如果要保留源文件 需要用-c 加上 >
> gzip -9 -c services > services.gz  用最佳的压缩比压缩，并保留原本的文件

#### zcat/zmore/zless/zgrep 读gzip压缩的文本文件
用法跟普通的一样

#### bzip2 [-cdkzv#] 文件名 比gzip压缩比更好
* -c  ：将压缩的过程产生的数据输出到屏幕上！ 
* -d  ：解压缩的参数 
* -k  ：保留原始文件，而不会删除原始的文件喔！ 
* -z  ：压缩的参数 （默认值，可以不加） 
* -v  ：可以显示出原文件/压缩文件的压缩比等信息； 
* -#  ：与 gzip 同样的，都是在计算压缩比的参数， -9 最佳， -1 最快！

####  bzcat/bzmore/bzless/bzgrep 读bzip2压缩的文本文件

#### xz [-dtlkc#] 文件名 比bzip2更强!
* -d  ：就是解压缩啊！ 
* -t  ：测试压缩文件的完整性，看有没有错误 
* -l  ：列出压缩文件的相关信息 
* -k  ：保留原本的文件不删除～ 
* -c  ：同样的，就是将数据由屏幕上输出的意思！ 
* -#  ：同样的，也有较佳的压缩比的意思！

#### xzcat/xzmore/xzless/xzgrep 你懂得

#### tar 打包
 > tar [-z|-j|-J] [cv] [-f 待创建的新文件名 待创建的新文件名] filename... <==打包与压缩 
 > tar [-z|-j|-J] [tv] [-f  既有的tar文件名]             <==察看文件名
 >  tar [-z|-j|-J] [xv] [-f  既有的tar文件名] [-C 目录]   <==解压缩
 
* -c  ：创建打包文件，可搭配 
* -v 来察看过程中被打包的文件名（filename） 
* -t  ：察看打包文件的内容含有哪些文件名，重点在察看“文件名”就是了； 
* -x  ：解打包或解压缩的功能，可以搭配 -C （大写） 在特定目录解开      特别留意的是， -c, -t, -x 不可同时出现在一串命令行中。 
* -z  ：通过 gzip  的支持进行压缩/解压缩：此时文件名最好为 *.tar.gz 
* -j  ：通过 bzip2 的支持进行压缩/解压缩：此时文件名最好为 *.tar.bz2 
* -J  ：通过 xz    的支持进行压缩/解压缩：此时文件名最好为 *.tar.xz      特别留意， -z, -j, -J 不可以同时出现在一串命令行中 
* -v  ：在压缩/解压缩的过程中，将正在处理的文件名显示出来！ 
* -f filename：-f 后面要立刻接要被处理的文件名！建议 -f 单独写一个选项啰！（比较不会忘记） 
* -C 目录    ：这个选项用在解压缩，若要在特定目录解压缩，可以使用这个选项。


其他后续练习会使用到的选项介绍： 
* -p（小写） ：保留备份数据的原本权限与属性，常用于备份（-c）重要的配置文件 文件名不带根目录
* -P（大写） ：保留绝对路径，亦即允许备份数据中含有根目录存在之意；危险,解压的时候不注意会直接覆盖原文件,慎用 
* --exclude=FILE：在压缩的过程中，不要将 FILE 打包！ 
* --newer [文件] 仅打包比指定文件新的文件,备份常用
* --newer-mtime=[时间] 仅打包mtime大于指定时间的文件,备份常用 时间格式:'yyyy/MM/dd HH:mm:ss'  
常用的指令
* 压　缩：tar -zcv -f filename.tar.bz2 要被压缩的文件或目录名称 
* 查　询：tar -ztv -f filename.tar.bz2 
* 解压缩：tar -zxv -f filename.tar.bz2 -C 欲解压缩的目录

解压缩单一文件,先查询文件名 然后用解压缩命令解压它即可,注意文件名带不带根目录
> tar -zxv -f 打包档.tar.bz2 待解开文件名


## 目录
#### 必须存在的目录
* / 根目录 系统启动恢复相关
    * /bin 放置指令
    * /boot 开机相关配置文件
    * /dev 硬件设备
    * /etc 配置文件
        * /etc/passwd 系统账号相关信息
        * /etc/shadow 个人密码
        * /etc/group 群组
        * /etc/opt 第三方协力软件配置
        * /etc/xml xml相关配置文件
    * /lib 函数库
        * /lib/modules 驱动程序 
    * /media 移动储存设备 硬盘,光盘
    * /mnt 暂时挂载设备
    * /opt 第三方软件
    * /run 开机后产生的各项日志
    * /sbin root专用系统指令,开机.修复.还原系统
    * /srv 网络服务提供出的数据
    * /tmp 文件暂时存放处(所有任都可以存取)
    * /usr 软件放置处 后续介绍```  
        * /usr/share/doc 说明文档目录
    * var 变动性的数据 后续介绍```

#### 建议目录

* /home 使用者主文件夹
* /root root的主文件夹
* /lib<其他格式> 不同格式的函数库 如/lib64 

#### 应放置文件内容
* /lost+found 系统错误的遗失片段存放目录(ext2/ext3/ext4文件系统才有)
* /proc 虚拟文件系统(所有数据都在内存中) 系统核心,形成信息,设备状态与网络状态
* /sys 虚拟文件系统(所有数据都在内存中) 核心与系统硬件相关信息

#### /usr (Unix Software Resource Unix操作系统软件资源)安装时占用较大硬盘容量的目录
* /usr/bin 一般用户指令(CentOS 7将/usr链接至此一模一样) 没有子目录
* /usr/lib 同理 和/lib一样
* /usr/local 自行下载安装的软件
* /usr/sbin 同理和/sbin一样
* /usr/share 只读架构的数据文件和共享文件
    * /usr/share/man 线上说明文档
    * /usr/share/doc 软件杂项的文件说明
    * /usr/share/zoneinfo 时区相关文件
* /usr/games 游戏
* /usr/include c语言相关header和include 
* /usr/libexec 不被一般使用者惯用的可执行文件或脚本
* /usr/lib<qual> 同理```
* /usr/src 源代码放置目录
* /usr/src/linux 核心源代码目录

#### /var 系统运行后会渐渐占用硬盘的目录
* /var/cache 应用程序本身运行过程中的缓存
* /var/lib 程序执行过程中,需要使用的数据文件目录,每个软件都有各自的目录
    * /var/lib/mysql mysql数据库目录
    * /var/lib/rpm rpm数据库目录
* /var/lock 将加锁(和java一样)的文件(包括设备)临时移入 目前链接至/run/lock
* /var/log 登录文件放置目录
* /var/mail 个人电子邮件信箱目录 链接至/var/spool/mail
* /var/run/ 程序或服务启动后,放置PID 链接至/run
* /var/spool 排队产生的缓存数据

## 其他常用目录
* /dev/sd[a-p][1-128]：为实体磁盘的磁盘文件名；
* /dev/vd[a-d][1-128]：为虚拟磁盘的磁盘文件名
* /lib/modules/(每个系统可能不一样)/kernel/fs  当前系统支持的文件系统

## 常用文件
* /proc/filesystems  当前已载入到内存中支持的文件系统

#### 链接总结
* /bin --> /usr/bin 
* /sbin --> /usr/sbin 
* /lib --> /usr/lib 
* /lib64 --> /usr/lib64 
* /var/lock --> /run/lock 
* /var/run --> /run


## 参考资料
http://linux.vbird.org/