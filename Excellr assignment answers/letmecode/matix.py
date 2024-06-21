matrix = [
            [0,1,1],
            [1,1,0],
            [1,1,1]
]

count =0


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[j]==1:
            count=count+1
            # if count>2 in matrix[j]:
            #     print(matrix[i])

print(matrix[i]) 
print(count)         



