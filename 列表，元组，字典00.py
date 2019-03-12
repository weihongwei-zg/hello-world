#global i作用是将局部变量提权（实例化为全局变量），可以通过globals（i）和locals（i）显示出局部变量和全局变量，id（i）打印地址
#type(i) 获取i的数据类型
def fun():
    global b1
    b1 = 100
    print(b1)
    print("I am in fun")
fun()
# print(b1)如果在函数调用上面，则不好使，报错，为什么？？？
print(b1,"\n","*"*50)

#eval()把一个字符串当成一个表达式来执行， 返回表达式执行后的结果
#exec()跟eval功能类似， 但是，不返回结果
x = 100
y = 200
z1 = x + y
z2 = exec("print('x+y=', x+y)")
z3 = eval('x+y')
print(z1)
print(z2)
print(z3)
print("*" * 50)
#递归调用，python递归不会无限，调用一定次数会停止
#列表操作切片x[a:b:c]  a为起点，b为终点但不包括b，c为步长，c为正从左到右，c为负右到左
#del 为删除命令，del x[i]为删除列表元素,   x.insert(i,k)表示插入数据
l = [3,4,56,76,32,21,43,5]
ll = l[:]
print(ll)
ll.insert(2,1000)
print(ll)
del ll[0]
print(ll)

#列表相加，和相乘都是在原有列表后接数据

x = list(i for i in range(0,11))
y = ['a',"dada"]
print(x+y)
print(x*3)
print("*" * 50)
# 双层列表循环
#a 为嵌套列表，或者叫双层列表,遍历
a = [["one", 1, 84], ["two", 2, 15], ["three", 3, 656] ]
for k,v,w in a:
    print(k, "---", v, "---",w)
print("*" * 50)
# 列表生成式可以嵌套
# 由两个列表a，b
a = [i for i in range(1,4)] # 生成list a
print(a)
b = [i for i in range(100,400) if i % 100 == 0]
print(b)

# 列表生成是可以嵌套,此时等于两个for循环嵌套
c = [  m+n for m in a for n in b]
print(c)
# 上面代码跟下面代码等价
for m in a:
    for n in b:
        print(m+n, end="  ")
print()
# 嵌套的列表生成式也可以用条件表达式
c = [  m+n for m in a for n in b if m+n < 250]
print(c)
s = "I love wangxiaojing"
print(list(s))


