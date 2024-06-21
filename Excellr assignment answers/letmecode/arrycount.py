Arr = [3,4,5,8,9]

count=0

for i in range(len(Arr)):
    if Arr[i]>=Arr[0]:
        count= count+1

print(count)


# import sys
# n= int(input("Enter n : "))
# c=0
# m=-sys.maxsize-1

# while n:
#     n= n-1
#     a=int(input("Enter array element: "))
#     if a>m:
#         m=a
#         c=c+1
    
# print(c)
