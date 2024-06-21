
def rem_vowel(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for x in string.lower():
        if x in vowels:
            string = string.replace(x," ")

def Count(a_string):
    # a_string = input("Enter a String : ")
    lowercase = a_string.lower()

    vowel_counts ={}

    for vowel in "aeiou":
           count=lowercase.count(vowel)
           vowel_counts[vowel]=count

    # print(vowel_counts)
    return vowel_counts

string ="PRANITA"
print(Count(string))
print(rem_vowel(string))




# from collections import Counter
# a="PRANITA"
# print(Counter(a))