# 变量：程序中用来存储单个数据的容器，通常把经常发生变化的数据存储在变量中
# python是动态类型语言，在程序运行时才进行类型检查，变量的类型可以在程序的运行过程中发生改变（一个变量可以赋值为多种类型）

num = 1213
print(num)

num = "Hello Python"
print(num)

# 结果发现 num第一输出1213，第二次输出"Hello Python"第一次数据类型为int，可以赋值给String类型数据

base = 20.5
incr = 30


#多个数据之间使用","进行分隔，而不是使用"+"进行拼接（但是输出时逗号会默认处理成空格）
print("目前播放量：",base+incr)

#解决办法1:sep 代表分隔符，默认 sep=' '（空格），设置为空字符串 sep=''
print("目前播放量：",base+incr,sep="")

# 解决办法2：使用字符串拼接"+",使用str()强制转换符，将float类型转化为String类型
print("目前播放量：" + str(base+incr))

# 一次定义多个变量
num1,num2 = 3,4
print(num1,num2)


# 标识符(变量/函数/类等元素的名字)命名规则：
# 1.只能包含字母(a-z,A-Z)，数字(0-9)，下划线(_)
# 2.不能逸数字开头
# 3.不能使用关键字：True,While,None,or,else,if等
# 4.严格区分大小写,如age,Age,AGE是三个不同的变量

# 标识符的命名规范：
# 1.见名知义 color,age
# 2.多个部分使用_ my_name,update_time
# 3.英语字母全小写
# 详情见PEP8：PEP是python社区的核心技术文档和标准化机制，而PEP8就是python的代码风格指南(https://peps.python.org/pep-0008)


#交换变量值

a = 10
b = 20
print(a,b)

c = a
a = b
b = c
print(a,b,c)