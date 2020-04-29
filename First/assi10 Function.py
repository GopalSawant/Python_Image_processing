def highest_even(li):
    highest=0
    for number in li:
        if number%2==0:
            if highest<number:
                highest=number

    return highest
            
            




print(highest_even([10,2,3,4,8,11,12,12,1000,2]))
