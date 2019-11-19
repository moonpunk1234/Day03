#List

fruits = ["Mango","Banana","Orange","Mango","Mango"]
print(fruits)
#Accessing Elements in a List
print(fruits[1])
#Modify List
fruits[0] = 'Jambura'
print(fruits)

fruits.append('Mango')
print(fruits)

fruits.insert(1,'Grapes')
print(fruits)

fruits.remove('Orange')
print(fruits)

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

fruits.reverse()
print(fruits)

x=fruits.index('Banana')
print(x)

print(fruits.index('Banana',0,3))
print(fruits.count('Mango'))

foll = fruits.copy()
print(foll)

item = foll.pop()
print("Item is : ",item)
print(foll)

fruits.extend(foll)
print(fruits)

fruits.clear()
print(fruits)

#print(help(fruits.extend))
#print(dir(list))
#['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
