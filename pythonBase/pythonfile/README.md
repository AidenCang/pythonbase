#Linux文件系统
#OS模块操作
#文件的概念
#文件的打开方式
#文件的读写操作
#文件指针
#文件属性对象

#Linux系统知识
#LinuxPython 开发环境
#掌握Python基础知识

#Python文件是对象
#Linux一切文件皆对象，一切设备多看着文件
#磁盘文件、管道、网络Socket、外设


#Python文件操作之文件打开方式

    open('name',mode = "",buf)
    name：文件名
    mode：打开方式
    buf：缓冲区大小

文件读取方式：

    read：size大小、默认全部读取
    readline：
    readlines：一次性读取完，返回以每一行组成的的列表

文件写入方式：

    write:将字符串写入文件
    writelines：写入多行文件
    
OS 模块、shutill
os.path
shutil 模块提供了大量的文件的高级操作，特别针对文件拷贝和删除。主要功能为目录和文件操作以及压缩操作