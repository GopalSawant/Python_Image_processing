updatedlist=input("Enter the Number: ")

#updatedlist=list(range(1,int(yourlist),2))
updatedlist=list(range(1,int(updatedlist)))


#print(type(len(updatedlist)))

lenthOfUpdatedList=(len(updatedlist))  #length of updated list

#print(f"length of updated list is {lenthOfUpdatedList} of list {updatedlist}")





while lenthOfUpdatedList>1:
    for number in updatedlist:
        print(updatedlist)
        if number%2==0 and number !=1:
            updatedlist.remove(number)
        elif number !=1:
            updatedlist.remove(number)
    
        print(updatedlist)
    lenthOfUpdatedList=(len(updatedlist))
    print(lenthOfUpdatedList)
    print(updatedlist)
    break
        
        

   # number=number+4
    



    
    
    
    


