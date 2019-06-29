#!/user/bin/env python
# _*_ coding: UTF-8 _*_

class Calculator:
    name = 'aabb'
    def add(self,x,y):
        result = x+y
        print(result)
    def minus(self,x,y):
        result = x-y
        print(result)
    def times(self,x,y):
        result = x*y
        print(result)
    def div(self,x,y):
        result = x/y
        print(result)    


a = Calculator()
print(a.name)

a.add(1,2)

#=================================
class Test:
    name = 'abab'
    price = 10
    def __init__(self,name,price):
        self.name = name
        self.price = price


b = Test('ccdd',20)
print(b.name)
