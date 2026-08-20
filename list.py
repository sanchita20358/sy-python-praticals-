list=[1,2,3,4,11,12,"d"]
print(list)

list.append(6)
print(list)

list.insert(2,10)
print(list)

list[2]=5
print(list)

list.extend([8,5,7])
print(list)

print(list[5])

list.remove(6)
print(list)

list.pop(3)
print(list)

list.pop()
print(list)

del list[1]
print(list)

print(len(list))  

if 8 in list:
    print("element is present")
else:
    print("element is not present")

for i in list:
    print(i)

print(list.count(4))

print(list.index(4))

list2=[2,4,6,8,3,1]
list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)

list2.reverse()
print(list2)

list.clear()
print(list) 

newlist=list2.copy()
print(newlist)

