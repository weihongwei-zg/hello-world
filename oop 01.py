'''
继承：继承就是一个类可以获得另外一个类中的成员属性和成员方法
- 作用： 减少代码，增加代码的复用功能， 同时可以设置类与类直接的关系
- 继承与被继承的概念：
    - 被继承的类叫父类，也叫基类，也叫超类
    - 用于继承的类，叫子类，也叫派生类
    - 继承与被继承一定存在一个 is-a 关系
- 继承的特征
    - 所有的类都继承自object类，即所有的类都是object类的子类
    - 子类一旦继承父类，则可以使用父类中除私有成员外的所有内容
    - 子类继承父类后并没有将父类成员完全赋值到子类中，而是通过引用关系访问调用
    - 子类中可以定义独有的成员属性和方法
    - 子类中定义的成员和父类成员如果相同，则优先使用子类成员
    - 子类如果想扩充父类的方法，可以在定义新方法的同时访问父类成员来进行代码重用，
    可以使用 [父类名.父类成员] 的格式来调用父类成员，也可以使用super().父类成员的
    格式来调用
- 继承变量函数的查找顺序问题
    - 优先查找自己的变量
    - 没有则查找父类
    - 构造函数如果本类中没有定义，则自动查找调用父类构造函数
    - 如果本类有定义，则不在继续向上查找
- 构造函数
    - 是一类特殊的函数，在类进行实例化之前进行调用
    - 如果定义了构造函数，则实例化时使用构造函数，不查找父类构造函数
    - 如果没定义，则自动查找父类构造函数
    - 如果子类没定义，父类的构造函数带参数，则构造对象时的参数应该按父类参数构造
- super
    - super不是关键字， 而是一个类
    - super的作用是获取MRO（MethodResolustionOrder）列表中的第一个类
    - super于父类直接没任何实质性关系，但通过super可以调用到父类
    - super使用两个方法,参见在构造函数中调用父类的构造函数

- 单继承和多继承
    - 单继承：每个类只能继承一个类
    - 多继承，每个类允许继承多个类
'''


# 子类扩充父类功能的案例
# 人由工作的函数， 老师也由工作的函数，但老师的工作需要讲课
class Person():
    name = "live"
    age = 18
    __score = 0  # 考试成绩是秘密，只要自己知道
    _petname = "xiaoming"  # 小名，是保护的，子类可以用，但不能公用
    def sleep(self):
        print("Sleeping ... ...")
    def work(self):
        print("make some money")
# 父类写在括号内
class Teacher(Person):
    teacher_id = "10000"
    name = "weihong"
    def make_test(self):
        print("哈哈哈")
    def work(self):
        # 扩充父类的功能只需要调用父类相应的函数
        # Person.work(self)
        # 扩充父类的另一种方法
        # super代表得到父类
        super().work()
        self.make_test()
t = Teacher()
t.work()
print('*' * 50)


# 继承中的构造函数 - 2
class Animel():
    def __init__(self):
        print("Animel")
class PaxingAni(Animel):
    name = 'animel'
    def __init__(self,*args):
        print("animel   cat")
class Dog(PaxingAni):
    # __init__就是构造函数
    # 每次实例化的时候，第一个被自动的调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print("I am init in dog")
# 实例话的时候，自动调用了Dog的构造函数
# 因为找到了构造函数，则不在查找父类的构造函数
kaka = Dog()
# 猫没有写构造函数
class Cat(PaxingAni):
    pass
# 此时应该自动调用构造函数，因为Cat没有构造函数，所以查找父类构造函数
# 在PaxingAni中查找到了构造函数且参数(收集参数)一致，则停止向上查找，如果不一致会报错
c = Cat(1,5,5,16,6)
