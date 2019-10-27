list1 = []
list2 = [1,2,3]
list3 = [1,2,"tomorrow",True]
print (list3)
print (list3[2])

list3[2] = 300
print (list3)

list4 = [1,2,3]
list5 = [4,5,6]
list6 = list4 + list5
print(list6)

list7 = [1,2,3]
print (list7 * 3)

list8 = [1,2,3]
print (3 in list8)
print (6 not in list8)
print (list8[1:3])
print (list8[0])

list9 = [[1,2,3],[4,5,6]]
print (list9[1][1])

list10 = [1,2,3,4]
list10.append(6)
print (list10)

list10.extend([6,7,8])
print (list10)

list11 = [1,2,3,4,5]
list11.insert(2,100)
print (list11)

list12 = [1,2,3,4,5]
list12.pop()
print (list12)

print (list12.pop(2))
print (list12)

list13 = [1,2,3,4,8]
list13.remove(8)
print (list13)
list13.clear()
print (list13)

list14 = [1,2,3,4,8]
index14 = list14.index(8)
print(index14)

list15 = [1,3,5,7]
print (len(list15))
print (max(list15))
print (min(list15))

list16 = [1,2,3,4,3,3]
print (list16.count(3))

num = 0
allnum =  list16.count(3)
while num < allnum:
 list16.remove(3)
 num += 1
print (list16)

list16.reverse()
print (list16)

