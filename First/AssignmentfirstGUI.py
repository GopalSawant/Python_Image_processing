picture=[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
    ]


     
for row in picture:
    for pixel in row:
        if pixel==0:
            print(" ",end="")
        else:
            print("*", end="")

    print("")
        
    
    

    
for row in range(1,10):
    for column in range(1,10):
        print('*', end="")
    print("")


print("###########")

for row1 in range(10):
    for column1 in range(1,10):
        print(' ', end="")
    print("")
    for star in range(row):
        print("*", end="")
        
