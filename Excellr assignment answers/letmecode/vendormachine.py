print("Coffee\nTea\nSoups\nBeverage")

coffee = ["Espresso","Cappuccino","Latte"]
tea = ["Palin","Assam","Ginger","Cardmom","Masala","Lemon","Green","Organic Darjeeling"]
soups = ['Hot and sour soup','Veg Corn soup','Tomato soup','Spicy Tomato soup']
Beverage = ['Hot Chocklate Drink','Badam Drink','Badam-Pista Drink']

order = input()

if order=='Coffee':
    for i in range(1,len(coffee)):
        print(i,coffee[i])
        
    ietm =input()
    for i in range(1,len(soups)):
       if order[i] == ietm:
            print("Welcome to CCD! \nEnjoy your" ,order[i])


elif order=='Tea':
    for i in range(1,len(tea)):
        print(i,tea[i])
        
    ietm =input()

    for i in range(1,len(soups)):
        if order[i] == ietm:
            print("Welcome to CCD! \nEnjoy your" ,order[i])


elif order=='Soups':
    for i in range(1,len(soups)):
        print(i,soups[i])
    
    ietm =input()

    for i in range(1,len(soups)):
        if order[i] == ietm:
            print("Welcome to CCD! \nEnjoy your" ,order[i])


elif order=='Beverage':
    for i in range(1,len(Beverage)):
        print(i,Beverage[i])
       
    ietm =input()

    for i in range(1,len(soups)):
        if order[i] == ietm:
            print("Welcome to CCD! \nEnjoy your" ,order[i])

else:
    print("INVALID INPUT")

