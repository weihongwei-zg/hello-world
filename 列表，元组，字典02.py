#元组（tyule）是特殊的列表，除了不可以被修改，其他都与列表一样
#虽然元组不可以被修改，但可以重新赋值，不过重新赋值得到的元组地址发生改变
a = [1,2,3,4,5,6]
a = tuple(a)
print(type(a))
print(a)
a = 1,
print(a)
print("*" * 50)
#集合（set）,和数学中定义一致，如果有重复数据，自动合并，且无顺序，无法索引和切片
# 如果定义时就一个大括号为字典类型（dict），里面只能放可哈希数据
b = {1,2,1,4,"DA",'DAWD',56}
print(type(b))
print(b)
a = [1,2,3,4,5,]
c = set(a)
print(type(c))
print(c)
print("*" * 50)
#.add往集合里面增加元素
#.clear 集合原地清空
#.pop()随机移除一个元素
#字典（dict）
'''
字典是一种组合数据，没有顺序的组合数据，数据以键值对形式出现

'''
# 创建空字典1
d = {}
print(d)
# 创建空字典2
d = dict()
print(d)
# 创建有值的字典， 每一组数据用冒号隔开， 每一对键值对用逗号隔开
d = {"one":1, "two":2, "three":3}
print(d)
# 用dict创建有内容字典1
d = dict({"one":1, "two":2, "three":3})
print(d)
# 用dict创建有内容字典2
# 利用关键字参数
d = dict(one=1, two=2, three=3)
print(d)
d = dict( [("one",1), ("two",2), ("three",3)])
print(d)
print("*" * 50)


# 便利在python2 和 3 中区别比较大，代码不通用
# 按key来使用for循环
d = {"one": 1, "two": 2, "three": 3}
# 使用for循环，直接按key值访问
for k in d:
    print(k, d[k])
# 上述代码可以改写成如下
for k in d.keys():
    print(k, d[k])
# 只访问字典的值
for v in d.values():
    print(v)
# 注意以下特殊用法
for k, v in d.items():
    print(k, '--', v)
print("*" * 50)


#字典生成式
a = {"aaa":1,"bbb":2,"ccc":3,"ddd":4}
b = {k:v for k,v in a.items() if v %2 == 0}
print(b)
print("*" * 50)


# 通用函数： len, max, min, dict
# str(字典): 返回字典的字符串格式
d = {"one":1, "two":2, "three":3}
print(str(d))
# clear: 清空字典
# items: 返回字典的键值对组成的元组格式
d = {"one":1, "two":2, "three":3}
i = d.items()
print(type(i))
print(i)
# keys:返回字典的键组成的一个结构
k = d.keys()
print(type(k))
print(k)
# values: 同理，一个可迭代的结构
v = d.values()
print(type(v))
print(v)
# fromkeys: 使用指定的序列作为键，使用一个值作为字典的所有的键的值
l = ["eins", "zwei", "drei"]
# 注意fromkeys两个参数的类型
# 注意fromkeys的调用主体
d = dict.fromkeys(l, "hahahahahah")
print(d)