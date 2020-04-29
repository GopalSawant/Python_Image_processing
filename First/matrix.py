#Matrix

matrix=[[1,2],[3,4]]
print(matrix[0][1])

picture=[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
    ]

print(picture[1][0])
for i in picture:
    for j in picture:
        print(i,j)
