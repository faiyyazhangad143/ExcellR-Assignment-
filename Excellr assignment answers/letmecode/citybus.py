import math

def getFare(source,destination):
    route=[ ["TH","GA","IC","HA","TE","LU","NI","CA"],
    [800,600,750,900,1400,1200,1100,1500]
    ]


    fare = 0.0

    if not (source in route[0] and destination):
        print("INVALID INPUT")
        exit()

    if route[0].index(source) < route[0].index(destination):
        for i in range(route[0].index(source),route[0].index(destination)):
            fare= fare+route[1][i]

    elif route[0].index(destination) < route[0].index(source):
        for i in range(route[0].index(source)+1,len(route[0])):
            fare= fare+route[1][i]

        for i in range(0,route[0].index(destination)+1):
            fare= fare+route[1][i]

    # return float(math.ceil(fare*0.005))

    print(float(math.ceil(fare*0.005)),"INR")


source = input()
destination = input()

fare = getFare(source,destination)


if fare == 0:
    print("INVALID INPUT")
else:
    print(fare)