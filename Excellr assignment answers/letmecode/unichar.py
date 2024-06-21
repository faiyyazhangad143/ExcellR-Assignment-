# def unichar(s):
#     char = set()

#     for letter in s:
#         if letter in char:
#             return False
#         else:
#             char.add(letter)
#     return True

# print(unichar("abccd"))


# def unichar(s):
#     # print(sorted(list(s)) )
#     # print(sorted(list(set(s))))
#     return sorted(list(s)) == sorted(list(set(s)))


# print(unichar('abccd'))


def unichar(s):
    print(len(set(s)))
    print(len(s))
    
    return len(set(s)) == len(s)


print(unichar('abccd'))