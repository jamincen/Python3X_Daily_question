"""
    三元表达式
    常规： 表达式1 if 条件 else 表达式2
            if 条件为真，取值表达式1
            if 条件为假，取值表达式2
"""
#  另外的替代写法

x, y = 6, 8

# 表达式a
z1 = {True: x, False: y}[x > y]
print(z1) # 8
"""
    我对表达式a的理解              
    表达式a 中：print([x > y]) # False
                条件为假，取值后者，即z1 = y = 8
                
"""

### 疑问： 如果我对表达a的理解无误，那么该如何解析如下表达式b、c、d的打印结果

# 表达式b
z2 = (x > y) and x or y   # 元组：返回假，返回真 条件为假，返回y
print(z2)  # 8

# 表达式c
z3 = (lambda : x , lambda : y) [x > y]()  #元组： 条件为真，输出为x
print(z3)  # 6

# 表达式d
z4 = (x, y)[x > y]  # 元组：[真或假]  # 条件为真 ，返回x
print(z4)  # 6 
