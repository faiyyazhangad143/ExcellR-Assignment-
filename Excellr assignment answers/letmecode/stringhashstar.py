s = input()

count = 0
sum=0

for i in s:
    if i=='*':
        count= count+1
    elif i=='#':
        sum= sum+1
# print(count-sum)



if (count>sum):
    print('positive int')


if (sum<count):
    print('negative int')

if (count==sum):
    print('0')


