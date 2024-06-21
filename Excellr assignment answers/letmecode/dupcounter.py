# from collections import Counter


# def remove_dup(s):
#     s = s.split(" ")

#     for i in range(0,len(s)):
#         s[i] ="".join(s[i])

#     Uniq = Counter(s)

#     s= " ".join(Uniq.keys())
#     print(s)


# s = "Python is great and Java is is great "

# print(remove_dup(s))


s = "Python is great and Java is is great "

l = s.split()
k=[]
for i in l:
    if (s.count(i))>1 and (i not in k) or s.count(i)==1:
        k.append(i)

print(' '.join(k))