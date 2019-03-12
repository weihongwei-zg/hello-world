#普通参数,默认参数,关键字参数,收集参数

#math函数：
#sin(x)：求x的正弦,cos(x)：求x的余弦,asin(x)：求x的反正弦
#acos(x)：求x的反余弦,tan(x)：求x的正切,atan(x)：求x的反正切,hypot(x,y)：求直角三角形的斜边长度,
#fmod(x,y)：求x/y的余数,ceil(x)：取不小于x的最小整数,floor(x)：求不大于x的正大整数
#fabs(x)：求绝对值,exp(x)：求e的x次幂,pow(x,y)：求x的y次幂,log10(x)：求x的以10位底的对数,sqrt(x)：求x的平方根
import math as mt
print(mt.e)

#默认参数形参带有默认值
#调用的时候，如果没有对相应形参赋值，则使用默认值
print("*" * 50,"\n","默认参数")
def printf(a, b="yes", c=10):#默认参数后面不能为普通参数，否则会报错
    if b == "yes":
        print("{0}   {1}   {0}    ".format(a,b),c)
    else:
        print("NO",b)
printf(3//2,"no",2)#//表示取商(地板除)
printf(1**2,)#**表示乘方
printf(1,2)#b赋值为2
print("*" * 25,end = "")#后面加上end = ""可以使print输出不换行且end不能为其他字母
print("*" * 25)
#关键字参数
#比较麻烦，但也有好处：
#不容易混淆， 一般实参和形参只是按照位置一一对应，容易出错
#使用关键字参数，可以不考虑参数位置
print("关键字参数")
def stu_key(a="No name", b=0, c="addr"):
    print("I am a student")
    print("我叫 {0}， 我今年 {1}岁了， 我住{2}".format(a, b, c))
stu_key(b=3, a="kankan", c="c楼")
print("*" * 50,"\n收集参数")
#收集参数：把没有位置，不能和定义时的参数位置相对应的参数，放入一个特定的数据结构中
#约定俗成 用*argc表示（要加*号），可以与其他参数同时存在
# 收集参数可以不带任何实参调用，此时收集参数为空tuple
def stu( *args):
    print("Hello 大家好，我自我介绍以下，简答说两句：")
    # type函数作用是检测变量的类型
    print(type(args))#type获取数据类型
    for item in args:
        print(item)
stu("kankan", 18, "c楼", "yes", "single")
stu("kankan")

print("*" * 50,"\n收集参数之关键字收集参数")
#把关键字参数按字典格式存入收集参数
#kwargs一般约定俗成
#调用的时候，把多余的关键字参数放入kwargs，用2个*
#访问kwargs需要按字典格式访问
# 收集参数案例
# 自我介绍
# 调用的时候需要使用关键字参数调用
def stu(**kwargs):
    # 在函数体内对于kwargs的使用不用带星号
    print("Hello 大家好，我先自我介绍一下：")
    print(type(kwargs))
    # 对于字典的访问，python2 和python3有区别
    for k, v in kwargs.items():
        print(k, "......", v)
    for k in kwargs.items():
        print(k)
stu(a="kankan", b=19, c="c楼", lover="王晓静", work="Teacher")
stu(name="kankan")



