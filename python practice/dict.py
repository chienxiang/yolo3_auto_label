#!/user/bin/env python
# _*_ coding: UTF-8 _*_

a = {'key1':1,'key2':2,3:'key3'}
print(a['key1'])

del a[3]
print(a)

a['key3']=3
print(a)

b = {'a':[1,2,3],'b':{'key1':1,2:3},'c':'c'}
print(b)

print(b['b']['key1'])
