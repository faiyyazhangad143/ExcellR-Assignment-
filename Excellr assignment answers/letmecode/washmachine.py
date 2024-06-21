n = int(input())

if n== 0:
    print("Time Estimated : 0 Minutes")

elif n>0 and n<=2000:
    print("Time Estimated : 25 Minutes")

elif n>2000 and n<=4000:
    print("Time Estimated : 35 Minutes")

elif n>4000 and n<=7000:
    print("Time Estimated : 45 Minutes")

else:
    print("INVALID INPUT")