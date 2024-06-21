num = int(input("Enter Number: "))

order= len(str(num))
sum=0
temp = num

while temp > 0:
    digit = temp % 10
    sum= sum+digit**order
    temp= temp//10
if num == sum:
    print("Armstron Number")
else:
    print("Non Armstrong Number")


# temp = 153
# print(temp //10)
# print(1//10)