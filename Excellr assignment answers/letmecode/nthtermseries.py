num = int(input("Enter Number: "))

if (num%2==0):
    num = num //2
    print(3**(num-1))
else:
    num = num // 2+1
    print(2**(num-1))

# print(3//2)