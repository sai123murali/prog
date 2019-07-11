p1=int(input())
o1=[]
for h1 in range(0,p1):
 pt1=input()
 o1.append(pt1)
de=[]
for h1 in zip(*o1):
 if(h1.count(h1[0])==len(h1)):
  de.append(h1[0])
 else:
  break
print(''.join(de))
