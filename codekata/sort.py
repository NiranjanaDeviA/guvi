num=int(input())
l1=map(int,list(input().split()))
sor=sorted(l1)
for x in range(0,len(sor)):
  print(sor[x],end=" ")
