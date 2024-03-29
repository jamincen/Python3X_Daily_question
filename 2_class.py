### python中的定义类方法有三种形式

#   1.普通方法
#   2.类方法(@classmethod)
#   3.静态方法(@staticmethod)

### 1.普通方法

class A():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_name(self):
        print("my name is", self.name)
   
    def get_age(self):
        print(f'i am {self.age} years old')
        
        
class B():
    def get_name(self, name):
        print('my name is', name)
        
    def get_age(self, age):
        print(f'i am {age} years old')
        
        
if __name__ == '__main__':
    a = A('tom',19)
    a.get_name()
    a.get_age()
    
    b = B()
    b.get_name('tom')
    b.get_age(19)
    

### class A()中，__init__()是一个特殊的方法，相当于对A进行初始化，__init__中的self是对象A本身，
### name和age是它们的形参，每次调用方法之前需要对类进行实例化，例如 a = A('tom', 19)


### 2.类方法（@classmethon）
# 普通方法每次调用类都需进行实例化，麻烦。
# @classmethod 不需要self来表示自身，而是用cls来代替

class C():
    @classmethod
    def get_name(cls, name):
        print(cls) # <class '__main__.C'>
        print('my name is %s' % name)
    @classmethod
    def get_age(cls, age):
        print(f'i am %s years old' % age)
        
if __name__ == '__main__':
    C.get_name('tom')
    C.get_age(19)
    
    
    
### 3.静态方法（@staticmethod)
# 不要表示自身对象的self或者cls作为参数

class D():
    @staticmethod
    def get_name(name):
        print('my name is %s' % name)
        
    @staticmethod
    def get_age(age):
        print(f'i am %s years old' % age)
        
if __name__ == '__main__':
    D.get_name('tom')
    D.get_age(19)
 
