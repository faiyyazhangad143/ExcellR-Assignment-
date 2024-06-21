v = int(input())
w = int(input())
# if 2<=w or w%2=0 or v<w:
if (w&1)==1 or w<2 or w<=v:
           print('INVALID INPUT')
else:
     x=((4*v-w))//2
     print(f'TW={x} FW={v-x}')



     