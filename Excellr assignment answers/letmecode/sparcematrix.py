# a= [
#     [4,0,0],
#     [9,0,0],
#     [2,0,6]
# ]

a=[]
for k in range():
    for m in range(): 

count=0
rows=len(a)
cols=len(a[0])
size=rows*cols

for i in range(0,rows):
    for j in range(0,cols):
        if (a[i][j]==0):
            count=count+1

if (count>size/2):
    print("it is sparse matrix")
else:
     print("it is not  sparse matrix")