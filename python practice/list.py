#!/user/bin/env python
# _*_ coding: UTF-8 _*_

tupleA = 1,2,3,4
listA = [5,6,7,8]

for index in range(len(tupleA)) :
    print('index=',index,'value in tuple',tupleA[index])
    
print('listA=',listA)
print('tupleA=',tupleA)

#===================================

listB =[1,2,3,4,3,2,1]
listB.append(0)
print(listB)
listB.insert(0,0)
print(listB)
listB.remove(2)
print(listB)

print(listB[-1])#search the last of listB
print(listB.count(3))

listB.sort()
print(listB)

listB.sort(reverse=True)
print(listB)

