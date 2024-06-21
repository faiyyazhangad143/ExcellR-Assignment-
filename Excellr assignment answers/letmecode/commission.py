parent_name = input("Enter parent name: ")
yes_no = input("Enter Y if you children: ")
children = []

if yes_no=='Y':
    no_of_children = int(input("Enter no of children: "))
    for i in range(no_of_children):
           name_of_children = input()
           children.append(name_of_children)

print( "Total Members:" ,1+len(children))
print("COMISSION DETAILS")
print(parent_name,":" ,len(children)*(10/100*5000),"INR")

for i in range(len(children)):
    print(children[i],":",5/100*5000,"INR")



