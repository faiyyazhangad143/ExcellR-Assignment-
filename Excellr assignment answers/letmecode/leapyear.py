y = int(input("Enter Year: "))

if (y%4==0):
    if (y%100==0):
        if (y%400==0):
            print("Year", y ,"is leap year")
        else:
             print("Year" ,y ,"is not leap year")
    else:
         print("Year", y ,"is leap year")
else:
     print("Year", y ,"is not leap year")