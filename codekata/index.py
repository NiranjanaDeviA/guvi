x=int(input())
l=list(map(int,input().split()))
if len(l)==x:
  for i in range(x):
    print(l[i],i)
