oxygen_level=[]
sum=0
for i in range(1,10): 
       oxygen_level_of_trainee = int(input())
       oxygen_level.append(oxygen_level_of_trainee)

for i in range(len(oxygen_level)):
        #   sum = sum+oxygen_level[i]
        # first=oxygen_level[0]
        maximum =max(oxygen_level)
        if oxygen_level[i]== maximum:
            print('Trainee Number:', i+1)
        elif oxygen_level[i]<70:
            print("Trainees unfit")


# for i in range(len(oxygen_level)):
#         avg= sum//len(oxygen_level)
#         if avg >= oxygen_level[i]:
#                 print('Trainee Number:', i)
#         else:
#             print("Trainees unfit")