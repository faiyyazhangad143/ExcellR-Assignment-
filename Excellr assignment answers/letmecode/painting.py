no_of_interior_wall = int(input("No_of_interior_wall: "))

no_of_exterior_wall = int(input("No_of_exterior_wall: "))

if no_of_interior_wall:
    int_walls =[]
    for i in range(no_of_interior_wall):
            int_walls.append(float(input()))

if no_of_exterior_wall:
    ext_walls =[]
    for i in range(no_of_exterior_wall):
            ext_walls.append(float(input()))

if no_of_exterior_wall<0 and no_of_interior_wall<0:
    print("Invalid Input")
    exit()

if no_of_exterior_wall and no_of_interior_wall:
    print("Total estimated cost : ",(sum(int_walls)*18+sum(ext_walls)*12),"INR")

else:
    if no_of_exterior_wall:
        print("Total estimated cost : ",sum(ext_walls)*12,"INR")

    elif no_of_interior_wall:
        print("Total estimated cost : ",sum(int_walls)*18,"INR")

    else:
        print("Total estimated cost 0.0 INR ")




