num = int(input("Enter Number:"))
a=0
b=0
# for i in range(1,num+1):
#     if(i%2!=0):
#         a=a+7
#     else:
#         b=b+6
# if (num%2!=0):
#     print(f"Term {num} is {a-7}")
# else:
#      print(f"Term {num} is {b-6}")



for i in range(1,num+1):
        if(i%2==0):
             b=b+6
        else:
           a=a+7
if (num%2==0):
    print(f"Term {num} is {b-6}")
else:
     print(f"Term {num} is {a-7}")