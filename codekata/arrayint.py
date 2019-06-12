n,m=map(int,input().split())
l=[]
add=0
l=map(int,input().split())
li=list(l)
if(len(li)==n):
  for i in range (len(li)):
    if(i<m):
      add=add+li[i]
  print(add)


