n = 6
count=0
mul =1
m=n//2
			
for i in range (1,m):
    count = count + i
    # print(count)
    mul = mul * i
    # print(mul)
    if (count==n) and ( mul==n):
        print("Number is Spy Number");
	         