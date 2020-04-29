list1=['a','b','c','b','d','m','n','n']

list2=[]

for item in list1:   #list1 traverse    
    if item not in list2:
        list2.append(item)  


print(list2)
list1=list2

print(f"List1 is: {list1} and \nliste2 is: {list2}")


