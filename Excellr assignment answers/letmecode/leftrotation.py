# def left(n,k,a):
#     for _ in range(k):
#         a.append(a.pop(0))
#         print(*a)


# print(left(4,1,[1,2,3,4,5]))


def rotleft(a,d):
    temp = []
    temp.extend(a[0:d])
    del a[0:d]
    a.extend(temp)
    return a


print(rotleft([1,2,3,4,5],2))