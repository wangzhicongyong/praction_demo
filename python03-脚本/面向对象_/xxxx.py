
"""
如果在子类中需要的构造方法就需要显示的调用父类的构造方法，或者不重写父类的构造方法。
子类不重写__init__，实例化子类时，会自动调用父类定义的__init__。

"""

class Father(object):
    def __init__(self, age):
        self.age = age
        print("age: %d" % (self.age))

    def getAge(self):
        print('父类的返回结果')
        return self.age


class Son(Father):
    def getAge(self):
        print('子类的返回结果：')
        return self.age


if __name__ == '__main__':
    son = Son(18)
    print(son.getAge())

# age: 18
# 子类的返回结果：
# 18
# 子类没有初始化__init__
# 方法，所以默认会自动调用父类定义的__init__，因此会出现一行：age: 18
