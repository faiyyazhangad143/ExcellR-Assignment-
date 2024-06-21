n = int(input())
k = int(input())
j = int(input())
m = int(input())
p = int(input())

atebanana = 0.0
atepeanut = 0.0

if (n<0 or k<0 or j<0 or m<0 or p<0):
    print("INVALID INPUT")

else:
    if k>0:
        atebanana = m/k
        m = m%k
    if j>0:
        atepeanut = p/j
        p =p%j
    
    n = n - atebanana - atepeanut
    if m!=0 or p!=0:
        n = n-1

    print("Number of Monkeys left on the tree", n)

