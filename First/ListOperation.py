#List

li=[1,2,3,4,5,"  ",]
print(li)
newLi=li
print(newLi)
newLi[5]="Gopal"
li[5]="Sawant"
print(newLi)
print(li)


list=[1,2,3,4,5,]
list.append(6)
list.insert(1,8)
list.extend("100")
print(list)
list.pop(8)
list.remove('0')
list.pop()
#list.clear()

print(list)
print("Final")


newlist=list
list.sort()
newlist[6]=4
newlist.sort()
list.reverse()
print(list)
newlist=newlist[::-1]
print(newlist)
print(list)
print(range(1,100))
#print(list(range(1,100)))

list=[]
print(list(range(1,100)))
