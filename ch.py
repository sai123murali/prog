av=int(input())
flag=0
a=list(map(int,input().split()))
for i in range(0,av):
    if (i==a[i]):
        flag=1
        print(i,end=" ")
if(flag==0):
    print("-1")