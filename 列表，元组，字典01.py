#关于列表的函数
# append 插入一个内容, 在末尾追加
# insert: 指定位置插入
# del 删除
print("*" * 50)
'''
 remove:在列表中删除指定的值的元素
 如果被删除的值没在list中，则报错
 即，删除list指定值的操作应该使用try。。。excepty语句，或者先行进行判断
discard移除和remove一样，但当不存在此值时不会报错
'''
a = [1,2,3,4,5,6,7,8]
a.insert(4, 666)
print(a)
print(id(a))
a.remove(666)
print(a)
print(id(a))
# 输出两个id值一样，说明，remove操作是在原list直接操作
print("*" * 50)

# clear:清空
print(a)
print(id(a))
a.clear()
print(a)
print(id(a))
# 如果不需要列表地址保持不变，则清空列表可以使用以下方式
# a = list()
# a = []
print("*" * 50)

# reverse:翻转列表内容，原地翻转
a = [ 1,2,3,4,5]
print(a)
print(id(a))
a.reverse()
print(a)
print(id(a))
print("*" * 50)

# extend:扩展列表，两个列表，把一个直接拼接到后一个上
a = [ 1,2,3,4,5]
b = [6,7,8,9,10]
print(a)
print(id(a))
a.extend(b)
print(a)
print(id(a))
print("*" * 50)

# count:查找列表中指定值或元素的个数
print(a)
a.append(8)
a.insert(4, 8)
print(a)
a_len = a.count(8)
print(a_len)
print("*" * 50)

# copy: 拷贝，此函数是浅拷贝，
# 列表类型变量赋值示例
a = [1,2,3,4,5,666]
print(a)
# list类型，简单赋值操作，是传地址
b = a
b[3] = 777
print(a)
print(id(a))
print(b)
print(id(b))
print("*" * 20)
# 为了解决以上问题，list赋值需要采用copy函数
b = a.copy()
print(a)
print(id(a))
print(b)
print(id(b))
print("*" * 20)
b[3] = 888
print(a)
print(b)
print("*" * 50)

# 深拷贝跟浅拷贝的区别
# 出现下列问题的原因是，copy‘函数是个浅拷贝函数，即只拷贝一层内容
# 深拷贝需要使用特定工具
a = [1,2,3, [10, 20, 30]]
b = a.copy()
print(id(a))
print(id(b))
print(id(a[3]))
print(id(b[3]))
a[3][2] = 666
print(a)
print(b)
print("*" * 50)




