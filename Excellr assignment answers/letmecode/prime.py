num = int(input("Enter Any No: "))




def prime(num):
    if (num%2!=0):
        if(num%num==0):
                print("Number is  prime")
    else:
        print("Number is not prime")



if (num < 0):
    print("Please Enter Positive Number")
else:
    prime(num)