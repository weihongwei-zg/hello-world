#收集参数的的解包，把参数放入list（列表）或者dict（字典）中，直接把list/dict中的值放入收集参数中
def stu(*args):
    print("哈哈哈哈哈")
    for i in args:
        print(type(i))
        print(i)
# stu("liuying", "liuxiaoyhing", 19, 200)
l = ["liuying", 19, 23, "wangxiaojing"]
stu(l)
# 此时，args的表示形式是字典内一个list类型的元素，即 arg = (["liuying", 19, 23, "wangxiaojing"],)
# 很显然跟我们最初的想法违背
# 此时的调用，我们就需要解包符号，即调用的时候前面加一个星号
stu(*l)
#如果是字典类型则加**
def sp(kwargs):
    print("啦啦啦啦啦")
    for v,k in kwargs.items():#.items()返回所有键值对信息,.keys()返回所有键信息,.values()返回所有值信息
        print(v,"....",k)
p = {"a":0,"b":1,"c":2}
sp(p)
def skp(**kwargs):
    print("啦啦啦啦啦")
    for v,k in kwargs.items():#.items()返回所有键值对信息,.keys()返回所有键信息,.values()返回所有值信息
        print(v,"....",k)
skp(a = "aaaa",b = "bbbb",c = "cccc")
#函数文档
'''
函数文档
函数的文档的作用是对当前函数提供使用相关的参考信息
文档的写法：
在函数内部开始的第一行使用三引号字符串定义符
一般具有特定格式
参看案例
文档查看
使用help函数，形如 help(func)
使用__doc__
'''
def stu(name, age):
    '''
    这是文档的文字内容
    :param name: 表示学生的姓名
    :param age: 表示学生的年龄
    :return: 此函数没有返回值
    '''
    pass
help(stu)
print("*" * 20)
print(stu.__doc__)
