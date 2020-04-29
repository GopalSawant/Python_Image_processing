

number=input("Enter the Number: ")

list1=list(range(1,int(number)))

while len(list1)>1:
    list1=list1[1::2]
    
print(list1)    
